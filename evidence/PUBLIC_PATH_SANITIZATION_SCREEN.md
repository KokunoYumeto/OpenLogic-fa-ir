# پاک‌سازی مسیرهای عمومی

گزارش‌های اصلی FLS، LOG، AUX، BBL و BLG در خروجی خصوصی ساخت باقی می‌مانند.
نسخه‌های عمومیِ این بسته با تبدیل مکانیکی زیر ساخته شده‌اند:

- ریشهٔ کامل پوشهٔ کاربر به `<USER_HOME>`؛
- ریشهٔ عمومی کاربران ویندوز به `<USERS_ROOT>`؛
- قطعهٔ نام کاربری که بر اثر شکستن سطر از ریشه جدا شده بود به `<USER>`.

برای هر فایل، بایت و SHA-256 نسخهٔ خام و عمومی در
`evidence/final-build-screen/PUBLIC_PATH_SANITIZATION_RECEIPT.json`
ثبت شده است. بررسی بدون حساسیت به بزرگی حروف برای نام حساب خصوصی در همهٔ
هشت فایل عمومی صفر نتیجه داشت.

این پاک‌سازی فقط رسیدهای متنی را تغییر می‌دهد. PDFهای ۰۵ و ۰۶،
راه‌اندازها، فایل‌های هدف ترجمه، نگاشت اصلاح پیوند و بیانیهٔ بسته‌شدن
دست‌نخورده‌اند.

## English descriptor

Private account and home-directory strings in the published FLS, LOG, AUX,
BBL, and BLG receipts were replaced with stable public placeholders. The
machine-readable receipt records raw and public byte counts and SHA-256 values.
No PDF, translation source, wrapper, closure manifest, or link-repair mapping
was changed by sanitization.
