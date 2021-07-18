!pip install pennylane #first time only
#importing pennylane stuff
import pennylane as qml
from pennylane import numpy as np
from pennylane.optimize import * #do we need this?
!pip install pennylane-qiskit #first time only


#import qiskit stuff
from qiskit import *
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit.providers.aer import *

# Loading your IBM Quantum account(s)
provider = IBMQ.load_account()

num_qubits = 4 #4 qubits
# device
#dev = qml.device('qiskit.ibmq', wires=num_qubits, backend='ibmq_qasm_simulator', provider=provider)
dev = qml.device("default.qubit", wires=4, shots=1024)
default_params = [np.pi/2, np.pi/2, np.pi/2]

#user input for rotation gate angles
"""
params_1 = list(map(float, input().strip().split(' ')))
params_2 = list(map(float, input().strip().split(' ')))
params_3 = list(map(float, input().strip().split(' ')))
params_4 = list(map(float, input().strip().split(' ')))
params_5 = list(map(float, input().strip().split(' ')))
params_6 = list(map(float, input().strip().split(' ')))
params_list = list(map(float, input().strip().split(' ')))
"""

params_1 = default_params #[phi, theta, omega]
params_2 = default_params #[phi, theta, omega]
params_3 = default_params #[phi, theta, omega]
params_4 = default_params #[phi, theta, omega]
params_5 = default_params #[phi, theta, omega]
params_6 = default_params #[phi, theta, omega]
params_list = default_params #[phi, theta, omega]

@qml.qnode(dev)
def vqc(params_1, params_2, params_3, params_4, params_5, params_6, params_list):
    #Cluster State
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    qml.Hadamard(wires=3)
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[1,2])
    qml.CNOT(wires=[2,3])
    qml.RY(np.pi, wires=0)
    qml.RY(np.pi, wires=1)
    qml.RY(np.pi, wires=2)
    qml.RY(np.pi, wires=3)
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[1,2])
    qml.CNOT(wires=[2,3])
    #QConvLayer1
    qml.U3(params_1[0], params_1[1], params_1[2], wires=0)
    qml.U3(params_2[0], params_2[1], params_2[2], wires=1)
    qml.U3(params_3[0], params_3[1], params_3[2], wires=2)
    qml.U3(params_4[0], params_4[1], params_4[2], wires=3)
    qml.CRot(params_5[0], params_5[1], params_5[2], wires=[0,1])
    qml.CRot(params_6[0], params_6[1], params_6[2], wires=[2,3])
    #QConvLayer2
    qml.CRot(params_list[0], params_list[1], params_list[2], wires=[0,2])
    #QPool1
    out1 = qml.expval(qml.PauliZ(1))
    out2 = qml.expval(qml.PauliZ(3))
    #QPool2
    out3 = qml.expval(qml.PauliZ(2))
    return out1, out2, out3

vqc(params_1, params_2, params_3, params_4, params_5, params_6, params_list)

"""Uncomment this part for the
other method of making a qubit"""

#circuit = qml.QNode(vqc, dev)
#outputs = [None, None, None]
#outputs[0], outputs[1], outputs[2] = vqc(params_1, params_2, params_3, params_4, params_5, params_6, params_list)
#print("Outputs are:", outputs)
