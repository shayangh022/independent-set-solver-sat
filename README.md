# Independent Set Solver using SAT (PySAT)

This Python project solves the Independent Set Problem using SAT solving techniques with the PySAT toolkit.

It reads a graph from a .clq file (DIMACS format), builds a CNF representation of the problem, solves it using the Minisat22 backend, and compares the solver's runtime to the theoretical brute-force complexity.

## Features
- Graph parser for .clq files
- CNF formula builder for independent set constraints
- DIMACS-compliant CNF generation
- Solver integration with PySAT / Minisat22
- Runtime analysis and visualization via matplotlib

## How to Run

```bash
python pro_independent_caculator.py
