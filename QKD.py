# H Gate

# from qiskit.quantum_info import Statevector
# from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# import numpy as np
# q = QuantumRegister(2,'q')
# c = ClassicalRegister(2,'c')
# qc = QuantumCircuit(q,c)

# # Get the statevector of the qubit
# state = Statevector.from_instruction(qc)

# m = qc.measure(q,c) # Qubits states are measured 
# print(m)
# # Get probabilities of measuring |0⟩ and |1⟩
# probs = np.abs(state.data)**2

# measurement = np.random.choice([0, 1], p=probs)
# print("Measured original state:", measurement)

# x = qc.h(q[0]) # H gate applied to quibit 0 
# m = qc.measure(q,c) # Qubits states are measured 
# print("Text:", m)
# print("Test", x)

# # Print the statevector to see the amplitudes of |0⟩ and |1⟩
# print("Statevector:", state)

# print("Probabilities:", probs)
# print("State data", state.data)

# # Simulate a measurement by randomly choosing |0⟩ or |1⟩ based on probabilities
# measurement = np.random.choice([0, 1], p=probs)
# print("Measured H state:", measurement)
# ------------------------------------------------------------------------------
from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
hadamard_gate = HGate()

measurement = np.random.choice([0, 1], p=probs)
print("Measured original state:", measurement)

qc.append(hadamard_gate, [0])

state = Statevector.from_instruction(qc)
probs = np.abs(state.data)**2

measurement = np.random.choice([0, 1], p=probs)
print("H-gate state:", measurement)
qc.draw('mpl')

# X Gate

# from qiskit.quantum_info import Statevector
# from qiskit.circuit import QuantumRegister
# from qiskit import QuantumCircuit
# import numpy as np

# # Select individual quibits
# # q0 = QuantumRegister(1, 'Alice')
# # q1 = QuantumRegister(1, 'Bob')
# # Create a quantum circuit with 2 qubits
# qc = QuantumCircuit(4)

# # Quibit Getter
# # def get_qubit_by_name(qc, name):
# #     for qubit in qc.qubits:
# #         if qubit.register.name == name:
# #             return qubit

# # Apply a CNOT gate to flip the state of the qubit
# # q2 = get_qubit_by_name(q0, 'Alice')
# qc.cx(0, 1)

# # Get the statevector of the qubit
# state = Statevector.from_instruction(qc)

# # Print the statevector to see the amplitudes of |0⟩ and |1⟩
# print("Statevector:", state)

# # Get probabilities of measuring |0⟩ and |1⟩
# probs = np.abs(state.data)**2
# print("Probabilities:", probs)
# print("State data", state.data)

# # Simulate a measurement by randomly choosing |0⟩ or |1⟩ based on probabilities
# measurement = np.random.choice([0, 1], p=probs)
# print("Measured state:", measurement)


# from qiskit.quantum_info import Statevector
# from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# import numpy as np

# circuit = QuantumCircuit(q,c)
# q = QuantumRegister(2,'q')
# c = ClassicalRegister(2,'c')

# m = circuit.measure(q,c) # Qubits states are measured 
# print(m)

# measurement = np.random.choice([0, 1], p=probs)
# print("Measured original state:", measurement)

# circuit.cx(q[0],q[1]) # CNOT applied to both qubits 
# m = circuit.measure(q,c) # Qubits states are measured 
# print("Text:", m)


# # Get the statevector of the qubit
# state = Statevector.from_instruction(qc)

# # Print the statevector to see the amplitudes of |0⟩ and |1⟩
# print("Statevector:", state)

# # Get probabilities of measuring |0⟩ and |1⟩
# probs = np.abs(state.data)**2
# print("Probabilities:", probs)
# print("State data", state.data)

# # Simulate a measurement by randomly choosing |0⟩ or |1⟩ based on probabilities
# measurement = np.random.choice([0, 1], p=probs)
# print("Measured CNOT state:", measurement)


# Import necessary libraries from Qiskit and NumPy
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

# Draw and visualize the quantum circuit
qc.draw('mpl')
