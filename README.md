# Password Generator — Kivy Android App

A mobile password generator built with Python and Kivy. Generates strong, random passwords with customizable character types and length. Compiles to an Android APK via Buildozer and GitHub Actions CI.

---

## Features

- Set password length (minimum 4 characters)
- Toggle character types independently:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Special symbols (!@#$…)
- Every selected character type is guaranteed to appear in the output
- One-tap copy to clipboard

---

## Project Structure

```
.
├── main.py                        # Kivy app source code
├── buildozer.spec                 # Android build configuration
├── requirements.txt               # Python dependencies
└── .github/
    └── workflows/
        └── build.yml              # GitHub Actions CI — builds APK automatically
```

---

## Run Locally (Desktop)

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

> On Linux you may also need:
> ```bash
> sudo apt-get install python3-kivy
> ```

### 2. Run the app

```bash
python main.py
```

The app window opens at 360×640 px to simulate a mobile screen.

---

## Build Android APK

### Option A — GitHub Actions (recommended)

Push to the `main` branch. The workflow at `.github/workflows/build.yml` builds the APK automatically.

1. Go to your repository on GitHub.
2. Click **Actions** → select the latest run.
3. Download the APK from the **Artifacts** section (`password-generator-apk`).

The APK is kept for **30 days** per run.

### Option B — Build locally

#### Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.11 |
| Buildozer | 1.5.0 |
| Cython | 0.29.37 |
| Java JDK | 17 |

#### Steps

```bash
# Install Buildozer
pip install buildozer cython==0.29.37

# Build debug APK
buildozer -v android debug
```

The APK will be created at `bin/passwordgenerator-1.0.0-arm64-v8a_armeabi-v7a-debug.apk`.

#### Install on device

```bash
buildozer android deploy run
```

Or copy the APK to your device and install manually (enable *Install unknown apps* in Android settings).

---

## Configuration (`buildozer.spec`)

| Setting | Value |
|---------|-------|
| Package name | `org.example.passwordgenerator` |
| Min Android API | 21 (Android 5.0) |
| Target Android API | 33 (Android 13) |
| Architectures | `arm64-v8a`, `armeabi-v7a` |
| Orientation | Portrait |

To change the app icon, add an `icon.png` file to the project root and uncomment the `icon.filename` line in `buildozer.spec`.

---

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Kivy password generator"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

Replace `<your-username>` and `<your-repo>` with your actual GitHub username and repository name. The CI pipeline starts automatically on the first push.

---

## License

MIT
