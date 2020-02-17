"""Read host details from file 'hostnames.txt' and connect using SSH to get CPU cores"""
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko import AuthenticationException


def parsehost(host):
    """ Function to parse hostname, port, username and password"""
    port = None
    if ':' in host:
        hostname, port = host.split(":")
        if '@' in port:
            port, username = port.split(" ")
            username, password = username.split("@")
        else:
            username = 'bhumikasanghvi'
            password = '242919'
        port = int(port)
    else:
        try:
            hostname, user_pass = host.split(" ")
        except IndexError:
            hostname = host
            user_pass = ''
        port = 22
        if '@' in user_pass:
            username, password = user_pass.split("@")
        else:
            username = 'bhumikasanghvi'
            password = '242919'


    return hostname, port, username, password


def get_cpucores(client):
    """ Function to run command to get the no. of CPU cores"""
    stdout = client.exec_command('getconf _NPROCESSORS_ONLN')[1]
    return stdout.readlines()[0]


def connect_ssh(host):
    """ Function to connect remote machine using SSH"""
    hostname, port, username, password = parsehost(host)
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        client.connect(hostname=hostname, port=port, username=username, password=password)
        return True, client
    except AuthenticationException as e_ex:
        return False, str(e_ex)


def close_ssh(client):
    """ Function to close SSH connection"""
    client.close()
