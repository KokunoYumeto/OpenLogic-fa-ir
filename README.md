# متن منطق باز — نسخهٔ کامل فارسی ایران با بازچینی افزوده برای صفحه‌نمایش

این مخزن نسخهٔ مستقل و کامل فارسی ایران از متن پروژهٔ منطق باز برای منبع
تثبیت‌شده است. انتشار `OLP-0722-SCREEN-20260818` دو پی‌دی‌اف افزوده برای
مطالعه روی صفحه‌نمایش فراهم می‌کند و همهٔ دارایی‌های چاپی انتشار
`OLP-0722-20260818` را بدون تغییر بایتی نگه می‌دارد.

## هویت انتشار

- DOI مفهومی پایدار فارسی ایران: [10.5281/zenodo.21921852](https://doi.org/10.5281/zenodo.21921852)
- آخرین DOI دقیقِ منتشرشده در Zenodo پیش از این انتشار صفحه‌نمایش: [10.5281/zenodo.21987687](https://doi.org/10.5281/zenodo.21987687)، ویژهٔ انتشار چاپی `OLP-0722-20260818`
- انتشار افزودهٔ GitHub: [fa-ir-olp-0722-screen-20260818](https://github.com/KokunoYumeto/OpenLogic-fa-ir/releases/tag/fa-ir-olp-0722-screen-20260818)
- نسخه: `OLP-0722-SCREEN-20260818`
- زبان: فارسی معیار دانشگاهی ایران (`fa-IR`؛ کد Zenodo: `fas`)
- تنها نویسنده و پدیدآور در فرادادهٔ استناد: `Open Logic Project`
- مرجع منبع: تعهد `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
- درخت منبع: `f67757bb9305b173634082ab4cefd5601a707a34`
- مجوز: CC BY 4.0، مگر آنکه یک مؤلفه به‌صراحت خلاف آن را اعلام کند

برای انتشار صفحه‌نمایش هنوز DOI دقیق و جداگانه‌ای در Zenodo ادعا نمی‌شود.
پروندهٔ `.zenodo.json` فرادادهٔ زبان‌محورِ آماده برای نسخهٔ تازهٔ آینده است؛
رکوردهای منتشرشدهٔ پیشین Zenodo دست‌کاری نشده‌اند.

## دامنه و دو چیدمان

محتوا در چیدمان چاپی و چیدمان صفحه‌نمایش یکسان است:

- خوانشگر پیونددار اصلی: 642 واحد.
- ضمیمهٔ فنی مستقل: 80 واحد بیرون از مسیر خوانشگر.
- حساب کامل: 642 + 80 = 722 واحد.

چیدمان چاپی در 839 و 127 صفحه باقی می‌ماند. بازچینی صفحه‌نمایش همان محتوا را
با قلم 12 نقطه، سطح متن گسترده‌تر، حاشیه‌های متقارن و نمای آغازین متناسب با
عرض صفحه، در 748 و 108 صفحه عرضه می‌کند. این خروجی ثابت است؛ سند واکنش‌گرا
یا بازروان‌شوندهٔ واقعی نیست.

## دارایی‌های انتشار

| شماره | دارایی | کارکرد |
|---:|---|---|
| 00 | `00_OPENLOGIC_fa-IR_COMPLETE_LINKED_READER_OLP-0722.pdf` | خوانشگر چاپی کامل، بدون تغییر بایتی |
| 01 | `01_OPENLOGIC_fa-IR_CLOSURE_SUPPLEMENT_80_UNITS_OLP-0722.pdf` | ضمیمهٔ چاپی، بدون تغییر بایتی |
| 02 | `02_OPENLOGIC_fa-IR_EDITABLE_SOURCES_OLP-0722.zip` | منابع کامل و قابل ویرایش انتشار پایه |
| 03 | `03_OPENLOGIC_fa-IR_EVIDENCE_AND_PROVENANCE_OLP-0722.zip` | شواهد و منشأ انتشار پایه |
| 04 | `04_OPENLOGIC_fa-IR_SHA256_MANIFEST_OLP-0722.txt` | هش‌های دارایی‌های 00 تا 03 |
| 05 | `05_OPENLOGIC_fa-IR_COMPLETE_LINKED_READER_SCREEN_OLP-0722.pdf` | خوانشگر بازچینی‌شده برای صفحه‌نمایش، 748 صفحه |
| 06 | `06_OPENLOGIC_fa-IR_CLOSURE_SUPPLEMENT_80_UNITS_SCREEN_OLP-0722.pdf` | ضمیمهٔ بازچینی‌شده برای صفحه‌نمایش، 108 صفحه |
| 07 | `07_OPENLOGIC_fa-IR_SCREEN_LAYOUT_SOURCES_AND_EVIDENCE_OLP-0722.zip` | راه‌اندازهای افزوده، دستور ساخت و شواهد ساخت/QA صفحه‌نمایش |
| 08 | `08_OPENLOGIC_fa-IR_SHA256_MANIFEST_SCREEN_UPDATE_OLP-0722.txt` | هش‌های SHA-256 دارایی‌های 00 تا 07 |

بیانیهٔ 08 خود را هش نمی‌کند. هر سطر از 64 رقم شانزدهی بزرگ، دو فاصله و نام
پایهٔ دارایی تشکیل شده است.

## ساخت بازتولیدپذیر

ساخت چاپی با `build/BUILD.ps1` و ساخت صفحه‌نمایش با
`build/BUILD_SCREEN.ps1` انجام می‌شود. ساخت صفحه‌نمایش ابتدا خوانشگر را با
LuaLaTeX و BibTeX می‌سازد و سپس ضمیمه را با ارجاع به AUX همان خوانشگر می‌سازد.
برنامه شمار صفحه، DOI مفهومی، نبود DOI دقیقِ نسخه در راه‌اندازها و هش‌های
اختیاری را کنترل می‌کند و از بازنویسی هر دارایی انتشار خودداری می‌کند.

جزئیات در `build/BUILD_REQUIREMENTS.md` و
`build/BUILD_SCREEN_REQUIREMENTS.md` آمده است.

## حدود اعلام‌شده

- پی‌دی‌اف‌ها برچسب‌گذاری ساختاری و گواهی PDF/UA یا تأیید دسترس‌پذیری ندارند.
- استخراج Unicode ریاضیات، نیم‌فاصله‌ها و ترتیب برخی مؤلفه‌های راست‌به‌چپ کاملاً مرجع نیست؛ فایل‌های TeX قابل ویرایش مرجع متنی‌اند.
- هیچ بازبینی انسانی یا بومیِ فارسی‌زبان یا تأیید جامعهٔ زبانی ادعا نمی‌شود.
- این نسخهٔ مستقل به معنای تأیید پروژهٔ منطق باز نیست.
- رابطهٔ موردنظر با منبع، اشتقاق/ترجمه از تعهد تثبیت‌شده است؛ برای مجموعهٔ جهانیِ ناموجود رابطهٔ `IsPartOf` ساخته نمی‌شود.

## English descriptor

This repository contains the independently maintained complete Iranian
Persian edition of *The Open Logic Text*. The additive
`OLP-0722-SCREEN-20260818` release preserves the existing print assets
byte-for-byte and adds a 642-unit, 748-page linked reader plus an 80-unit,
108-page closure supplement retypeset for on-screen reading. These PDFs use a
fixed Letter page with larger type, a wider text block, symmetric margins, and
FitH opening behavior; they are not genuinely responsive or reflowable. They
remain untagged and are not PDF/UA certified. No separate Zenodo version DOI is
claimed until a new Zenodo version is actually published.
