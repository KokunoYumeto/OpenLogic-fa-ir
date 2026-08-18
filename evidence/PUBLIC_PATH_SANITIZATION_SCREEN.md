# پاک‌سازی مسیرهای عمومی

نسخه‌های اصلی FLS و LOG در خروجی خصوصی ساخت باقی مانده‌اند و منتشر نمی‌شوند.
در نسخه‌های این بسته، همهٔ نمونه‌های نام کاربری و ریشهٔ کاربری ویندوز با
نشانگرهای `<USER>`، `<USER_HOME>` یا `<USERS>` جایگزین شده‌اند. پس از
جایگزینی، جست‌وجوی بایتی برای نام کاربری و دو شکل جداکنندهٔ مسیر Windows
صفر نتیجه داشت.

این پاک‌سازی فقط رسیدهای متنی را تغییر می‌دهد. PDFهای 05 و 06، راه‌اندازها
و فایل‌های هدف ترجمه دست‌نخورده‌اند. هش رسیدهای خام در
`inventories/RAW_BUILD_EVIDENCE_SHA256.tsv` و هش نسخه‌های عمومی در
`inventories/SCREEN_BUNDLE_SHA256.tsv` ثبت می‌شود.

## English descriptor

Private build paths in published FLS and LOG receipts were replaced with
public placeholders. Raw receipt hashes are retained separately. No PDF,
translation source, wrapper, manifest, or binding byte was changed by this
sanitization.
