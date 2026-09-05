![alt text](pythonji.gif)

# 📐 Python 3rd - গণিতীয় প্রোগ্রাম সংগ্রহ

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-Open%20Source-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

<div align="center">
  
  **Python-এ বিভিন্ন গণিতীয় সমস্যার শিক্ষামূলক সমাধান ও উদাহরণসমূহ**
  
</div>

---

## 📖 সংক্ষিপ্ত বর্ণনা

এই রিপোজিটরিটি শিক্ষার্থী বা নবীন Python প্রোগ্রামারদের জন্য সহজ ও স্পষ্টভাবে লেখা কিছু মৌলিক গণিতীয় প্রোগ্রামের সংগ্রহ। প্রতিটি স্ক্রিপ্ট ছোট, স্বতন্ত্��� ও টার্মিনাল-ভিত্তিক ইনপুট/আউটপুট প্রদর্শন করে — তাই নতুনরা দ্রুত কনসেপ্টগুলো অনুশীলন করতে পারবেন।

---

## 📁 ফাইল কাঠামো

```
python-3rd/
├── README.md          # এই ফাইল (প্রকল্প বিবরণ এবং চালানোর নির্দেশ)
├── E=mc².py            # E = mc² গণনা উদাহরণ
├── area.py            # আয়তক্ষেত্রের ক্ষেত্রফল নির্ণয়
├── factorial.py       # ফ্যাক্টোরিয়াল গণনা (রিকার্সিভ)
├── triangle.py        # ত্রিভুজের ক্ষেত্রফল (Heron's formula)
├── regexemail.py      # ইমেইল প্যাটার্ন ম্যাচিং (উদাহরণ)
├── regexword.py       # শব্দ ম্যাচিং/সার্চ (উদাহরণ)
└── pythonji.gif       # পরিচিতিমূলক GIF
```

---

## 🚀 প্রোগ্রামসমূহ ও ব্যবহার

নীচে প্রতিটি প্রোগ্রামের সংক্ষিপ্ত বর্ণনা ও চালানোর উদাহরণ দেয়া আছে।

### 1️⃣ আয়তক্ষেত্রের ক্ষেত্রফল — `area.py`
দৈর্ঘ্য (Length) ও প্রস্থ (Width) প্রদান করে আয়তক্ষেত্রের ক্ষেত্রফল গণনা করে।

চালানোর উপায়:
```bash
python area.py
```
উদাহরণ ইনপুট/আউটপুট:
```
Enter Length: 10
Enter Width: 5
The area of rectangle is: 50.0
```

---

### 2️⃣ ফ্যাক্টোরিয়াল — `factorial.py`
রিকার্সিভ ফাংশন ব্যবহার করে n! নির্ণয় করে। নেতিবাচক ইনপুটের ক্ষেত্রে প্রোগ্রাম একত্রে বাতিল করে একটি বার্তা দেখায়।

চালানোর উপায়:
```bash
python factorial.py
```
উদাহরণ:
```
Enter a positive number: 5
The factorial of 5 is: 120
```

---

### 3️⃣ ত্রিভুজের ক্ষেত্রফল — `triangle.py`
Heron's formula ব্যবহার করে তিনটি ব���হুর দৈর্ঘ্য দিয়ে ত্রিভুজের ক্ষেত্রফল গণনা করে। কোণগুলো বৈধ না হলে প্রোগ্রাম সতর্ক করে।

চালানোর উপায়:
```bash
python triangle.py
```
উদাহরণ:
```
Enter the value of a : 3
Enter the value of b : 4
Enter the value of c : 5
The area of this Triangle is : 6.0
```

---

### 4️⃣ E = mc² উদাহরণ — `E=mc².py`
Einstein-এর ভর-শক্তি সমীকরণ E = m c² অনুসারে দেয়া ভর (kilograms) থেকে জুলে শক্তি বের করে। স্ক্রিপ্টে উদাহরণ হিসেবে mass=1 kg ব্যবহার আছে।

চালানোর উপায়:
```bash
python "E=mc².py"
```
উদাহরণ আউটপুট (সংক্ষিপ্ত):
```
Mass : 1 kg
Speed of light : 299792458 m/s
Energy (E): 89,875,517,873,681,764 joules
Energy (E): 89,875.52 petajoules
```

---

### 5️⃣ রেগুলার এক্সপ্রেশন উদাহরণ — `regexemail.py`, `regexword.py`
- `regexemail.py` — ইমেইল প্যাটার্ন শনাক্ত করার সরল উদাহরণ
- `regexword.py` — কোনো টেক্সটে নির্দিষ্ট শব্দ বা প্যাটার্ন খোঁজার উদাহরণ

চালানোর উপায়:
```bash
python regexemail.py
python regexword.py
```

---

## 📋 প্রয়োজনীয়তা

- Python 3.x
- কোন বাহ্যিক লাইব্রেরি লাগবে না (স্ট্যান্ডার্ড লাইব্রেরির math ও re মডিউল ব্যবহার করা হয়েছে)

---

## 🔧 ক্লোন ও চালানো

রিপোজিটরি ক্লোন করে একটি প্রোগ্রাম চালানোর দ্রুততম উপায়:

```bash
git clone https://github.com/jeyaulhoquebd/python-3rd.git
cd python-3rd
python area.py
```

উপরের কমান্ডগুলো Terminal / Command Prompt-এ চলবে।

---

## 💡 শেখার বিষয়

এই প্রজেক্টটি থেকে আপনি শিখতে পারবেন:
- ফাংশন সংজ্ঞা ও ব্যবহার (function definition & calls)
- রিকার্সন (recursive functions) ও বেইস কেস
- ইনপুট/আউটপুট (input / print)
- শর্তসাপেক্ষ লজিক (if / else) ও ডেটা ভেলিডেশন
- মডিউল ব্যবহার (math, re)

---

## 📊 অ্যালগরিদম জটিলতা

| প্রোগ্রাম | টাইম কমপ্লেক্সিটি | স্পেস কমপ্লেক্সিটি |
|---------|------------------:|------------------:|
| area.py | O(1) | O(1) |
| factorial.py | O(n) | O(n) |
| triangle.py | O(1) | O(1) |

---

## 🤝 অবদান (Contributing)

অবদান দিতে চাইলে নিম্নলিখিত ধাপ অনুসরণ করুন:

1. রিপোজিটরি ফর্ক করুন
2. নতুন ব্রাঞ্চ তৈরি করুন (`git checkout -b feature/YourFeature`)
3. পরিবর্তন কমিট করুন (`git commit -m "Add YourFeature"`)
4. ব্রাঞ্চ পুশ করুন (`git push origin feature/YourFeature`)
5. Pull Request খোলুন

আপনি নতুন ছোট প্রোগ্রাম যোগ করতে পারেন, বাগ রিপোর্ট করতে পারেন, বা বিদ্যমান ��োড উন্নত করতে পারেন।

---

## 📝 লাইসেন্স

এই প্রকল্পটি ওপেন সোর্স হিসেবে উপলব্ধ। যদি একটি নির্দিষ্ট লাইসেন্স যোগ করতে চান (উদাহরণ: MIT, Apache-2.0), তাহলে একটি LICENSE ফাইল যোগ করুন।

---

## 👨‍💻 লেখক

**jeyaulhoquebd**

---

## 📧 যোগাযোগ

কোনো প্রশ্ন বা ফিচার অনুরোধ থাকলে রিপোজিটরির Issues সেকশনে একটি Issue খুলুন।

---

<div align="center">

**Happy Learning! 🎉 Python দিয়ে প্রোগ্রামিং উপভোগ করুন!**

</div>
