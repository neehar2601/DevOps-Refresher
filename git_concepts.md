# Git & GitHub: The DevOps Analogy 🚛

## 🧠 The Core Concepts

* **Git (The Time Machine 🕰️):** A tool on your laptop that saves snapshots of your work history.
* **GitHub (The Shop 🏪):** The central website/cloud where code is stored and shared.
* **Repository (The Lab/Project):** The folder where your project lives.

## 🌌 The "Parallel Universe" Workflow

### 1. Branches
* **Main Branch (Hawkins/Real World):** The safe, production-ready code.
* **Feature Branch (The Upside Down):** An isolated parallel dimension. You can experiment and break things here without affecting the Real World.

### 2. The Cycle
1.  **Work in the Upside Down:** You write and test code in your isolated branch (`git checkout -b feature`).
2.  **Staging (`git add`):** You pick which files (harvest) to load onto the truck.
3.  **Commit (`git commit`):** You seal the truck and write in the logbook.
4.  **Push (`git push`):** You drive the truck to the Shop's back room (GitHub).
5.  **Pull Request (The Inspection 🔍):** You ask your team to inspect the cargo.
6.  **Merge (The Portal 🌀):** Once approved, the portal opens, and your changes are brought into the Real World (`main`).

### 🔑 Key Term
* **Origin:** The nickname for the remote Shop URL in your GPS.
