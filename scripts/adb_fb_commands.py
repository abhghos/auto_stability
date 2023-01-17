import os
import time
import random

adb_device_id = "f42edf4e"
fastboot_device_id = "f42edf4e"

def adb_reboot(adb_device_id):
	print("ADB REBOOT")
	os.system("adb -s " + str(adb_device_id) + " wait-for-device")
	os.system("adb -s " + str(adb_device_id) + " root")
	os.system("adb -s " + str(adb_device_id) + " reboot")
	time.sleep(10)


def fastboot_continue(adb_device_id):
	print("ADB FASTBOOT CONTINUE")
	os.system("adb -s " + str(adb_device_id) + " wait-for-device")
	os.system("adb -s " + str(adb_device_id) + " root")
	os.system("adb -s " + str(adb_device_id) + " reboot bootloader")
	time.sleep(20)
	os.system("fastboot -s " + str(adb_device_id) + " continue")


def fastboot_reboot(adb_device_id, fastboot_device_id):
	print("ADB FASTBOOT REBOOT")
	os.system("adb -s " + str(adb_device_id) + " wait-for-device")
	os.system("adb -s " + str(adb_device_id) + " root")
	os.system("adb -s " + str(adb_device_id) + " reboot bootloader")
	time.sleep(30)
	os.system("fastboot -s " + str(fastboot_device_id) + " reboot")


def remount():
	print("ADB REMOUNT")
	os.system("adb -s " + str(adb_device_id) + " wait-for-device")
	os.system("adb -s " + str(adb_device_id) + " root")
	os.system("adb -s " + str(adb_device_id) + " remount")

i = 0
while 1:
	print("Iteration " + str(i))
	i=i+1
	reboot_type = 0
	reboot_type = random.randrange(0,5,1)
	os.system("adb wait-for-device")
	
	if(reboot_type == 1):
		adb_reboot()
		
	if(reboot_type == 2):
		fastboot_continue()
		
	if(reboot_type == 3):
		fastboot_reboot()
		
	if (reboot_type == 4):
		remount()
		
	if(reboot_type != 0):
		#trigger_shell_script()
		random_time = random.randint(60,120)
		print("Sleeping for "+ str(random_time))
		time.sleep(random_time)