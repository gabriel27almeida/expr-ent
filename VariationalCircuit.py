import qiskit as q
import random
from math import pi


class VariationalCircuit:
    def __init__(self, id, circuit_func, num_qubits, num_parameters, num_2q_gates=None, depth=None):
        self.id = id
        self.num_qubits = num_qubits
        self.num_parameters = num_parameters
        self.circuit = q.QuantumCircuit(num_qubits)
        self.circuit_func = circuit_func
        self.num_2q_gates = num_2q_gates
        self.depth = depth
    

    def generate_random(self, L):
        self.circuit = self.circuit_func([random.random()*2*pi for _ in range(self.num_parameters*L)], L)
