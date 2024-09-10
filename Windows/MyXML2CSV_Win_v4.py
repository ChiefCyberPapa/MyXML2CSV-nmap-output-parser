import os
import xml.etree.ElementTree as ET
import csv
import sys
from collections import defaultdict
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def parse_nmap_xml(xml_file, ports, port_states):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        data_dict = defaultdict(list)
        headers = ['IP Address', 'Hostname']

        for host in root.findall('host'):
            ip_address_elem = host.find('address[@addrtype="ipv4"]')
            hostname_elem = host.find('hostnames/hostname')
            ip_address = ip_address_elem.get('addr') if ip_address_elem is not None else "Unknown"
            hostname = hostname_elem.get('name') if hostname_elem is not None else "Unknown"

            for port in host.findall('ports/port'):
                portid = port.get('portid')
                protocol = port.get('protocol')
                state = port.find('state').get('state')
                service_elem = port.find('service')
                service_name = service_elem.get('name') if service_elem is not None else "Unknown"

                if any((int(portid) >= start and int(portid) <= end) for start, end in ports) and (state in port_states or 'all' in port_states):
                    port_info = {
                        'Port': portid,
                        'Protocol': protocol,
                        'State': state,
                        'Service': service_name
                    }

                    # Add any new headers dynamically
                    for key in port_info.keys():
                        if key not in headers:
                            headers.append(key)

                    data_dict[(ip_address, hostname)].append(port_info)

        return data_dict, headers
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

def export_to_csv(data_dict, csv_file, headers):
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            
            for (ip_address, hostname), ports in data_dict.items():
                base_info = [ip_address, hostname]
                for port in ports:
                    row = base_info + [port.get(header, '') for header in headers[2:]]
                    writer.writerow(row)
                    base_info = ['', '']
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
    print(f"{Fore.YELLOW}Please input the source XML file. The directory format should be C:\\Users\\...\\Documents\\nmap outputs\\scan1.xml. Example: C:\\Users\\User\\Documents\\nmap outputs\\scan1.xml:{Style.RESET_ALL}")
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
