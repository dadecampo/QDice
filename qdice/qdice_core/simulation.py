from qiskit_aer import AerSimulator
__sim = AerSimulator()

def simulate(qc) -> list:
    job = __sim.run(qc)
    result = job.result()
    return result.get_counts()