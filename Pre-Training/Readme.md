### 🚀 GPT-2 Pretraining on Wuthering Waves Dataset (Educational Demo)

This repository contains a simple, fully reproducible example of **pretraining GPT-2** on a custom text dataset — in this case, text sourced from **Wuthering Waves** (fan dialogues, lore, story text, etc.).

This project is for **educational and demonstration purposes only**, showing how GPT-2 can be pretrained on any dataset using the HuggingFace ecosystem.

---

### 📌 What This Project Demonstrates

- Loading a custom text dataset  
- Tokenizing text for GPT-2  
- Using `Trainer` & `DataCollatorForLanguageModeling`  
- Running GPT-2 **Causal Language Modeling (CLM)** pretraining  
- Saving the final model & tokenizer  
- Clean, readable training code for beginners  

This is NOT full-scale LLM training — just a **small demo** to understand the workflow.

---

### 🛠️ Tech Stack

- Python  
- PyTorch  
- HuggingFace Transformers  
- HuggingFace Datasets  
- Accelerate (optional for GPU)

Install everything using:

```bash
pip install transformers datasets accelerate
```

### 📂 Project Structure
```bash
├── Pre_training_GPT2_Wuwa.ipynb        # Main training script
├── wuwa_dataset.txt        # Wuthering Waves text (cleaned)
├── README.md
```

### 🔥 How Pretraining Works (Causal LM)

## This project uses Causal Language Modeling (CLM):

The model reads tokens left → right

Predicts the next word

Learns writing style, tone, lore, and patterns

Same method used by GPT-2 & GPT-3

Perfect for learning how GPT models are trained.
