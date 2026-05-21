#!/data/data/com.termux/files/usr/bin/bash
# ============================================================
# Development el dood — Termux APK Builder
# شغّل السكريبت ده في Termux على موبايلك
# ============================================================

set -e  # وقف لو في أي خطأ

echo ""
echo "=============================="
echo "  Development el dood Builder "
echo "=============================="
echo ""

# ── 1. تحديث الحزم ─────────────────────────────────────────
echo "[1/7] تحديث حزم Termux..."
pkg update -y && pkg upgrade -y

# ── 2. تثبيت الأدوات الأساسية ──────────────────────────────
echo "[2/7] تثبيت الأدوات الأساسية..."
pkg install -y \
    python \
    python-pip \
    git \
    wget \
    unzip \
    zip \
    openjdk-17 \
    clang \
    make \
    autoconf \
    automake \
    libtool \
    pkg-config \
    openssl \
    libffi \
    zlib

# ── 3. تثبيت Cython و Buildozer ────────────────────────────
echo "[3/7] تثبيت Cython و Buildozer..."
pip install --upgrade pip wheel
pip install "cython==0.29.37" "buildozer==1.5.0"

# ── 4. إعداد متغيرات Android SDK/NDK ──────────────────────
echo "[4/7] إعداد متغيرات Android..."
export ANDROID_HOME="$HOME/.buildozer/android/platform/android-sdk"
export ANDROIDSDK="$ANDROID_HOME"

# ── 5. الحصول على الكود ────────────────────────────────────
echo "[5/7] جلب الكود من GitHub..."
if [ ! -d "Password-Generator" ]; then
    git clone https://github.com/mahmoueda769-crypto/Password-Generator.git
fi
cd Password-Generator

# ── 6. إصلاح بروتوكول git:// ───────────────────────────────
echo "[6/7] إصلاح بروتوكول git..."
git config --global url."https://".insteadOf git://

# ── 7. بناء الـ APK ────────────────────────────────────────
echo "[7/7] بناء الـ APK (هياخد وقت)..."
buildozer -v android debug

echo ""
echo "=============================="
echo "  تم! الـ APK في مجلد bin/   "
echo "=============================="
ls -lh bin/*.apk 2>/dev/null || echo "مفيش APK — اتفرج على الـ log فوق"
