🩻 AI for Automated Radiology Report Generation using Chest X-rays and Deep Learning
Final Project – DATA 606: Capstone in Data Science (Spring 2025)

This project presents an end-to-end deep learning pipeline to detect thoracic diseases from chest X-rays and automatically generate structured radiology reports. We leverage multi-label classification using an ensemble of CNN models and generate basic AI-driven summaries to assist radiologists with faster, more consistent diagnostics.

🚀 Key Features
Dataset: CXR8-Selected (NIH ChestX-ray14 subset; ~112k images)

Diseases Detected (7 classes):

Effusion, Atelectasis, Nodule, Mass, Pneumothorax, Cardiomegaly, Pneumonia

Models Used: DenseNet121 + EfficientNet-B3 (Ensemble)

Technique: Multi-label classification with 5-fold stratified training

Deployment: Hosted on Hugging Face using Gradio for real-time inference

📊 Workflow Overview
Data Cleaning & Label Binarization

Exploratory Data Analysis (EDA)

CLAHE Contrast Enhancement + Augmentations

5-Fold Multilabel Stratified Training

Model Ensembling & Evaluation

Test-Time Inference + Report Generation

🔗 Project Links
🔴 Live App on Hugging Face

📘 GitHub Pages Site

🧠 Dataset Source (also hosted on Hugging Face)

👩‍💻 Team Members
Sugayathri Devi Ponnada

Deepika Bode

Ishita Reddy Annreddy

Project supervised by Dr. Zak Sakoglu – UMBC
