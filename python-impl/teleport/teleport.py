from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import transpile
from qiskit.providers.basic_provider import BasicSimulator

coupling_map = [[0, 1], [0, 2], [1, 2], [3, 2], [3, 4], [4, 2]]
backend = BasicSimulator()

q = QuantumRegister(3, "q")
c0 = ClassicalRegister(1, "c0")
c1 = ClassicalRegister(1, "c1")
c2 = ClassicalRegister(1, "c2")
qc = QuantumCircuit(q, c0, c1, c2, name="teleport")

# Prepare an initial state
qc.u(0.3, 0.2, 0.1, q[0])

# Prepare a Bell pair
qc.h(q[1])
qc.cx(q[1], q[2])

# Barrier following state preparation
qc.barrier(q)

# Measure in the Bell basis
qc.cx(q[0], q[1])
qc.h(q[0])
qc.measure(q[0], c0[0])
qc.measure(q[1], c1[0])

# Apply a correction
qc.barrier(q)
qc.z(q[2]).c_if(c0, 1)
qc.x(q[2]).c_if(c1, 1)
qc.measure(q[2], c2[0])

initial_layout = {q[0]: 0, q[1]: 1, q[2]: 2}
job = backend.run(
    transpile(qc, backend=backend, coupling_map=None, initial_layout=initial_layout), shots=1024
)

result = job.result()
print(result.get_counts(qc))

# Second version: mapped to 2x8 array coupling graph
job = backend.run(
    transpile(qc, backend=backend, coupling_map=coupling_map, initial_layout=initial_layout),
    shots=1024,
)
result = job.result()
print(result.get_counts(qc))