import re
import os
import requests
import argparse


class autoremote:
    def __init__(self, url=None):
        self.key_url = requests.get(url, allow_redirects=True)
        if self.key_url.status_code == 200:
            url = self.key_url.url
            self.key = re.search(r'key=(.*)', url, re.DOTALL)
            self.key = self.key.group(1)
        else:
            raise Exception("Can not connect to AutoRemote!!!")

        print("Fetching global ip")
        self.public_ip = requests.get("http://ipecho.net/plain")
        if self.public_ip.status_code == 200:
            self.public_ip = self.public_ip.text
            print('Global IP:', self.public_ip)
        print("Fetching local ip")
        self.local_ip = os.popen("ifconfig|grep inet|head -1|sed 's/\:/ /'|awk '{print $3}'").read()
        print('local IP:', self.local_ip)

    def register(self, name=None):
        print ("device name:", name)
        reg_url = 'http://autoremotejoaomgcd.appspot.com/registerpc?key={0}&name={1}&id=3&type=linux&publicip={2}&localip={3}'.format(self.key, name, self.public_ip, self.local_ip)
        reg_req = requests.get(reg_url)
        if reg_req.status_code == 200:
            print("Registered successfully")

    def send(self, msg):
        send_url = "http://autoremotejoaomgcd.appspot.com/sendmessage?key={0}&message={1}".format(self.key, msg)
        send_req = requests.get(send_url)
        if send_req.status_code == 200:
            print("{0} sent successfully".format(msg))
        else:
            raise Exception("AutoRemote failed to send message!!!")
if __name__ == "__main__":

    # Define and parse command line arguments
    # example:  -n "S5"  -u "http://goo.gl/T8nIJr" -m "notify Test=:=This is a Autoremote test!"
    parser = argparse.ArgumentParser(description="Autoremote")
    parser.add_argument("-n", "--name", help="Autoremote name")
    parser.add_argument("-u", "--url", help="Autoremote url")
    parser.add_argument("-m", "--msg", help="Autoremote message")

    # Handle command Line arguments
    args = parser.parse_args()

    print (args)

    if args.name:
        _name = args.name
    else:
        _name = ""

    if args.url:
        _url = args.url
    else:
        _url = "[YOUR AUTOREMOTE URL]"

    if args.msg:
        _msg = args.msg
    else:
        #  _msg= "say 5=:=This is a AutoRemote test!"
        _msg = "notify Test=:=This is a AutoRemote test!"

    # noinspection PyBroadException
    try:
        ar = autoremote(url=_url)   # Connect to AutoRemote server
        if _name:
            # noinspection PyBroadException
            try:
                ar.register(name=_name)   # Register device
            except:
                print ("Unable to register device with AutoRemote!!!")
        if _msg:
            # noinspection PyBroadException
            try:
                ar.send(_msg)			  # Send Message
            except:
                print ("Unable to send message!!!")
    except:
        print ("Unable to connect to AutoRemote!!!")
