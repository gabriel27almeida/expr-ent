import qiskit as q
from math import pi, log
import random
import matplotlib.pyplot as plt
import numpy as np

def D(u, v):
    n = u.num_qubits
    D = 0
    for i in range(2**n):
        for j in range(i+1,2**n):
            D += abs(u.data[i]*v.data[j] - u.data[j]*v.data[i])**2
    return D

def bin(num, width):
    ans = []
    for i in range(width):
        ans.append((num // (2**(width-1-i))) % 2)
    return ans

def iota(j,b, v):
    n = v.num_qubits

    ans_data = np.zeros(2**(n-1), dtype=complex)
    for i in range(2**n):
        bin_repr = bin(i, n)
        if bin_repr[j] != b:
            continue

        aux_data = np.zeros(2**(n-1), dtype=complex)
        num = 0
        for k in range(n):
            if k == j:
                continue
            num *= 2
            num += bin_repr[k]
        
        aux_data[num] = v.data[i]
        ans_data += aux_data
    return q.quantum_info.Statevector(ans_data)

def meyer_wallach_measure(statevec):
    Q = 0
    n = statevec.num_qubits
    for j in range(n):
        Q += D(iota(j,0,statevec), iota(j,1,statevec))
    Q = Q*4/n
    return Q

def get_expr_ent(circuit, L, N_samples, n_bins, visualize = False):
    #random.seed(475)
    statevec_sim = q.Aer.get_backend("statevector_simulator")

    fidelities = []
    Q = []

    n_qubits = circuit.num_qubits

    for _ in range(N_samples):
        circuit.generate_random(L)
        c1 = circuit.circuit
        circuit.generate_random(L)
        c2 = circuit.circuit

        statevec1 = q.execute(c1, backend=statevec_sim).result().get_statevector()
        statevec2 = q.execute(c2, backend=statevec_sim).result().get_statevector()
        fidelities.append(q.quantum_info.state_fidelity(statevec1, statevec2))
        
        Q.append(meyer_wallach_measure(statevec1))
        Q.append(meyer_wallach_measure(statevec2))

    hist, bin_edges = np.histogram(fidelities, bins=n_bins)
    p_harr = []
    p_pqc = []
    N = 2**(n_qubits)
    for bin in range(n_bins):
        f1 = bin_edges[bin]
        f2 = bin_edges[min(bin+1,n_bins-1)]
        p_harr.append(((1-f1)**(N-1) - (1-f2)**(N-1)))
        p_pqc.append(hist[bin]/N_samples)

    if visualize:
        plt.stairs(p_harr, bin_edges,label = "Haar", alpha=0.6, fill=True)
        plt.stairs(p_pqc, bin_edges,label = "Circuit", alpha=0.6, fill=True, edgecolor = 'k')
        plt.xlabel("Fidelity")
        plt.ylabel("Probability")
        plt.title(f"{L} layers")
        plt.legend()
        plt.show()

    expressibility = 0
    
    for bin in range(n_bins):
        if p_pqc[bin]*p_harr[bin] == 0:
            continue
        expressibility += p_pqc[bin] * log(p_pqc[bin]/p_harr[bin])

    ent = np.mean(Q)
    
    return expressibility, ent