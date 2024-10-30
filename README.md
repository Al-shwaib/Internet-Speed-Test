# اختبار سرعة الإنترنت باستخدام مكتبة جاهزة (Internet Speed Test)

## الوصف (Description)
برنامج بسيط مكتوب بلغة Python لقياس سرعة الإنترنت لديك. يقوم البرنامج بقياس:
- سرعة التحميل
- سرعة الرفع
- زمن الاستجابة (Ping)

This is a simple Python program that measures your internet connection speed. The program measures:
- Download speed
- Upload speed
- Response time (Ping)

## المتطلبات (Requirements)
- Python 3.x
- مكتبة speedtest-cli
```bash
pip install speedtest-cli
```

## التثبيت (Installation)
1. قم بتثبيت Python من [python.org](https://python.org)
2. قم بتثبيت المكتبات المطلوبة:
```bash
pip install speedtest-cli
```
3. قم بتحميل الملف `speedinternettest.py`

## الاستخدام (Usage)
قم بتشغيل البرنامج باستخدام الأمر التالي:
```bash
python speedinternettest.py
```

سيقوم البرنامج تلقائياً بـ:
1. اختيار أفضل خادم للاختبار
2. قياس سرعة التحميل
3. قياس سرعة الرفع
4. قياس زمن الاستجابة
5. عرض النتائج