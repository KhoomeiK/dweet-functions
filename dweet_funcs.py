#!/Users/rohan/anaconda3/bin/python

import json, argparse
from urllib.request import urlopen

# processes comand line arguments
def args():
	parser = argparse.ArgumentParser()
	parser.add_argument("func", type=str)
	parser.add_argument("thing", type=str)
	parser.add_argument("bOrContent", type=str)
	argm = parser.parse_args()

	if argm.func == "get":
		if argm.bOrContent == "True":
			bl = True
			get(argm.thing, bl)
		elif argm.bOrContent == "False":
			bl = False
			return(get(argm.thing, bl))
		else:
			print("bOrContent must be a bool")

	elif argm.func == "post":
		return(post(argm.thing, argm.bOrContent))
	else:
		print("Required Arguments: \n func = the dweet function to execute (get or post) \n thing = the dweet 'thing' to interact with \n bOrContent = bool for get or content for post")

# gets latest dweet for a thing
def get(thing, b):
	if b: # prints dweet info to console
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

	elif b == False: # returns data in list with format: [name of thing, latest dweet, time of dweet]
		l = [thing, None, None]

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
		print("b must be a bool; True prints basic data, False returns data in a list")

# posts dweet to thing with content
def post(thing, content):
	if " " in content:
		return "content may not have any spaces"

	url = "https://dweet.io/dweet/for/" + thing + "?" + content

	uClient = urlopen(url)
	data = uClient.read()
	uClient.close()
	data = json.loads(data)

	l = [None, None, None, None]

	if "because" in data: # if unable to post dweet, all elements in list will be None type
		return l

	else: # returns list with format: [name of thing, content dweeted, time of dweet, dweet transaction code]
		l = [thing, content, data["with"]["created"], data["with"]["transaction"]]
		return l

args() # remove this line if you don't want to use on command line 
