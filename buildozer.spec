[app]

title = Development el dood
package.name = passwordgenerator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0.0

# Core requirements — python3 version is handled by the NDK toolchain
requirements = python3,kivy==2.3.0,cryptography

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# Android API — target 34 (Android 14, latest stable)
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# 32-bit only — widest device support, lower memory use in CI
android.archs = armeabi-v7a

android.private_storage = True
android.allow_backup = True

# android.sdk_path and android.ndk_path are injected at CI build time via sed

[buildozer]

# Full verbose logging — catches every warning and env issue
log_level = 2
warn_on_root = 1
