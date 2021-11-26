from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket, get_qubit_state


def main(app_config=None):
    # Create a socket to recv classical information
    socket = Socket("receiver", "sender", log_config=app_config.log_config)
    # Create a EPR socket for entanglement generation
    epr_socket = EPRSocket("sender")

    # Initialize the connection
    receiver = NetQASMConnection(
        app_name=app_config.app_name,
        log_config=app_config.log_config,
        epr_sockets=[epr_socket],
    )
    with receiver:
        # Put Receiver's code here
        pass

        # To produce a densitiy matrix of the final qubit in the results:
        # dm = get_qubit_state(<Receiver's qubit>)
        # return {"final_state": dm.tolist()}
