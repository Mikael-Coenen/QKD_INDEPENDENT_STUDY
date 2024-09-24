from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply a Hadamard gate to put the qubit into superposition
qc.h(0)

# Get the statevector of the qubit
state = Statevector.from_instruction(qc)

# Print the statevector to see the amplitudes of |0⟩ and |1⟩
print("Statevector:", state)

# Get probabilities of measuring |0⟩ and |1⟩
probs = np.abs(state.data)**2
print("Probabilities:", probs)

# Simulate a measurement by randomly choosing |0⟩ or |1⟩ based on probabilities
measurement = np.random.choice([0, 1], p=probs)
print("Measured state:", measurement)
