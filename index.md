---
layout: default
title: 🩺 AI Radiology Report Generator
---

# 🧠 AI for Automated Radiology Report Generation  
## Using Chest X-rays and Deep Learning

🎓 **DATA 606 – Capstone in Data Science (Spring 2025)**  
👩‍💻 Team F: Sugayathri Devi Ponnada, Ishita Reddy Annreddy, Deepika Bode

---

## 🚀 Project Overview

Our project uses deep learning to detect thoracic diseases from chest X-rays and generate structured radiology reports using AI.

We built an ensemble of **DenseNet121 + EfficientNet-B3**, trained on over **51,000 chest X-rays**, and deployed a real-time demo.

---

## 🔬 Dataset Summary

- **Source**: [CXR8-Selected](https://www.kaggle.com/datasets/myylee/cxr8-selected) (NIH ChestX-ray14 subset)
- **Samples**: 112,120 frontal X-rays
- **Labels**: 14 thoracic diseases → used 7 (Effusion, Atelectasis, etc.)
- **Preprocessing**: CLAHE, grayscale conversion, multi-label binarization

---

## 🧠 Model & Approach

- ✅ **Multi-label classification** using sigmoid output
- ✅ 5-Fold Stratified Cross-Validation
- ✅ Ensemble architecture with:
  - 🔹 DenseNet121
  - 🔹 EfficientNet-B3
- ✅ Custom thresholds for each disease
- ✅ PDF report generation using ReportLab

---

## 📊 Evaluation Results

| Metric         | Score     |
|----------------|-----------|
| AUROC          | **0.83**  |
| Macro F1 Score | **0.51**  |
| Accuracy       | 78.7%     |

Fold 1 was selected for deployment due to stable performance.

---

## 🌐 Live Demo

👉 [Launch AI Radiology Gradio App 🚀](https://huggingface.co/spaces/Sugayathri/ai_radiology)

Upload a chest X-ray image to see detected diseases and download an AI-generated radiology report.

---

## 🧩 GitHub Repo

🔗 [View Source Code on GitHub](https://github.com/sugayathriponnada/DS606_TeamF_Ponnada_Annreddy_Bode_AI-RADIOLOGY_P3Final)

---

## 📌 What's Next?

- 🧠 Add Grad-CAM explainability
- 💬 Use BioGPT or T5 for smarter report summaries
- 🤝 Collaborate with radiologists for validation
- 🚀 Deploy as a clinical decision support tool

---

© 2025 Team F – UMBC DS606 | AI for Healthcare Innovation
