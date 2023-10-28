# Expressibility and entangling capability of parametrized quantum circuits

This is a repository to reproduce results from https://arxiv.org/abs/1905.10876

Content:
* `ExprEnt.py`, utility functions that compute expressibility (expr) and entangling capability (ent)
* `VariationalCircuit.py`, definition of the `VariationalCircuit` class
* * `circuits_3q.py`, `circuits_4q.py`, etc., files with instances of variational circuits
* `circuit-analyser.ipynb`, notebook that analyses variational circuits
* `csv` files that store the results of the analysis
* `plotting.ipynb` and `plotting2.ipynb`, notebooks to visualize the data
* `pareto-front.ipynb`, notebook that studies complexity and draws Pareto's front
