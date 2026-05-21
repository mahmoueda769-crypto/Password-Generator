[app]

title = Password Generator
package.name = passwordgenerator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# Keep requirements minimal — kivymd removed (not used in main.py)
requirements = python3==3.10.14,kivy==2.3.0

orientation = portrait
fullscreen = 0

# Pin p4a to a stable release tag compatible with kivy 2.3.0
p4a.branch = v2023.09.16

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
