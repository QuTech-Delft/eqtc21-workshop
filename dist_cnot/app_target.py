import math

from netqasm.sdk import EPRSocket, Qubit
from netqasm.sdk.external import NetQASMConnection, Socket


def main(app_config=None, phi=0.0, theta=0.0):
    phi *= math.pi
    theta *= math.pi

    # socket for creating an EPR pair with Controller
    controller_epr = EPRSocket("controller")
    # socket for communicating classical messages with Controller
    class_socket = Socket("target", "controller", log_config=app_config.log_config)

    # connect to the back-end
    target = NetQASMConnection(
        app_name=app_config.app_name,
        log_config=app_config.log_config,
        epr_sockets=[controller_epr],
    )

    with target:
        # Put Target's code here
        pass

        # To produce a densitiy matrix of the final qubit in the results:
        # dm = get_qubit_state(<Target's final qubit>)
        # return {"final_state": dm.tolist()}
