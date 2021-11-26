import math

from netqasm.sdk import EPRSocket, Qubit
from netqasm.sdk.external import NetQASMConnection, Socket


def main(app_config=None, phi=0.0, theta=0.0):
    # Inputs are coefficients of pi, e.g. phi=0.5 -> angle 0.5*pi
    phi *= math.pi
    theta *= math.pi

    # socket for creating an EPR pair with target
    target_epr = EPRSocket("target")
    # socket for communicating classical messages with target
    class_socket = Socket("controller", "target", log_config=app_config.log_config)

    # connect to the back-end
    controller = NetQASMConnection(
        app_name=app_config.app_name,
        log_config=app_config.log_config,
        epr_sockets=[target_epr],
    )

    with controller:
        # Put Controllers's code here
        pass

        # To produce a densitiy matrix of the final qubit in the results:
        # dm = get_qubit_state(<Controller's final qubit>)
        # return {"final_state": dm.tolist()}
