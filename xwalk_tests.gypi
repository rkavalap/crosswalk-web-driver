{
  'targets': [
    {
      'target_name': 'xwalk_all_tests',
      'type': 'none',
      'dependencies': [
        'xwalk_browsertest',
        'xwalk_unittest',
        'extensions/extensions_tests.gyp:xwalk_extensions_browsertest',
        'extensions/extensions_tests.gyp:xwalk_extensions_unittest',
        'sysapps/sysapps_tests.gyp:xwalk_sysapps_browsertest',
        'sysapps/sysapps_tests.gyp:xwalk_sysapps_unittest',
      ],
      'conditions': [
        ['OS=="linux"', {
          'dependencies': [
            'dbus/xwalk_dbus.gyp:xwalk_dbus_unittests',
          ],
        }],
      ],
    },
    {
      'target_name': 'xwalk_unittest',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../content/content.gyp:content_common',
        '../content/content_shell_and_tests.gyp:test_support_content',
        '../testing/gtest.gyp:gtest',
        '../ui/base/ui_base.gyp:ui_base',
        'test/base/base.gyp:xwalk_test_base',
        'xwalk_application_lib',
        'xwalk_runtime',
      ],
      'sources': [
        'application/browser/application_event_router_unittest.cc',
        'application/browser/application_storage_impl_unittest.cc',
        'application/browser/installer/package_unittest.cc',
        'application/common/application_unittest.cc',
        'application/common/application_file_util_unittest.cc',
        'application/common/id_util_unittest.cc',
        'application/common/manifest_handlers/csp_handler_unittest.cc',
        'application/common/manifest_handlers/main_document_handler_unittest.cc',
        'application/common/manifest_handlers/permissions_handler_unittest.cc',
        'application/common/manifest_handlers/warp_handler_unittest.cc',
        'application/common/manifest_handlers/widget_handler_unittest.cc',
        'application/common/manifest_handler_unittest.cc',
        'application/common/manifest_unittest.cc',
        'runtime/common/xwalk_content_client_unittest.cc',
        'runtime/common/xwalk_runtime_features_unittest.cc',
      ],
      'conditions': [
        ['toolkit_views == 1', {
          'sources': [
            'runtime/browser/ui/top_view_layout_views_unittest.cc',
          ],
          'dependencies': [
            '../skia/skia.gyp:skia',
          ],
        }],
        ['tizen==1', {
          'sources': [
            'application/common/manifest_handlers/navigation_handler_unittest.cc',
          ],
        }],
      ],
    },
    {
      'target_name': 'automation_client_lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../net/net.gyp:net',
        '../third_party/zlib/zlib.gyp:minizip',
        '../third_party/zlib/zlib.gyp:zlib',
        '../third_party/zlib/google/zip.gyp:zip',
        '../ui/events/events.gyp:events',
        '../ui/gfx/gfx.gyp:gfx',
        '../ui/base/ui_base.gyp:ui_base',
        '../url/url.gyp:url_lib',
      ],
      'include_dirs': [
        '..',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)',
        ],
      },
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/js.cc',
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/js.h',
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/user_data_dir.cc',
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/user_data_dir.h',
        'test/xwalkdriver/xwalk/adb_impl.cc',
        'test/xwalkdriver/xwalk/adb_impl.h',
        'test/xwalkdriver/xwalk/android_device.cc',
        'test/xwalkdriver/xwalk/android_device.h',
        'test/xwalkdriver/xwalk/console_logger.cc',
        'test/xwalkdriver/xwalk/console_logger.h',
        'test/xwalkdriver/xwalk/debugger_tracker.cc',
        'test/xwalkdriver/xwalk/debugger_tracker.h',
        'test/xwalkdriver/xwalk/device.h',
        'test/xwalkdriver/xwalk/device_bridge.h',
        'test/xwalkdriver/xwalk/device_manager.cc',
        'test/xwalkdriver/xwalk/device_manager.h',
        'test/xwalkdriver/xwalk/devtools_client.h',
        'test/xwalkdriver/xwalk/devtools_client_impl.cc',
        'test/xwalkdriver/xwalk/devtools_client_impl.h',
        'test/xwalkdriver/xwalk/devtools_event_listener.cc',
        'test/xwalkdriver/xwalk/devtools_event_listener.h',
        'test/xwalkdriver/xwalk/devtools_http_client.cc',
        'test/xwalkdriver/xwalk/devtools_http_client.h',
        'test/xwalkdriver/xwalk/dom_tracker.cc',
        'test/xwalkdriver/xwalk/dom_tracker.h',
        'test/xwalkdriver/xwalk/frame_tracker.cc',
        'test/xwalkdriver/xwalk/frame_tracker.h',
        'test/xwalkdriver/xwalk/geolocation_override_manager.cc',
        'test/xwalkdriver/xwalk/geolocation_override_manager.h',
        'test/xwalkdriver/xwalk/geoposition.h',
        'test/xwalkdriver/xwalk/heap_snapshot_taker.cc',
        'test/xwalkdriver/xwalk/heap_snapshot_taker.h',
        'test/xwalkdriver/xwalk/javascript_dialog_manager.cc',
        'test/xwalkdriver/xwalk/javascript_dialog_manager.h',
        'test/xwalkdriver/xwalk/log.h',
        'test/xwalkdriver/xwalk/log.cc',
        'test/xwalkdriver/xwalk/navigation_tracker.cc',
        'test/xwalkdriver/xwalk/navigation_tracker.h',
        'test/xwalkdriver/xwalk/performance_logger.h',
        'test/xwalkdriver/xwalk/performance_logger.cc',
        'test/xwalkdriver/xwalk/sdb_impl.cc',
        'test/xwalkdriver/xwalk/sdb_impl.h',
        'test/xwalkdriver/xwalk/status.cc',
        'test/xwalkdriver/xwalk/status.h',
        'test/xwalkdriver/xwalk/tizen_device.cc',
        'test/xwalkdriver/xwalk/tizen_device.h',
        'test/xwalkdriver/xwalk/ui_events.cc',
        'test/xwalkdriver/xwalk/ui_events.h',
        'test/xwalkdriver/xwalk/util.cc',
        'test/xwalkdriver/xwalk/util.h',
        'test/xwalkdriver/xwalk/version.cc',
        'test/xwalkdriver/xwalk/version.h',
        'test/xwalkdriver/xwalk/web_view.h',
        'test/xwalkdriver/xwalk/web_view_impl.cc',
        'test/xwalkdriver/xwalk/web_view_impl.h',
        'test/xwalkdriver/xwalk/xwalk.h',
        'test/xwalkdriver/xwalk/xwalk_android_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_android_impl.h',
        'test/xwalkdriver/xwalk/xwalk_desktop_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_desktop_impl.h',
        'test/xwalkdriver/xwalk/xwalk_existing_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_existing_impl.h',
        'test/xwalkdriver/xwalk/xwalk_finder.cc',
        'test/xwalkdriver/xwalk/xwalk_finder.h',
        'test/xwalkdriver/xwalk/xwalk_finder_mac.mm',
        'test/xwalkdriver/xwalk/xwalk_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_impl.h',
        'test/xwalkdriver/xwalk/xwalk_tizen_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_tizen_impl.h',
        'test/xwalkdriver/net/adb_client_socket.cc',
        'test/xwalkdriver/net/adb_client_socket.h',
        'test/xwalkdriver/net/net_util.cc',
        'test/xwalkdriver/net/net_util.h',
        'test/xwalkdriver/net/port_server.cc',
        'test/xwalkdriver/net/port_server.h',
        'test/xwalkdriver/net/sync_websocket.h',
        'test/xwalkdriver/net/sync_websocket_factory.cc',
        'test/xwalkdriver/net/sync_websocket_factory.h',
        'test/xwalkdriver/net/sync_websocket_impl.cc',
        'test/xwalkdriver/net/sync_websocket_impl.h',
        'test/xwalkdriver/net/url_request_context_getter.cc',
        'test/xwalkdriver/net/url_request_context_getter.h',
        'test/xwalkdriver/net/websocket.cc',
        'test/xwalkdriver/net/websocket.h',
      ],
      'actions': [
        {
          'action_name': 'embed_js_in_cpp',
          'inputs': [
            'test/xwalkdriver/cpp_source.py',
            'test/xwalkdriver/embed_js_in_cpp.py',
            'test/xwalkdriver/js/add_cookie.js',
            'test/xwalkdriver/js/call_function.js',
            'test/xwalkdriver/js/dispatch_context_menu_event.js',
            'test/xwalkdriver/js/execute_async_script.js',
            'test/xwalkdriver/js/focus.js',
            'test/xwalkdriver/js/get_element_region.js',
            'test/xwalkdriver/js/is_option_element_toggleable.js',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/js.cc',
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/js.h',
          ],
          'action': [ 'python',
                      'test/xwalkdriver/embed_js_in_cpp.py',
                      '--directory',
                      '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk',
                      'test/xwalkdriver/js/add_cookie.js',
                      'test/xwalkdriver/js/call_function.js',
                      'test/xwalkdriver/js/dispatch_context_menu_event.js',
                      'test/xwalkdriver/js/execute_async_script.js',
                      'test/xwalkdriver/js/focus.js',
                      'test/xwalkdriver/js/get_element_region.js',
                      'test/xwalkdriver/js/is_option_element_toggleable.js',
          ],
          'message': 'Generating sources for embedding js in xwalkdriver',
        },
        {
          'action_name': 'embed_user_data_dir_in_cpp',
          'inputs': [
            'test/xwalkdriver/cpp_source.py',
            'test/xwalkdriver/embed_user_data_dir_in_cpp.py',
            'test/xwalkdriver/xwalk/preferences.txt',
            'test/xwalkdriver/xwalk/local_state.txt',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/user_data_dir.cc',
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/user_data_dir.h',
          ],
          'action': [ 'python',
                      'test/xwalkdriver/embed_user_data_dir_in_cpp.py',
                      '--directory',
                      '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk',
                      'test/xwalkdriver/xwalk/preferences.txt',
                      'test/xwalkdriver/xwalk/local_state.txt',
          ],
          'message': 'Generating sources for embedding user data dir in xwalkdriver',
        },
      ],
      # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
      'msvs_disabled_warnings': [ 4267, ],
    },
    {
      'target_name': 'xwalkdriver_lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'dependencies': [
        'automation_client_lib',
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../crypto/crypto.gyp:crypto',
        '../net/net.gyp:http_server',
        '../net/net.gyp:net',
        '../ui/events/events.gyp:events',
        '../ui/gfx/gfx.gyp:gfx',
        '../ui/base/ui_base.gyp:ui_base',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/version.cc',
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/version.h',
        '../third_party/webdriver/atoms.cc',
        '../third_party/webdriver/atoms.h',
        'test/xwalkdriver/alert_commands.cc',
        'test/xwalkdriver/alert_commands.h',
        'test/xwalkdriver/basic_types.cc',
        'test/xwalkdriver/basic_types.h',
        'test/xwalkdriver/capabilities.cc',
        'test/xwalkdriver/capabilities.h',
        'test/xwalkdriver/command.h',
        'test/xwalkdriver/commands.cc',
        'test/xwalkdriver/commands.h',
        'test/xwalkdriver/element_commands.cc',
        'test/xwalkdriver/element_commands.h',
        'test/xwalkdriver/element_util.cc',
        'test/xwalkdriver/element_util.h',
        'test/xwalkdriver/key_converter.cc',
        'test/xwalkdriver/key_converter.h',
        'test/xwalkdriver/keycode_text_conversion.h',
        'test/xwalkdriver/keycode_text_conversion_x.cc',
        'test/xwalkdriver/logging.cc',
        'test/xwalkdriver/logging.h',
        'test/xwalkdriver/server/http_handler.cc',
        'test/xwalkdriver/server/http_handler.h',
        'test/xwalkdriver/session.cc',
        'test/xwalkdriver/session.h',
        'test/xwalkdriver/session_commands.cc',
        'test/xwalkdriver/session_commands.h',
        'test/xwalkdriver/session_thread_map.h',
        'test/xwalkdriver/util.cc',
        'test/xwalkdriver/util.h',
        'test/xwalkdriver/window_commands.cc',
        'test/xwalkdriver/window_commands.h',
        'test/xwalkdriver/xwalk_launcher.cc',
        'test/xwalkdriver/xwalk_launcher.h',
      ],
      'actions': [
        {
          'action_name': 'embed_version_in_cpp',
          'inputs': [
            'test/xwalkdriver/cpp_source.py',
            'test/xwalkdriver/embed_version_in_cpp.py',
            'test/xwalkdriver/VERSION',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/version.cc',
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/version.h',
          ],
          'action': [ 'python',
                      'test/xwalkdriver/embed_version_in_cpp.py',
                      '--version-file',
                      'test/xwalkdriver/VERSION',
                      '--directory',
                      '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/',
          ],
          'message': 'Generating version info',
        },
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)',
        ],
      },
    },
    {
      'target_name': 'xwalkdriver',
      'type': 'executable',
      'dependencies': [
        'xwalkdriver_lib',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'test/xwalkdriver/server/xwalkdriver_server.cc',
      ],
    },
    {
      'target_name': 'xwalkdriver_unittests',
      'type': 'executable',
      'dependencies': [
        'xwalkdriver_lib',
        '../base/base.gyp:base',
        '../base/base.gyp:run_all_unittests',
        '../net/net.gyp:http_server',
        '../net/net.gyp:net',
        '../testing/gtest.gyp:gtest',
        '../ui/events/events.gyp:events',
        '../ui/gfx/gfx.gyp:gfx',
        '../ui/base/ui_base.gyp:ui_base',
      ],
      'include_dirs': [
        '..,'
      ],
      'sources': [
        'test/xwalkdriver/capabilities_unittest.cc',
        'test/xwalkdriver/commands_unittest.cc',
        'test/xwalkdriver/logging_unittest.cc',
        'test/xwalkdriver/server/http_handler_unittest.cc',
        'test/xwalkdriver/session_commands_unittest.cc',
        'test/xwalkdriver/session_unittest.cc',
        'test/xwalkdriver/util_unittest.cc',
        'test/xwalkdriver/xwalk/console_logger_unittest.cc',
        'test/xwalkdriver/xwalk/devtools_client_impl_unittest.cc',
        'test/xwalkdriver/xwalk/devtools_http_client_unittest.cc',
        'test/xwalkdriver/xwalk/dom_tracker_unittest.cc',
        'test/xwalkdriver/xwalk/frame_tracker_unittest.cc',
        'test/xwalkdriver/xwalk/geolocation_override_manager_unittest.cc',
        'test/xwalkdriver/xwalk/heap_snapshot_taker_unittest.cc',
        'test/xwalkdriver/xwalk/javascript_dialog_manager_unittest.cc',
        'test/xwalkdriver/xwalk/navigation_tracker_unittest.cc',
        'test/xwalkdriver/xwalk/performance_logger_unittest.cc',
        'test/xwalkdriver/xwalk/status_unittest.cc',
        'test/xwalkdriver/xwalk/stub_xwalk.cc',
        'test/xwalkdriver/xwalk/stub_xwalk.h',
        'test/xwalkdriver/xwalk/stub_devtools_client.cc',
        'test/xwalkdriver/xwalk/stub_devtools_client.h',
        'test/xwalkdriver/xwalk/stub_web_view.cc',
        'test/xwalkdriver/xwalk/stub_web_view.h',
        'test/xwalkdriver/xwalk/web_view_impl_unittest.cc',
        'test/xwalkdriver/xwalk/xwalk_finder_unittest.cc',
      ],
    },
    {
      'target_name': 'automation_client_lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../net/net.gyp:net',
        '../third_party/zlib/zlib.gyp:minizip',
        '../third_party/zlib/zlib.gyp:zlib',
        '../third_party/zlib/google/zip.gyp:zip',
        '../ui/events/events.gyp:events',
        '../ui/gfx/gfx.gyp:gfx',
        '../ui/base/ui_base.gyp:ui_base',
        '../url/url.gyp:url_lib',
      ],
      'include_dirs': [
        '..',
        '<(SHARED_INTERMEDIATE_DIR)',
        '/opt/X11/include/',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)',
        ],
       'libraries': [
         '/opt/X11/lib/libX11.dylib',
        ],
      },
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/js.cc',
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/js.h',
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/user_data_dir.cc',
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/user_data_dir.h',
        'test/xwalkdriver/xwalk/adb_impl.cc',
        'test/xwalkdriver/xwalk/adb_impl.h',
        'test/xwalkdriver/xwalk/android_device.cc',
        'test/xwalkdriver/xwalk/android_device.h',
        'test/xwalkdriver/xwalk/console_logger.cc',
        'test/xwalkdriver/xwalk/console_logger.h',
        'test/xwalkdriver/xwalk/debugger_tracker.cc',
        'test/xwalkdriver/xwalk/debugger_tracker.h',
        'test/xwalkdriver/xwalk/device.h',
        'test/xwalkdriver/xwalk/device_bridge.h',
        'test/xwalkdriver/xwalk/device_manager.cc',
        'test/xwalkdriver/xwalk/device_manager.h',
        'test/xwalkdriver/xwalk/devtools_client.h',
        'test/xwalkdriver/xwalk/devtools_client_impl.cc',
        'test/xwalkdriver/xwalk/devtools_client_impl.h',
        'test/xwalkdriver/xwalk/devtools_event_listener.cc',
        'test/xwalkdriver/xwalk/devtools_event_listener.h',
        'test/xwalkdriver/xwalk/devtools_http_client.cc',
        'test/xwalkdriver/xwalk/devtools_http_client.h',
        'test/xwalkdriver/xwalk/dom_tracker.cc',
        'test/xwalkdriver/xwalk/dom_tracker.h',
        'test/xwalkdriver/xwalk/frame_tracker.cc',
        'test/xwalkdriver/xwalk/frame_tracker.h',
        'test/xwalkdriver/xwalk/geolocation_override_manager.cc',
        'test/xwalkdriver/xwalk/geolocation_override_manager.h',
        'test/xwalkdriver/xwalk/geoposition.h',
        'test/xwalkdriver/xwalk/heap_snapshot_taker.cc',
        'test/xwalkdriver/xwalk/heap_snapshot_taker.h',
        'test/xwalkdriver/xwalk/javascript_dialog_manager.cc',
        'test/xwalkdriver/xwalk/javascript_dialog_manager.h',
        'test/xwalkdriver/xwalk/log.h',
        'test/xwalkdriver/xwalk/log.cc',
        'test/xwalkdriver/xwalk/navigation_tracker.cc',
        'test/xwalkdriver/xwalk/navigation_tracker.h',
        'test/xwalkdriver/xwalk/performance_logger.h',
        'test/xwalkdriver/xwalk/performance_logger.cc',
        'test/xwalkdriver/xwalk/sdb_impl.cc',
        'test/xwalkdriver/xwalk/sdb_impl.h',
        'test/xwalkdriver/xwalk/status.cc',
        'test/xwalkdriver/xwalk/status.h',
        'test/xwalkdriver/xwalk/tizen_device.cc',
        'test/xwalkdriver/xwalk/tizen_device.h',
        'test/xwalkdriver/xwalk/ui_events.cc',
        'test/xwalkdriver/xwalk/ui_events.h',
        'test/xwalkdriver/xwalk/util.cc',
        'test/xwalkdriver/xwalk/util.h',
        'test/xwalkdriver/xwalk/version.cc',
        'test/xwalkdriver/xwalk/version.h',
        'test/xwalkdriver/xwalk/web_view.h',
        'test/xwalkdriver/xwalk/web_view_impl.cc',
        'test/xwalkdriver/xwalk/web_view_impl.h',
        'test/xwalkdriver/xwalk/xwalk.h',
        'test/xwalkdriver/xwalk/xwalk_android_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_android_impl.h',
        'test/xwalkdriver/xwalk/xwalk_desktop_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_desktop_impl.h',
        'test/xwalkdriver/xwalk/xwalk_existing_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_existing_impl.h',
        'test/xwalkdriver/xwalk/xwalk_finder.cc',
        'test/xwalkdriver/xwalk/xwalk_finder.h',
        'test/xwalkdriver/xwalk/xwalk_finder_mac.mm',
        'test/xwalkdriver/xwalk/xwalk_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_impl.h',
        'test/xwalkdriver/xwalk/xwalk_tizen_impl.cc',
        'test/xwalkdriver/xwalk/xwalk_tizen_impl.h',
        'test/xwalkdriver/net/adb_client_socket.cc',
        'test/xwalkdriver/net/adb_client_socket.h',
        'test/xwalkdriver/net/net_util.cc',
        'test/xwalkdriver/net/net_util.h',
        'test/xwalkdriver/net/port_server.cc',
        'test/xwalkdriver/net/port_server.h',
        'test/xwalkdriver/net/sync_websocket.h',
        'test/xwalkdriver/net/sync_websocket_factory.cc',
        'test/xwalkdriver/net/sync_websocket_factory.h',
        'test/xwalkdriver/net/sync_websocket_impl.cc',
        'test/xwalkdriver/net/sync_websocket_impl.h',
        'test/xwalkdriver/net/url_request_context_getter.cc',
        'test/xwalkdriver/net/url_request_context_getter.h',
        'test/xwalkdriver/net/websocket.cc',
        'test/xwalkdriver/net/websocket.h',
      ],
      'actions': [
        {
          'action_name': 'embed_js_in_cpp',
          'inputs': [
            'test/xwalkdriver/cpp_source.py',
            'test/xwalkdriver/embed_js_in_cpp.py',
            'test/xwalkdriver/js/add_cookie.js',
            'test/xwalkdriver/js/call_function.js',
            'test/xwalkdriver/js/dispatch_context_menu_event.js',
            'test/xwalkdriver/js/execute_async_script.js',
            'test/xwalkdriver/js/focus.js',
            'test/xwalkdriver/js/get_element_region.js',
            'test/xwalkdriver/js/is_option_element_toggleable.js',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/js.cc',
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/js.h',
          ],
          'action': [ 'python',
                      'test/xwalkdriver/embed_js_in_cpp.py',
                      '--directory',
                      '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk',
                      'test/xwalkdriver/js/add_cookie.js',
                      'test/xwalkdriver/js/call_function.js',
                      'test/xwalkdriver/js/dispatch_context_menu_event.js',
                      'test/xwalkdriver/js/execute_async_script.js',
                      'test/xwalkdriver/js/focus.js',
                      'test/xwalkdriver/js/get_element_region.js',
                      'test/xwalkdriver/js/is_option_element_toggleable.js',
          ],
          'message': 'Generating sources for embedding js in xwalkdriver',
        },
        {
          'action_name': 'embed_user_data_dir_in_cpp',
          'inputs': [
            'test/xwalkdriver/cpp_source.py',
            'test/xwalkdriver/embed_user_data_dir_in_cpp.py',
            'test/xwalkdriver/xwalk/preferences.txt',
            'test/xwalkdriver/xwalk/local_state.txt',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/user_data_dir.cc',
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk/user_data_dir.h',
          ],
          'action': [ 'python',
                      'test/xwalkdriver/embed_user_data_dir_in_cpp.py',
                      '--directory',
                      '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/xwalk',
                      'test/xwalkdriver/xwalk/preferences.txt',
                      'test/xwalkdriver/xwalk/local_state.txt',
          ],
          'message': 'Generating sources for embedding user data dir in xwalkdriver',
        },
      ],
      # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
      'msvs_disabled_warnings': [ 4267, ],
    },
    {
      'target_name': 'xwalkdriver_lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'dependencies': [
        'automation_client_lib',
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../crypto/crypto.gyp:crypto',
        '../net/net.gyp:http_server',
        '../net/net.gyp:net',
        '../ui/events/events.gyp:events',
        '../ui/gfx/gfx.gyp:gfx',
        '../ui/base/ui_base.gyp:ui_base',
      ],
      'include_dirs': [
        '..',
         '/opt/X11/include/',
      ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/version.cc',
        '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/version.h',
        '../third_party/webdriver/atoms.cc',
        '../third_party/webdriver/atoms.h',
        'test/xwalkdriver/alert_commands.cc',
        'test/xwalkdriver/alert_commands.h',
        'test/xwalkdriver/basic_types.cc',
        'test/xwalkdriver/basic_types.h',
        'test/xwalkdriver/capabilities.cc',
        'test/xwalkdriver/capabilities.h',
        'test/xwalkdriver/command.h',
        'test/xwalkdriver/commands.cc',
        'test/xwalkdriver/commands.h',
        'test/xwalkdriver/element_commands.cc',
        'test/xwalkdriver/element_commands.h',
        'test/xwalkdriver/element_util.cc',
        'test/xwalkdriver/element_util.h',
        'test/xwalkdriver/key_converter.cc',
        'test/xwalkdriver/key_converter.h',
        'test/xwalkdriver/keycode_text_conversion.h',
        'test/xwalkdriver/keycode_text_conversion_mac.mm',
        'test/xwalkdriver/logging.cc',
        'test/xwalkdriver/logging.h',
        'test/xwalkdriver/server/http_handler.cc',
        'test/xwalkdriver/server/http_handler.h',
        'test/xwalkdriver/session.cc',
        'test/xwalkdriver/session.h',
        'test/xwalkdriver/session_commands.cc',
        'test/xwalkdriver/session_commands.h',
        'test/xwalkdriver/session_thread_map.h',
        'test/xwalkdriver/util.cc',
        'test/xwalkdriver/util.h',
        'test/xwalkdriver/window_commands.cc',
        'test/xwalkdriver/window_commands.h',
        'test/xwalkdriver/xwalk_launcher.cc',
        'test/xwalkdriver/xwalk_launcher.h',
      ],
      'actions': [
        {
          'action_name': 'embed_version_in_cpp',
          'inputs': [
            'test/xwalkdriver/cpp_source.py',
            'test/xwalkdriver/embed_version_in_cpp.py',
            'test/xwalkdriver/VERSION',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/version.cc',
            '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/version.h',
          ],
          'action': [ 'python',
                      'test/xwalkdriver/embed_version_in_cpp.py',
                      '--version-file',
                      'test/xwalkdriver/VERSION',
                      '--directory',
                      '<(SHARED_INTERMEDIATE_DIR)/xwalk/test/xwalkdriver/',
          ],
          'message': 'Generating version info',
        },
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)',
        ],
         'libraries': [
         '/opt/X11/lib/libX11.dylib',
        ],
      },
    },
    {
      'target_name': 'xwalkdriver',
      'type': 'executable',
      'dependencies': [
        'xwalkdriver_lib',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'test/xwalkdriver/server/xwalkdriver_server.cc',
      ],
    },
    {
      'target_name': 'xwalkdriver_unittests',
      'type': 'executable',
      'dependencies': [
        'xwalkdriver_lib',
        '../base/base.gyp:base',
        '../base/base.gyp:run_all_unittests',
        '../net/net.gyp:http_server',
        '../net/net.gyp:net',
        '../testing/gtest.gyp:gtest',
        '../ui/events/events.gyp:events',
        '../ui/gfx/gfx.gyp:gfx',
        '../ui/base/ui_base.gyp:ui_base',
      ],
      'include_dirs': [
        '..,'
      ],
      'sources': [
        'test/xwalkdriver/capabilities_unittest.cc',
        'test/xwalkdriver/commands_unittest.cc',
        'test/xwalkdriver/logging_unittest.cc',
        'test/xwalkdriver/server/http_handler_unittest.cc',
        'test/xwalkdriver/session_commands_unittest.cc',
        'test/xwalkdriver/session_unittest.cc',
        'test/xwalkdriver/util_unittest.cc',
        'test/xwalkdriver/xwalk/console_logger_unittest.cc',
        'test/xwalkdriver/xwalk/devtools_client_impl_unittest.cc',
        'test/xwalkdriver/xwalk/devtools_http_client_unittest.cc',
        'test/xwalkdriver/xwalk/dom_tracker_unittest.cc',
        'test/xwalkdriver/xwalk/frame_tracker_unittest.cc',
        'test/xwalkdriver/xwalk/geolocation_override_manager_unittest.cc',
        'test/xwalkdriver/xwalk/heap_snapshot_taker_unittest.cc',
        'test/xwalkdriver/xwalk/javascript_dialog_manager_unittest.cc',
        'test/xwalkdriver/xwalk/navigation_tracker_unittest.cc',
        'test/xwalkdriver/xwalk/performance_logger_unittest.cc',
        'test/xwalkdriver/xwalk/status_unittest.cc',
        'test/xwalkdriver/xwalk/stub_xwalk.cc',
        'test/xwalkdriver/xwalk/stub_xwalk.h',
        'test/xwalkdriver/xwalk/stub_devtools_client.cc',
        'test/xwalkdriver/xwalk/stub_devtools_client.h',
        'test/xwalkdriver/xwalk/stub_web_view.cc',
        'test/xwalkdriver/xwalk/stub_web_view.h',
        'test/xwalkdriver/xwalk/web_view_impl_unittest.cc',
        'test/xwalkdriver/xwalk/xwalk_finder_unittest.cc',
      ],
    },
    {
      'target_name': 'xwalk_browsertest',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../content/content.gyp:content_browser',
        '../content/content.gyp:content_common',
        '../content/content_shell_and_tests.gyp:test_support_content',
        '../net/net.gyp:net',
        '../skia/skia.gyp:skia',
        '../testing/gmock.gyp:gmock',
        '../testing/gtest.gyp:gtest',
        '../third_party/libxml/libxml.gyp:libxml',
        '../ui/base/ui_base.gyp:ui_base',
        'test/base/base.gyp:xwalk_test_base',
        'xwalk_application_lib',
        'xwalk_resources',
        'xwalk_runtime',
      ],
      'includes': [
        '../build/filename_rules.gypi',
      ],
      'defines': [
        'HAS_OUT_OF_PROC_TEST_RUNNER',
      ],
      'sources': [
        'application/test/application_browsertest.cc',
        'application/test/application_browsertest.h',
        'application/test/application_event_test.cc',
        'application/test/application_eventapi_test.cc',
        'application/test/application_main_document_browsertest.cc',
        'application/test/application_multi_app_test.cc',
        'application/test/application_testapi.cc',
        'application/test/application_testapi.h',
        'application/test/application_testapi_test.cc',
        'runtime/browser/devtools/xwalk_devtools_browsertest.cc',
        'runtime/browser/geolocation/xwalk_geolocation_browsertest.cc',
        'runtime/browser/ui/taskbar_util_browsertest_win.cc',
        'runtime/browser/xwalk_download_browsertest.cc',
        'runtime/browser/xwalk_form_input_browsertest.cc',
        'runtime/browser/xwalk_runtime_browsertest.cc',
        'runtime/browser/xwalk_switches_browsertest.cc',
      ],
    }
  ],
}
