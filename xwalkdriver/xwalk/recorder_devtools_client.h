// Copyright (c) 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef XWALK_TEST_XWALKDRIVER_XWALK_RECORDER_DEVTOOLS_CLIENT_H_
#define XWALK_TEST_XWALKDRIVER_XWALK_RECORDER_DEVTOOLS_CLIENT_H_

#include <vector>

#include "base/values.h"
#include "xwalk/test/xwalkdriver/xwalk/stub_devtools_client.h"

namespace base {
class DictionaryValue;
}

class Status;

struct Command {
  Command() {}
  Command(const std::string& method, const base::DictionaryValue& params)
      : method(method) {
    this->params.MergeDictionary(&params);
  }
  Command(const Command& command) {
    *this = command;
  }
  Command& operator=(const Command& command) {
    method = command.method;
    params.Clear();
    params.MergeDictionary(&command.params);
    return *this;
  }
  ~Command() {}

  std::string method;
  base::DictionaryValue params;
};

class RecorderDevToolsClient : public StubDevToolsClient {
 public:
  RecorderDevToolsClient();
  ~RecorderDevToolsClient() override;

  // Overridden from StubDevToolsClient:
  Status SendCommandAndGetResult(
      const std::string& method,
      const base::DictionaryValue& params,
      scoped_ptr<base::DictionaryValue>* result) override;

  std::vector<Command> commands_;
};

#endif  // XWALK_TEST_XWALKDRIVER_XWALK_RECORDER_DEVTOOLS_CLIENT_H_
