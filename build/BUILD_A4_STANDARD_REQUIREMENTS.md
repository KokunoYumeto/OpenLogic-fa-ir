# نیازمندی‌های ساخت معیار A4 فارسی ایران OLP-0722

این سند ساخت جاری و اصلاحی نسخهٔ کامل فارسی ایران را توصیف می‌کند. خروجی
جاری صفحهٔ عمودی استاندارد A4 با ابعاد ۲۱۰ × ۲۹۷ میلی‌متر است. ساخت‌های
صفحه‌نمایش پیشین فقط سابقه‌اند و با این ساخت جایگزین شده‌اند.

## هویت و حدود

- نسخه: OLP-0722-A4-STANDARD-20260819
- DOI مفهومی تنها: 10.5281/zenodo.21921852
- DOI دقیق تازه: ندارد؛ اقدام نسخهٔ تازهٔ Zenodo با HTTP 403 رد شد.
- تعهد منبع: 9620cc73f9c8e0ad003c514a5d3748f29611c4c0
- درخت منبع: f67757bb9305b173634082ab4cefd5601a707a34
- تنها پدیدآور: Open Logic Project
- تنها مشارکت‌کننده: AI typesetting & translation، نوع Other

این ساخت هیچ فایل ترجمه، ردیف بیانیهٔ ۷۲۲ واحدی یا مرجع منبع را تغییر
نمی‌دهد. تغییر فقط در راه‌انداز چیدمان، ساخت و اصلاح بسته‌به‌خطای مستطیل
پیوند است.

## ورودی‌های تثبیت‌شده

فایل‌های راه‌انداز به‌علت حفظ نام کار و پیوندهای خارجی پسوند تاریخی
-screen.tex دارند؛ محتوای جاری آن‌ها A4 عمودی است.

| ورودی | بایت | SHA-256 |
|---|---:|---|
| source/locale/fa-IR/open-logic-complete-fa-IR-screen.tex | 2,154 | 5CD40F62DCAD37678CC41E5D660FB1FE0FECF30E9CE3CBEEB466DE4BEA64A9FA |
| source/locale/fa-IR/open-logic-closure-supplement-fa-IR-screen.tex | 2,182 | 98459D24BF0BABF26FF86CBD118B290D17FAEBBD4E7DDBFFCCC3C9E75B57077E |
| source/locale/fa-IR/open-logic-complete-fa-IR.tex | 6,502 | E27F85DBD8C039CCDD8A42FD037414A2AD716173E8142E40D136480767EB70E4 |
| source/locale/fa-IR/open-logic-closure-supplement-fa-IR.tex | 16,275 | 72E222C7983DBC7B445475B9D0CC69294BB775DCF976EFF20648245A0A1688F8 |

FLS نهایی ۷۴۸ ورودی محلی استفاده‌شده را ثبت می‌کند. چهار فایل بالا تنها
تفاوت‌های چیدمانی نسبت به بستهٔ انتشار پیشین‌اند؛ ۷۴۴ ورودی محلی دیگر
بایت‌به‌بایت برابرند. پوشش ترجمه همچنان ۶۴۲ + ۸۰ = ۷۲۲ واحد است.

## ابزارها

- PowerShell 7 یا Windows PowerShell 5.1
- LuaLaTeX و BibTeX از توزیع تثبیت‌شده
- Python 3 با pypdf و PyMuPDF
- build/repair_rtl_link_rects_fa.py
- build/repair_rtl_link_rects_fa_a4.py

برنامه هیچ بسته‌ای دانلود نمی‌کند، Git را اجرا نمی‌کند و مخزن را به‌طور
بازگشتی نمی‌پوید.

## اجرا

پوشهٔ خروجی باید تازه یا خالی باشد:

    pwsh -NoProfile -File .\build\BUILD_A4_STANDARD.ps1 -OutputDirectory <پوشه-پاک-صریح>

برنامه با SOURCE_DATE_EPOCH ثابت، FORCE_SOURCE_DATE=1 و TZ=UTC اجرا می‌شود؛
خوانشگر را با LuaLaTeX، BibTeX و دو گذر پایانی می‌سازد، سپس ضمیمه را در دو
گذر می‌سازد. PDF خام فقط پس از تطابق هش به اصلاح‌گر مستطیل پیوند سپرده
می‌شود.

## دروازه‌های قطعی

| خروجی | صفحه | پیوند | بایت | SHA-256 |
|---|---:|---:|---:|---|
| خوانشگر | 798 | 2,986 | 7,844,397 | B7C622A99E6317ADF9F5CCC903138A7BB1264266889A1F1D1C97094D57D2C3E7 |
| ضمیمه | 113 | 137 | 1,204,824 | 1019D4639FD0F56C17AF618BB877857D4A1BFD2A4EA354D0B164957145D826AB |

- MediaBox و CropBox: 595.276 × 841.89 نقطه؛ معادل A4 عمودی.
- چرخش همهٔ صفحات: صفر.
- نمایش آغازین: /Fit.
- چیدمان: /SinglePage.
- حالت صفحه: /UseOutlines.
- مستطیل پیوند بیرون از صفحه: صفر.
- هش PDF خام خوانشگر:
  FBD13FA9EE4F77B0626E175D1D911E3FEDE4B2E17B8E72648D57FC3E61E6B78B
- هش PDF خام ضمیمه:
  AF01DA08D66B46CAD03BC4145BB2C6C0694B1C4B6659B974A96CA6885EA8ED7F
- هش گزارش نهایی خوانشگر:
  48F38976B368BB8D9BEB94CB2D3A122C205E3221B299E3549918E9B75A88D5E9
- هش گزارش نهایی ضمیمه:
  DC111396E0FEF0EC7E21ADA59CE0F677823F34F7C2AA7D846E2DF230ACA961F0

هر دو گزارش باید صفر خطای TeX، نویسهٔ گمشده، ارجاع تعریف‌نشده، استناد
تعریف‌نشده و درخواست اجرای دوباره داشته باشند.

## اصلاح پیوند

اصلاح‌گر A4 فقط مختصات سوم /Rect، یعنی x1، را برای ۱۴۱ پیوند خوانشگر و
۹ پیوند ضمیمه تغییر می‌دهد. این نگاشت از PDF خام با هش تثبیت‌شده آغاز
می‌شود و در صورت هر تفاوت شکست می‌خورد. محتوای صفحه، مقصدها، کنش‌ها،
شمار پیوند هر صفحه، نشانک‌ها، هندسه، فراداده و همهٔ فیلدهای دیگر annotation
باید برابر بمانند.

## بستهٔ شواهد

دارایی 02_OPENLOGIC_fa-IR_A4_STANDARD_SOURCES_AND_EVIDENCE_OLP-0722.zip
با مسیرهای مرتب، زمان ثابت 2026-08-19T00:00:00Z و فهرست داخلی SHA-256
ساخته می‌شود. دو ساخت مستقل ZIP باید بایت‌به‌بایت برابر باشند. بیانیهٔ
انتشار بیرونی اندازه و SHA-256 دارایی‌های ۰۰ تا ۰۲ را ثبت می‌کند و خود را
عمداً فهرست نمی‌کند.

## English descriptor

Build the complete Iranian Persian edition on standard 210 × 297 mm portrait
A4 pages. Require the frozen wrapper, raw-PDF, final-PDF, and log hashes;
798/113 pages; 2,986/137 links; zero overflow; /Fit, /SinglePage, and
/UseOutlines. The current correction uses the stable concept DOI only and
claims no new Zenodo version DOI.
