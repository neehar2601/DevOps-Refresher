# Git & GitHub: A DevOps Analogy (Time Machine + Shop + Truck)

This guide explains Git and GitHub using a simple “parallel universe + delivery” analogy.

## Core concepts

- **Git**: The time machine on your laptop. It saves snapshots (commits) of your project over time.
- GitHub: The online shop that hosts your repository so you can collaborate, review, and share.
- Repository (repo): Your project folder plus its Git history (stored in a hidden `.git` directory).

## The three “places” your changes live

Think of your work moving through three zones:

1. Working directory (workbench): Where you edit files.
2. Staging area (loading dock): Where you select what will go into the next snapshot.
3. Commit history (sealed shipments): Permanent snapshots with messages.

## Parallel universes: branches

- `main` branch (real world): Stable, approved inventory.
- Feature branch (parallel universe): A safe place to experiment without breaking `main`.

Create a branch:
```bash
git switch -c feature/login
