// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef XWALK_TEST_XWALKDRIVER_XWALK_HEAP_SNAPSHOT_TAKER_H_
#define XWALK_TEST_XWALKDRIVER_XWALK_HEAP_SNAPSHOT_TAKER_H_

#include <string>

#include "base/compiler_specific.h"
#include "base/macros.h"
#include "base/memory/scoped_ptr.h"
#include "xwalk/test/xwalkdriver/xwalk/devtools_event_listener.h"

namespace base {
class DictionaryValue;
class Value;
}

class DevToolsClient;
class Status;

// Take the heap snapshot.
class HeapSnapshotTaker : public DevToolsEventListener {
 public:
  explicit HeapSnapshotTaker(DevToolsClient* client);
  ~HeapSnapshotTaker() override;

  Status TakeSnapshot(scoped_ptr<base::Value>* snapshot);

  // Overridden from DevToolsEventListener:
  Status OnEvent(DevToolsClient* client,
                 const std::string& method,
                 const base::DictionaryValue& params) override;

 private:
  Status TakeSnapshotInternal();

  DevToolsClient* client_;
  std::string snapshot_;

  DISALLOW_COPY_AND_ASSIGN(HeapSnapshotTaker);
};

#endif  // XWALK_TEST_XWALKDRIVER_XWALK_HEAP_SNAPSHOT_TAKER_H_
