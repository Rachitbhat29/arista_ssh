"""Read host details from file 'hostnames.txt' and connect using SSH to get CPU cores"""
from multiprocessing import Process
import utils


def cpuinfo_process(hostinfo):
    """ Function to parse host details and get CPU cores"""
    status, client = utils.connect_ssh(hostinfo)
    result = None
    if status:
        result = utils.get_cpucores(client)
        utils.close_ssh(client)
    else:
        result = client
    try:
        result = int(result)
        result = 'No. of cores:'+str(result)
    except TypeError:
        pass

    print(hostinfo, result)

PROCS = []

if __name__ == '__main__':
    with open('hostnames.txt', 'r') as f:
        for i in f.readlines():
            host = i.strip('\n')
            proc = Process(target=cpuinfo_process, args=(host,)) # Process creation
            PROCS.append(proc)
            proc.start()

    for proc in PROCS:
        proc.join() #Process joining
