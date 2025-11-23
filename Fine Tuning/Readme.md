# 🧠 Fine-Tuning GPT-2 on *Feliz Pero – Chapter 1*

This repository contains code for **fine-tuning GPT-2** on a custom dataset consisting of **Chapter 1 of my original story _"Feliz Pero"_**.  
The goal of this project is to observe how fine-tuning affects a language model when trained on a **small, narrative-style dataset written by the author**, and to demonstrate a complete fine-tuning pipeline using Hugging Face `transformers`.

> ✅ This fine-tuning was done **for educational and experimental purposes only**  
> ✅ The dataset is original content written by me

---

## 🚀 Features

- Fine-tuning GPT-2 using Hugging Face
- Custom narrative dataset (fictional story)
- Full training + text generation pipeline
- GPU/CPU compatible
- Easy template for fine-tuning on any text

---

## 📂 Repository Structure

📁 GPT2-FineTune-FelizPero
│
├── dataset/
│ └── feliz.txt
│
├── fine_tune.py
└── README.md

---

## 🗂️ Dataset

The dataset used for training contains:

- Chapter 1 of my story **Feliz Pero**
- Fictional, narrative writing
- Emotional and descriptive storytelling style

The dataset is formatted as a single `.txt` file for easy training.

> ⚠️ The story is **original content**, please do not redistribute without permission.

---
## Main libraries:

- transformers
- datasets
- torch
- accelerate
- tokenizer
