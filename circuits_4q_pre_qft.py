from VariationalCircuit import *

circuits = []

def circ1(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=2*n

    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)
        c.barrier()
    return c

circuits.append(VariationalCircuit("1", circ1, 4, 8))

def circ2(theta, L):
    n=4
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

circuits.append(VariationalCircuit("2", circ2, 4, 8))

def circ3(theta, L):
    n=4
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

circuits.append(VariationalCircuit("3", circ3, 4, 11))

def circ4(theta, L):
    n=4
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

circuits.append(VariationalCircuit("4", circ4, 4, 11))

def circ5(theta, L):
    n=4
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

circuits.append(VariationalCircuit("5", circ5, 4, 28))

def circ6(theta, L):
    n=4
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

circuits.append(VariationalCircuit("6", circ6, 4, 28))

def circ7(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=19
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        c.crz(theta[k*i+2*n], 0, 1)
        c.crz(theta[k*i+2*n+1], 2, 3)
        for qubit in range(n):
            c.rx(theta[k*i+2*n+2+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+3*n+2+qubit],qubit)
        c.crz(theta[k*i+4*n+2],1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("7", circ7, 4, 19))

def circ8(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=19
    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        c.crx(theta[k*i+2*n], 0, 1)
        c.crx(theta[k*i+2*n+1], 2, 3)
        for qubit in range(n):
            c.rx(theta[k*i+2*n+2+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+3*n+2+qubit],qubit)
        c.crx(theta[k*i+4*n+2],1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("8", circ8, 4, 19))

def circ9(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=4
    for i in range(L):
        for qubit in range(n):
            c.h(qubit)
        for qubit in range(n-1):
            c.cz(qubit, qubit+1)
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        c.barrier()
    return c

circuits.append(VariationalCircuit("9", circ9, 4, 4))

def circ10(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=4

    for i in range(L):
        for qubit in range(n):
            c.cz(qubit, (qubit+1)%n)
        for qq in range(n):
            c.ry(theta[k*i+qq], qq)
        c.barrier()
    return c

circuits.append(VariationalCircuit("10", circ10, 4, 4))

def circ11(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=12

    for i in range(L):
        for qubit in range(n):
            c.ry(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        c.cnot(0,1)
        c.cnot(2,3)
        c.ry(theta[k*i+2*n], 1)
        c.ry(theta[k*i+2*n+1], 2)
        c.rz(theta[k*i+2*n+2], 1)
        c.rz(theta[k*i+2*n+3], 2)
        c.cnot(1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("11", circ11, 4, 12))

def circ12(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=12

    for i in range(L):
        for qubit in range(n):
            c.ry(theta[k*i+qubit],qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit],qubit)
        c.cz(0,1)
        c.cz(2,3)
        c.ry(theta[k*i+2*n], 1)
        c.ry(theta[k*i+2*n+1], 2)
        c.rz(theta[k*i+2*n+2], 1)
        c.rz(theta[k*i+2*n+3], 2)
        c.cz(1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("12", circ12, 4, 12))

def circ13(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=16

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

circuits.append(VariationalCircuit("13", circ13, 4, 16))

def circ14(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=16

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

circuits.append(VariationalCircuit("14", circ14, 4, 16))

def circ15(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=8

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

circuits.append(VariationalCircuit("15", circ15, 4, 8))

def circ16(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=11

    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)

        c.crz(theta[k*i+2*n], 0,1)
        c.crz(theta[k*i+2*n+1],2,3)
        c.crz(theta[k*i+2*n+2],1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("16", circ16, 4, 11))

def circ17(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=11

    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)

        c.crx(theta[k*i+2*n], 0,1)
        c.crx(theta[k*i+2*n+1],2,3)
        c.crx(theta[k*i+2*n+2],1,2)
        c.barrier()
    return c

circuits.append(VariationalCircuit("17", circ17, 4, 11))

def circ18(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=12

    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)
        for qubit in range(n):
            c.crz(theta[k*i+2*n+qubit], qubit, (qubit+1)%n)
        c.barrier()
    return c

circuits.append(VariationalCircuit("18", circ18, 4, 12))

def circ19(theta, L):
    n=4
    c = q.QuantumCircuit(n)
    k=12

    for i in range(L):
        for qubit in range(n):
            c.rx(theta[k*i+qubit], qubit)
        for qubit in range(n):
            c.rz(theta[k*i+n+qubit], qubit)
        for qubit in range(n):
            c.crx(theta[k*i+2*n+qubit], qubit, (qubit+1)%n)
        c.barrier()
    return c

circuits.append(VariationalCircuit("19", circ19, 4, 12))



