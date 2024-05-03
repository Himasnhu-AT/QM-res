from qiskit import QuantumCircuit

from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import CommutationAnalysis, CommutativeCancellation

circuit = QuantumCircuit(5)
# Quantum Instantaneous Polynomial Time example
circuit.cx(0, 1)
circuit.cx(2, 1)
circuit.cx(4, 3)
circuit.cx(2, 3)
circuit.z(0)
circuit.z(4)
circuit.cx(0, 1)
circuit.cx(2, 1)
circuit.cx(4, 3)
circuit.cx(2, 3)
circuit.cx(3, 2)

print(circuit)

pm = PassManager()
pm.append([CommutationAnalysis(), CommutativeCancellation()])
new_circuit = pm.run(circuit)
print(new_circuit)