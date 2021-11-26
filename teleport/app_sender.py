import math

from netqasm.sdk import EPRSocket, Qubit
from netqasm.sdk.classical_communication.message import StructuredMessage
from netqasm.sdk.external import NetQASMConnection, Socket


def main(app_config=None, phi=0.0, theta=0.0):
    # Inputs are coefficients of pi, e.g. phi=0.5 -> angle 0.5*pi
    phi *= math.pi
    theta *= math.pi

    # Create a socket to send classical information
    socket = Socket("sender", "receiver", log_config=app_config.log_config)
    # Create a EPR socket for entanglement generation
    epr_socket = EPRSocket("receiver")

    # Initialize the connection to the backend
    sender = NetQASMConnection(
        app_name=app_config.app_name,
        log_config=app_config.log_config,
        epr_sockets=[epr_socket],
    )
    with sender:
        # Put Sender's code here
        return {}
