# ⛓️ Saad Chain - Simple Blockchain in Python

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> مشروع بلوكشين بسيط ومتكامل تم بناؤه باستخدام **Python** و **Flask**. يهدف إلى فهم أساسيات تقنية البلوكشين مثل التعدين (Mining)، إثبات العمل (Proof of Work)، المعاملات (Transactions)، وشبكات P2P اللامركزية.

---

## 📖 جدول المحتويات
- [المميزات](#-المميزات)
- [التقنيات المستخدمة](#-التقنيات-المستخدمة)
- [هيكل المشروع](#-هيكل-المشروع)
- [كيفية التشغيل](#-كيفية-التشغيل)
- [واجهات API](#-واجهات-api)
- [المساهمة](#-المساهمة)
- [الترخيص](#-الترخيص)

---

## ✨ المميزات

- 🧱 **إنشاء بلوك البداية (Genesis Block):** نقطة انطلاق السلسلة.
- ⛏️ **تعدين البلوكات (Mining):** باستخدام خوارزمية إثبات العمل (Proof of Work).
- 💸 **إضافة المعاملات (Transactions):** مع دعم التوقيع الرقمي.
- ✅ **التحقق من صحة السلسلة (Chain Validity):** التأكد من عدم التلاعب.
- 🔐 **نظام المحفظة (Wallet):** توليد مفاتيح عامة وخاصة (ECDSA).
- 💾 **قاعدة بيانات SQLite:** لحفظ البلوكات بشكل دائم.
- 🌐 **شبكة P2P:** ربط عدة عقد (Nodes) ومزامنتها تلقائياً.
- 🎨 **واجهة مستخدم (HTML/CSS):** لعرض البلوكات وإرسال المعاملات.

---

## 🛠️ التقنيات المستخدمة

| التقنية | الاستخدام |
|---------|-----------|
| **Python 3.14** | لغة البرمجة الأساسية |
| **Flask** | إطار العمل لبناء الـ API |
| **SQLite** | قاعدة بيانات لحفظ البلوكات |
| **ECDSA** | التوقيع الرقمي وتوليد المفاتيح |
| **HTML/CSS** | واجهة المستخدم |
| **Git/GitHub** | إدارة الإصدارات |

---

## 📂 هيكل المشروع

```

saad-chain/
├── blockchain/          # منطق البلوكشين
│   ├── init.py
│   ├── block.py         # كلاس البلوك
│   ├── core.py          # كلاس السلسلة (Blockchain)
│   ├── transaction.py   # كلاس المعاملة
│   └── consensus.py     # خوارزمية الإجماع
├── nodes/               # كود العقدة (Node)
│   ├── init.py
│   ├── node.py          # الـ API الرئيسي
│   ├── peer.py          # كود P2P
│   └── templates/       # قوالب HTML
│       └── index.html
├── wallet/              # نظام المحفظة
│   ├── init.py
│   └── wallet.py
├── tests/               # اختبارات الكود
│   └── test_blockchain.py
├── api/                 # مسارات API إضافية
│   ├── init.py
│   └── routes.py
├── config.py            # إعدادات المشروع
├── main.py              # نقطة التشغيل
├── requirements.txt     # المكتبات المطلوبة
└── README.md            # هذا الملف

```

---

## 🚀 كيفية التشغيل

### 1. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

2. تشغيل العقدة الأولى (Node 1)

```bash
python -m nodes.node
```

سيعمل السيرفر على: http://127.0.0.1:5005

3. تشغيل العقدة الثانية (Node 2) - اختياري

افتح تيرمنال جديد وشغل:

```bash
python -m nodes.node 5006
```

سيعمل السيرفر على: http://127.0.0.1:5006

4. فتح الواجهة

· المستكشف: http://127.0.0.1:5005/explorer
· التعدين: http://127.0.0.1:5005/mine
· السلسلة: http://127.0.0.1:5005/chain
· التحقق: http://127.0.0.1:5005/valid

---

🔌 واجهات API

الرابط الطريقة الوصف
/ GET الصفحة الرئيسية (ملخص السلسلة)
/chain GET عرض السلسلة كاملة
/mine GET تعدين بلوك جديد
/transaction POST إضافة معاملة جديدة
/valid GET التحقق من صحة السلسلة
/explorer GET واجهة HTML لعرض البلوكات
/nodes/register POST تسجيل عقدة جديدة في الشبكة
/nodes/resolve GET حل النزاعات (Consensus)

---

🤝 المساهمة

المساهمات مرحب بها! إذا كنت ترغب في تحسين المشروع:

1. قم بعمل Fork للمستودع.
2. أنشئ Branch جديداً (git checkout -b feature/AmazingFeature).
3. قم بعمل Commit لتعديلاتك (git commit -m 'Add some AmazingFeature').
4. ارفع التعديلات (git push origin feature/AmazingFeature).
5. افتح Pull Request.

---

📄 الترخيص

هذا المشروع مفتوح المصدر ومتاح بموجب MIT License. راجع ملف LICENSE للمزيد من التفاصيل.

---

📞 التواصل

· المطور: Saad Ibrahem
· GitHub: @saadibraheem023-sketch
· المستودع: saad-chain

---

<p align="center">صُنع بـ ❤️ في العراق</p>
```