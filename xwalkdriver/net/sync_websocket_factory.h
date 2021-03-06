// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef XWALK_TEST_XWALKDRIVER_NET_SYNC_WEBSOCKET_FACTORY_H_
#define XWALK_TEST_XWALKDRIVER_NET_SYNC_WEBSOCKET_FACTORY_H_

#include "base/callback.h"
#include "base/memory/scoped_ptr.h"

class SyncWebSocket;
class URLRequestContextGetter;

typedef base::Callback<scoped_ptr<SyncWebSocket>()> SyncWebSocketFactory;

SyncWebSocketFactory CreateSyncWebSocketFactory(
    URLRequestContextGetter* getter);

#endif  // XWALK_TEST_XWALKDRIVER_NET_SYNC_WEBSOCKET_FACTORY_H_
