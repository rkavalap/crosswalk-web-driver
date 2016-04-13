// Copyright (c) 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "xwalk/test/xwalkdriver/xwalk/xwalk_desktop_impl.h"

#if defined(OS_POSIX)
#include <errno.h>
#include <signal.h>
#include <sys/wait.h>
#include <unistd.h>
#endif

#include "base/files/file_path.h"
#include "base/logging.h"
#include "base/posix/eintr_wrapper.h"
#include "base/process/kill.h"
#include "base/sys_info.h"
#include "base/threading/platform_thread.h"
#include "base/time/time.h"
#include "xwalk/test/xwalkdriver/net/port_server.h"
#include "xwalk/test/xwalkdriver/xwalk/devtools_client.h"
#include "xwalk/test/xwalkdriver/xwalk/devtools_http_client.h"
#include "xwalk/test/xwalkdriver/xwalk/status.h"
#include "xwalk/test/xwalkdriver/xwalk/web_view_impl.h"

namespace {

bool KillProcess(const base::Process& process) {
#if defined(OS_POSIX)
  kill(process.Pid(), SIGKILL);
  base::TimeTicks deadline =
      base::TimeTicks::Now() + base::TimeDelta::FromSeconds(30);
  while (base::TimeTicks::Now() < deadline) {
    pid_t pid = HANDLE_EINTR(waitpid(process.Pid(), NULL, WNOHANG));
    if (pid == process.Pid())
      return true;
    if (pid == -1) {
      if (errno == ECHILD) {
        // The wait may fail with ECHILD if another process also waited for
        // the same pid, causing the process state to get cleaned up.
        return true;
      }
      LOG(WARNING) << "Error waiting for process " << process.Pid();
    }
    base::PlatformThread::Sleep(base::TimeDelta::FromMilliseconds(50));
  }
  return false;
#endif

  if (!process.Terminate(0, true)) {
    int exit_code;
    return base::GetTerminationStatus(process.Handle(), &exit_code) !=
        base::TERMINATION_STATUS_STILL_RUNNING;
  }
  return true;
}

}  // namespace

XwalkDesktopImpl::XwalkDesktopImpl(
    scoped_ptr<DevToolsHttpClient> client,
    ScopedVector<DevToolsEventListener>& devtools_event_listeners,
    scoped_ptr<PortReservation> port_reservation,
    base::Process process,
    const base::CommandLine& command,
    base::ScopedTempDir* extension_dir)
    : XwalkImpl(client.Pass(),
                 devtools_event_listeners,
                 port_reservation.Pass()),
      process_(process.Pass()),
      command_(command) {
  if (extension_dir->IsValid())
    CHECK(extension_dir_.Set(extension_dir->Take()));
}

XwalkDesktopImpl::~XwalkDesktopImpl() {
  if (!quit_) {
    base::FilePath extension_dir = extension_dir_.Take();
    LOG(WARNING) << "xwalk detaches, take care of directory:"
                 << extension_dir.value();
  }
}

Status XwalkDesktopImpl::WaitForPageToLoad(const std::string& url,
                                            const base::TimeDelta& timeout,
                                            scoped_ptr<WebView>* web_view) {
  base::TimeTicks deadline = base::TimeTicks::Now() + timeout;
  std::string id;
  while (base::TimeTicks::Now() < deadline) {
    WebViewsInfo views_info;
    Status status = devtools_http_client_->GetWebViewsInfo(&views_info);
    if (status.IsError())
      return status;

    for (size_t i = 0; i < views_info.GetSize(); ++i) {
      if (views_info.Get(i).url.find(url) == 0) {
        id = views_info.Get(i).id;
        break;
      }
    }
    if (!id.empty())
      break;
    base::PlatformThread::Sleep(base::TimeDelta::FromMilliseconds(100));
  }
  if (id.empty())
    return Status(kUnknownError, "page could not be found: " + url);

  scoped_ptr<WebView> web_view_tmp(new WebViewImpl(
      id, GetBuildNo(), devtools_http_client_->CreateClient(id)));
  Status status = web_view_tmp->ConnectIfNecessary();
  if (status.IsError())
    return status;

  status = web_view_tmp->WaitForPendingNavigations(
      std::string(), deadline - base::TimeTicks::Now(), false);
  if (status.IsOk())
    *web_view = web_view_tmp.Pass();
  return status;
}

XwalkDesktopImpl* XwalkDesktopImpl::GetAsDesktop() {
  return this;
}

std::string XwalkDesktopImpl::GetOperatingSystemName() {
  return base::SysInfo::OperatingSystemName();
}

Status XwalkDesktopImpl::QuitImpl() {
  if (!KillProcess(process_))
    return Status(kUnknownError, "cannot kill xwalk");
  return Status(kOk);
}

const base::CommandLine& XwalkDesktopImpl::command() const {
  return command_;
}
