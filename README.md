# 🩻 AI for Automated Radiology Report Generation using Chest X-rays and Deep Learning  
*Final Project – DATA 606: Capstone in Data Science (Spring 2025)*  

This project presents a complete deep learning pipeline to detect thoracic diseases from chest X-rays and automatically generate structured radiology reports. We apply **multi-label classification** using an ensemble of CNN models, and deliver basic AI-generated summaries to assist radiologists with faster and more consistent diagnostic support.

---

## 🚀 Key Features

- **Dataset**: [CXR8-Selected (NIH ChestX-ray14 subset)](https://www.kaggle.com/datasets/myylee/cxr8-selected) (~112k frontal-view chest X-rays)  
- **Target Diseases (7 classes)**:  
  Effusion, Atelectasis, Nodule, Mass, Pneumothorax, Cardiomegaly, Pneumonia  
- **Model Architecture**:  
  Ensemble of [DenseNet121](https://arxiv.org/abs/1608.06993) + [EfficientNet-B3](https://arxiv.org/abs/1905.11946)  
- **Learning Setup**:  
  Multi-label classification using **5-Fold Multilabel Stratified Cross-Validation**
- **Enhancements**:  
  CLAHE contrast boosting, Albumentations-based image augmentations
- **Deployment**:  
  Real-time inference via [Gradio](https://gradio.app/) and hosted on Hugging Face Spaces

---

## 📊 Workflow Overview

1. **Data Cleaning & Label Binarization**
2. **Exploratory Data Analysis (EDA)**
3. **CLAHE Contrast Enhancement + Augmentations**
4. **Stratified 5-Fold Cross-Validation Training**
5. **Ensemble Model Construction & Evaluation**
6. **AI-Generated Report Creation (Inference Phase)**

---

## 🔗 Project Links

- 🔴 **[Live App on Hugging Face](https://huggingface.co/spaces/Sugayathri/ai_radiology/resolve/main/app.py)**  
- 📘 **[GitHub Pages Site](https://sugayathriponnada.github.io/DS606_TeamF_Ponnada_Annreddy_Bode_AI-RADIOLOGY_P3Final/)**  
- 🧠 **[Dataset Source – CXR8-Selected (Kaggle)](https://www.kaggle.com/datasets/myylee/cxr8-selected)**  
- ☁️ **[Mirror on Hugging Face Datasets](https://huggingface.co/datasets/Sugayathri/crx8selected)**  

---

## 👩‍💻 Team Members

- **Sugayathri Devi Ponnada**  
- **Deepika Bode**  
- **Ishita Reddy Annreddy**  

**Advisor**: *Dr. Zak Sakoglu – University of Maryland, Baltimore County (UMBC)*

---

## 📄 License

This project is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

