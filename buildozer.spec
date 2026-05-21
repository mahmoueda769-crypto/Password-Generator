[app]

title = Development el dood
package.name = passwordgenerator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# SDK/NDK paths are injected via ANDROIDSDK/ANDROIDNDK env vars in CI
# python3 version is managed by the NDK toolchain — do not pin it
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# 32-bit — faster build, wider device support, lower memory usage
android.archs = armeabi-v7a

android.private_storage = True
android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
