# SIMPLE-QASM

## Description

This QASM (Quantum Assembly Language) code is a simple quantum circuit written for a two-qubit system. It applies the Hadamard gate to the first qubit (`q[0]`) and then performs a controlled-NOT (CNOT) gate with `q[0]` as the control qubit and `q[1]` as the target qubit.

## Prerequisites

- This code assumes you have a quantum simulator or quantum hardware platform that supports QASM and the gates used in the code, namely the Hadamard gate (H) and the controlled-NOT (CX) gate.
- Ensure that you have included the standard quantum library `qelib1.inc`, which provides definitions for common quantum gates.

## Usage

1. Load the QASM file into your quantum simulator or quantum hardware platform.
2. Run the simulation or execute the circuit on the quantum hardware.

## Circuit Details

- **Quantum Register**: `q[2]` declares a quantum register with two qubits.
- **Hadamard Gate (H)**: Applied to `q[0]`, it creates a superposition of states, putting the qubit in a state of equal probability of being measured as 0 or 1.
- **Controlled-NOT Gate (CX)**: Applied with `q[0]` as the control qubit and `q[1]` as the target qubit, it flips the state of the target qubit if the control qubit is in state |1⟩.

## Example

Suppose `q[0]` is initialized to |0⟩ and `q[1]` is initialized to |0⟩. After applying this circuit:

- `q[0]` will be in a superposition of states (|0⟩ + |1⟩) / √2.
- `q[1]` will be in the same state as `q[0]`, as a result of the controlled-NOT gate.
