from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator

circ = QuantumCircuit.from_qasm_file("examples/qasm/entangled_registers.qasm")
print(circ)

# See the backend
sim_backend = BasicSimulator()

# Compile and run the Quantum circuit on a local simulator backend
job_sim = sim_backend.run(circ)
sim_result = job_sim.result()

# Show the results
print("simulation: ", sim_result)
print(sim_result.get_counts(circ))