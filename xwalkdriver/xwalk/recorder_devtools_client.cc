// Copyright (c) 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "xwalk/test/xwalkdriver/xwalk/recorder_devtools_client.h"
#include "xwalk/test/xwalkdriver/xwalk/status.h"

RecorderDevToolsClient::RecorderDevToolsClient() {}

RecorderDevToolsClient::~RecorderDevToolsClient() {}

Status RecorderDevToolsClient::SendCommandAndGetResult(
    const std::string& method,
    const base::DictionaryValue& params,
    scoped_ptr<base::DictionaryValue>* result) {
  commands_.push_back(Command(method, params));

  // For any tests that directly call SendCommandAndGetResults, we'll just
  // always return { "result": true }. Currently only used when testing
  // "canEmulateNetworkConditions".
  (*result).reset(new base::DictionaryValue);
  (*result)->SetBoolean("result", true);
  return Status(kOk);
}
