from qiskit import QuantumCircuit

def get_easy_qc() -> QuantumCircuit:
    qc = QuantumCircuit(3, 3)
    qc.measure([0,1,2], [0,1,2])
    return qc
