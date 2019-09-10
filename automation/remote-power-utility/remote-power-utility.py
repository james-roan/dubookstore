"""
remote-power-utility.py
James Roan
29 June 2019
"""
import paramiko
import json
import socket  # for socket exceptions
import sys

class Kiosks(object):
	"""docstring for Kiosks"""

	DEFAULT_FILENAME="kiosks.json"

	def __init__(self, filename=DEFAULT_FILENAME):
		self.ssh_client = paramiko.SSHClient()
		"""
		Since the only hosts that we're going to be connecting to are
		computers that we have physically in front of us, it's okay
		to just default to trusting them.
		"""
		self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		self.filename = filename # the name of the file to read/write the JSON doc to

		self.data = {} # blank dict is essentially a json document
		self.data['kiosks'] = []
		self._loadKiosks()

	def _loadKiosks(self):
		with open(self.filename) as json_file:
			self.data = json.load(json_file)
			print("Loaded {} kiosk(s) from file successfully.".format(len(self.data['kiosks'])))

	def _writeKiosks(self):
		with open(self.filename, 'w') as outfile:
			json.dump(self.data, outfile)

	def _addKiosk(self, details):
		"""
		Add a kiosk to the list and save the list to disk.
		TODO: Validate data
		kiosks must have a name, hostname, username, password, and ip
		"""
		self.data['kiosks'].append(details)
		self._writeKiosks()
		pass

	def shutdown(self, kiosk):
		"""
		Shutdown a kiosk via SSH
		"""
		try:
			self.ssh_client.connect(hostname=kiosk['hostname'],
			                        username=kiosk['username'],
			                        password=kiosk['password'],
			                        timeout=5,
			                        auth_timeout=5,
			                        banner_timeout=5)
		except socket.timeout:
			print("\t\tConnection timed out :( Is the computer already off?")
			return

		stdin,stdout,stderr=self.ssh_client.exec_command("echo {} | sudo -S -k shutdown -h now".format(kiosk['password']))

		print("\t\t" + stdout.read())
		#print("\t\t" + stderr.read())
		self.ssh_client.close() # because garbage collection isn't fast enough
		#print("\t\tSuccess.")

	def shutdown_all(self):
		"""
		Shutdown all kiosks in the list
		"""
		print("Shutting down all kiosks...")
		for kiosk in self.data['kiosks']:
			print("\tShutting down kiosk '{}' {}@{} {}".format(kiosk['name'], kiosk['username'], kiosk['hostname'], kiosk['password']))
			self.shutdown(kiosk)


if __name__ == '__main__':
	if (len(sys.argv) == 1):
		print("Remote power utility requires at least one argument.")
		exit()
	elif(sys.argv[1] == "all"):
		k = Kiosks()
		k.shutdown_all()
		
