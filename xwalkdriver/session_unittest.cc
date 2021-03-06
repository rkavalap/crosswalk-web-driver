// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <string>
#include <utility>

#include "base/memory/scoped_ptr.h"
#include "testing/gtest/include/gtest/gtest.h"
#include "xwalk/test/xwalkdriver/session.h"
#include "xwalk/test/xwalkdriver/xwalk/status.h"
#include "xwalk/test/xwalkdriver/xwalk/stub_web_view.h"
#include "xwalk/test/xwalkdriver/xwalk/stub_xwalk.h"

namespace {

class MockXwalk : public StubXwalk {
 public:
  MockXwalk() : web_view_("1") {}
  ~MockXwalk() override {}

  Status GetWebViewById(const std::string& id, WebView** web_view) override {
    if (id == web_view_.GetId()) {
      *web_view = &web_view_;
      return Status(kOk);
    }
    return Status(kUnknownError);
  }

 private:
  StubWebView web_view_;
};

}  // namespace

TEST(Session, GetTargetWindowNoXwalk) {
  Session session("1");
  WebView* web_view;
  ASSERT_EQ(kNoSuchWindow, session.GetTargetWindow(&web_view).code());
}

TEST(Session, GetTargetWindowTargetWindowClosed) {
  scoped_ptr<Xwalk> xwalk(new MockXwalk());
  Session session("1", std::move(xwalk));
  session.window = "2";
  WebView* web_view;
  ASSERT_EQ(kNoSuchWindow, session.GetTargetWindow(&web_view).code());
}

TEST(Session, GetTargetWindowTargetWindowStillOpen) {
  scoped_ptr<Xwalk> xwalk(new MockXwalk());
  Session session("1", std::move(xwalk));
  session.window = "1";
  WebView* web_view = NULL;
  ASSERT_EQ(kOk, session.GetTargetWindow(&web_view).code());
  ASSERT_TRUE(web_view);
}

TEST(Session, SwitchToParentFrame) {
  scoped_ptr<Xwalk> xwalk(new MockXwalk());
  Session session("1", std::move(xwalk));

  // Initial frame should be top frame.
  ASSERT_EQ(std::string(), session.GetCurrentFrameId());

  // Switching to parent frame should be a no-op.
  session.SwitchToParentFrame();
  ASSERT_EQ(std::string(), session.GetCurrentFrameId());

  session.SwitchToSubFrame("1.1", std::string());
  ASSERT_EQ("1.1", session.GetCurrentFrameId());
  session.SwitchToParentFrame();
  ASSERT_EQ(std::string(), session.GetCurrentFrameId());

  session.SwitchToSubFrame("2.1", std::string());
  ASSERT_EQ("2.1", session.GetCurrentFrameId());
  session.SwitchToSubFrame("2.2", std::string());
  ASSERT_EQ("2.2", session.GetCurrentFrameId());
  session.SwitchToParentFrame();
  ASSERT_EQ("2.1", session.GetCurrentFrameId());
  session.SwitchToParentFrame();
  ASSERT_EQ(std::string(), session.GetCurrentFrameId());
}

TEST(Session, SwitchToTopFrame) {
  scoped_ptr<Xwalk> xwalk(new MockXwalk());
  Session session("1", std::move(xwalk));

  // Initial frame should be top frame.
  ASSERT_EQ(std::string(), session.GetCurrentFrameId());

  // Switching to top frame should be a no-op.
  session.SwitchToTopFrame();
  ASSERT_EQ(std::string(), session.GetCurrentFrameId());

  session.SwitchToSubFrame("3.1", std::string());
  ASSERT_EQ("3.1", session.GetCurrentFrameId());
  session.SwitchToSubFrame("3.2", std::string());
  ASSERT_EQ("3.2", session.GetCurrentFrameId());
  session.SwitchToTopFrame();
  ASSERT_EQ(std::string(), session.GetCurrentFrameId());
}
