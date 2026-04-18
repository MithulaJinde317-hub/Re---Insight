# Re-Insight

Author: Mihtula J
Affiliation: Institute of applied sciences, Parul University
Email: mithullaajinde317@gmail.com
## 📄 Citation
This project is published on Zenodo:
https://doi.org/10.5281/zenodo.19638491

# 🔬 RE-Insight

Context-Aware Restriction Enzyme Analysis Tool for Mutation Differentiation

---

## 📌 Overview

**RE-Insight** is a Python-based bioinformatics tool designed to identify restriction enzymes that can differentiate closely related DNA sequences, such as wild-type and mutant variants.

Unlike conventional restriction site finders, this tool focuses on **comparative analysis**, enabling users to select enzymes useful for **PCR-RFLP experiments, mutation detection, and cloning workflows**.

---

## 🚀 Key Features

* 🧬 **Multi-Enzyme Scanning**
  Supports multiple restriction enzymes for comprehensive analysis

* 🔍 **Degenerate Base Recognition**
  Handles IUPAC ambiguity codes using regex-based pattern matching

* ⚡ **Mutation-Aware Comparison (Core Feature)**
  Identifies enzymes that uniquely cut:

  * Only wild-type sequence
  * Only mutant sequence

* 🧪 **In-Silico Digestion Simulation**
  Predicts fragment sizes after enzyme digestion

* 🔁 **Reverse Complement Analysis**
  Scans both DNA strands for accurate detection

* 📂 **FASTA File Support**
  Accepts real biological sequence data

---

## 🧠 How It Works

1. Input two DNA sequences (wild-type and mutant)
2. the program Converts enzyme recognition patterns into regex
3. Scans the  sequences for restriction sites
4. Compares enzyme cutting patterns
5. Output - enzymes that differentiate sequences
6. Simulate digestion fragments

---

## 📁 Project Structure

```
RE-Insight/
│
├── main.py              # Entry point
├── enzymes.py          # Enzyme database
├── degenerate.py       # Degenerate base handling
├── comparison.py       # Core comparison logic
├── utils.py            # Helper functions
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/RE-Insight.git
cd RE-Insight
```

### 2. Run the program

```bash
python main.py
```

---

## 🧪 Example

**Input:**

```
Wild-type:  GAATTCCGGAATTC  
Mutant:     GAATTCCGGTTTC  
```

**Output:**

```
Enzymes cutting ONLY wild-type: ['EcoRI']  
Enzymes cutting ONLY mutant: []  
```
sample data input provided - BRCA1 dataset is derived from reference sequence (NCBI RefSeq: NM_007294.4). A single nucleotide mutation was introduced to simulate variant analysis.
mutation created manually 

## Applications

* PCR-RFLP experiment design
* SNP / mutation detection
* Molecular cloning validation
* Bioinformatics education

## Technologies Used

* Python
* Regular Expressions (`re`)
* Modular programming approach

##  Limitations

* Limited enzyme dataset (expandable)
* No wet-lab validation (in-silico only)

---

##  Future Improvements

* Integration with REBASE database
* Visualization of restriction maps
* GUI / Web interface
* Machine learning for site prediction

---

## Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request.

#**NOTE**
Developed as a bioinformatics small project focusing on restriction enzyme-based mutation analysis.

