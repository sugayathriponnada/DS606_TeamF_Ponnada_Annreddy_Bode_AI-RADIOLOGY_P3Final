# Application Code Overview (app.py)

This app is deployed on Hugging Face Spaces and provides a web UI to:
- Upload chest X-rays
- Run a pre-trained DenseNet121 model
- Display predicted disease labels
- (Optional) Show Grad-CAM explanation heatmaps

The interface uses Gradio Blocks to organize the layout, and Python for model inference and preprocessing.
