import airsim
import time
import argparse


def control_car(state, client):
    if state == "focused":
        handle_focused_state(client)
    elif state == "unfocused":
        handle_unfocused_state(client)
    elif state == "drowsy":
        handle_drowsy_state(client)


def reset_control(client):
    # Signal car control to other states then give full control to the
    # user.
    client.enableApiControl(True)
    time.sleep(0.05)
    client.enableApiControl(False)


def handle_focused_state(client):
    client.simPrintLogMessage("Driving State: ",
                              "Focused - Stay Safe!", 0)
    reset_control(client)


def handle_unfocused_state(client):
    client.simPrintLogMessage("Driving State: ",
                              "Unfocused", 1)
    reset_control(client)

    car_controls = airsim.CarControls()
    car_controls.brake = 1

    while True:
        if client.getCarState().speed > 10:
            client.simPrintLogMessage("Driving State: ",
                                      "Unfocused - Exceeded Speed Limit!", 1)
            client.enableApiControl(True)
            client.setCarControls(car_controls)
            time.sleep(0.5)
            client.enableApiControl(False)
            client.simPrintLogMessage("Driving State: ",
                                      "Unfocused", 1)
        if client.isApiControlEnabled():
            break


def handle_drowsy_state(client):
    client.simPrintLogMessage(
        "Driving State: ",
        "Drowsy - Auto Parking", 2)
    reset_control(client)

    client.enableApiControl(True)

    car_controls = airsim.CarControls()
    car_controls.throttle = 0.5
    car_controls.steering = 0.05
    client.setCarControls(car_controls)

    while True:
        collision_info = client.simGetCollisionInfo()
        # If a collision has occurred in the last second
        if collision_info.has_collided and \
                (time.time() - collision_info.time_stamp*1e-9) < 1:
            break
        # If car control is taken by another state, break
        if not client.isApiControlEnabled():
            return

    car_controls.throttle = 0
    car_controls.steering = 0
    car_controls.handbrake = True
    client.setCarControls(car_controls)

    for s in range(60, 0, -1):
        client.simPrintLogMessage(
            "Driving State: ",
            "Drowsy - Waiting for {} seconds".format(s), 2)
        time.sleep(1)
        # If car control is taken by another state, break
        if not client.isApiControlEnabled():
            return

    client.simPrintLogMessage("Driving State: ")
    client.enableApiControl(False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--state",
                        choices=["focused", "unfocused", "drowsy"],
                        required=True)

    state = parser.parse_args().state
    client = airsim.CarClient()
    client.confirmConnection()
    control_car(state, client)


if __name__ == "__main__":
    main()
