Autoremote.py 

Simple Python tool to use autoremote to send data to a phone running tasker.


Install:

```sudo pip -install git+https://github.com/sriramsv/autoremote.git```

General API usage:
```
ar=autoremote("your autoremote url")   	# Connect to autoremote server
ar.register("your device name")   		# Register device
ar.send("message to send")			  	# Send Message
```
Command line usage:
```	
usage: autoremote.py [-h] [-n NAME] [-u URL] [-m MSG]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Autoremote name
  -u URL, --url URL     Autoremote url
  -m MSG, --msg MSG     Autoremote message
```
