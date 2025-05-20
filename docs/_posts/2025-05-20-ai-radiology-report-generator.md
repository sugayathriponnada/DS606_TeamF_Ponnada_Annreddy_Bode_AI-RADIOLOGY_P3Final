---
layout: single
title: "🩺 AI Radiology Report Generator"
subtitle: "Deep learning-based chest X-ray disease detection and automated report generation"
date: 2025-05-20
author_profile: true
read_time: true
toc: true
toc_sticky: true
toc_label: "Contents"
classes: wide
---

This project presents an end-to-end deep learning pipeline for automated chest X-ray interpretation. Built using an ensemble of **DenseNet121** and **EfficientNet-B3**, the model classifies thoracic diseases and generates structured radiology reports. It is deployed using **Gradio** on **Hugging Face Spaces**.

---

## 🧠 Project Overview

- **Dataset**: NIH ChestX-ray14 (100,000+ labeled images)
- **Model**: Ensemble of DenseNet121 + EfficientNet-B3
- **Interface**: Gradio-based web UI
- **Deployment**: Hugging Face Spaces
- **Outputs**: Disease classification, report text, downloadable PDF

---

## 🚀 Application Features

- **Image Upload**: Accepts `.jpg` or `.png` X-ray files
- **Ensemble Prediction**: Model outputs per-class probabilities
- **Threshold-Based Detection**: Tuned thresholds per disease label
- **Explainable Output**: Adds condition-specific interpretations
- **PDF Report**: Generates downloadable radiology report

---

## 🔬 Diseases Detected

The system identifies the following thoracic conditions:

- Atelectasis
- Cardiomegaly
- Effusion
- Mass
- Nodule
- Pneumonia
- Pneumothorax

Each detected condition is explained in the output report using clinical-style descriptions.

---

## 🧪 Technical Stack

| Component     | Details                                      |
|---------------|----------------------------------------------|
| Framework     | PyTorch + timm                              |
| Preprocessing | CLAHE, grayscale normalization, resizing    |
| Architecture  | Custom Ensemble (DenseNet121 + EfficientNet-B3) |
| Interface     | Gradio Blocks                               |
| Deployment    | Hugging Face Spaces                         |
| Reporting     | ReportLab PDF generation                    |

---

## 📷 Sample Output

Example model prediction with interpreted report:

![Sample Output](../assets/images/Sample_Output.png)

---

## 🌐 Live Demo

👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/Sugayathri/ai_radiology)

---

## 📎 GitHub Repository

🔗 [Project Source Code](https://github.com/sugayathriponnada/DS606_TeamF_Ponnada_Annreddy_Bode_AI-RADIOLOGY_P3Final)

---

## 👩‍💻 Team Members

- Sugayathri Devi Ponnada  
- Ishita Reddy Annreddy  
- Deepika Bode  

_Capstone Project – DATA 606, Spring 2025, University of Maryland, Baltimore County_

---

> 💬 _"Empowering radiologists with AI-driven diagnostics and report automation."_
