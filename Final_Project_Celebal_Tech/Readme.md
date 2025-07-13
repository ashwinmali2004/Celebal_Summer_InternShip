# Document Clustering and Topic Modeling

## Overview

This project applies unsupervised machine learning techniques—specifically **Latent Dirichlet Allocation (LDA)** and **K-Means Clustering**—to group and understand large collections of text documents. It aims to extract hidden topics and structure from unlabelled textual data.

The project was completed as the final deliverable for a data science internship.

## Project Structure

├── main.ipynb # Main Jupyter Notebook containing the implementation

├── data/ # Folder containing dataset files

└── README.md # Project description and instructions

## Objectives

- Perform text preprocessing and feature extraction (TF-IDF, CountVectorizer).
- Apply **K-Means Clustering** for document grouping.
- Apply **Latent Dirichlet Allocation (LDA)** for topic modeling.
- Compare results from both methods to evaluate their effectiveness.
- Visualize clusters and topics for interpretability.

## Algorithms Used

### 1. K-Means Clustering
- Groups similar documents based on TF-IDF features.
- Visualized using dimensionality reduction (e.g., PCA or t-SNE).

### 2. Latent Dirichlet Allocation (LDA)
- Uncovers latent semantic topics in a corpus.
- Topics interpreted by analyzing top keywords per topic.

## Dataset

The dataset used for this project is located in the `data/` folder and consists of a collection of textual documents suitable for topic modeling and clustering.

## Dependencies

- Python 3.8+
- Jupyter Notebook
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- gensim
- pyLDAvis

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
(Note: If no requirements.txt is provided, manually install packages as needed.)

How to Run
Clone this repository or download the files.

Place your text dataset in the data/ directory if not already present.

Open and run the main.ipynb notebook step-by-step in Jupyter Notebook.

Results
K-Means provided clear clusters for document grouping, evaluated using inertia and silhouette scores.

LDA effectively identified coherent topics across documents, evaluated using coherence score and word clouds.

Topic and cluster visualizations helped better understand the underlying themes in the text corpus.
```

# Conclusion
Both K-Means and LDA are powerful tools for document clustering and topic modeling. K-Means excels in separating documents into distinct clusters, while LDA provides interpretable topics, making it well-suited for large-scale corpus exploration.
