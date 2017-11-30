import json
from urllib.request import urlopen

def get(thing, b):
	if b==True:
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

	elif b==False:
		l = [thing, False, False]

		url = "https://dweet.io/get/latest/dweet/for/" + thing

		uClient = urlopen(url)
		data = uClient.read()
		uClient.close()
		data = json.loads(data)

		if "because" in data:
			return l

		else:
			content = data["with"][0]["content"]

			for key in content:
			   l[1] = key

			l[2] = data["with"][0]["created"]

			return l

	else:
		print("b must be a bool; True prints basic data, False returns data in a list")

def send(thing, content):
	url = "https://dweet.io/dweet/for/" + thing + "?" + content

	uClient = urlopen(url)
	data = uClient.read()
	uClient.close()
	data = json.loads(data)

	l = [False, False, False, False]

	if "because" in data:
		return l

	else:
		l = [thing, content, data["with"]["created"], data["with"]["transaction"]]
		return l