
# 🤖 AI Paraphrasing Model – Humanize AI-Generated Text

This project is a Streamlit-based web app that takes AI-generated or robotic-sounding text and paraphrases it to make it sound more natural and human-like using the Pegasus transformer model.

---

## 🚀 Features

- 📝 Paste any paragraph or AI-generated content
- 🧠 Uses Pegasus NLP model to rewrite text
- 💬 Generates more human-sounding paraphrases
- ⚡ Powered by HuggingFace Transformers and PyTorch
- 🌐 Simple and interactive Streamlit web interface

---

## 📦 Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🧪 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/rishishankar-03/AI_Paraphrazing_Model.git
cd AI_Paraphrazing_Model
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. The app will open in your browser at:
```
http://localhost:8501
```

---

## 💻 Project Structure

```
AI_Paraphrazing_Model/
├── app.py               # Streamlit app script
├── requirements.txt     # Required Python packages
├── README.md            # Project description
```

---

## ✨ Example

**Input:**
```
Artificial intelligence is a growing field that is reshaping various industries.
```

**Output:**
```
The rapidly expanding field of artificial intelligence is transforming many sectors.
```

---

## 🧠 Model Used

- [`tuner007/pegasus_paraphrase`](https://huggingface.co/tuner007/pegasus_paraphrase) – a fine-tuned Pegasus model on paraphrasing tasks from Hugging Face.

---

## 🤝 Contributions

Contributions and suggestions are welcome. Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.
EOF
