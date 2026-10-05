# Food-Label-Information-Extractor
# Food Label Information Extractor

A beginner-friendly AI application that extracts useful information from food product label images using OCR, Text Embedding, Attention Mechanism, and Regular Expressions.

## Project Overview

Food packages contain important information such as weight, calories, ingredients, protein, fat, carbohydrates, and dates.

This project allows the user to upload a food label image and automatically extract useful information from the image.

## Project Workflow

Food Label Image
↓
OCR
↓
Text Extraction
↓
Text Embedding
↓
Attention Mechanism
↓
Information Extraction
↓
Streamlit Output

## Features

- Upload food label image
- Extract text using OCR
- Convert text into numerical embeddings
- Calculate attention scores
- Extract weight
- Extract calories
- Extract dates
- Extract protein
- Extract fat
- Extract carbohydrates
- Detect ingredients
- Display results in a simple web interface

## Technologies Used

- Python
- Streamlit
- Tesseract OCR
- Pytesseract
- Pillow
- Sentence Transformers
- all-MiniLM-L6-v2
- PyTorch
- NumPy
- OpenCV
- Regular Expressions

## OCR

Tesseract OCR is used to read text from the uploaded food label image.

## Text Embedding

The extracted text is converted into numerical vectors using the Sentence Transformer model:

`all-MiniLM-L6-v2`

The model produces 384-dimensional embeddings.

## Attention Mechanism

A scaled dot-product attention mechanism is used to calculate relationships between the extracted text embeddings and generate relative importance scores.

## Information Extraction

Regular expressions are used to identify:

- Weight
- Calories
- Dates
- Protein
- Fat
- Carbohydrates
- Ingredients

## Project Structure

```text
Food_Label_Extractor/
│
├── app.py
├── ocr.py
├── embedding.py
├── attention.py
├── extractor.py
├── requirements.txt
└── README.md
