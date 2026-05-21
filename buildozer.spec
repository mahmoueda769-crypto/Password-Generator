[app]

title = Password Generator
package.name = passwordgenerator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3==3.11.0,kivy==2.3.0,kivymd

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
