from load_data import load_sensor_data


data = []
print("Sensor Data App")

data = load_sensor_data()
print("Loaded records: {}".format(len(data)))
