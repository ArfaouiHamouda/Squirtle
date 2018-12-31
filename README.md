# Squirtle Data&Files Scrapper

Python Data Scrapper OpenSource API made Scrapping Data from webpages (JSON/CSV format , optional : Download offline Files ) easier , also it includes Web API to Web Deployment . (Work still in progress for webService API ) please Contribute .

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them :

```
Python Version 3.6
Flask
Flask-RESTful
beautifulsoup4
```

### Installing

A step by step series of examples that tell you how to get a development env running

Python3.6 & pip3 Installation ( Why pip3 ? pip will automatically uses python2.X):

```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
python3 -V
sudo apt-get install python3-pip
```

BeautifulSoup4 installation using pip3 :
```
pip3 install beautifulsoup4
```

Flask installation using pip3 :
```
pip3 install flask
pip3 install flask-restful
```

Running Script :
```
python3 main.py
```
Running Flask Server :
```
export FLASK_APP=api.py
python3 -m flask run
```
The Web API will will be available : http://localhost:5000/getJSON


