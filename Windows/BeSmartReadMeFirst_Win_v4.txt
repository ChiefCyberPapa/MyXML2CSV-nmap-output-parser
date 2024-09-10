###Prerequisites###

Steps to get it running in a Windows environment:

    Install Python if you haven't already. You can download it from the official Python website.
    Install the colorama package if you haven't already by running "pip install colorama" in your command prompt.
    Copy the provided script into a Python file (e.g., MyXML2CSV_Win_v3.py) using a text editor.
    Open Command Prompt or PowerShell.
    Navigate to the directory where you saved the MyXML2CSV python file.
    Run the script by typing "python pythonfilename" and pressing Enter.
    Follow the prompts to input the XML file path, ports, port states, and output file name.

The information that follows is broken down into each version. Scroll to the version you are currently using for specific version info, or read through it all to see the history of this project.



###Version 3.0 for Windows (booooo...you should be using Linux)###

Thank you for using ChiefCyberPapa's MyXML2CSV script, used for converting XML output from nmap to a useable CSV file. The output will provide the IP addresses, the hostname if it was resolved, the port(s) and the status of the port(s), along with services in an easy to use CSV format.
    
Error handling is added to catch any exceptions during file processing and exit gracefully.

That is it! Now you can open it in Excel, LibreOffice, or whatever you are comfortable with, and make some fancy pivot tables to look like a boss when briefing the organization you just pwned. If you have any suggestions for improvement, please send them to ChiefCyberPapa@proton.me.



###Version 4.0 for Windows (booooo...you should be using Linux)###

The script will now dynamically create column headers based upon what is in the xml source file, when previous versions statically only created the IP Address, Hostname, port, port status and port service. This means that if you have a scan source file that includes other content like MAC Address, OS fingerprinting, and service versioning, the script will create those columns for you in the csv file so that no information is lost.
