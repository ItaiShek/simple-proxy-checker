#!/usr/bin/env python3

# ProxyChecker: Check if proxy servers are up
# (c) 2021 Itai Shek
# Version 1.1.0

import sys
import getopt
from functions import *


def main():
    filename = ''
    output = ''
    proxyList = []
    wait = 5    # The default is 5 seconds

    # check if there are less than two arguments
    if len(sys.argv) < 2:
        usage()
        sys.exit()

    # get arguments from the command line
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   shortopts="hf:o:t:",
                                   longopts=["help=", "file=", "output=", "time="]
                                   )
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)
        usage()
        sys.exit(1)

    # set the variables with the corresponding arguments
    for opt, arg in opts:
        if opt in ('-h', '--help'):      # help screen
            usage()
            sys.exit()
        elif opt in ('-f', '--file'):    # proxy list file
            filename = arg
        elif opt in ('-o', '--output'):  # output file of good proxies
            output = arg
        elif opt in ('-t', '--time'):    # set waiting time
            wait = arg
            if wait.isdigit():
                wait = int(wait)
            else:
                print('Invalid time')
                sys.exit(1)
        else:
            assert False, "unhandled option"

    # check if the proxy input is valid
    if args is None and filename == '':
        print('No proxy was entered')
        sys.exit(1)

    # get proxies from file
    try:
        if filename != '':  # check if filename is blank
            with open(filename, "r") as f:
                for line in f:
                    proxyList.append(line.strip())
            f.close()
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)

    # get proxy from terminal
    if args is not None:
        for proxy in args:
            proxyList.append(proxy)

    # check the proxy list
    counter = checkProxyList(proxyList=proxyList, output=output, wait=wait)

    print(f'Finished in {counter} seconds')
    sys.exit(0)


def usage():
    # print usage message
    print("Usage: ProxyChecker [OPTIONS] IP:PORT [IP:PORT IP:PORT...]")
    print("Options:")
    print('         -h, --help:         This screen')
    print('         -f, --file:         Get proxies from file                               (e.g. -f proxy_list.txt)')
    print('         -o, --output:       Output file for all the working proxies             (e.g. -o output.txt)')
    print('         -t, --time:         Maximum waiting time for a connection to the proxy  (e.g. -t 10)')


if __name__ == "__main__":
    main()
