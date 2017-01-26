# static_server_starter_kit
Quickly setup a static server 

## 0. Requirements:

### To install Python 3.6, nginx, and virtualenv

If on Ubuntu 16.04:

```
sudo add-apt-repository ppa:jonathonf/python-3.6
```

Then if on Ubuntu 16.10 or 16.04:

```
sudo apt-get update
sudo apt install python3.6 nginx virtualenv;
```

## 1. A server to host your static files

```
mkdir ~/StaticServer;
virtualenv -p python3.6 .venv
source .venv/bin/activate
pip install flask
wget https://raw.githubusercontent.com/JCharante/static_server_starter_kit/master/server.py 
python server.py
```

## 2. Setup a reverse proxy for nginx

Using the script from [here](https://github.com/AI-Productions/nginx-reverse-proxy)

```
wget https://raw.githubusercontent.com/AI-Productions/nginx-reverse-proxy/master/nrp.py
```

You use it like
```
sudo python3.6 nrp.py -r <a[ppend]/o[verwrite]> -p <port> -d <domain> -t <http/ws>
```

In our case:

```
sudo python3.6 nrp.py -r a -p 4847 -d static.jcharante.com -t http
```

## 3.

Now just edit your DNS settings (in our case, point static.jcharante.com towards our server's ip address) and you'll all set!
