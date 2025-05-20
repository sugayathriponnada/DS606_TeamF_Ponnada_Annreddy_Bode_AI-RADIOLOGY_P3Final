---
layout: single
title: "🩺 AI Radiology Report Generator"
subtitle: "Deep learning-based disease detection and automated radiology reporting using chest X-rays"
date: 2025-05-20
author_profile: true
read_time: true
toc: true
toc_sticky: true
toc_label: "Contents"
classes: wide
---

This project presents a deep learning system for automated interpretation of chest X-rays. The model detects thoracic diseases and generates structured radiology reports using an ensemble of **DenseNet121** and **EfficientNet-B3**, trained on the **NIH ChestX-ray14** dataset. The app is deployed on [Hugging Face Spaces](https://huggingface.co/spaces/Sugayathri/ai_radiology).

---

## 🧠 Project Highlights

- 🔍 Utilized the **NIH ChestX-ray14** dataset containing over **100,000 labeled X-ray images**
- 📦 Downloaded and processed data automatically using **Hugging Face Datasets**
- 🧹 Built a **multi-label preprocessing pipeline** using `MultiLabelBinarizer`
- 📊 Incorporated **bounding box annotations** from `BBox_List_2017.csv` for localization
- 📁 Cleaned and filtered multi-label mappings (e.g., Effusion, Cardiomegaly)
- 🧠 Designed and tested a **custom CNN architecture** in addition to DenseNet
- ⚙️ Developed a **reproducible data pipeline** for loading, cleaning, and processing
- ✅ Addressed **class imbalance** with multi-label stratified splits

---

## 💡 Application Overview

The final application performs the following:

- 🖼️ Uploads chest X-ray images for evaluation
- 🔍 Predicts probabilities for 7 disease classes using an **ensemble model**
- ✅ Applies per-class **sigmoid thresholds** for accurate detection
- 📄 Generates a **structured radiology report** (Impression, Findings, Conclusion)
- 🧾 Outputs the report as a **downloadable PDF**
- 🌐 Hosted using **Gradio** on Hugging Face

---

## 🧪 Detected Conditions

- Atelectasis  
- Cardiomegaly  
- Effusion  
- Mass  
- Nodule  
- Pneumonia  
- Pneumothorax  

Each condition includes a human-readable explanation in the generated report if the confidence exceeds its threshold.

---

## 🚀 Live Demo

👉 [**Try the App on Hugging Face Spaces**](https://huggingface.co/spaces/Sugayathri/ai_radiology)  
Upload a chest X-ray and receive disease predictions and a downloadable report.

---

## 📷 Sample Output

Here’s a sample prediction and AI-generated report:

![Sample Output](Sample_Output.png)

---

## 📎 GitHub Repository

🔗 [**View Project Code on GitHub**](https://github.com/sugayathriponnada/DS606_TeamF_Ponnada_Annreddy_Bode_AI-RADIOLOGY_P3Final)

---

## 👩‍💻 Team Members

- **Sugayathri Devi Ponnada**  
- **Ishita Reddy Annreddy**  
- **Deepika Bode**

> _Capstone Project — DATA 606: Capstone in Data Science (Spring 2025)_  
> _University of Maryland, Baltimore County (UMBC)_

---

> 💬 _“Empowering radiologists through explainable AI and automated reporting.”_
