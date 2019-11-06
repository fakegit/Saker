<p align="center">
  <a href="" target="_blank" rel="noopener noreferrer">
    <img width="200" src="https://raw.githubusercontent.com/LyleMi/Saker/master/logo.jpg" alt="Saker logo">
  </a>
</p>

<h4 align="center">Penetrate Testing Auxiliary Suite</h4>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6-blue.svg">
  <img src="https://img.shields.io/github/issues/lylemi/saker.svg">
  <img src="https://img.shields.io/github/forks/lylemi/saker.svg">
  <img src="https://img.shields.io/github/stars/lylemi/saker.svg">
  <img src="https://img.shields.io/github/license/lylemi/saker.svg">
</p>

[中文版本(Chinese version)](README.zh-cn.md)

Saker is a flexible penetrate testing auxiliary suite. 

> Note: This project is for research and study only, do not use Saker for unauthorized penetration testing.

## TL;DR

brief support features:

+ scan website
  + infomation gathering
  + framework fingerprint
+ fuzz web request
  + XSS
  + SQL injection
  + SSRF
  + XXE
  + ...
+ subdomain gathering
+ port scanner
+ bruteforce
  + web dir
  + zip password
  + domain
  + ...
+ auxiliary servers
  + dns rebinding
  + ssrf
  + xss
+ third party api integration
  + crtsh
  + dns dumper
  + github
  + sqlmap

## Quick Setup

### latest version

```bash
pip install git+https://github.com/lylemi/saker
```

```bash
git clone https://github.com/LyleMi/Saker.git
pip install -r requirements.txt
python setup.py install
```

### stable version

```bash
pip install Saker
```

## Example Cases

### Scan Website

```python
from saker.core.scaner import Scanner
s = Scanner("http://127.0.0.1")
s.scan(filename="index.php", ext="php")
```

or by shell

```bash
python -m saker scan

usage: main.py [options]

Saker Scanner

optional arguments:
  -h, --help            show this help message and exit
  -s, --scan            run with list model
  -f file, --file file  scan specific file
  -e ext, --ext ext     scan specific ext
  -i, --interactive     run with interactive model
  -u URL, --url URL     define specific url
  -p PROXY, --proxy PROXY
                        proxy url
  -t INTERVAL, --timeinterval INTERVAL
                        scan time interval, random sleep by default
```

### Fuzz Website

```python
from saker.core.mutator import Mutator
options = {
    "url": "http://127.0.0.1:7777/",
    "params": {
        "test": "test"
    }
}
m = Mutator(options)
m.fuzz('url')
m.fuzz('params', 'test')
```

or by shell

```bash
python -m saker fuzz

usage: [options]

Saker Fuzzer

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     define specific url
  -m METHOD, --method METHOD
                        request method, use get as default
  -p PARAMS, --params PARAMS
                        request params, use empty string as default
  -d DATA, --data DATA  request data, use empty string as default
  -H HEADERS, --headers HEADERS
                        request headers, use empty string as default
  -c COOKIES, --cookies COOKIES
                        request cookies, use empty string as default
  -P PART, --part PART  fuzz part, could be url / params / data / ...
  -k KEY, --key KEY     key to be fuzzed
  -v VULN, --vuln VULN  Vulnarability type to be fuzzed
  -t INTERVAL, --timeinterval INTERVAL
                        scan time interval, random sleep by default
```

### Generate fuzz payload

#### Unicode Fuzz

```python
from saker.fuzzer.code import Code
payload = Code.fuzzErrorUnicode(payload)
```

#### Fuzz SSI

```python
from saker.fuzzers.ssi import SSI
payloads = [i for i in SSI.fuzz()]
```

### Brute password or others

```python
from saker.brute.dir import DirBrute
dirBrute = DirBrute("php", "index.php")
paths = dirBrute.weakfiles()
```

now support brute http basic auth, ftp, mysql, ssh, telnet, zipfile...

### Call Third Party API

#### Crt.sh

```python
from saker.api.crtsh import crtsh
crtsh("github.com")
```

#### DNSDumper

```python
from saker.api.dnsdumper import DNSdumpster
DNSdumpster("github.com")
```

#### Github API

```python
from saker.api.githubapi import GithubAPI
g = GithubAPI()
g.gatherByEmail("@github.com")
```

#### SQLMap API

```python
from saker.api.sqlmap import SQLMap
options = {"url": "https://github.com"}
SQLMap().scan(options)
```

### Handle HTML

```python
import requests
from saker.handler.htmlHandler import HTMLHandler
r = requests.get("https://github.com")
h = HTMLHandler(r.text)
print(h.title)
The world’s leading software development platform · GitHub
print(h.subdomains("github.com"))
['enterprise.github.com', 'resources.github.com', 'developer.github.com', 'partner.github.com', 'desktop.github.com', 'api.github.com', 'help.github.com', 'customer-stories-feed.github.com', 'live-stream.github.com', 'services.github.com', 'lab.github.com', 'shop.github.com', 'education.github.com']
```

### Port Scanner

```python
from saker.port.nmap import Nmap
n = Nmap(domain)
ret = n.run()
print(n.ret)
```

### Special Server

```python
from saker.servers.socket.dnsrebinding import RebindingServer
values = {
    'result': ['8.8.8.8', '127.0.0.1'],
    'index': 0
}
dnsServer = RebindingServer(values)
dnsServer.serve_forever()
```

## Contributing

Contributions, issues and feature requests are welcome.

Feel free to check [issues page](https://github.com/lylemi/saker/issues) if you want to contribute.

## Show your support

Please star this repository if this project helped you.

## License

Copyright © 2019 [Lyle](https://github.com/lylemi).

This project is [GPLv3](https://github.com/lylemi/saker/blob/master/LICENSE) licensed.
