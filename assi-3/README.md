Advance Mathematics
Learning Probability Density Functions using Roll-Number-Parameterized Non-Linear Model
Objective
The objective of this assignment is to apply a non-linear transformation to real-world NO₂ air quality data and model the transformed data using a Gaussian Probability Density Function (PDF). The parameters of the distribution are estimated using statistical techniques.

Dataset
India Air Quality Dataset (Kaggle)

Feature used:

NO₂ concentration
Methodology
Step 1 – Data Preprocessing
Loaded dataset using Pandas
Selected NO₂ column
Removed missing values
Step 2 – Non-Linear Transformation
Each value (x) is transformed to (z) using:

z = x + a_r sin(b_r x)

where

a_r = 0.05 (r mod 7)
b_r = 0.3 (r mod 5 + 1)

r = 102317272

This introduces non-linearity into the data.

Step 3 – PDF Modeling
The transformed variable is modeled using:

p(z) = c · exp(-λ (z − μ)²)

Since this is a Gaussian distribution, parameters are estimated using Maximum Likelihood Estimation (MLE):

μ = mean(z)
σ² = variance(z)
λ = 1 / (2σ²)
c = sqrt(λ / π)
Implementation
Language: Python
Libraries:

Pandas
NumPy
Math
Results
Estimated parameters:

μ = 25.8082
λ = 0.001460
c = 0.021559

Conclusion
The NO₂ data was successfully transformed and modeled using a Gaussian probability density function. The parameters were estimated analytically using statistical methods.
