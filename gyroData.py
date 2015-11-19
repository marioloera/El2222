import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math

SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
	print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
	print("IMU Init Failed");
	sys.exit(1)
else:
	print("IMU Init Succeeded");

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

try:
	while True:
		if imu.IMURead():
			data = imu.getIMUData()
			gyroData = data["gyro"]
			print("x: %f y: %f z: %f" % (gyroData[0], gyroData[1], gyroData[2]))
			time.sleep(poll_interval*1.0/1000.0)
except KeyboardInterrupt:
	pass

