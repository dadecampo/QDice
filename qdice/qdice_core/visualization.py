import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

def visualize(qc: QuantumCircuit) -> None:
    qc.draw(output='mpl')
    plt.show()