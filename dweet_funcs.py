import json
from urllib.request import urlopen

# gets latest dweet for a thing
def get(thing, b):
	if b==True: # prints dweet info to console
		print("Fetching latest dweet for '" + thing + "' ...")
		url = "https://dweet.io/get/latest/dweet/for/" + thing

		uClient = urlopen(url)
		data = uClient.read()
		uClient.close()
		data = json.loads(data)

		if "because" in data:
			print(thing + " could not be found")

		else:
			content = data["with"][0]["content"]

			if not bool(content):
				print("No content was passed")

			else: 
				for key in content:
				   print("content = " + key)

			print("time = " + data["with"][0]["created"])
			

	elif b==False: # returns data in list with format: [name of thing, latest dweet, time of dweet]
		l = [thing, False, False]

		url = "https://dweet.io/get/latest/dweet/for/" + thing

		uClient = urlopen(url)
		data = uClient.read()
		uClient.close()
		data = json.loads(data)

		if "because" in data: # if unable to fetch latest dweet, second 2 elements in list will be False
			return l

		else:
			content = data["with"][0]["content"]

			for key in content:
			   l[1] = key

			l[2] = data["with"][0]["created"]

			return l

	else: # b was not a bool
		print("b must be a bool; True prints data to console, False returns data in a list")

# sends dweet for thing with content
def send(thing, content):
	url = "https://dweet.io/dweet/for/" + thing + "?" + content

	uClient = urlopen(url)
	data = uClient.read()
	uClient.close()
	data = json.loads(data)

	l = [False, False, False, False]

	if "because" in data: # if unable to send dweet, all elements in list will be False
		return l

	else: # returns list with format: [name of thing, content dweeted, time of dweet, dweet transaction code
		l = [thing, content, data["with"]["created"], data["with"]["transaction"]]
		return l
