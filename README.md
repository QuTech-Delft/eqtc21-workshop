## Challenge: implement the QNE applications

On the [QNE website](https://www.quantum-network.com/applications/), there are three pre-built applications that you can run. These applications have been developed
using the [QNE-ADK](https://www.quantum-network.com/adk/).

In this challenge, the goal is to (re-)implement one or more of these applications.

The QNE-ADK uses the [netqasm](https://github.com/QuTech-Delft/netqasm) library
to develop applications. Since we don't intend to use QNE-specific functionality (like uploading application to QNE, or visualizing with animations), in this challenge we wil directly use the `netqasm` library to develop the application.
To run the application, we'll use [squidasm](https://github.com/QuTech-Delft/squidasm) as the simulator. This is in fact also the simulator used by the QNE website.


### Preparation
The required software has only been tested on Linux.
On Windows, WSL can be used.


First make sure you have installed `netqasm` and `squidasm`:

For `netqasm`, simply do
```
pip install netqasm
```

`squidasm` internally uses [NetSquid](https://netsquid.org/), which requires you to create an account on the NetSquid forum (see the NetSquid website for details).
Then, use your account info to install `squidasm`:

```
pip install squidasm --extra-index-url=https://{netsquid-user-name}:{netsquid-password}@pypi.netsquid.org
```

Clone this repository and `cd` into it:

```
git clone https://github.com/QuTech-Delft/eqtc21-workshop
cd eqtc21-workshop
```

Try to run one of the (empty) applications, e.g.
```
netqasm simulate --app-dir teleport --log-level INFO
```
If the command successfully exits, and if you see a `log/LAST/results.yaml` file appearing in the application directory (e.g. `teleport/`), this means that you can successfully run an application!


### Implementing the application
Now you are ready to fill in the source files (e.g. `app_alice.py` and `app_bob.py` for `teleportation`) with the required code. Each application directory has a `README.md` with the pseudocode.

Refer to the [NetQASM documentation](https://netqasm.readthedocs.io/en/latest/) 
or have a look at some of the [example applications](https://github.com/QuTech-Delft/netqasm/tree/develop/netqasm/examples) to get a feel of how to start.

### Running and testing
Run an application by `netqasm simulate --app-dir <directory>`, e.g. `netqasm simulate --app-dir teleport`.

You may want to add an extra `--log-level INFO` or `--log-level DEBUG` flag to this command to see what's going on while simulating the application.

Results are put in `log/LAST/results.yaml`. (There are also other logs in the `log/LAST` directory, like which instructions were executed and when which quantum state existed. These logs are actually used on the QNE website to produce the animations!)

Make sure your application code ends with a `return {}` statement, returing the values you want to see in the `results.yaml` file.