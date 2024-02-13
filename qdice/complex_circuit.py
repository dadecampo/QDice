from qdice_core.components import get_easy_qc
from qdice_core.simulation import simulate
from qdice_core.visualization import visualize

my_qc =  get_easy_qc()
print(simulate(my_qc))
visualize(my_qc)
