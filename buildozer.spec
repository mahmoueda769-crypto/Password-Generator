[app]

title = Development el dood
package.name = passwordgenerator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# python3 version managed by NDK toolchain — do not pin
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# 32-bit only — faster CI, wider device support
android.archs = armeabi-v7a

android.private_storage = True
android.allow_backup = True

# android.sdk_path and android.ndk_path are appended by CI at build time

[buildozer]

log_level = 2
warn_on_root = 1
