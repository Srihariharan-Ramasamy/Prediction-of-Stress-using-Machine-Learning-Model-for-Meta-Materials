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

## Repository Structure
1. Datasets- contains all the datasets utilised for training the model
2. Codes- contains the codes for all three models (ANN, XGBoost, CNN)
