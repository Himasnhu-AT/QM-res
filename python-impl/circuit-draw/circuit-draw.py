from qiskit import QuantumCircuit

def build_bell_circuit():
    """Returns a circuit putting 2 qubits in the Bell state."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc

bell_circuit = build_bell_circuit()

print(bell_circuit)