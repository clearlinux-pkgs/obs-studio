PKG_NAME := obs-studio
URL = https://github.com/obsproject/obs-studio/archive/30.2.0/obs-studio-30.2.0.tar.gz
ARCHIVES = https://github.com/obsproject/libdshowcapture/archive/ef8c1d2e19c93e664100dd41e1a0df4f8ad45430.tar.gz plugins/win-dshow/libdshowcapture https://github.com/obsproject/obs-browser/archive/b4f724ae6abd371f8f0378f29c908f51065190f3.tar.gz plugins/obs-browser https://github.com/microsoft/ftl-sdk/archive/d0c8469f66806b5ea738d607f7d2b000af8b1129.tar.gz plugins/obs-outputs/ftl-sdk https://github.com/obsproject/obs-websocket/archive/5b4aa9dabd26e488c3556ba83a92b9cef7a032c3.tar.gz plugins/obs-websocket

include ../common/Makefile.common
