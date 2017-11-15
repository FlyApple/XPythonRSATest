# encoding: utf-8

import base64;
import socket;
from urllib import request;
from html.parser import HTMLParser;

#
from share import share;

#
url = "http://www.baidu.com";
response = request.urlopen(url, data = None, timeout = socket._GLOBAL_DEFAULT_TIMEOUT);

#
content_type = response.headers["Content-Type"];

#
html= str(response.read(), encoding = "utf-8");
parser = HTMLParser();
parser.feed(html);
parser.close();

#save public key to file:
file_write = open("test.html", mode="w", encoding="utf-8");
file_write.write(html);
file_write.close();