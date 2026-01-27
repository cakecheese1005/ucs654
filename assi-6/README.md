# Assignment 6 – Simulation Based Data Generation

# Assignment 6 – Simulation Based Data Generation for Machine Learning

## Objective
The objective of this assignment is to generate a synthetic dataset using a simulation tool and apply multiple machine learning models to analyze and predict system behavior. The assignment demonstrates how modelling and simulation can be used to create data for machine learning tasks when real-world data is unavailable or costly to obtain.

---

## Simulator Used
**SimPy (Python Discrete Event Simulation Library)**

SimPy is an open-source, Python-based library used for discrete-event simulation. It is widely used to model queueing systems, networks, and service processes.

---

## Simulation Description
A **single-server queueing system** was simulated. In this system:
- Entities arrive according to a stochastic arrival process.
- They wait in a queue if the server is busy.
- Each entity is served by a single server.
- The average waiting time of entities is recorded.

This simulation models real-world systems such as network routers, help desks, and service counters.

---

## Simulation Parameters and Ranges

| Parameter | Description | Range |
|---------|------------|-------|
| Arrival Rate | Rate at which entities arrive | 0.5 – 5 |
| Service Rate | Rate at which entities are served | 1 – 6 |
| Queue Capacity | Maximum queue size | 5 – 50 |
| Simulation Time | Total simulation duration | 50 – 200 |

---

## Data Generation Methodology
- Random values for simulation parameters were generated within defined bounds.
- The simulator was executed **1000 times** with different parameter combinations.
- For each simulation run, the **average waiting time** was recorded.
- The generated dataset was stored as `simulation_data.csv`.

---

## Machine Learning Task
- **Problem Type:** Regression  
- **Target Variable:** Average Waiting Time  
- **Input Features:** Arrival rate, service rate, queue capacity, simulation time

---

## Machine Learning Models Used
The following machine learning models were trained and evaluated:

- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- Gradient Boosting Regressor  

---

## Evaluation Metrics
Models were evaluated using the following metrics:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **R² Score**

The comparison results are stored in `model_comparison_results.csv`.

---

## Results and Analysis
- Linear models showed lower performance due to the non-linear nature of the simulation data.
- Tree-based models performed significantly better.
- **Gradient Boosting Regressor achieved the highest R² score**, indicating superior ability to capture non-linear relationships in simulation-generated data.
- A visual comparison of model performance is shown in `model_comparison_r2.png`.

---

## Conclusion
This assignment demonstrates that simulation-based synthetic data can effectively be used for machine learning tasks. Discrete-event simulation provides a controlled environment for data generation, and ensemble machine learning models are well-suited for predicting outcomes in non-linear simulated systems.

---

## Repository Contents
- `UCS654_sim.ipynb` – Colab notebook with simulation and ML code  
- `simulation_data.csv` – Synthetic dataset generated using simulation  
- `model_comparison_results.csv` – ML model evaluation results  
- `model_comparison_r2.png` – Performance comparison graph  

---

