I created these Python scripts to easily parse out the information I wanted from nmap scans into a CSV format. The original version was strictly command line with no error handling and was clunky, but as my Python skill improved, so did the script. 
Eventually it became more user friendly with user prompts and color coding for the text, and expanded functionality by comma separating for multiple port numbers and statuses. The latest version now dynamically creates column headers based upon what is in the XML source file.
The project initially started in Linux (I mostly run Kali), which is what I use mainly when doing audits and penetration tests.
The Windows version was created later by request and works in the same way. More information can be found in the readme text file included in each OS version folder.

If you have any input to make this tool better, or find any errors, please email me at ChiefCyberPapa@proton.me.

Below you will find the pre-requisites for each OS version.


###Linux Prerequisites###

You will need to install python3 if it isn't already. To install enter "sudo apt install python3 -y". You will also need to install the colorama library if it isn't already. To do so, enter "sudo pip install colorama" from your terminal.

###Windows Prerequisites###

Steps to get it running in a Windows environment:

    Install Python if you haven't already. You can download it from the official Python website.
    Install the colorama package if you haven't already by running "pip install colorama" in your command prompt.
    Copy the provided script into a Python file (e.g., MyXML2CSV_Win_v3.py) using a text editor.
    Open Command Prompt or PowerShell.
    Navigate to the directory where you saved the MyXML2CSV python file.
    Run the script by typing "python pythonfilename" and pressing Enter.
    Follow the prompts to input the XML file path, ports, port states, and output file name.
