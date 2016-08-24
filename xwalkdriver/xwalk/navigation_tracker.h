// Copyright (c) 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef XWALK_TEST_XWALKDRIVER_XWALK_NAVIGATION_TRACKER_H_
#define XWALK_TEST_XWALKDRIVER_XWALK_NAVIGATION_TRACKER_H_

#include <set>
#include <string>

#include "base/compiler_specific.h"
#include "base/macros.h"
#include "base/memory/scoped_ptr.h"
#include "xwalk/test/xwalkdriver/xwalk/devtools_event_listener.h"
#include "xwalk/test/xwalkdriver/xwalk/status.h"

namespace base {
class DictionaryValue;
}

struct BrowserInfo;
class DevToolsClient;
class JavaScriptDialogManager;
class Status;

// Tracks the navigation state of the page.
class NavigationTracker : public DevToolsEventListener {
 public:
  enum LoadingState {
    kUnknown,
    kLoading,
    kNotLoading,
  };

  NavigationTracker(DevToolsClient* client,
                    const BrowserInfo* browser_info,
                    const JavaScriptDialogManager* dialog_manager);

  NavigationTracker(DevToolsClient* client,
                    LoadingState known_state,
                    const BrowserInfo* browser_info,
                    const JavaScriptDialogManager* dialog_manager);

  ~NavigationTracker() override;

  // Gets whether a navigation is pending for the specified frame. |frame_id|
  // may be empty to signify the main frame.
  Status IsPendingNavigation(const std::string& frame_id, bool* is_pending);

  void set_timed_out(bool timed_out);

  // Overridden from DevToolsEventListener:
  Status OnConnected(DevToolsClient* client) override;
  Status OnEvent(DevToolsClient* client,
                 const std::string& method,
                 const base::DictionaryValue& params) override;
  Status OnCommandSuccess(DevToolsClient* client,
                          const std::string& method,
                          const base::DictionaryValue& result) override;

 private:
  DevToolsClient* client_;
  LoadingState loading_state_;
  const BrowserInfo* browser_info_;
  const JavaScriptDialogManager* dialog_manager_;
  std::set<std::string> pending_frame_set_;
  std::set<std::string> scheduled_frame_set_;
  std::set<int> execution_context_set_;
  std::string dummy_frame_id_;
  int dummy_execution_context_id_;
  bool load_event_fired_;
  bool timed_out_;

  void ResetLoadingState(LoadingState loading_state);
  bool IsExpectingFrameLoadingEvents();

  DISALLOW_COPY_AND_ASSIGN(NavigationTracker);
};

#endif  // XWALK_TEST_XWALKDRIVER_XWALK_NAVIGATION_TRACKER_H_
