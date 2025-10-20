# Prediction of Von Mises Stress using Machine Learning Model for Meta-Materials

**Authors:** Nitin Sharma, Srihariharan Ramasamy, Vigneshwar Subbammal Rohini Murali  
**Course:** Machine Learning Methods for Mechanics  

---

## Introduction

Metamaterials are artificially engineered materials designed to exhibit properties not found in nature. Their behavior depends on internal architecture rather than chemical composition.  
This project presents a **machine learning approach** to predict the **von Mises stress** distribution of 2D metamaterial unit cells. The results are compared with **Finite Element (FE)** simulations to validate the predictive accuracy.

---

## Data Generation

A dataset of 10,000 procedurally generated **2D unit cells** was created on a 10×10 grid using binary encoding (1 = material, 0 = void).  
Each unique geometry was generated from a symmetric 5×5 “seed” matrix and validated using:
- **Material connectivity** (single contiguous body)
- **No internal voids**
- **Boundary constraints** for tileability

These grids were converted into **continuous boundary coordinates** for FE simulation and machine learning input.

---

## Finite Element Simulations

Each geometry was simulated under 1% tensile strain using FE analysis.  
- The bottom surface was fixed; the top surface displaced.  
- Stress results were categorized into **4 von Mises stress brackets:**
  1. below 1500 MPa  
  2. 1501–2500 MPa  
  3. 2501–3500 MPa  
  4. above 3500 MPa  

This converted the regression output into a **classification problem**.

---

## Feature Engineering – Shape Frequency Features (SFF)

Each 10×10 binary image was translated into a **26-element feature vector** using the **Shape Frequency Feature (SFF)** method.  
- A library of 26 fundamental geometric templates (bars, blocks, L-shapes, diagonals, etc.) was defined.  
- Each template was slid across the unit cell, and matches were normalized to obtain feature frequencies.

This created a compact and interpretable geometric representation for ML models.

---

## Dataset Insights

- **Class imbalance:** Majority in stress bucket 2 (~6,500 samples).  
- **Material distribution:** Corners more likely to contain material.  
- **Feature usage:** Simple features (e.g., small bars, single pixels) dominate; complex patterns appear less frequently.

---

## Feature Analysis

- **Mutual Information (MI):** Identified influential SFFs (bars, small blocks, single pixels).  
- **Correlation analysis:** Revealed redundancy between similar features.  
- **Volume Fraction (VF):** Higher VF corresponds to higher stress classes.  

A reduced, more efficient feature set was derived for model training.

---

## Principal Component Analysis (PCA)

PCA reduced the dataset to **17 principal components**, retaining **90.59%** of total variance.  
This compressed representation was used to optimize model performance and training time.

---

## Machine Learning Models

### 1. Artificial Neural Network (ANN)
- Architecture: 3 hidden layers (64 → 32 → 32 neurons) with ReLU activations  
- Dropout (30%) to prevent overfitting  
- Standardized input data  

| Input Type | Weighted F1 Score |
|-------------|------------------|
| PCA (Raw + SFF) | **0.83** |
| Raw Geometry | 0.82 |
| SFF Only | 0.54 |

**Conclusion:** ANN performs best with PCA-transformed inputs.

---

### 2. Random Forest & XGBoost
Hyperparameter tuning via **Randomized Search Cross-Validation**.

| Input Type | Weighted F1 Score (XGBoost) |
|-------------|-----------------------------|
| Raw Geometry | **0.849** |
| Raw + SFF | 0.828 |
| PCA Features | 0.702 |

**Conclusion:** XGBoost performs best on raw geometric data.

---

### 3. Convolutional Neural Network (CNN)
- Architecture: **ResNet-18** (transfer learning from ImageNet)  
- Optimizer: AdamW with OneCycleLR  
- Batch Size: 64 | LR: 0.0003 | Image Size: 224×224  

| Metric | Score |
|--------|--------|
| Accuracy | **0.93** |
| Weighted F1 | **0.93** |
| Macro F1 | 0.90 |

**Conclusion:** CNN achieved the best performance and generalization, outperforming all other models.

---

## Interpretability

Using **SHAP (SHapley Additive Explanations)** and feature gain analysis:
- Raw geometric pixels provided strong global predictive power.
- Simple SFFs (bars, small blocks) offered interpretable insights into geometry–stress relationships.

---

## Conclusion

- Machine learning can **accurately predict von Mises stress** of metamaterials, reducing the need for computationally expensive FE simulations.  
- **CNN** models outperform ANN and XGBoost, achieving the highest accuracy and generalization.  
- **SFF** improves interpretability but has limited predictive benefit.  
- Future work: Explore **inverse design** and **contour-based feature extraction** for higher accuracy.

---

## References
1. Chen, Z. *et al.* “How to see hidden patterns in metamaterials with interpretable machine learning,” *Extreme Mechanics Letters*, 2022.  
2. Bastek, J.H. & Kochmann, D.M. “Inverse design of nonlinear mechanical metamaterials via video denoising diffusion models,” *Nature Machine Intelligence*, 2023.


---

## Repository Structure
1. Datasets- contains all the datasets utilised for training the model
2. Codes- contains the codes for all three models
