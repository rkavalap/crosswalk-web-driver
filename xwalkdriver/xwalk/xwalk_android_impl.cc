// Copyright (c) 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "xwalk/test/xwalkdriver/xwalk/xwalk_android_impl.h"

#include <utility>

#include "base/strings/string_split.h"
#include "xwalk/test/xwalkdriver/net/port_server.h"
#include "xwalk/test/xwalkdriver/xwalk/device_manager.h"
#include "xwalk/test/xwalkdriver/xwalk/devtools_client.h"
#include "xwalk/test/xwalkdriver/xwalk/devtools_http_client.h"
#include "xwalk/test/xwalkdriver/xwalk/status.h"

XwalkAndroidImpl::XwalkAndroidImpl(
    scoped_ptr<DevToolsHttpClient> http_client,
    scoped_ptr<DevToolsClient> websocket_client,
    ScopedVector<DevToolsEventListener>& devtools_event_listeners,
    scoped_ptr<PortReservation> port_reservation,
    scoped_ptr<Device> device)
    : XwalkImpl(std::move(http_client),
                 std::move(websocket_client),
                 devtools_event_listeners,
                 std::move(port_reservation)),
      device_(std::move(device)) {}

XwalkAndroidImpl::~XwalkAndroidImpl() {}

Status XwalkAndroidImpl::GetAsDesktop(XwalkDesktopImpl** desktop) {
  return Status(kUnknownError, "operation is unsupported on Android");
}

std::string XwalkAndroidImpl::GetOperatingSystemName() {
  return "ANDROID";
}

bool XwalkAndroidImpl::HasTouchScreen() const {
  const BrowserInfo* browser_info = GetBrowserInfo();
  if (browser_info->browser_name == "webview")
    return browser_info->major_version >= 44;
  else
    return browser_info->build_no >= 2388;
}

Status XwalkAndroidImpl::QuitImpl() {
  return device_->TearDown();
}

