# نیازمندی‌های ساخت بازچینی صفحه‌نمایش فارسی ایران OLP-0722

این سند ساخت افزودهٔ دو پی‌دی‌اف ثابت و مناسب مطالعه روی صفحه‌نمایش را شرح
می‌دهد. ساخت چاپی و دارایی‌های 00 تا 04 دست‌نخورده باقی می‌مانند.

## هویت و خروجی تثبیت‌شده

- نسخه: `OLP-0722-SCREEN-20260818`
- DOI مفهومی پایدار: `10.5281/zenodo.21921852`
- DOI دقیق نسخه در راه‌اندازها درج نمی‌شود، زیرا نسخهٔ تازهٔ Zenodo هنوز منتشر نشده است.
- تعهد منبع: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
- خوانشگر صفحه‌نمایش: 748 صفحه، 7,666,348 بایت، SHA-256 `A4B7BEAC391B9C8704BA970B9422913D5236E3C6B4E0F123170D74D08771993C`
- ضمیمهٔ صفحه‌نمایش: 108 صفحه، 1,185,336 بایت، SHA-256 `710116E91278A63C362F523C93F1916458048A2B1B1E5A0E7942DA39840F38C0`

## ورودی‌ها

- `source/locale/fa-IR/open-logic-complete-fa-IR-screen.tex`
- `source/locale/fa-IR/open-logic-closure-supplement-fa-IR-screen.tex`
- دو راه‌انداز پایهٔ متناظر و همهٔ 722 فایل هدف موجود در بستهٔ منبع OLP-0722
- کتاب‌نامه و سبک BibTeX زیر `source/bib/`
- خطوط تثبیت‌شدهٔ Scheherazade زیر `00_control/fonts/scheherazade-2.100/`

راه‌اندازهای صفحه‌نمایش تنها هندسه، اندازهٔ قلم، زیرعنوان و رفتار آغاز PDF را
می‌افزایند و سپس راه‌اندازهای پایهٔ تثبیت‌شده را ورودی می‌گیرند. هیچ فایل هدف
ترجمه، بیانیهٔ بسته‌شدن یا اتصال واحدها در این انتشار تغییر نکرده است.

## ابزارها و توالی

- PowerShell 7 یا Windows PowerShell 5.1
- LuaLaTeX، BibTeX و Poppler `pdfinfo`
- همان محیط تثبیت‌شدهٔ MiKTeX و خطوط ثبت‌شده در شواهد OLP-0722

`BUILD_SCREEN.ps1` مقدارهای `SOURCE_DATE_EPOCH=1783874174`،
`FORCE_SOURCE_DATE=1` و `TZ=UTC` را فقط برای فرایند ساخت تنظیم می‌کند و سپس
مقدارهای پیشین را بازمی‌گرداند. خوانشگر سه بار با یک گذر BibTeX میان گذر اول
و دوم ساخته می‌شود؛ سپس ضمیمه دو بار با AUX خوانشگر صفحه‌نمایش ساخته می‌شود.

اجرای پاک و بررسی هش‌های نهایی:

```powershell
pwsh -NoProfile -File .\build\BUILD_SCREEN.ps1 `
  -OutputDirectory <پوشه-پاک-صریح> `
  -ExpectedCompleteSha256 A4B7BEAC391B9C8704BA970B9422913D5236E3C6B4E0F123170D74D08771993C `
  -ExpectedSupplementSha256 710116E91278A63C362F523C93F1916458048A2B1B1E5A0E7942DA39840F38C0
```

برنامه هیچ دانلود، اجرای Git یا پویش سامانهٔ فایل ندارد. کلید
`-StageReleaseAssets` فقط برای مرحله‌بندی اولیهٔ 05 و 06 است و اگر مقصدی وجود
داشته باشد، از بازنویسی آن خودداری می‌کند.

## دروازه‌های پذیرش

- 748 و 108 صفحه، بدون رمزگذاری، در اندازهٔ Letter.
- نمای آغاز `/FitH`، چیدمان `/OneColumn` و پنل نشانک‌ها `/UseOutlines`.
- وجود DOI مفهومی و نبود DOI دقیق پیشین یا فعلی در هر دو راه‌انداز.
- همگرایی LuaLaTeX/BibTeX و نبود خطای توقف در گزارش‌ها.
- یکسانی بایتی دو ساخت پاک مستقل.
- تطابق هش‌های راه‌اندازها و PDFها با موجودی انتشار.
- حفظ بایتی دارایی‌های چاپی 00 تا 04.

این دروازه‌ها ادعای سند واکنش‌گرا، بازروان‌شونده، PDF/UA، دسترس‌پذیری یا
بازبینی انسانی فارسی ایجاد نمی‌کنند.

## English descriptor

Build the additive fixed-layout screen reader and closure supplement from the
frozen OLP-0722 source without changing any translation target, closure
manifest, or print asset. Require 748 and 108 pages, the recorded SHA-256
values, FitH opening behavior, and byte-identical independent rebuilds. The
screen PDFs are untagged and are not genuinely responsive or reflowable.
