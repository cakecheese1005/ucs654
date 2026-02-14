# Advance Mathematics Assignment  
## Learning Probability Density Functions using Roll-Number-Parameterized Non-Linear Model  

---

## 📌 Objective  

The objective of this assignment is to apply a **non-linear transformation** to real-world NO₂ air quality data and model the transformed data using a **Gaussian Probability Density Function (PDF)**.  

The parameters of the distribution are estimated using **Maximum Likelihood Estimation (MLE)**.

---

## 📂 Dataset  

**Dataset Used:** India Air Quality Dataset (Kaggle)  

**Feature Selected:**  
- NO₂ concentration  

---

## 🧮 Methodology  

### Step 1 – Data Preprocessing  

1. Loaded dataset using **Pandas**  
2. Selected the **NO₂ column**  
3. Removed missing values  
4. Converted data into NumPy array for computation  

---

### Step 2 – Non-Linear Transformation  

Each NO₂ value \( x \) is transformed into a new variable \( z \) using:

\[
z = x + a_r \sin(b_r x)
\]

Where:

\[
a_r = 0.05 (r \bmod 7)
\]

\[
b_r = 0.3 (r \bmod 5 + 1)
\]

Given:

\[
r = 102317272
\]

First compute:

\[
r \bmod 7 = 5
\]

\[
r \bmod 5 = 2
\]

So,

\[
a_r = 0.05 \times 5 = 0.25
\]

\[
b_r = 0.3 \times (2 + 1) = 0.9
\]

Final transformation:

\[
z = x + 0.25 \sin(0.9x)
\]

This transformation introduces **controlled non-linearity** into the dataset.

---

### Step 3 – Gaussian PDF Modeling  

The transformed variable \( z \) is modeled using:

\[
p(z) = c \cdot \exp\left(-\lambda (z - \mu)^2\right)
\]

Since this is a **Gaussian distribution**, parameters are estimated using **Maximum Likelihood Estimation (MLE)**:

\[
\mu = \text{mean}(z)
\]

\[
\sigma^2 = \text{variance}(z)
\]

\[
\lambda = \frac{1}{2\sigma^2}
\]

\[
c = \sqrt{\frac{\lambda}{\pi}}
\]

---

## 💻 Implementation  

**Programming Language:** Python  

**Libraries Used:**
- Pandas  
- NumPy  
- Math  

---

## 📊 Results  

Estimated Parameters:

- **Mean (μ)** = 25.8082  
- **Lambda (λ)** = 0.001460  
- **Normalization Constant (c)** = 0.021559  

---

## 📈 Interpretation  

- The non-linear transformation slightly perturbs the original NO₂ values.
- Despite the transformation, the data closely follows a Gaussian distribution.
- Parameters were estimated analytically using statistical formulas derived from MLE.

---

## ✅ Conclusion  

The NO₂ air quality data was successfully:

1. Preprocessed  
2. Transformed using a roll-number-parameterized non-linear model  
3. Modeled using a Gaussian Probability Density Function  

The parameters were estimated analytically using Maximum Likelihood Estimation, demonstrating how real-world environmental data can be transformed and statistically modeled using probability theory.

---

## 🚀 Key Learning Outcomes  

- Application of non-linear transformations  
- Understanding Gaussian PDF structure  
- Deriving parameters using Maximum Likelihood Estimation  
- Modeling real-world environmental data statistically  

---

