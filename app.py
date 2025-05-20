import torch
import cv2
import timm
import gradio as gr
import numpy as np
from torch import nn
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# CONFIG
IMG_SIZE = 512
MODEL_PATH = "fold1_bests_model.pt"

class_labels = ["Atelectasis", "Cardiomegaly", "Effusion", "Mass",
                "Nodule", "Pneumonia", "Pneumothorax"]

label_to_finding = {
    "Atelectasis": "Partial or complete collapse of the lung is noted.",
    "Cardiomegaly": "The heart appears enlarged.",
    "Effusion": "Pleural effusion is present, showing fluid buildup.",
    "Mass": "A pulmonary mass is noted.",
    "Nodule": "Solitary or multiple lung nodules are observed.",
    "Pneumonia": "Findings are consistent with pneumonia.",
    "Pneumothorax": "Air is present in the pleural space, indicating pneumothorax."
}

thresholds = {
    "Effusion": 0.35,
    "Atelectasis": 0.45,
    "Nodule": 0.43,
    "Mass": 0.50,
    "Pneumothorax": 0.45,
    "Cardiomegaly": 0.42,
    "Pneumonia": 0.40
}

# MODEL
class EnsembleModel(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.dense = timm.create_model("densenet121", pretrained=False)
        self.dense.classifier = nn.Linear(self.dense.classifier.in_features, num_classes)
        self.efficient = timm.create_model("efficientnet_b3", pretrained=False)
        self.efficient.classifier = nn.Linear(self.efficient.classifier.in_features, num_classes)

    def forward(self, x):
        return (self.dense(x) + self.efficient(x)) / 2

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = EnsembleModel(num_classes=len(class_labels))
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

# IMAGE PREPROCESSING
def preprocess_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    gray = np.stack([gray] * 3, axis=-1)
    resized = cv2.resize(gray, (IMG_SIZE, IMG_SIZE))
    norm = (resized / 255.0 - 0.5) / 0.5
    tensor = torch.tensor(norm).permute(2, 0, 1).float().unsqueeze(0).to(device)
    return tensor

# REPORT GENERATION
def generate_pdf_report(report_text, filename="report.pdf"):
    pdf_path = os.path.join("/tmp", filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    y = height - 50

    for line in report_text.split("\n"):
        c.drawString(40, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 50

    c.save()
    return pdf_path

# INFERENCE
def predict(image):
    img_tensor = preprocess_image(image)

    with torch.no_grad():
        output = torch.sigmoid(model(img_tensor)).cpu().numpy()[0]

    predictions = {label: round(float(output[i]), 3) for i, label in enumerate(class_labels)}
    detected = [(label, prob) for label, prob in predictions.items() if prob > thresholds[label]]
    detected_sorted = sorted(detected, key=lambda x: x[1], reverse=True)

    if detected_sorted:
        impression = "The AI model detected the following potential findings:"
        findings = "\n".join(
            f"- {label} (confidence: {prob:.3f}): {label_to_finding[label]}"
            for label, prob in detected_sorted
        )
        conclusion = "These findings may require further clinical evaluation or follow-up imaging."
        report = f"Impression:\n{impression}\n\nFindings:\n{findings}\n\nConclusion:\n{conclusion}"
    else:
        report = "No significant abnormalities detected on the chest X-ray."

    pdf_path = generate_pdf_report(report)
    return predictions, report, pdf_path

# GRADIO UI
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="numpy", label="Upload Chest X-ray"),
    outputs=[
        gr.Label(num_top_classes=len(class_labels), label="Predicted Probabilities"),
        gr.Textbox(label="AI-Generated Radiology Report"),
        gr.File(label="Download Report as PDF")
    ],
    title="🫁 AI Chest X-ray Disease Detection & Report Generator",
    description="Upload a chest X-ray to get disease predictions and download the AI-generated report as a PDF."
)

demo.launch()
