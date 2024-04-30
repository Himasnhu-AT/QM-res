# Plaquette_check QASM

## Description

This QASM code implements a simple quantum circuit to perform a plaquette check operation. It involves initializing a 5-qubit quantum register (`q`), applying Pauli-X gates to qubits 1 and 4, entangling the qubits, and then measuring each qubit.

## Prerequisites

- Make sure you have a quantum simulator or quantum hardware platform that supports QASM 2.0 and the gates used in the code, including Pauli-X gates (X) and controlled-NOT (CX) gates.
- Include the standard quantum library `qelib1.inc`, which provides definitions for common quantum gates.

## Usage

1. Load the QASM file into your quantum simulator or quantum hardware platform.
2. Run the simulation or execute the circuit on the quantum hardware.

## Circuit Details

- **Quantum Register**: One quantum register `q` consisting of 5 qubits.
- **Pauli-X Gate (X)**: Applied to qubits 1 and 4 to flip their states from |0⟩ to |1⟩.
- **Controlled-NOT Gate (CX)**: Entangles qubits 0, 1, 3, and 4 with qubit 2.
- **Barrier**: Used to separate different parts of the circuit, ensuring no gate optimizations occur across it.
- **Measurements**: Each qubit is measured, and the results are stored in classical register `c`.

## Example

Suppose all qubits are initialized to |0⟩. After applying this circuit:
- Qubits 1 and 4 will be flipped to |1⟩.
- Qubits 0, 1, 3, and 4 will be entangled with qubit 2.
- The measurement results in classical register `c` will represent the collapsed states of the qubits after measurement.
