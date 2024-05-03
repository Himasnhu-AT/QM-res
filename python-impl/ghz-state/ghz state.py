from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator

num_qubits = 5
qc = QuantumCircuit(num_qubits, num_qubits, name="ghz")

# Create a GHZ state
qc.h(0)
for i in range(num_qubits - 1):
    qc.cx(i, i + 1)
# Insert a barrier before measurement
qc.barrier()
# Measure all of the qubits in the standard basis
for i in range(num_qubits):
    qc.measure(i, i)

sim_backend = BasicSimulator()
job = sim_backend.run(transpile(qc, sim_backend), shots=1024)
result = job.result()
print("Basic simulator : ")
print(result.get_counts(qc))