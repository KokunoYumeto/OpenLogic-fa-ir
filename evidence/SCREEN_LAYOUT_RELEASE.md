# منابع و شواهد بازچینی ۱۶:۹ فارسی ایران

این بستهٔ افزوده به دارایی منبع کامل
`02_OPENLOGIC_fa-IR_EDITABLE_SOURCES_OLP-0722.zip` وابسته است. دو
راه‌انداز صفحه‌نمایش را بر همان درخت منبع قرار دهید و
`build/BUILD_SCREEN.ps1` را در یک پوشهٔ خروجی خالی اجرا کنید:

- `source/locale/fa-IR/open-logic-complete-fa-IR-screen.tex`
- `source/locale/fa-IR/open-logic-closure-supplement-fa-IR-screen.tex`

خروجی نهایی خوانشگر ۱۵۷۸ صفحه و خروجی نهایی ضمیمه ۲۲۲ صفحه دارد. همهٔ
صفحه‌ها دقیقاً ۹۶۰ × ۵۴۰ نقطه، سطح خواندن دقیقاً ۷۴۴ × ۴۶۸ نقطه و نمای
آغاز `/Fit` دارند. کلاس قلم ۱۷ نقطه و فاصلهٔ سطر ۱٫۱۶ است.

هیچ فایل هدف ترجمه، بیانیهٔ بسته‌شدن یا اتصال واحد تغییر نکرده است. اجرای
بازپخش‌شدهٔ بیانیه، ۷۲۲ هدف از ۷۲۲ هدف و سبک محلی تثبیت‌شده را بدون اختلاف
تأیید کرد. دارایی‌های چاپی ۰۰ تا ۰۴ نیز بدون تغییر بایتی باقی مانده‌اند.

## اصلاح مستطیل‌های پیوند

فایل‌های خامِ LuaLaTeX به‌ترتیب ۱۳۷ و ۹ مستطیل پیوند راست‌به‌چپ داشتند که
از پهنای صفحه بیرون می‌رفتند. `build/repair_rtl_link_rects_fa.py`
تنها x1 این مستطیل‌ها را از روی بازهٔ نویسه‌ای رنگی و یکتا اصلاح می‌کند و
در صورت ابهام متوقف می‌شود. دو JSON زیر نگاشت کامل خام به نهایی، هش‌های دو
طرف و اثبات برابری مقصدها، محتوا، هندسه، طرح کلی و فراداده را نگه می‌دارند:

- `evidence/link-repair/open-logic-complete-fa-IR-screen.link-rect-repair-evidence.json`
- `evidence/link-repair/open-logic-closure-supplement-fa-IR-screen.link-rect-repair-evidence.json`

فرمان بازپخش دقیق:

    python build/repair_rtl_link_rects_fa.py --input <raw-before-link-repair.pdf> --output <fresh-output.pdf> --evidence <fresh-evidence.json>

اسکریپت فقط دو هش خام ثبت‌شده را می‌پذیرد و خروجی یا رسید موجود را بازنویسی
نمی‌کند.

## شواهد عمومی

- `evidence/final-build-screen/` گزارش‌های LOG و FLS، AUXها، BBL/BLG
  خوانشگر و رسید پاک‌سازی مسیر را نگه می‌دارد.
- `evidence/final-qa/PERSIAN_SCREEN_REFLOW_FINAL_QA.json` همهٔ
  دروازه‌های ساختاری، دیداری، پیوند، منبع و بازتولیدپذیری را ثبت می‌کند.
- `inventories/RAW_SCREEN_BUILD_EVIDENCE_SHA256.tsv` هش فایل‌های
  خام خصوصی و فایل‌های نهایی را ثبت می‌کند.
- `inventories/SCREEN_SOURCE_BINDING_SHA256.tsv` بستهٔ منبع،
  بیانیه، سبک محلی و دو راه‌انداز نهایی را به هم مقید می‌کند.
- `inventories/SCREEN_BUNDLE_SHA256.tsv` تمام اعضای این ZIP به‌جز
  خود موجودی را هش می‌کند.

DOI دقیق نسخه `10.5281/zenodo.22015765` در فراداده ثبت شده است.
خود PDFها عمداً DOI مفهومی پایدار `10.5281/zenodo.21921852` را
نمایش می‌دهند.

## English descriptor

Reproducibility and QA bundle for the corrected Iranian Persian 16:9 screen
edition. It contains the final wrappers, deterministic builders, hash-gated
RTL link-rectangle repair, complete raw-to-final mapping evidence, sanitized
build receipts, and final QA. The 722 translation targets and print assets
remain unchanged.
