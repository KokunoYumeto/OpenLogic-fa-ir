# نیازمندی‌های ساخت نسخهٔ کامل فارسی ایران OLP-0722

این فایل ساخت نهایی خوانشگر قانونی فارسی ایران و ضمیمهٔ فنی بسته‌شدن را
توصیف می‌کند. هیچ PDF خروجی تا زمانی که دو ساخت پاک موفق، بایت‌ها و هش‌های
یکسان، و ثبت در بیانیهٔ نهایی SHA-256 نداشته باشد دارایی منتشرشده نیست.

## هویت تثبیت‌شده

- نسخه: `OLP-0722-20260818`
- DOI مفهومی: `10.5281/zenodo.21921852`
- DOI دقیق رزروشده: `10.5281/zenodo.21987687`
- تعهد منبع: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
- درخت منبع: `f67757bb9305b173634082ab4cefd5601a707a34`
- هش بیانیهٔ بسته‌شدن واحدها: `0CCA3735E506581BE93C87542FA1F8236281834B71831C9D767C4B43E5361952`
- پیوند کامل دو هدف: `C7ADBCC67F6D7C6ED79FF81EE2F12E8597A994EB4894BA1AAA2F6B1610B78BB4`

## درخت ورودی لازم

برنامه از مخزن انتشار اجرا می‌شود و انتظار دارد:

- `source/locale/fa-IR/open-logic-complete-fa-IR.tex`
- `source/locale/fa-IR/open-logic-closure-supplement-fa-IR.tex`
- همهٔ 722 فایل هدف فارسی نام‌برده در `CLOSURE_MANIFEST.csv`
- اجتماع ورودی‌های `INPUT` در دو FLS نهایی، پس از کنارگذاشتن خروجی‌های ساخت
- `source/bib/open-logic.bib` و`source/bib/natbib-oup.bst`
- فایل‌های تثبیت‌شدهٔ Scheherazade زیر `00_control/fonts/scheherazade-2.100/`

FLS باید ثابت کند که خوانشگر به 642 فایل هدف و ضمیمه به 80 فایل دیگر
می‌رسد و اجتماع آن‌ها بدون فقدان یا هم‌پوشانی اعلام‌نشده برابر 722 است.

## ابزارها

- PowerShell 7 یا Windows PowerShell 5.1
- LuaLaTeX از توزیع MiKTeX تثبیت‌شده و ثبت‌شده در رسید ساخت
- BibTeX
- Poppler `pdfinfo`

برنامه هیچ بسته‌ای دانلود نمی‌کند، Git را اجرا نمی‌کند و سامانهٔ فایل را
نمی‌پوید. همهٔ بسته‌ها باید پیشاپیش نصب باشند و نسخهٔ MiKTeX، بسته‌ها و
خطوط در شواهد انتشار ثبت شود.

## خطوط تثبیت‌شده

| فایل | SHA-256 |
|---|---|
| `Scheherazade-Regular.ttf` | `034C3ED203CCF91E20A75181350759CC5878E0E369BB0E2E83ACEE15A829184F` |
| `Scheherazade-Bold.ttf` | `62DDE529B296DF074EFBF75B40A986E8FF82E997B98CEC9AD7AB6795BB17A622` |
| `OFL.txt` | `458314C1EBC013A6ED6055EC23ACB93C4EF54BC41D8BA35C0BBC232849D0D804` |
| `FONT_RECEIPT.md` | `8CFE02B657E0120BC98884F75CDFFBF3C0BFD6E572FDE5E67969EF795A51A879` |

## ترتیب ساخت

`BUILD.ps1` مقادیر زیر را برای فرایند ساخت تنظیم می‌کند و سپس مقادیر پیشین
محیط را بازمی‌گرداند:

- `SOURCE_DATE_EPOCH=1783874174`
- `FORCE_SOURCE_DATE=1`
- `TZ=UTC`
- `TEXINPUTS` با تقدم پوشهٔ خروجی بر مسیر پیش‌فرض

سپس اجرا می‌کند:

1. LuaLaTeX روی خوانشگر کامل.
2. BibTeX روی کار خوانشگر در پوشهٔ خروجی.
3. دو گذر دیگر LuaLaTeX روی خوانشگر.
4. دو گذر LuaLaTeX روی ضمیمه، با حل ارجاع‌ها از AUX خوانشگر.
5. بررسی وجود دو PDF، شمار صفحه‌ها و SHA-256.

اجرای معمول:

```powershell
pwsh -NoProfile -File .\build\BUILD.ps1 -OutputDirectory <پوشه-پاک-صریح>
```

بررسی هش‌های شناخته‌شده:

```powershell
pwsh -NoProfile -File .\build\BUILD.ps1 `
  -OutputDirectory <پوشه-پاک-صریح> `
  -ExpectedCompleteSha256 <SHA256> `
  -ExpectedSupplementSha256 <SHA256>
```

کلید `-StageReleaseAssets` فقط پس از پایان QA نهایی به‌کار می‌رود و برنامه
از بازنویسی هر دارایی انتشار موجود خودداری می‌کند.

## دروازه‌های پذیرش

- خوانشگر کامل: 839 صفحه.
- ضمیمهٔ 80 واحد: 127 صفحه.
- نبود DOI قدیمیِ ساخته‌شده از دو جزء `10.5281/zenodo.` و `21921853` در هر دو راه‌انداز.
- وجود DOI رزروشدهٔ `10.5281/zenodo.21987687` در هر دو راه‌انداز.
- همگرایی ارجاع‌ها و استنادها و نبود خطای LuaLaTeX/BibTeX.
- یکسانی هش PDF هر کار میان دو ساخت پاک و مستقل.
- موفقیت بررسی پیوند، خط، استخراج و نمایش همهٔ صفحه‌ها.

دو PDF برچسب‌گذاری ساختاری ندارند و استخراج ریاضیات، نیم‌فاصله و ترتیب
راست‌به‌چپ کامل نیست؛ موفقیت ساخت ادعای PDF/UA، دسترس‌پذیری یا بازبینی
انسانی فارسی ایجاد نمی‌کند.

## بازچینی افزوده برای صفحه‌نمایش

این سند ساخت چاپی 839 و 127 صفحه‌ای را ثابت نگه می‌دارد. انتشار افزودهٔ
صفحه‌نمایش با راه‌اندازهای مستقل و `build/BUILD_SCREEN.ps1` ساخته می‌شود و
در 748 و 108 صفحه، همان 722 واحد را بازچینی می‌کند. نیازمندی‌ها، هش‌ها و
دروازه‌های مستقل آن در `build/BUILD_SCREEN_REQUIREMENTS.md` ثبت شده‌اند.
دارایی‌های چاپی 00 تا 04 در این فرایند بازنویسی نمی‌شوند.

## English descriptor

Build the 642-unit, 839-page canonical Iranian Persian reader first,
including BibTeX, then build the separate 80-unit, 127-page closure supplement
against the reader AUX. Run twice in distinct clean output directories and
require byte-identical PDFs before release staging. The script performs no Git
or network operation and refuses to overwrite existing release assets.
