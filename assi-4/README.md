# Learning Probability Density Functions using GANs  

---

## 📌 Overview  

This project focuses on estimating the **Probability Density Function (PDF)** of an unknown random variable using only observed samples.  

Instead of assuming any analytical or parametric distribution (such as Gaussian or Exponential), a **Generative Adversarial Network (GAN)** is trained to learn the distribution directly from data.

The experiment is performed on **NO₂ concentration data**, which is first transformed using a nonlinear function and then modeled using a GAN.

---

## 📂 Dataset  

- **Feature Used:** NO₂ concentration  
- **Source:** India Air Quality Dataset (Kaggle)  

---

## 🧹 Preprocessing  

1. Selected only the NO₂ column  
2. Removed missing values  
3. Converted values to numerical format  
4. Applied nonlinear transformation  
5. Used transformed samples for GAN training  

---

## 🔁 Data Transformation  

Each NO₂ value \( x \) is transformed using the nonlinear mapping:

\[
z = x + a_r \sin(b_r x)
\]

Where:

\[
a_r = 0.5 \times (r \bmod 7)
\]

\[
b_r = 0.3 \times ((r \bmod 5) + 1)
\]

---

### Parameters Used  

**Roll Number:** 102317272  

\[
r \bmod 7 = 6
\]

\[
r \bmod 5 = 2
\]

\[
a_r = 0.5 \times 6 = 3.0
\]

\[
b_r = 0.3 \times (2 + 1) = 0.9
\]

Final transformation:

\[
z = x + 3.0 \sin(0.9x)
\]

This introduces controlled non-linearity and produces an **unknown probability distribution**.

---

## 📊 Distribution of Transformed Data  

The empirical distribution of the transformed variable \( z \) is visualized using histogram density estimation.

**Real Distribution**

---

## 🤖 GAN Architecture  

### Generator  

- **Input:** Gaussian noise sampled from \( \mathcal{N}(0,1) \)  
- **Output:** Synthetic samples of transformed variable  
- **Architecture:**  
  - Fully connected neural network  
  - ReLU activation functions  
  - Final linear output layer  

---

### Discriminator  

- **Input:** Real or generated samples  
- **Output:** Probability of the sample being real  
- **Architecture:**  
  - Fully connected neural network  
  - ReLU hidden layers  
  - Sigmoid output layer  

---

## ⚙️ Training Details  

- **Loss Function:** Binary Cross Entropy  
- **Optimizer:** Adam  
- **Learning Rate:** 0.001  
- **Epochs:** 3000  
- **Batch Size:** 256  

No parametric probability distribution is assumed during training.

The generator learns implicitly by competing with the discriminator in a minimax game.

---

## 📈 PDF Estimation Procedure  

After training the GAN:

1. A large number of synthetic samples are generated using the trained generator  
2. Histogram-based density estimation is applied  
3. The Probability Density Function is approximated  

---

## 📊 Results  

### Generated PDF from GAN  

**GAN PDF**

---

### Comparison: Real vs Generated Distribution  

**Comparison Plot**

---

## 🔎 Observations  

- The generator successfully captures the overall shape of the distribution  
- Good mode coverage is observed  
- Training stabilizes after initial adversarial fluctuations  
- No significant mode collapse detected  
- Minor deviations appear in extreme tails due to limited sampling  

---

## ✅ Conclusion  

This project demonstrates that **Generative Adversarial Networks can effectively learn unknown probability density functions directly from sample data.**

The generator implicitly models the distribution by transforming random noise into realistic samples, allowing the PDF to be approximated without assuming any predefined analytical form.

This highlights the power of adversarial learning in non-parametric density estimation.

---

## 🛠 Tools and Libraries  

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- PyTorch  

---

## 🚀 Key Learning Outcomes  

- Non-parametric density estimation  
- Adversarial training dynamics  
- GAN architecture design  
- Implicit distribution modeling  
- Practical PDF approximation using deep learning  

---

