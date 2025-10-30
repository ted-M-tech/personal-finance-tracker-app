# Personal Finance Tracker App

## Project Overview

This project is a Python-based interactive, text-based Personal Finance Tracker App. It helps users manage and analyze their spending habits. Users can import a CSV file containing transaction data, perform operations like viewing, adding, editing, and deleting transactions, and analyze spending patterns. The app also includes data visualization capabilities, displaying monthly spending trends and top spending categories.

The project emphasizes Python programming, pandas for data handling, and matplotlib for visualization, along with GitHub for collaboration and version control.

## Transaction Data
Original Data is from Kaggle: https://www.kaggle.com/datasets/tharunprabu/my-expenses-data/data

## Development Conventions

This project follows a trunk-based development branching model. The `main` branch is the trunk, and all development is done in short-lived feature branches.

### Branch Naming Convention

When creating a new branch, please follow this naming convention:

`[developername]/issue[#]`

For example: `john/issue123`

This makes it easy to identify who is working on the branch and which issue it relates to.

### Branching Strategy

```
main (trunk)
  |
  +-- [developername]/issue[1] (feature branch)
  |     |
  |    (commit)
  |     |
  |    (commit)
  |     /
  +-- (merge)
  |
  +-- [developername]/issue[2] (feature branch)
  |     |
  |    (commit)
  |     /
  +-- (merge)
  |
 (HEAD)
```
