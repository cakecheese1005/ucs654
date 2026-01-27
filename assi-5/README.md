# Assignment 5 – Text Conversational Model Selection using TOPSIS

## Objective
The objective of this assignment is to apply the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method to identify the best **pre-trained text conversational model**.  
The assignment demonstrates how multi-criteria decision-making techniques can be used to compare multiple conversational AI models based on system-level and output-based performance metrics.

---

## Task Category
**Text Conversational**  
(Assigned for roll numbers ending with **4 or 9**)

---

## Models Used
The following **pre-trained conversational / instruction-based models** were selected from the **Hugging Face Model Hub**:

- DialoGPT-small  
- DialoGPT-medium  
- FLAN-T5-small  
- FLAN-T5-base  
- BlenderBot-90M  

All models were used **without any fine-tuning**.

---

## Experimental Setup
- Platform: **Google Colab**
- Framework: **Hugging Face Transformers**
- Backend: **PyTorch**
- Hardware: CPU

### Common Conversational Prompt
User: I am feeling very stressed about my exams.
Assistant:

All models were executed on the **same conversational prompt** to ensure a fair and consistent comparison.

---

## Evaluation Criteria
To avoid subjective scoring, **observable and measurable metrics** were extracted directly from model execution.

| Criterion | Description | Type |
|---------|------------|------|
| Model Size (M) | Number of parameters (in millions) | Cost |
| Latency (s) | Time taken to generate a response | Cost |
| Response Length | Number of words in the generated reply | Benefit |
| Keyword Matches | Count of stress/exam-related keywords in output | Benefit |

Keyword relevance was calculated using a predefined list of stress-related terms such as *stress, exam, relax, focus, calm,* etc.

---

## Methodology
1. Load each pre-trained conversational model from Hugging Face.
2. Generate a conversational response using `model.generate()`.
3. Measure inference latency and model size.
4. Extract output-based metrics such as response length and keyword relevance.
5. Construct a decision matrix using the extracted criteria.
6. Apply the **TOPSIS algorithm** with equal weights assigned to all criteria.
7. Rank the models based on their TOPSIS scores.
8. Visualize the ranking using bar graphs.

---

## Results and Analysis
- All models were successfully executed and evaluated on the same input prompt.
- Smaller models showed lower latency but varied in response quality.
- Larger models generated longer responses but incurred higher computational cost.
- The **TOPSIS ranking identified the most balanced conversational model** by considering both performance and efficiency.
- The final ranking is visualized using a TOPSIS score bar graph.

---

## Conclusion
This assignment demonstrates that **TOPSIS can effectively be applied to select the best pre-trained conversational model** by jointly considering multiple performance criteria.  
Using output-based and system-level metrics ensures a transparent and reproducible evaluation without relying on manual quality scoring.

---

## Repository Contents
- `text_conversational_topsis.ipynb` – Complete implementation and experiments  
- `results/topsis_conversational_ranking.png` – TOPSIS ranking visualization  
- `README.md` – Project description and methodology  

---

## Tools & Libraries Used
- Python  
- Hugging Face Transformers  
- PyTorch  
- NumPy  
- Pandas  
- Matplotlib  

---

## Author
**Ananya Singh**  
Course: **UCS654**

