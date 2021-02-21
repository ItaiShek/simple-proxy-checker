# ProxyChecker: Check if proxy servers are up
# (c) 2021 Itai Shek

import socket
from os.path import exists
from time import time


# return True if the host responds to ping, and False if not.
def checkProxy(ip, port, wait):
    # create stream socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(wait)    # maximum time to connect - default time is 5 seconds
    connect = sock.connect_ex((ip, port))

    # close socket
    sock.close()

    # The host is up
    if connect == 0:
        return True
    # The host is down, or passed the time limit
    return False


# check all the proxies
def checkProxyList(proxyList, output, wait):
    output_mark = False
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
        output_mark = True

    start = time()

    # go through the proxy list and check each element
    for proxy in proxyList:
        print(f'Checking: {proxy}')
        if not validateProxy(proxy):
            print(f'"{proxy}" is not a valid proxy')
            continue

        ip, port = proxy.split(':')
        if checkProxy(ip, int(port), wait):
            print('host is up')
            if output_mark:     # write to output file
                output_file.write(proxy + '\n')
                output_file.flush()
        else:
            print('host is down')
        print()

    # close output file
    if output_mark:
        output_file.close()
    end = time()

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
