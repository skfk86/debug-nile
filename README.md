# Debug Nile

تطبيق أندرويد (Capacitor 8) يُبنى تلقائيًا عبر GitHub Actions. ملفات الويب في `www/`.

## أول مرة (من Termux)
```
cd debug-nile-app
git init -b main
git add -A && git commit -m "first commit"
gh repo create debug-nile --private --source=. --push      # بعد gh auth login
```
بعد الدفع افتح تبويب Actions: سيظهر بناء "Android build". عند نجاحه نزّل الملف:
```
gh run download -n app-debug-apk
```
ثم ثبّت ملف `app-debug.apk` على الهاتف.

## تحديث التطبيق
استبدل `www/index.html` ثم: `git add -A && git commit -m "update" && git push`

## نسخة موقّعة للنشر (APK + AAB)
أضف الأسرار الأربعة (KEYSTORE_BASE64 وKEYSTORE_PASSWORD وKEY_ALIAS وKEY_PASSWORD) ثم ادفع وسمًا:
`git tag v1.0.0 && git push --tags` — ستجد الملفات الموقّعة في Releases وفي artifact باسم `app-release-signed`.
خطوات إنشاء المفتاح والأسرار في مهارة capacitor-android-ci (references/signing-and-release.md).

## ملاحظات
- معرّف التطبيق: `com.kairosapp.debugnile` (يتغيّر في `capacitor.config.json` قبل أول نشر فقط).
- مجلد `android/` يُنشأ داخل CI تلقائيًا (`npx cap add android`).
