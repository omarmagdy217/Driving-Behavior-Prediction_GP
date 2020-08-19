import airsim

client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(False)
position = client.simGetGroundTruthKinematics().position
print(position.x_val, position.y_val)
