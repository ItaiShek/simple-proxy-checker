## General info
A program that checks if one or more proxy servers are up.

## How to use
```
Usage: ProxyChecker [-p IP:HOST] [-f proxy-list] [-o output-list] [-t connection's-max-time]
Options:
         -h, --help:         This screen
         -p, --proxy:        proxy server and port to check, of the form IP:PORT
         -f, --file:         Proxy file list to check, which is of the form IP:PORT for all proxy in the list
         -o, --output:       Output file for all the working proxies
         -t, --time:         Maximum time to wait for connection to the proxy (the default is 5 seconds)
```
```
Example:
python ProxyChecker.py -f proxies.txt -o working_proxies.txt
```

## Notes
* All proxies must be of the form IP:PORT, if it's not then the program skips to the next proxy on the list
* It is not recommended to set the waiting time below 5 seconds
* The option '-p' will accept only ONE proxy
* The option '-f' will accept only ONE file
* You can choose either one proxy from the command line, or one file with proxies, but not both at the same time
* Only working proxies will be written to the outout file
