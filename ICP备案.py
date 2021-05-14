import os
import sys
import re
import time
import urllib.request


def perror_and_exit(message, status=-1):
    sys.stderr.write(message + '\n')
    sys.exit(status)


def get_text_from_html_tag(html):
    pattern_text = re.compile(r">.*?    return pattern_text.findall(html)[0][1:-2].strip()


def parse_alexa(url):
    url_alexa = "http://icp.alexa.cn/index.php?q=%s" % url
    print(url_alexa)