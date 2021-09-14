# This entrypoint file to be used in development. Start by reading README.md
import port_scanner

# Toti diversidade
# Called with URL

# Edit below this line
url = "totidiversidade.com.br"
port_range = [400, 500]
# Edit above this line

hostname = url[:url.find(".")].capitalize()
print(f"Getting ports for {url}")
print(f"Scaning ports from {port_range[0]} to {port_range[-1]}")
ports = port_scanner.get_open_ports(url, port_range)
print("Open ports:", ports)
print(f"{hostname} has been scanned")


# Arasuper
# Called with URL

# Edit below this line
url = "arasuper.com.br"
port_range = [8000, 8100]
# Edit above this line

print(f"Getting ports for {url}")
print(f"Scaning ports from {port_range[0]} to {port_range[-1]}")
ports = port_scanner.get_open_ports(url, port_range)
print("Open ports:", ports)
print("Arasuper has been scanned")


# Called with URL
ports = port_scanner.get_open_ports("www.freecodecamp.org", [75,85])
print("Open ports:", ports)

# Called with ip address
ports = port_scanner.get_open_ports("104.26.10.78", [8079, 8090])
print("Open ports:", ports)

# Verbose called with ip address and no host name returned -- single open port
ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
print(ports + '\n')

# Verbose called with ip address and valid host name returned -- single open port
ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
print(ports + '\n')

# Verbose called with host name -- multiple ports returned
ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
print(ports + '\n')
