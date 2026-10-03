# NumPy Matrix Operations

**Author:** Ayush Rajput  
**Track:** AI & ML — Level 1, Day 14  
**Language:** Python  
**Library:** NumPy  
**Environment:** Jupyter Notebook or Python terminal

## Objective
Create two user-defined matrices and perform addition, subtraction, matrix multiplication, and transpose operations.

## Requirements
- Python 3.8 or newer
- NumPy

Install NumPy:
```bash
pip install -r requirements.txt
```

## Run
```bash
python matrix_operations.py
```

Enter the row count and column count for each matrix, then enter each row's values separated by spaces.

## Operations
- **Addition:** `A + B` (same dimensions required)
- **Subtraction:** `A - B` (same dimensions required)
- **Matrix multiplication:** `A @ B` (columns of A must equal rows of B)
- **Transpose:** `A.T` (rows and columns are interchanged)

The program checks dimensions before performing operations and displays a clear message when an operation is not valid.
