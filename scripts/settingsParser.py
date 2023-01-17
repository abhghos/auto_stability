from configparser import ConfigParser

config = ConfigParser()
config.read("settings.ini")

#print(config.sections())
#print(config['SETTINGS'])
#print(list(config['SETTINGS']))

def get_adb_id():
	return (config['SETTINGS']['adb_id'])

def get_device_name():
	return (config['SETTINGS']['device_name'])

def get_meta_type():
	return (config['SETTINGS']['meta'])

def get_edl_port():
	return (config['SETTINGS']['edl_com_port'])


print(get_adb_id())
print(get_device_name())
print(get_meta_type())
print(get_edl_port())