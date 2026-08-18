# متن منطق باز — نسخهٔ کامل فارسی ایران برای منبع تثبیت‌شده

این نسخهٔ مستقل و کامل فارسی ایران از متن پروژهٔ منطق باز در انتشار
`OLP-0722-20260818` است. بسته‌شدن ترجمه همهٔ 722 واحد محتوایی
منبع تثبیت‌شده را پوشش می‌دهد.

## هویت انتشار

- DOI مفهومی پایدار فارسی ایران: [10.5281/zenodo.21921852](https://doi.org/10.5281/zenodo.21921852)
- DOI دقیق این نسخه: [10.5281/zenodo.21987687](https://doi.org/10.5281/zenodo.21987687)
- انتشار GitHub: [fa-ir-olp-0722-20260818](https://github.com/KokunoYumeto/OpenLogic-fa-ir/releases/tag/fa-ir-olp-0722-20260818)
- نسخه: `OLP-0722-20260818`
- زبان: فارسی معیار دانشگاهی ایران (`fa-IR`؛ کد Zenodo: `fas`)
- تنها نویسنده و پدیدآور در فرادادهٔ استناد: `Open Logic Project`
- تنها مشارکت‌کننده: `AI typesetting & translation` با نقش Zenodo «Other»، بدون شناسه یا وابستگی سازمانی
- مرجع منبع: تعهد `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
- درخت منبع: `f67757bb9305b173634082ab4cefd5601a707a34`
- مجوز: CC BY 4.0، مگر آنکه یک مؤلفه به‌صراحت خلاف آن را اعلام کند

## دامنهٔ بسته‌شدن

- خوانشگر پیونددارِ اصلی: 642 واحد در مسیر کتاب، در 839 صفحه.
- ضمیمهٔ فنی و مستقل بسته‌شدن: 80 واحد نگه‌داشته‌شده بیرون از مسیر خوانشگر، در 127 صفحه.
- حساب کامل: 642 + 80 = 722 واحد.

ضمیمه به‌عنوان شاهد فنیِ بسته‌شدن ترجمه و ساخت منتشر می‌شود، اما بخشی از
ترتیب اصلی خوانش کتاب نیست و ساختار خوانشگر را تغییر نمی‌دهد.

## دارایی‌های انتشار

| شماره | دارایی | کارکرد |
|---:|---|---|
| 00 | `00_OPENLOGIC_fa-IR_COMPLETE_LINKED_READER_OLP-0722.pdf` | خوانشگر کامل و پیونددار فارسی ایران |
| 01 | `01_OPENLOGIC_fa-IR_CLOSURE_SUPPLEMENT_80_UNITS_OLP-0722.pdf` | ضمیمهٔ فنی 80 واحد نگه‌داشته‌شده |
| 02 | `02_OPENLOGIC_fa-IR_EDITABLE_SOURCES_OLP-0722.zip` | منابع TeX قابل ویرایش و ورودی‌های دقیق ساخت |
| 03 | `03_OPENLOGIC_fa-IR_EVIDENCE_AND_PROVENANCE_OLP-0722.zip` | شواهد منبع، ساخت، نمایش، استخراج و منشأ |
| 04 | `04_OPENLOGIC_fa-IR_SHA256_MANIFEST_OLP-0722.txt` | هش‌های SHA-256 دارایی‌های 00 تا 03 |

هیچ نسخه‌ای در یک پوشهٔ ساختِ کاری، دارایی منتشرشده نیست. بایت‌ها و هش‌های
نهایی فقط پس از موفقیت ساخت نهایی و بازسازی مستقل در بیانیهٔ SHA-256
ثبت می‌شوند.

## ساخت بازتولیدپذیر

`build/BUILD.ps1` ابتدا خوانشگر کامل را با LuaLaTeX و BibTeX می‌سازد،
سپس ضمیمه را دو بار با حل ارجاع‌ها از AUX خوانشگر می‌سازد. برنامه
`SOURCE_DATE_EPOCH` و منطقهٔ زمانی را تثبیت می‌کند، شمار صفحه‌ها را
می‌سنجد، می‌تواند هش‌های مورد انتظار را بررسی کند، و فقط با کلید صریح
`-StageReleaseAssets` دو PDF نهایی را در سطح انتشار قرار می‌دهد.

نیازمندی‌های محیط و گام‌های دقیق در `build/BUILD_REQUIREMENTS.md` آمده‌اند.

## محدودیت‌های اعلام‌شده

- دو PDF برچسب‌گذاری ساختاری ندارند و گواهی PDF/UA یا تأیید دسترس‌پذیری ندارند.
- استخراج Unicode ریاضیات، نیم‌فاصله‌ها و ترتیب برخی مؤلفه‌های راست‌به‌چپ کاملاً مرجع نیست؛ فایل‌های TeX قابل ویرایش مرجع متنی‌اند.
- هیچ بازبینی انسانی یا بومیِ فارسی‌زبان یا تأیید جامعهٔ زبانی ادعا نمی‌شود.
- این نسخهٔ مستقل به معنای تأیید پروژهٔ منطق باز نیست.
- رابطهٔ موردنظر با منبع، اشتقاق/ترجمه از تعهد تثبیت‌شده است؛ برای مجموعهٔ جهانیِ ناموجود رابطهٔ `IsPartOf` ساخته نمی‌شود.

## English descriptor

This is the independently maintained complete Iranian Persian edition of
*The Open Logic Text* for the frozen Open Logic source release. Version
`OLP-0722-20260818` closes all 722 translation units as a 642-unit, 839-page
canonical linked reader plus a separate 80-unit, 127-page technical closure
supplement. The PDFs are untagged; mathematical, ZWNJ, and RTL extraction is
not fully authoritative; editable TeX is authoritative. No Persian-speaking
human/native review, community approval, accessibility certification, or
Open Logic Project endorsement is claimed.
