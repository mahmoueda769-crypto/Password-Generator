[app]

title = Development el dood
package.name = passwordgenerator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# Minimal — python3 version is managed internally by the NDK toolchain
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# Target API and NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# 32-bit only — faster CI build, lower memory usage, wider device compatibility
android.archs = armeabi-v7a
# android.archs = arm64-v8a  ← disabled

android.private_storage = True
android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
