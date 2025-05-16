# Erdős–Rényi Randomized Graphs – IE102 Project

This repository contains the Python code used in building the **IE102 (Introduction to Probability and Statistics) Project** titled **"Erdős–Rényi Randomized Graphs"**.

> “The study of random graphs is central to understanding a wide variety of complex systems – from social networks and epidemiology to the internet and biological networks.”

---

## 🧠 Project Context

In the IE102 course at IIT Bombay, students were encouraged to explore **open-ended topics** related to **probability and statistics** for their final project. This flexibility allowed us to dive deep into areas that spark both curiosity and real-world relevance.

I chose to study the **Erdős–Rényi model of random graphs** — a deceptively simple yet profoundly powerful theoretical framework. It provides one of the earliest formalizations of how connections can randomly form in a network. Despite its simplicity, the model reveals **critical threshold behavior**, **phase transitions**, and surprising results that mirror complex phenomena in nature and technology.

---

## 📄 Final Report

All the insights, graphs, and results generated from the code in this repository are compiled in the final project report:

📘 **[View the Final Report (Google Drive)](https://drive.google.com/file/d/1ar_MQXolbE5ggT5ceoJhKIKBv9WD-Sgw/view)**

---

## 🗂️ Repository Contents

This repo contains modular Python scripts used for simulations and analysis:

### `connectivity.py`
Simulates random graphs for varying values of edge probability `p` and checks for connectivity across multiple trials. This script estimates the **critical threshold** where a graph transitions from disconnected to connected.

### `giant.py`
Analyzes the size of the **largest connected component** as `p` increases, demonstrating the **phase transition** behavior in Erdős–Rényi graphs.

### `epidemic_spread.py`
Models the **spread of an epidemic** over a random graph, showing how network randomness affects infection dynamics — a practical application of random graphs in real-world problems.

And some utility files that helps with generating graphs using **NetworkX** and visualizing them with **Matplotlib**.

---

## 🔬 Key Concepts Explored

- Threshold phenomena in random graphs
- Emergence of a giant component
- Probabilistic simulations and statistical averaging
- Modeling real-world networks and epidemic dynamics
- Differences between structured and random networks

---

## ⚙️ How to Run

Ensure you have Python 3 installed with the required libraries:

```bash
pip install networkx matplotlib numpy
