# Netflix Clustering MLOps Project

## 📊 Deskripsi Proyek

Project ini melakukan eksplorasi data, preprocessing, feature engineering, scaling, balancing, serta clustering pada dataset Netflix yang diperoleh dari Kaggle.  
Selain itu, project ini di-deploy menggunakan MLOps pipeline berbasis Jenkins, Docker, dan GitHub untuk otomatisasi training dan deployment.

---

## 📂 Sumber Data

Link dataset:  
https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies/data

---

## 🏗 Struktur Direktori
MLOps_Project/
├── data/
│ ├── titles.csv
│ └── credits.csv
├── Dockerfile
├── Jenkinsfile
├── README.md
├── requirements.txt
└── full_pipeline.py


---

## 🛠 Tools & Library

| Kategori | Tools |
| -------- | ----- |
| Bahasa Pemrograman | Python 3.9 |
| Data Processing | pandas, numpy |
| Visualisasi | seaborn, matplotlib |
| Clustering | scikit-learn |
| MLOps | GitHub, Jenkins, Docker |

---

## 🚀 Alur Pipeline

1. Data diambil dari Kaggle
2. Preprocessing (cleaning, log transform, feature scaling)
3. Feature Selection (penggunaan skor & votes)
4. Clustering menggunakan K-Means
5. Pipeline diotomasi melalui:
   - GitHub (version control)
   - Jenkins (CI/CD automation)
   - Docker (containerization)
6. Deployment


