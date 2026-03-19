# 🎬 Movie Recommendation System

## 📌 Problem Statement

With the rapid growth of online streaming platforms, users are overwhelmed with a huge number of movie choices.
It becomes difficult to decide **what to watch next**.

This project solves this problem by building a **Movie Recommendation System** that suggests similar movies based on user selection.

---

## 💡 Solution

This system uses **Content-Based Filtering** to recommend movies by analyzing:

* Movie genres
* Keywords
* Cast and crew
* Overview/description

It calculates similarity between movies using **cosine similarity** and recommends the **top 10 similar movies**.

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* Streamlit (for UI)

---

## 📂 Dataset

We used the following datasets:

* TMDB 5000 Movies Dataset
* TMDB 5000 Credits Dataset

Due to GitHub file size limitations, the processed model file is hosted externally.

---

## 🔗 Model / Data File Download

Download the trained data file from here:

👉 **[Click to Download movie_data.pkl](PASTE_YOUR_GITHUB_RELEASE_LINK_HERE)**

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https:https://github.com/SURESH-DEV10/Movie-Recommendation-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

(Add your Streamlit link here after deployment)

---

## 🎯 Features

* Movie recommendation based on similarity
* Clean and interactive UI
* Displays movie posters
* Fast and efficient

---

## ⚠️ Note

The `movie_data.pkl` file is not included in the repository due to GitHub's file size limit.
It is downloaded dynamically from the provided link.

---


## 👨‍💻 Authors

* Suresh Raneni


---

## 📌 Future Improvements

* Add collaborative filtering
* Add user login system
* Improve recommendation accuracy
* Deploy on cloud with database

---
