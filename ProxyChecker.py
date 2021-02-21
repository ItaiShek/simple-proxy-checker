# ProxyChecker: Check if proxy servers are up
# (c) 2021 Itai Shek

import sys
import getopt
from functions import *


def main():
    proxy = ''
    filename = ''
    output = ''
    proxyList = []
    wait = 5

    # check if there are less than two arguments
    if len(sys.argv) < 2:
        usage()
        sys.exit()

    # get arguments from the command line
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   shortopts="hf:p:o:t:",
                                   longopts=["help=", "file=", "proxy=", "output=", "time="]
                                   )
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)
        usage()
        sys.exit(2)

    # set the variables with the corresponding arguments
    for opt, arg in opts:
        if opt in ('-h', '--help'):     # help screen
            usage()
            sys.exit()
        elif opt in ('-p', '--proxy'):  # proxy server of the form IP:PORT
            proxy = arg
        elif opt in ('-f', '--file'):  # proxy list file
            filename = arg
        elif opt in ('-o', '--output'):  # output file of good proxies
            output = arg
        elif opt in ('-t', '--time'):  # output file of good proxies
            wait = arg
            if wait.isdigit():
                wait = int(wait)
            else:
                print('Invalid time')
                exit(1)
        else:
            assert False, "unhandled option"

    # check if the proxy input is valid
    if proxy == '' and filename == '':
        print('No proxy was entered')
        sys.exit(1)
    elif proxy != '' and filename != '':
        print('Only one option is allowed at a time')

    # get proxies from file
    try:
        if filename != '':  # check if filename is blank
            with open(filename, "r") as f:
                for line in f:
                    proxyList.append(line.strip())
            f.close()
    except FileNotFoundError as err:
        print(err)
        exit(2)

    # get proxy from terminal
    if proxy != '':
        proxyList.append(proxy)

    # check the proxy list
    counter = checkProxyList(proxyList=proxyList, output=output, wait=wait)

    print(f'Finished in {counter} seconds')


def usage():
    # print usage message
    print("Usage: ProxyChecker [-p IP:HOST] [-f proxy-list] [-o output-list] [-t connection's-max-time]")
    print("Options:")
    print('         -h, --help:         This screen')
    print('         -p, --proxy:        proxy server and port to check, of the form IP:PORT')
    print('         -f, --file:         Proxy file list to check, which is of the form IP:PORT for all proxy in the list')
    print('         -o, --output:       Output file for all the working proxies')
    print('         -t, --time:         Maximum time to wait for connection to the proxy')


if __name__ == "__main__":
    main()
