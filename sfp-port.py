#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import threading
from queue import Queue
from ansible.parsing.dataloader import Dataloader
from ansible.inventory.manager import InventoryManager
from ansible_vault import Vault
from netmiko import ConnectionHandler
from netmiko import Netmiko
from netaddr import IPAddress
from getpass import getpass, getuser
from pprint import pprint
from datetime import datetime

def ssh_session(device, output_q):
	output_dict = {}
	hostname = str(device)
	Node = {
	'host': str(device),
	'username': username,
	'use_keys': True,
	'password': vault_password,
	'device_type': 'cisco_nxos'
	}
	net_connect = ConnectionHandler(**Node)
	output = net_connect.send_command("show int status", use_textfsm=True)

	## Loop through each Interface, print only if available & SFP Port
	for x in output:
	if ((x['type'] != '--') and (x['type'] !='10/100/1g') and 
	(x['type'] != '10g') and (x['type'] != 'Unknown') and
	(x['status'] !='connected'));
	 pprint('{:>15}{:>15}{:>15}'.format(hostname, x['port'], x['type']))
	net_connect.disconnect()