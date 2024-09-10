import os
import xml.etree.ElementTree as ET
import csv
import sys
from colorama import Fore, Style

def parse_nmap_xml(xml_file, ports, port_states):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        data_dict = {}
        headers = ['IP Address', 'Hostname']

        for host in root.findall('host'):
            ip_address_elem = host.find('address[@addrtype="ipv4"]')
            mac_address_elem = host.find('address[@addrtype="mac"]')
            ip_address = ip_address_elem.get('addr') if ip_address_elem is not None else "Unknown"
            hostname_elem = host.find('hostnames/hostname')
            hostname = hostname_elem.get('name') if hostname_elem is not None else "Unknown"
            mac_address = mac_address_elem.get('addr') if mac_address_elem is not None else "Unknown"
            vendor = mac_address_elem.get('vendor') if mac_address_elem is not None and 'vendor' in mac_address_elem.attrib else "Unknown"

            host_info = {
                'IP Address': ip_address,
                'Hostname': hostname,
                'MAC Address': mac_address,
                'Vendor': vendor
            }

            # Add any new headers to the list
            for key in host_info.keys():
                if key not in headers:
                    headers.append(key)

            # Add host information to the data dictionary
            if (ip_address, hostname) not in data_dict:
                data_dict[(ip_address, hostname)] = [host_info]

        return data_dict, headers
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

def export_to_csv(data_dict, csv_file, headers):
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for _, host_info_list in data_dict.items():
                for host_info in host_info_list:
                    writer.writerow(host_info)
        print(f"{Fore.GREEN}CSV file generated successfully.{Style.RESET_ALL}")
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

def parse_ports(ports_input):
    ports = []
    if ports_input.lower() == "all":
        return [(0, 65535)]  # Assuming ports range from 0 to 65535
    for port in ports_input.replace(" ", "").split(','):
        if '-' in port:
            start, end = map(int, port.split('-'))
            ports.append((start, end))
        else:
            ports.append((int(port), int(port)))
    return ports

if __name__ == "__main__":
    # Ask for the source XML file
    print(f"{Fore.YELLOW}Please input the source XML file. The directory format should be /home/user/..., not ~/....  Example: /home/user/Documents/nmap outputs/scan1.xml:{Style.RESET_ALL}")
    xml_file = input()

    xml_file = os.path.expanduser(xml_file)  # Expand ~ to the user's home directory
    xml_file = xml_file.strip('"')  # Strip double quotes if present

    # Ask for the ports
    print(f"{Fore.YELLOW}Please input the port or ports you wish to export. You can list one port, multiples separated by a comma, or port ranges separated by a dash. You can also enter 'all' to see all scanned ports. Example: 21 or 21-80 or 21-80,161-443:{Style.RESET_ALL}")
    ports_input = input()
    ports = parse_ports(ports_input)

    # Ask for the port states
    print(f"{Fore.YELLOW}Please input the port states you wish to export. You can list one state or multiples separated by a comma, or input 'all' to list all. The port states are open, closed, filtered, unfiltered, open|filtered, and closed|filtered. Example: open,filtered,closed or all:{Style.RESET_ALL}")
    port_states_input = input()
    port_states = port_states_input.split(',')

    # Ask for the output file name
    print(f"{Fore.YELLOW}Please input the output file name with the CSV extension. Example: output1.csv:{Style.RESET_ALL}")
    csv_file = input()
    csv_file = csv_file.strip('"')  # Strip double quotes if present

    data_dict, headers = parse_nmap_xml(xml_file, ports, port_states)
    export_to_csv(data_dict, csv_file, headers)

    print(f"{Fore.GREEN}Wow...that was easy! Thank you for using the MyXML2CSV script, used for converting XML output from nmap to a useable CSV file. You can buy me a coffee if you like this or send complaints and improvements to ChiefCyberPapa@proton.me.{Style.RESET_ALL}")
