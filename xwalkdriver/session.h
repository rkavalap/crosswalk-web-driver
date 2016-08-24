// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef XWALK_TEST_XWALKDRIVER_SESSION_H_
#define XWALK_TEST_XWALKDRIVER_SESSION_H_

#include <list>
#include <string>

#include "base/files/scoped_temp_dir.h"
#include "base/memory/scoped_ptr.h"
#include "base/memory/scoped_vector.h"
#include "base/time/time.h"
#include "xwalk/test/xwalkdriver/basic_types.h"
#include "xwalk/test/xwalkdriver/command_listener.h"
#include "xwalk/test/xwalkdriver/xwalk/device_metrics.h"
#include "xwalk/test/xwalkdriver/xwalk/geoposition.h"
#include "xwalk/test/xwalkdriver/xwalk/network_conditions.h"

namespace base {
class DictionaryValue;
}

class Xwalk;
class Status;
class WebDriverLog;
class WebView;

struct FrameInfo {
  FrameInfo(const std::string& parent_frame_id,
            const std::string& frame_id,
            const std::string& xwalkdriver_frame_id);

  std::string parent_frame_id;
  std::string frame_id;
  std::string xwalkdriver_frame_id;
};

struct Session {
  static const base::TimeDelta kDefaultPageLoadTimeout;

  explicit Session(const std::string& id);
  Session(const std::string& id, scoped_ptr<Xwalk> xwalk);
  ~Session();

  Status GetTargetWindow(WebView** web_view);

  void SwitchToTopFrame();
  void SwitchToParentFrame();
  void SwitchToSubFrame(const std::string& frame_id,
                        const std::string& xwalkdriver_frame_id);
  std::string GetCurrentFrameId() const;
  std::vector<WebDriverLog*> GetAllLogs() const;
  std::string GetFirstBrowserError() const;

  const std::string id;
  bool quit;
  bool detach;
  bool force_devtools_screenshot;
  scoped_ptr<Xwalk> xwalk;
  std::string window;
  int sticky_modifiers;
  // List of |FrameInfo|s for each frame to the current target frame from the
  // first frame element in the root document. If target frame is window.top,
  // this list will be empty.
  std::list<FrameInfo> frames;
  WebPoint mouse_position;
  base::TimeDelta implicit_wait;
  base::TimeDelta page_load_timeout;
  base::TimeDelta script_timeout;
  scoped_ptr<std::string> prompt_text;
  scoped_ptr<Geoposition> overridden_geoposition;
  scoped_ptr<DeviceMetrics> overridden_device_metrics;
  scoped_ptr<NetworkConditions> overridden_network_conditions;
  // Logs that populate from DevTools events.
  ScopedVector<WebDriverLog> devtools_logs;
  scoped_ptr<WebDriverLog> driver_log;
  base::ScopedTempDir temp_dir;
  scoped_ptr<base::DictionaryValue> capabilities;
  bool auto_reporting_enabled;
  // |command_listeners| should be declared after |xwalk|. When the |Session|
  // is destroyed, |command_listeners| should be freed first, since some
  // |CommandListener|s might be |CommandListenerProxy|s that forward to
  // |DevToolsEventListener|s owned by |xwalk|.
  ScopedVector<CommandListener> command_listeners;
};

Session* GetThreadLocalSession();

void SetThreadLocalSession(scoped_ptr<Session> session);

#endif  // XWALK_TEST_XWALKDRIVER_SESSION_H_
