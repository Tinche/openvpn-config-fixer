openvpn-config-fixer
====================

Parses and converts your bundled OpenVPN config file to make it suitable for import by Network Manager.

Suppose your company has provided you with an OpenVPN config file which has
all the certificates bundled inside; the GNOME Network Manager, as of Ubuntu
13.04 cannot parse and import these properly.

Take your config file and feed it to the decouple-openvpn.py script, which
will slurp all necessary data into separate files into the current working
directory and generate a 'fixed-client.ovpn' for you to import.

Thanks to http://naveensnayak.wordpress.com/2013/03/04/ubuntu-openvpn-with-ovpn-file/.

If the VPN connection still doesn't work, check the original file for the
key-direction parameter and set it manually under VPN -> Advanced -> TLS
Authentication.
