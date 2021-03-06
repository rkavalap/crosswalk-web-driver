// Copyright (c) 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef XWALK_TEST_XWALKDRIVER_XWALK_FRAME_TRACKER_H_
#define XWALK_TEST_XWALKDRIVER_XWALK_FRAME_TRACKER_H_

#include <map>
#include <string>

#include "base/compiler_specific.h"
#include "base/macros.h"
#include "xwalk/test/xwalkdriver/xwalk/devtools_event_listener.h"

namespace base {
class DictionaryValue;
class Value;
}

class DevToolsClient;
class Status;

// Tracks execution context creation.
class FrameTracker : public DevToolsEventListener {
 public:
  explicit FrameTracker(DevToolsClient* client);
  ~FrameTracker() override;

  Status GetContextIdForFrame(const std::string& frame_id, int* context_id);

  // Overridden from DevToolsEventListener:
  Status OnConnected(DevToolsClient* client) override;
  Status OnEvent(DevToolsClient* client,
                 const std::string& method,
                 const base::DictionaryValue& params) override;

 private:
  std::map<std::string, int> frame_to_context_map_;

  DISALLOW_COPY_AND_ASSIGN(FrameTracker);
};

#endif  // XWALK_TEST_XWALKDRIVER_XWALK_FRAME_TRACKER_H_
