# QLoRA Fine-Tuning Project

This repository demonstrates how to fine-tune a Large Language Model (LLM) using **QLoRA (Quantized Low-Rank Adaptation)** for parameter-efficient training on consumer hardware.

QLoRA enables training very large models using **4-bit quantization + LoRA adapters**, drastically reducing GPU memory usage while maintaining strong performance.

---

## 📌 Project Overview

- ✅ Uses **4-bit quantization (NF4)**  
- ✅ Applies **LoRA adapters** on top of a frozen base model  
- ✅ Memory-efficient fine-tuning on limited GPU (Colab / single GPU)  
- ✅ Suitable for instruction tuning / domain-specific chat models  

---

## 🧠 What is QLoRA?

QLoRA combines:
- **Quantization** → Loads the base model in 4-bit precision
- **LoRA** → Trains only small low-rank adapters
- **Frozen base model** → No full model weight updates

📉 Memory use reduced by ~65–75% compared to full fine-tuning.

---

## 🛠️ Tech Stack

- **Python**
- **PyTorch**
- **Hugging Face Transformers**
- **PEFT**
- **BitsAndBytes**
- **Datasets**
- **QLoRA**



