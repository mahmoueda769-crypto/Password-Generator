[app]

title = Password Generator
package.name = passwordgenerator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# Minimal requirements — python3 version is managed by the NDK toolchain
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True

# Single arch keeps CI fast and avoids out-of-memory on GitHub Actions
android.archs = arm64-v8a

android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
