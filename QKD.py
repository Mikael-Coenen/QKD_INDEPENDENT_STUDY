# Hadamard Gate

from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate
from qiskit.quantum_info import Statevector
import numpy as np

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Create a Hadamard gate
hadamard_gate = HGate()

# Update the state after initialization by creating a Statevector from the current circuit
state = Statevector.from_instruction(qc)

# Calculate the probabilities of measuring |0⟩ or |1⟩ based on the current state
probs = np.abs(state.data)**2
print("Probabilities:", probs)

# Measure the initial state based on the calculated probabilities
measurement = np.random.choice([0, 1], p=probs)
print("Measured original state:", measurement)

# Add the hadamard gate to the quibit
# If commented probs will be [0, 1] or [1, 0]
# If uncommented probs will be [0.5, 0.5] which simulates superposition since it transforms 
# the qubit’s state into an equal probability of being measured as |0⟩ or |1⟩.
qc.append(hadamard_gate, [0])

# Measure the initial state based on the calculated probabilities
measurement = np.random.choice([0, 1], p=probs)
print("H-gate state:", measurement)

# Draw and visualize the quantum circuit
qc.draw('mpl')



# Pauli-X Gate

from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate
from qiskit.quantum_info import Statevector
import numpy as np

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Randomly initialize the state to |0⟩ or |1⟩
initial_state = np.random.choice([0, 1])

# If the randomly chosen initial state is |1⟩, apply the X-gate to set the initial state to |1⟩
if initial_state == 1:
    qc.x(0)  # Apply X-gate to the qubit at index 0

# Update the state after initialization by creating a Statevector from the current circuit
state = Statevector.from_instruction(qc)

# Calculate the probabilities of measuring |0⟩ or |1⟩ based on the current state
probs = np.abs(state.data)**2

# Probabilites
print("Probabilities:", probs)

# Measure the initial state based on the calculated probabilities
measurement = np.random.choice([0, 1], p=probs)

# Output the result of the initial measurement
print("Measured initial state:", measurement)

# Apply the X-gate to flip the state of the qubit
qc.append(XGate(), [0])

# Update the state after applying the X-gate by creating a new Statevector
final_state = Statevector.from_instruction(qc)

# Calculate the new probabilities of measuring |0⟩ or |1⟩ after the X-gate is applied
final_probs = np.abs(final_state.data)**2

# Measure the new state after the X-gate using the updated probabilities
final_measurement = np.random.choice([0, 1], p=final_probs)

# Output the result of the final measurement after applying the X-gate
print("X-gate state:", final_measurement)

# Probabilites
print("Probabilities:", final_probs)

# Draw and visualize the quantum circuit
qc.draw('mpl')


# Controlled NOT Gate

from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate
from qiskit.quantum_info import Statevector
import numpy as np

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Update the state after initialization by creating a Statevector from the current circuit
state = Statevector.from_instruction(qc)

# Calculate the probabilities of measuring |0⟩ or |1⟩ based on the current state
probs = np.abs(state.data)**2
print("Probabilities:", probs)

# Measure the initial state based on the calculated probabilities
measurement = np.random.choice([0, 1], p=probs)
print("Measured original state:", measurement)

# Applying cx to control qubit 0 to target qubit 1
qc.cx(0, 1)

# Measure the initial state based on the calculated probabilities
measurement = np.random.choice([0, 1], p=probs)
print("CNOT-gate state:", measurement)

# Draw and visualize the quantum circuit
qc.draw('mpl')