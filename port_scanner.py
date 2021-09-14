import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        msg = 'Error: Invalid IP address' if target.count('.') == 3 else 'Error: Invalid hostname'
        return msg
    for p in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        connection = sock.connect_ex((ip, p))
        if not connection:
            open_ports.append(p)
    if not verbose:
        return(open_ports)
    else:
        try:
            host = socket.gethostbyaddr(ip)[0]
            text = 'Open ports for %s (%s)\nPORT     SERVICE' %(host, ip)
        except socket.herror:
            text = 'Open ports for %s\nPORT     SERVICE' %(ip)
        for p in open_ports:
            name = ports_and_services[p]
            text += '\n' + '{:<9}'.format(p) + name
        return text

