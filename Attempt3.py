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
#provider = IBMQ.load_account()

num_qubits = 4 #4 qubits

provider = IBMQ.load_account()
dev = qml.device('default.qubit', wires=4, shots=2048)
#dev = qml.device('qiskit.ibmq', wires=4, backend='ibmq_qasm_simulator', provider=provider)

@qml.qnode(dev)
def vqc2(RX_param1, RY_param1, RZ_param1,
         RX_param2, RY_param2, RZ_param2,
         U_params1, U_params2, U_params3,
         U_params4, U_params5, U_params6):
    #Cluster State QC with "better" Entanglement
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    qml.Hadamard(wires=3)
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[0,2])
    qml.CNOT(wires=[0,3])
    qml.CNOT(wires=[1,2])
    qml.CNOT(wires=[1,3])
    qml.CNOT(wires=[2,3])
    qml.RX(RX_param1, wires=0)
    qml.RY(RY_param1, wires=1)
    qml.RZ(RZ_param1, wires=2)
    qml.T(wires=3)
    qml.T(wires=0)
    qml.RX(RX_param2, wires=1)
    qml.RY(RY_param2, wires=2)
    qml.RZ(RZ_param2, wires=3)
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[0,2])
    qml.CNOT(wires=[0,3])
    qml.CNOT(wires=[1,2])
    qml.CNOT(wires=[1,3])
    qml.CNOT(wires=[2,3])
    #QConv1
    qml.Toffoli(wires=[0,1,2])
    qml.U3(U_params1[0],U_params1[1],U_params1[2], wires=0)
    qml.U3(U_params2[0],U_params2[1],U_params2[2], wires=1)
    qml.U3(U_params3[0],U_params3[1],U_params3[2],wires=2)
    qml.U3(U_params4[0],U_params4[1],U_params4[2],wires=3)
    qml.Toffoli(wires=[0,1,3])
    #QConv2
    qml.Toffoli(wires=[0,2,3])
    qml.CRot(U_params5[0],U_params5[1],U_params5[2], wires=[0,1])
    qml.CRot(U_params6[0],U_params6[1],U_params6[2], wires=[2,3])
    qml.Toffoli(wires=[1,2,3])
    #QPool1 and 2
    return qml.expval(qml.PauliZ(1)), qml.expval(qml.PauliZ(2)), qml.expval(qml.PauliZ(3))
  
default = [np.pi/2, np.pi/2, np.pi/2]
RX_param1, RY_param1, RZ_param1 = np.pi, np.pi, np.pi
RX_param2, RY_param2, RZ_param2 = np.pi, np.pi, np.pi
U_params1, U_params2, U_params3 = default, default, default
U_params4, U_params5, U_params6 = default, default, default

def user_input_rot():
    RX_param1 = float(input().strip())
    RY_param1 = float(input().strip())
    RZ_param1 = float(input().strip())
    RX_param2 = float(input().strip())
    RY_param2 = float(input().strip())
    RZ_param2 = float(input().strip())
    U_params1 = list(map(float, input().strip().split(' ')))
    U_params2 = list(map(float, input().strip().split(' ')))
    U_params3 = list(map(float, input().strip().split(' ')))
    U_params4 = list(map(float, input().strip().split(' ')))
    U_params5 = list(map(float, input().strip().split(' ')))
    U_params6 = list(map(float, input().strip().split(' ')))
    
vqc2(RX_param1, RY_param1, RZ_param1,
         RX_param2, RY_param2, RZ_param2,
         U_params1, U_params2, U_params3,
         U_params4, U_params5, U_params6)
