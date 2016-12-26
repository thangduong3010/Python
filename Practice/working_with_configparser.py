import ConfigParser
import os

def createConfig(path):
	"""
	Create a config file
	"""
	config = ConfigParser.ConfigParser()
	config.add_section("Settings")
	config.set("Settings", "font", "Courier")
	config.set("Settings", "font_size", "11")
	config.set("Settings", "font_style", "Normal")
	config.set("Settings", "font_info",
				"You are using %(font)s at %(font_size)s pt")

	# in Python 3, we only have to specify "w" for writing
	with open(path, "wb") as config_file:
		config.write(config_file)

def getConfig(path):
	"""
	Return the config object
	"""
	if not os.path.exists(path):
		createConfig(path)

	config = ConfigParser.ConfigParser()
	config.read(path)
	return config

def getSettings(path, section, setting):
	"""
	Get the current values
	"""
	config = getConfig(path)
	value = config.get(section, setting)
	msg = "{section} {setting} is {value}".format(section=section, setting=setting, value=value)
	print(msg)
	return value

def updateSettings(path, section, setting, value):
	"""
	Update settings
	"""
	config = getConfig(path)
	config.set(section, setting, value)

	with open(path, "wb") as config_file:
		config.write(config_file)

def deleteSettings(path, section, setting):
	"""
	Delete settings
	"""
	config = getConfig(path)
	config.remove_section(section, setting)

	with open(path, "wb") as config_file:
		config.write(config.file)

if __name__ == "__main__":
	path = r"F:\Github\Python\Practice\Files\data\settings.ini"
	font = getSettings(path, "Settings", "font")
	font_size = getSettings(path, "Settings", "font_size")
	font_info = getSettings(path, "Settings", "font_info")