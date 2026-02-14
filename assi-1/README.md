# ucs654

## web-service link:link:https://ucs654-ananya-102303594.streamlit.app/

## package:https://pypi.org/project/Topsis-Ananya-102303594/0.2/

# Assignment 01 – TOPSIS Implementation

**Course:** UCS654 – Quantitative Methods  
**Assignment:** Assignment 01 – TOPSIS  
**Instructor:** Dr. P. S. Rana  
**Student Name:** Ananya Singh  
**Roll Number:** 102303594  

---

## 📌 Introduction

This assignment implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method for multi-criteria decision making (MCDM).  
TOPSIS is used to rank alternatives based on their distance from an ideal best and an ideal worst solution.

The assignment is divided into three parts:

1. **Part 1:** Understanding and implementation of TOPSIS logic  
2. **Part 2:** Creating a reusable Python package and publishing it on PyPI  
3. **Part 3:** Developing and deploying a web service using Streamlit  

---

## 🧠 Methodology (TOPSIS Algorithm)

The TOPSIS algorithm follows these steps:

1. **Input Data**  
   - A CSV file containing alternatives and criteria values  
   - Weights for each criterion  
   - Impact of each criterion (`+` for benefit, `-` for cost)

2. **Normalization**  
   The decision matrix is normalized using vector normalization.

3. **Weighted Normalized Matrix**  
   Each normalized value is multiplied by its respective weight.

4. **Ideal Best & Ideal Worst**  
   - Ideal Best: best values based on impacts  
   - Ideal Worst: worst values based on impacts  

5. **Distance Calculation**  
   Euclidean distance of each alternative from:
   - Ideal Best  
   - Ideal Worst  

6. **TOPSIS Score Calculation**  


7. **Ranking**  
Alternatives are ranked based on descending TOPSIS scores.

---

## 📊 Result

- The final output is a CSV file containing:
- TOPSIS Score
- Rank of each alternative

- Higher TOPSIS score ⇒ Better alternative

---


---

---

# TOPSIS Python Package (Part 2)

**Course:** UCS654 – Quantitative Methods  
**Assignment:** Assignment 01 – TOPSIS  
**Part:** Part 2 – Python Package Creation  
**Student Name:** Ananya Singh  
**Roll Number:** 102303594  

---

## 📌 Objective

The objective of this part is to convert the TOPSIS algorithm into a **reusable Python package**, publish it on **PyPI**, and allow users to run TOPSIS directly from the command line.

---

## 📦 Package Information

- **Package Name:** Topsis-Ananya-102303594  
- **Version:** 0.2  
- **Platform:** PyPI  
- **Language:** Python  

🔗 **PyPI Link:**  
https://pypi.org/project/Topsis-Ananya-102303594/

---

## ⚙️ Installation

Install the package using pip:

```bash
pip install Topsis-Ananya-102303594


# 🌐 PART-3 : README.md (Web Service – Streamlit)

👉 **Location:** `assi-1/part-3/README.md`

```md
# TOPSIS Web Service (Part 3)

**Course:** UCS654 – Quantitative Methods  
**Assignment:** Assignment 01 – TOPSIS  
**Part:** Part 3 – Web Service Development  
**Student Name:** Ananya Singh  
**Roll Number:** 102303594  

---

## 📌 Objective

The objective of this part is to develop a **web-based interface** for the TOPSIS algorithm using **Streamlit**, allowing users to run TOPSIS without using the command line.

---

## 🌐 Web Application Features

- Upload CSV file
- Enter weights and impacts
- Run TOPSIS algorithm
- Download result CSV file
- User-friendly interface

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Streamlit
- GitHub
- Streamlit Cloud

---

## ▶️ Running the App Locally

1. Install dependencies:

```bash
pip install -r requirements.txt

