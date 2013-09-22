#!/usr/bin/env python
"""Transform a bundled OpenVPN configuration file.

   Based on http://naveensnayak.wordpress.com/2013/03/04/ubuntu-openvpn-with-ovpn-file/
"""
import sys

def extract_between_tags(lines, tag):
    """Extract all lines between the provided tag."""
    found_tag = False
    extracted_lines = []
    for line in lines:
        if not found_tag:
            found_tag = (line.strip() == ("<%s>" % tag))
        else:
            if line.strip() == "</%s>" % tag:
                break
            else:
                extracted_lines.append(line)
    return extracted_lines

def write_lines_to(filename, lines):
    """Write the provided lines into filename, overwriting any existing"""
    with open(filename, 'w+') as output:
        output.write("".join(lines))

def main():
    """Generate all files needed for successful import into the NM."""
    orig_file = sys.argv[1] if len(sys.argv) > 1 else 'client.ovpn'
    with open(orig_file) as opf:
        all_lines = opf.readlines()

    ca_cert = extract_between_tags(all_lines, 'ca')
    write_lines_to('ca.crt', ca_cert)

    client_crt = extract_between_tags(all_lines, 'cert')
    write_lines_to('client.crt', client_crt)

    client_key = extract_between_tags(all_lines, 'key')
    write_lines_to('client.key', client_key)

    ta_key = extract_between_tags(all_lines, 'tls-auth')
    write_lines_to('ta.key', ta_key)

    lines_to_insert = [
            'ca ca.crt\n',
            'cert client.crt\n',
            'key client.key\n',
            'tls-auth ta.key\n',
            ]

    index = all_lines.index('## -----BEGIN RSA SIGNATURE-----\n')
    for line in lines_to_insert:
        all_lines.insert(index, line)

    with open('fixed-client.ovpn', 'w') as opf:
        opf.writelines(all_lines)

if __name__ == '__main__':
    main()
