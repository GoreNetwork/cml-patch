import netmiko
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def run_command_on_net_connect(net_connect,command):
	return net_connect.send_command_expect(command)

username = 'dhimes'
password = 'password'

ips = [
    '10.0.0.1',
    '10.0.0.2',
    '10.0.0.3',
    '10.0.0.4',
    '10.0.0.5',
    ]

connections = []


for ip in ips:
    net_connect = netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)
    connections.append(net_connect)
while True:
    for connection in connections:
        command = 'sh run | i hostname'
        print (run_command_on_net_connect(connection,command))
        command = 'ping 8.8.8.8 so lo0'
        print (run_command_on_net_connect(connection,command))
    for ip in ips:
        ping(ip)