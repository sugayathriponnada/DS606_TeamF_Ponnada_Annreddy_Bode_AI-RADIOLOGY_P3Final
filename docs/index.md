# 🩺 AI Radiology Report Generator

This project uses deep learning to generate radiology reports from chest X-rays.  
Built using DenseNet121 and trained on the NIH ChestX-ray14 dataset.

## 🧠 Project Highlights

-🔍 Used the NIH ChestX-ray14 dataset with over 100,000 labelled X-ray images.

-📦 The dataset was downloaded and extracted automatically from Hugging Face Datasets.

-🧹 Implemented a multi-label preprocessing pipeline with label binarization using MultiLabelBinarizer.

-📊 Worked with bounding box annotations for disease localization (BBox_List_2017.csv).

-📁 Cleaned and filtered image-label mappings with multi-label splits (Example: Effusion, Cardiomegaly).

-🧠 Designed a custom CNN model (not DenseNet) to perform thoracic disease classification.

-⚙️ Automated the full data loading, extraction, and cleaning process in a reproducible pipeline.

-✅ Verified class imbalance and prepared data for multi-label stratified splits.


## 👩‍💻 Team Members
- Sugayathri Devi Ponnada
- Ishita Reddy Annreddy
- Deepika Bode

## 🚀 Live Demo
[👉 Try the App on Hugging Face](https://huggingface.co/spaces/Sugayathri/ai_radiology)


## 📷 Sample Output

Here’s how the model interprets and classifies a chest X-ray:

![Sample Output](Sample_Output.png)

## 📎 GitHub Repo
[View Project Repository](https://github.com/sugayathriponnada/DS606_TeamF_Ponnada_Annreddy_Bode_AI-RADIOLOGY_P3Final)
