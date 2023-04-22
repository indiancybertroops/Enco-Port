import socket
import sys
from tabulate import tabulate

# Get website from user input
website = input("Enter website URL: ")

# Create list of commonly used ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 1433, 3306, 3389]

# Initialize list to store results
results = []

# ASCII art banner
print(r"""

██████╗  ██████╗ ██████╗ ████████╗   ███████╗███╗   ██╗ ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝   ██╔════╝████╗  ██║██╔════╝██╔═══██╗
██████╔╝██║   ██║██████╔╝   ██║█████╗█████╗  ██╔██╗ ██║██║     ██║   ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║╚════╝██╔══╝  ██║╚██╗██║██║     ██║   ██║
██║     ╚██████╔╝██║  ██║   ██║      ███████╗██║ ╚████║╚██████╗╚██████╔╝
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ 
                                                                                                
  python Based Port Scanner Without NMAP 
  Lightweight Port Scanner
  Desined By : Indian Cyber Troops With Love                              
""")

# Loop through ports and attempt to connect to each one
for port in ports:
    try:
        # Create socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        # Attempt to connect to port
        result = sock.connect_ex((website, port))

        # Check if port is open
        if result == 0:
            # Add port information to results list
            service = socket.getservbyport(port)
            results.append([port, service, "Open"])
        else:
            # Add port information to results list
            results.append([port, "", "Closed"])

        # Close socket connection
        sock.close()

    except KeyboardInterrupt:
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    except socket.error:
        print("Could not connect to server")
        sys.exit()

# Print results in table format
table_headers = ["Port", "Service", "Status"]
print(tabulate(results, headers=table_headers))

# Add beware message
print("\nBeware: The results may include potentially dangerous information. Use at your own risk.")
