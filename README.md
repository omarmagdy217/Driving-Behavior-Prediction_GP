# Driving-Behavior-Prediction_GP

**Graduation Project**

Driving Behavior Prediction based on Brain Activity

- Supervised By: Dr. Seif Eldawlatly

According to the World Health Organization (WHO), 1.25 million deaths result from road
accidents every year. Consequently, lots of technologies have been developed in order to reduce
the accidents to save people’s lives. This project aims at developing a Brain-Computer Interface
(BCI) that enables the prediction of the driver’s behavior based on Electroencephalography (EEG)
brain activity of car drivers. The project capitalizes on the extensive research that has been carried
out on using spectral analysis of electroencephalogram (EEG) activity to estimate different
physiological and psychological states. The developed system will relate the brain activity of the
driver before starting to drive the car with the driving pattern. Spectral signatures that correspond
to different mental states will be extracted from the recorded EEG. Such signatures will be used to
train different machine learning algorithms that will be subsequently used to decode the driver’s
EEG activity to infer his/her driving behavior. Implemented algorithms will be first examined on
benchmark data of mental states available online. The algorithms will be then examined on data
that will be recorded during the project. These algorithms will be then tailored to operate within
the AUTOSAR framework. Based on the detected mental state, recommendations to the driver
will be given. In addition, signals will be sent to different car components to limit the driver’s
capabilities in case of predicting a risky driving behavior.

**Project Modules:**
1. Driving Simulator: An open-source simulator will be used in the project to simulate driving
environment and conditions. The simulator will be programmed to respond to inputs coming
from a PlayStation braking pedal that corresponds to actual physical braking.
2. Signal Pre-processing: Recorded EEG signals will be filtered to eliminate possible noise.
Frequency-domain representation of the filtered signals will then be obtained.
3. Machine Learning Algorithms: These algorithms will decode the recorded brain EEG signals
in order to identify the underlying emotion.
4. AUTOSAR Implementation: USB to Control Area Network (CAN) driver module will
interface between brain signal acquisition kit and automotive evaluation board in order to take
actions with different Electronic Control Units (ECUs). A partial CAN stack will be
implemented to interface between Software components and CAN bus.

## Demo
Link on youtube: [Driving Behavior and Performance Prediction Based on EEG Brain Activity - Final Project Mini Demo](https://www.youtube.com/watch?v=jJmXSDqGJN0&t)
