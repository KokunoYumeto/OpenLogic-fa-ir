# متن منطق باز — نسخهٔ معیار A4 فارسی ایران

*متن منطق باز* یک کتاب درسی باز و مشارکتی در منطق صوری برای مطالعهٔ دقیق
در سطح میانی است. این مخزن نسخهٔ مستقل و کامل فارسی ایران را عرضه می‌کند:
همهٔ ۷۲۲ واحد منبع تثبیت‌شده، شامل خوانشگر پیونددار ۶۴۲ واحدی و ضمیمهٔ
فنی ۸۰ واحدی.

نسخهٔ جاری OLP-0722-A4-STANDARD-20260819 است. هر دو PDF روی صفحهٔ
استاندارد A4 عمودی با ابعاد ۲۱۰ × ۲۹۷ میلی‌متر حروف‌چینی شده‌اند. نمایش
آغازین /Fit، چیدمان /SinglePage و حالت /UseOutlines است؛ بنابراین صفحهٔ
کامل عمودی گشوده می‌شود و فهرست نشانک‌ها در دسترس است.

## هویت انتشار

- انتشار جاری GitHub:
  [fa-ir-olp-0722-a4-standard-20260819](https://github.com/KokunoYumeto/OpenLogic-fa-ir/releases/tag/fa-ir-olp-0722-a4-standard-20260819)
- نسخه: OLP-0722-A4-STANDARD-20260819
- DOI مفهومی پایدار فارسی ایران:
  [10.5281/zenodo.21921852](https://doi.org/10.5281/zenodo.21921852)
- وضعیت Zenodo برای این اصلاح: ایجاد نسخهٔ تازه مجاز نشد (403 Forbidden)؛
  در نتیجه DOI دقیق تازه‌ای ادعا یا ثبت نشده و فقط DOI مفهومی به‌کار می‌رود.
- زبان: فارسی معیار دانشگاهی ایران (fa-IR؛ کد Zenodo: fas)
- تنها پدیدآور/نویسنده در فراداده: Open Logic Project
- تنها مشارکت‌کنندهٔ فنی: AI typesetting & translation با نوع Other؛
  این مشارکت‌کننده نویسنده یا پدیدآور نیست و شناسه یا وابستگی سازمانی ندارد.
- مرجع منبع: تعهد 9620cc73f9c8e0ad003c514a5d3748f29611c4c0
- درخت منبع: f67757bb9305b173634082ab4cefd5601a707a34
- مجوز: CC BY 4.0، مگر آنکه مؤلفه‌ای صریحاً مجوز دیگری داشته باشد.

## خروجی‌های معیار A4

| دارایی | کارکرد |
|---|---|
| 00_OPENLOGIC_fa-IR_COMPLETE_LINKED_READER_A4_STANDARD_OLP-0722.pdf | خوانشگر کامل ۶۴۲ واحدی، ۷۹۸ صفحه |
| 01_OPENLOGIC_fa-IR_CLOSURE_SUPPLEMENT_80_UNITS_A4_STANDARD_OLP-0722.pdf | ضمیمهٔ فنی ۸۰ واحدی، ۱۱۳ صفحه |
| 02_OPENLOGIC_fa-IR_A4_STANDARD_SOURCES_AND_EVIDENCE_OLP-0722.zip | راه‌اندازها، سازنده، شواهد ساخت، اصلاح پیوند و QA |
| 03_OPENLOGIC_fa-IR_SHA256_MANIFEST_A4_STANDARD_OLP-0722.txt | اندازه و SHA-256 دارایی‌های ۰۰ تا ۰۲ |

خوانشگر کامل ۷٬۸۴۴٬۳۹۷ بایت و SHA-256
B7C622A99E6317ADF9F5CCC903138A7BB1264266889A1F1D1C97094D57D2C3E7
است. ضمیمه ۱٬۲۰۴٬۸۲۴ بایت و SHA-256
1019D4639FD0F56C17AF618BB877857D4A1BFD2A4EA354D0B164957145D826AB
است.

هندسهٔ همهٔ صفحات دقیقاً A4 عمودی است؛ چرخش صفر است. شمار پیوندها در
خوانشگر و ضمیمه به‌ترتیب ۲۹۸۶ و ۱۳۷ است و شمار مستطیل‌های پیوند بیرون از
صفحه پس از اصلاح بسته‌به‌خطا صفر است. محتوای صفحه، مقصدهای پیوند، نشانک‌ها
و فراداده در اصلاح مستطیل‌های پیوند تغییر نکرده‌اند.

## ساخت بازتولیدپذیر

ساخت جاری با این فرمان اجرا می‌شود:

    pwsh -NoProfile -File .\build\BUILD_A4_STANDARD.ps1 -OutputDirectory <پوشه-پاک-صریح>

فایل‌های راه‌انداز به‌دلیل حفظ پیوندهای داخلی نام تاریخی -screen.tex را
نگه داشته‌اند، اما محتوای جاری آن‌ها فقط A4 عمودی است. هش راه‌انداز کامل
5CD40F62DCAD37678CC41E5D660FB1FE0FECF30E9CE3CBEEB466DE4BEA64A9FA
و هش راه‌انداز ضمیمه
98459D24BF0BABF26FF86CBD118B290D17FAEBBD4E7DDBFFCCC3C9E75B57077E
است. جزئیات در
[build/BUILD_A4_STANDARD_REQUIREMENTS.md](build/BUILD_A4_STANDARD_REQUIREMENTS.md)
آمده است.

## انتشارهای پیشین

انتشار چاپی
[fa-ir-olp-0722-20260818](https://github.com/KokunoYumeto/OpenLogic-fa-ir/releases/tag/fa-ir-olp-0722-20260818)
و همهٔ دارایی‌های آن بدون تغییر حفظ شده‌اند.

دو انتشار صفحه‌نمایش پیشین نیز برای سابقه و بازتولیدپذیری بدون حذف یا
بازنویسی دارایی نگه داشته شده‌اند، اما هر دو با انتشار معیار A4 جایگزین
شده‌اند:

- [fa-ir-olp-0722-screen-20260818](https://github.com/KokunoYumeto/OpenLogic-fa-ir/releases/tag/fa-ir-olp-0722-screen-20260818)
- [fa-ir-olp-0722-reflow-16x9-20260819](https://github.com/KokunoYumeto/OpenLogic-fa-ir/releases/tag/fa-ir-olp-0722-reflow-16x9-20260819)

## حدود اعلام‌شده

- PDFها برچسب‌گذاری ساختاری و گواهی PDF/UA ندارند.
- استخراج Unicode ریاضیات، نیم‌فاصله‌ها و ترتیب برخی مؤلفه‌های راست‌به‌چپ
  کاملاً مرجع نیست؛ فایل‌های TeX قابل ویرایش مرجع متنی‌اند.
- هیچ بازبینی انسانی یا بومی فارسی‌زبان، تأیید جامعهٔ زبانی یا تأیید پروژهٔ
  منطق باز ادعا نمی‌شود.

## English descriptor

This repository contains the complete 722-unit Iranian Persian edition of
*The Open Logic Text*: a 642-unit linked reader and an 80-unit technical
supplement. The current release, OLP-0722-A4-STANDARD-20260819, uses
standard 210 × 297 mm portrait A4 pages and opens with /Fit, /SinglePage,
and /UseOutlines. The reader has 798 pages and the supplement 113 pages.
Both earlier screen releases are preserved but superseded. Zenodo returned
HTTP 403 for a new-version action, so this correction uses only the stable
concept DOI 10.5281/zenodo.21921852 and claims no new exact DOI.
