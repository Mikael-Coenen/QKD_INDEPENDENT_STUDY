# H Gate

from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit
import numpy as np

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply a Hadamard gate to put the qubit into superposition
qc.h(0)

# Get the statevector of the qubit
state = Statevector.from_instruction(qc)

# Print the statevector to see the amplitudes of |0⟩ and |1⟩
print("Statevector:", state)

# Get probabilities of measuring |0⟩ and |1⟩
probs = np.abs(state.data)**2
print("Probabilities:", probs)
print("State data", state.data)

# Simulate a measurement by randomly choosing |0⟩ or |1⟩ based on probabilities
measurement = np.random.choice([0, 1], p=probs)
print("Measured state:", measurement)


# CNOT Gate

# CNOT Gate

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



# CNOT Gate

from qiskit.quantum_info import Statevector
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import numpy as np


q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

m = circuit.measure(q,c) # Qubits states are measured 
print(m)

circuit = QuantumCircuit(q,c)
circuit.cx(q[0],q[1]) # CNOT applied to both qubits 
m = circuit.measure(q,c) # Qubits states are measured 
print(m)


# Get the statevector of the qubit
state = Statevector.from_instruction(qc)

# Print the statevector to see the amplitudes of |0⟩ and |1⟩
print("Statevector:", state)

# Get probabilities of measuring |0⟩ and |1⟩
probs = np.abs(state.data)**2
print("Probabilities:", probs)
print("State data", state.data)

# Simulate a measurement by randomly choosing |0⟩ or |1⟩ based on probabilities
measurement = np.random.choice([0, 1], p=probs)
print("Measured state:", measurement)