### Multithreading Execution Model 

![Multithreading Model Diagram]()

#### Thread 1 (EEG Recording):

*To-do*

#### Thread 2 (Driving Simulator):

1. Download the latest compiled binaries of you preferred simulation environment from the [AirSim releases page]( https://github.com/Microsoft/AirSim/releases). The `main.py` file uses the [**Blocks**](https://github.com/microsoft/AirSim/releases/download/v.1.2.2/Blocks.zip) environment.
2. Unzip the downloaded archive into the root of this directory.

#### Execution

1. Run the `main.py` python script which launces both the EEG data recorder and the simulator each on a separate thread.
2. Click the record button in the simulator window to start recording driving behavior data.

