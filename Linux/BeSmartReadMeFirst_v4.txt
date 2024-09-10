###Prerequisites###

You will need to install python3 if it isn't already. To install enter "sudo apt install python3 -y". You will also need to install the colorama library if it isn't already. To do so, enter "sudo pip install colorama" from your terminal.

The information that follows is broken down into each version. Scroll to the version you are currently using for specific version info, or read through it all to see the history of this project.



###Version 1.0###

Thank you for using ChifCyberPapa's XML2CSV script, used for converting XML output from nmap to a useable CSV file. The output will provide the IP addresses sorted from smallest to largest, the hostname if it was resolved, the port(s) and the status of the port(s), in an easy to use CSV format.

This script is using command-line arguments (sys.argv) to pass the XML file path, port number, and output CSV file path. So when you run this script from the terminal in Linux, you'll provide these arguments directly.
    
Error handling is added to catch any exceptions during file processing and exit gracefully.
The script directly exits if the correct number of command-line arguments is not provided.
Instead of prompting, the script assumes you'll pass the necessary information directly through the command line.

Gee golly, that all sure sounds swell, but how do I actually use this nifty tool?

First, open your terminal and change your directory to where this python script is located.

Next, simply provide the source file, for example, ~/Documents/nmap\ outputs/scan1 (notice the \ to escape the space...very important), port or ports (comma separated if using more than one) and the output file location and name. If you want to export to the location where the script is, just name the export file followed by .csv.

A full example if I had an nmap output XML file located in ~/Documents/nmap outputs named "scan1" and I wanted to export a CSV to the same location as where I am running the script for port 22 would be:

python3 MyXML2CSV.py ~/Documents/nmap\ outputs/scan1 22 scan1.csv

If I wanted to do the same thing but with multiple ports, the example would be:

python3 MyXML2CSV.py ~/Documents/nmap\ outputs/scan1 22,53,443,3389 scan1.csv



###Version 2.0###

The capability has been added to output all ports and statuses rather than comma separating them all out. 

Example: python3 MyXML2CSV.py ~/Documents/nmap\ outputs/scan1 all all scan1.csv

You can still specify ports and statuses, mix and match as needed.

Example: python3 MyXML2CSV.py ~/Documents/nmap\ outputs/scan1 all open scan1.csv

Additionally, the output file is more user friendly by only listing the IP address and hostname once, with ports, statuses and services listed under each host.



###Version 3.0###

Instead of entering all the information such as the source file, ports, port status and export file name in the command line straight away, the script now asks for user input for each and gives examples in formatting. The instructions are in yellow text to make it easier to read and distingquish from the user input. Just enter "Python3 MyXML2CSV_v3.py" from the command line and follow the prompts.

Additionally, you can now enter ranges of ports, not just a single port or comma separated. You can also simply input 'all' to see all ports. You can even do combinations of each such as, 21,22-80,161-443

That is it! Now you can open it in Word, LibreOffice, or whatever you are comfortable with, and make some fancy pivot tables to look like a boss when briefing the organization you just pwned. If you have any suggestions for improvement, please send them to cyberpapa.botanist055@passmail.net.



###Version 4.0###

The script will now dynamically create column headers based upon what is in the xml source file, when previous versions statically only created the IP Address, Hostname, port, port status and port service. This means that if you have a scan source file that includes other content like MAC Address, OS fingerprinting, and service versioning, the script will create those columns for you in the csv file so that no information is lost.
