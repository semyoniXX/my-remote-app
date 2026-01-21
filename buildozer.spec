[app]
title = MyRemoteApp
package.name = remoteapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow
orientation = portrait
android.permissions = INTERNET
android.archs = armeabi-v7a, arm64-v8a
android.api = 31
android.minapi = 21
ios.kivy_version = 1.10.1

[buildozer]
log_level = 2
warn_on_root = 1
