// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef XWALK_TEST_XWALKDRIVER_XWALK_MOBILE_DEVICE_H_
#define XWALK_TEST_XWALKDRIVER_XWALK_MOBILE_DEVICE_H_

#include <string>
#include "base/memory/scoped_ptr.h"
#include "xwalk/test/xwalkdriver/xwalk/device_metrics.h"

class Status;

struct MobileDevice {
  MobileDevice();
  ~MobileDevice();
  scoped_ptr<DeviceMetrics> device_metrics;
  std::string user_agent;
};

Status FindMobileDevice(std::string device_name,
                        scoped_ptr<MobileDevice>* mobile_device);

#endif  // XWALK_TEST_XWALKDRIVER_XWALK_MOBILE_DEVICE_H_
