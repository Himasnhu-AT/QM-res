from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.providers.basic_provider import BasicSimulator

# making first circuit: bell state
qc1 = QuantumCircuit(2, 2)
qc1.h(0)
qc1.cx(0, 1)
qc1.measure([0, 1], [0, 1])

# making another circuit: superpositions
qc2 = QuantumCircuit(2, 2)
qc2.h([0, 1])
qc2.measure([0, 1], [0, 1])

# running the job
sim_backend = BasicSimulator()
job_sim = sim_backend.run(transpile([qc1, qc2], sim_backend))
sim_result = job_sim.result()

# Show the results
print(sim_result.get_counts(qc1))
print(sim_result.get_counts(qc2))