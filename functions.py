# ProxyChecker: Check if proxy servers are up
# (c) 2021 Itai Shek

import socket
from os.path import exists
from time import time
from threading import Thread, Lock

print_lock = Lock()
counter = 1

# return True if the host responds to ping, and False if not.
def checkProxy(ip, port, wait, outfile):
    # create stream socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(wait)    # maximum time to connect - default time is 5 seconds
    connect = sock.connect_ex((ip, port))

    # close socket
    sock.close()

    global counter
    print_lock.acquire()
    counter += 1
    print(f'Checking {ip}:{str(port)}')

    # The host is up
    if connect == 0:
        print('host is up')
        print_lock.release()

        if outfile: # write to file
            outfile.write(ip + ':' + str(port) + '\n')
            outfile.flush()

        return True

    # The host is down, or passed the time limit
    print('host is down')
    print_lock.release()

    return False


# check all the proxies
def checkProxyList(proxyList, output, wait):
    output_file = ''

    # check if the output file already exists
    if output != '':
        if exists(output):
            while True:
                print(f'The file "{output}" already exists, would you like to append to it? [y/n]')
                choice = input().lower()
                if choice in ['y', 'yes']:
                    break
                elif choice in ['n', 'no']:
                    exit()
                else:
                    print('Not a valid choice, please try again\n')

        output_file = open(output, 'a')

    start = time()

    # validate all proxies
    for proxy in proxyList:
        if not validateProxy(proxy):
            print(f'"{proxy}" is not a valid proxy')
            proxyList.remove(proxy)
            continue

    threads = []

    # create thread list
    for proxy in proxyList:
        ip, port = proxy.split(':')
        t = Thread(target=checkProxy, args=(ip, int(port), wait, output_file))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # close output file
    if output_file:
        output_file.close()
    end = time()

    print(f'\nChecked {str(counter)} proxies')
    return str(end-start)


# return True if the IP and the port are valid, and False if not
def validateProxy(proxy):
    if proxy.count(':') != 1:
        return False
    ip, port = proxy.split(':')

    # check port
    if not port.isdigit():
        return False
    port = int(port)
    if port < 1 or port > 65535:
        return False

    # check ip
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
