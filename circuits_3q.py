from VariationalCircuit import *

circuits = []

def circ1(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=2*n
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)
        c.barrier()
    return c

circuits.append(VariationalCircuit("1-3q", circ1, 3, 6))

def circ2(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=2*n
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        for qubit in range(n-1):
            c.cnot(qubit, qubit+1)
        c.barrier()
    return c

circuits.append(VariationalCircuit("2-3q", circ2, 3, 6))

def circ3(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=3*n-1
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        for qubit in range(n-1):
            c.crz(theta[k*i+2*n+qubit],qubit,qubit+1)
        c.barrier()
    return c

circuits.append(VariationalCircuit("3-3q", circ3, 3, 8))

def circ4(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=3*n-1
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        for qubit in range(n-1):
            c.crx(theta[k*i+2*n+qubit],qubit,qubit+1)
        c.barrier()
    return c

circuits.append(VariationalCircuit("4-3q", circ4, 3, 8))

def circ5(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=4*n+n*(n-1)
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        for qubit in range(n):
            for qq in range(n-1):
                c.crz(theta[k*i+n+qubit*(n-1)+qq], qubit, (qubit+qq+1)%n)
        for qubit in range(n):
            c.rx(theta[k*i+2*n+n*(n-1)+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+3*n+n*(n-1)+qubit],qubit)
        c.barrier()
    return c

circuits.append(VariationalCircuit("5-3q", circ5, 3, 18))

def circ6(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=4*n+n*(n-1)
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        for qubit in range(n):
            for qq in range(n-1):
                c.crx(theta[k*i+n+qubit*(n-1)+qq], qubit, (qubit+qq+1)%n)
        for qubit in range(n):
            c.rx(theta[k*i+2*n+n*(n-1)+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+3*n+n*(n-1)+qubit],qubit)
        c.barrier()
    return c

circuits.append(VariationalCircuit("6-3q", circ6, 3, 18))

def circ7(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=14
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        c.crz(theta[k*i+2*n], 0, 1)
        for qubit in range(n):
            c.rx(theta[k*i+2*n+1+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+3*n+1+qubit],qubit)
        c.crz(theta[k*i+4*n+1],1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("7-3q", circ7, 3, 14))

def circ8(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=14
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        c.crx(theta[k*i+2*n], 0, 1)
        for qubit in range(n):
            c.rx(theta[k*i+2*n+1+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+3*n+1+qubit],qubit)
        c.crx(theta[k*i+4*n+1],1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("8-3q", circ8, 3, 14))

def circ9(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=n
    for i in range(L):
        for qubit in range(n):
            c.h(qubit)
        for qubit in range(n-1):
            c.cz(qubit, qubit+1)
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        c.barrier()
    return c

circuits.append(VariationalCircuit("9-3q", circ9, 3, 3))

def circ10(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=n

    for i in range(L):
        for qubit in range(n):
            c.cz(qubit, (qubit+1)%n)
        for qq in range(n):
            c.ry(theta[k*i+qq], qq)
        c.barrier()
    return c

circuits.append(VariationalCircuit("10-3q", circ10, 3, 3))

def circ11(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=10

    for i in range(L):
        for qubit in range(n):
            c.ry(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        c.cnot(0,1)
        c.ry(theta[k*i+2*n], 1)
        c.ry(theta[k*i+2*n+1], 2)
        c.rz(theta[k*i+2*n+2], 1)
        c.rz(theta[k*i+2*n+3], 2)
        c.cnot(1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("11-3q", circ11, 3, 10))

def circ12(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=10

    for i in range(L):
        for qubit in range(n):
            c.ry(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        c.cz(0,1)
        c.ry(theta[k*i+2*n], 1)
        c.ry(theta[k*i+2*n+1], 2)
        c.rz(theta[k*i+2*n+2], 1)
        c.rz(theta[k*i+2*n+3], 2)
        c.cz(1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("12-3q", circ12, 3, 10))

def circ13(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=4*n

    for i in range(L):
        for qubit in range(n):
            c.ry(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.crz(theta[k*i+n+qubit],qubit, (qubit+1)%n)
        for qubit in range(n):
            c.ry(theta[k*i+2*n+qubit], qubit)
        for qubit in range(n):
            c.crz(theta[k*i+3*n+qubit],qubit, (qubit-1)%n)
        c.barrier()
    return c

circuits.append(VariationalCircuit("13-3q", circ13, 3, 12))

def circ14(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=4*n

    for i in range(L):
        for qubit in range(n):
            c.ry(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.crx(theta[k*i+n+qubit],qubit, (qubit+1)%n)
        for qubit in range(n):
            c.ry(theta[k*i+2*n+qubit], qubit)
        for qubit in range(n):
            c.crx(theta[k*i+3*n+qubit],qubit, (qubit-1)%n)
        c.barrier()
    return c

circuits.append(VariationalCircuit("14-3q", circ14, 3, 12))

def circ15(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=2*n

    for i in range(L):
        for qubit in range(n):
            c.ry(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.cnot(qubit, (qubit+1)%n)
        for qubit in range(n):
            c.ry(theta[k*i+n+qubit], qubit)
        for qubit in range(n):
            c.cnot(qubit, (qubit-1)%n)
        c.barrier()
    return c

circuits.append(VariationalCircuit("15-3q", circ15, 3, 6))

def circ16(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=8

    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)

        c.crz(theta[k*i+2*n], 0,1)
        c.crz(theta[k*i+2*n+1],1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("16-3q", circ16, 3, 8))

def circ17(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=8

    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)

        c.crx(theta[k*i+2*n], 0,1)
        c.crx(theta[k*i+2*n+1],1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("17-3q", circ17, 3, 8))

def circ18(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=3*n

    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)
        for qubit in range(n):
            c.crz(theta[k*i+2*n+qubit], qubit, (qubit+1)%n)
        c.barrier()
    return c

circuits.append(VariationalCircuit("18-3q", circ18, 3, 9))

def circ19(theta, L):
    n=3
    c = q.QuantumCircuit(n)
    k=3*n

    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)
        for qubit in range(n):
            c.crx(theta[k*i+2*n+qubit], qubit, (qubit+1)%n)
        c.barrier()
    return c

circuits.append(VariationalCircuit("19-3q", circ19, 3, 9))



