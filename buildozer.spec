[app]

# عنوان التطبيق
title = Password Generator

# اسم الحزمة (package name)
package.name = passwordgenerator

# نطاق الحزمة
package.domain = org.example

# المجلد الرئيسي للكود
source.dir = .

# الملفات المشمولة
source.include_exts = py,png,jpg,kv,atlas

# إصدار التطبيق
version = 1.0.0

# المتطلبات
requirements = python3,kivy

# الأيقونة (ضع صورة icon.png في نفس المجلد إن أردت)
# icon.filename = %(source.dir)s/icon.png

# شاشة التحميل
# presplash.filename = %(source.dir)s/presplash.png

# توجيه الشاشة
orientation = portrait

# دعم الأجهزة
fullscreen = 0

# إعدادات Android
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True
android.archs = arm64-v8a, armeabi-v7a

# إعدادات iOS (اختياري)
# ios.kivy_ios_url = https://github.com/kivy/kivy-ios
# ios.kivy_ios_branch = master

[buildozer]

# مستوى السجل: 0=error, 1=info, 2=debug
log_level = 2

# حفظ ملفات البناء المؤقتة
warn_on_root = 1
