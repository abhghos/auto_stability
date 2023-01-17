import time
import TACDev

alpacaVersion = TACDev.AlpacaVersion()
print("Alpaca Version: ", alpacaVersion)

tacVersion = TACDev.TACVersion()
print("TAC Version: ", tacVersion)

deviceCount  = TACDev.GetDeviceCount()
print("Number of Device Connected: ", deviceCount)

if (deviceCount > 0):
	tacDevice = TACDev.GetDevice(0)
	if (tacDevice != None):
		if (tacDevice.Open()) :
			print("Serial Number: " + tacDevice.SerialNumber())
			print("UUID" + tacDevice.Get_UUID())
			while(1):
				usb0state = tacDevice.GetUsb0State()
				print("USB State: ", str(usb0state))
				tacDevice.Usb0(not usb0state)
				time.sleep(30)
			tacDevice.Close()
else:
	print("Device Not Found")