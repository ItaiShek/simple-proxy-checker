<!-- Badges -->
[![](https://img.shields.io/github/v/release/ItaiShek/simple-proxy-checker)](https://github.com/ItaiShek/simple-proxy-checker/releases)
![](https://img.shields.io/github/downloads/ItaiShek/simple-proxy-checker/total?color=red)
[![](https://img.shields.io/github/issues/ItaiShek/simple-proxy-checker?color=yellow)](https://github.com/ItaiShek/simple-proxy-checker/issues)
[![](https://img.shields.io/github/license/ItaiShek/simple-proxy-checker?label=license&color=green)](https://github.com/ItaiShek/simple-proxy-checker/blob/main/LICENSE)

# Description
ProxyChecker will check if one or more proxy servers are up and running.

## Installation

<details>

<summary style="font-size:large">Linux</summary>

#### Method 1: Using curl 

```bash
sudo curl -L https://github.com/ItaiShek/simple-proxy-checker/releases/download/v1.1.0/ProxyChecker -o /usr/local/bin/ProxyChecker
sudo chmod a+rx /usr/local/bin/ProxyChecker
```

#### Method 2: Using wget

```bash
sudo wget https://github.com/ItaiShek/simple-proxy-checker/releases/download/v1.1.0/ProxyChecker -O /usr/local/bin/ProxyChecker
sudo chmod a+rx /usr/local/bin/ProxyChecker
```

#### Method 3: Direct download

Download it from **[here](https://github.com/ItaiShek/simple-proxy-checker/releases/download/v1.1.0/ProxyChecker)**.


#### Method 4: Clone repository

```bash
git clone https://github.com/ItaiShek/simple-proxy-checker.git && cd simple-proxy-checker
sudo chmod a+rx ProxyChecker
```


</details>



<details>

<summary style="font-size:large">Windows</summary>

#### Direct download

Download it from **[here](https://github.com/ItaiShek/simple-proxy-checker/releases/download/v1.1.0/ProxyChecker.exe)**.

</details>

## How to use
```
Usage: ProxyChecker [OPTIONS] IP:PORT [IP:PORT IP:PORT...]
Options:
         -h, --help:         This screen
         -f, --file:         Get proxies from file                               (e.g. -f proxy_list.txt)
         -o, --output:       Output file for all the working proxies             (e.g. -o output.txt)
         -t, --time:         Maximum waiting time for a connection to the proxy  (e.g. -t 10)

Example: ProxyChecker -f proxylist.txt -o working.txt
```
## Notes
* All proxies must be of the form IP:PORT, if it's not then the program skips to the next proxy on the list
* It is not recommended to set the waiting time below 5 seconds
* Only working proxies will be written to the output file
```
