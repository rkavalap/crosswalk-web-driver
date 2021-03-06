// Copyright (c) 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef XWALK_TEST_XWALKDRIVER_XWALK_NETWORK_CONDITIONS_H_
#define XWALK_TEST_XWALKDRIVER_XWALK_NETWORK_CONDITIONS_H_

#include <string>
#include "base/memory/scoped_ptr.h"

class Status;

struct NetworkConditions {
  NetworkConditions();
  NetworkConditions(bool offline, double latency,
                    double download_throughput, double upload_throughput);
  ~NetworkConditions();
  bool offline;
  double latency;
  double download_throughput;
  double upload_throughput;
};

Status FindPresetNetwork(
    std::string network_name,
    NetworkConditions* network_conditions);

#endif  // XWALK_TEST_XWALKDRIVER_XWALK_NETWORK_CONDITIONS_H_
