#!/usr/bin/python3

# Vidio API Python
# Created by:  @thefirefox12537

import argparse
import requests
import json
import re
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--channel-code", required=True, help="channel code")
parser.add_argument("-n", "--channel-name", required=True, help="channel name")
parser.add_argument("-u", "--username", help="user name")
parser.add_argument("-p", "--password", help="password")
parser.add_argument("output", nargs="?", help="output file")
args = parser.parse_args()

vidio_url = 'vidio.com'
windows = True if 'win' in sys.platform else False

def nosignal():
    url = 'http://thefirefox12537.github.io/streams/nosignal'
    m3u8_get = requests.get(f"{url}/index.m3u8").text
    for ts in ['01.m3u8', '02.m3u8']:
        m3u8_get = m3u8_get.replace(ts, f"{url}/{ts}")
    return m3u8_get

def grab(code, name):
    global mesg
    headers = {}

    try:
        payload = {}
        payload['Authority'] = "www.{}".format(vidio_url)
        payload['Content-Length'] = '0'
        payload['Origin'] = "https://www.{}".format(vidio_url)
        payload['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        payload['Dnt'] = '1'
        payload['Accept'] = '*/*'
        payload['Sec-Fetch-Site'] = 'same-origin'
        payload['Sec-Fetch-Mode'] = 'cors'
        payload['Referer'] = "https://www.{}/live/{}-{}".format(vidio_url, code, name);
        payload['Accept-Encoding'] = 'gzip, deflate, br';
        payload['Accept-Language'] = 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7';

        get = s.post("https://www.{}/live/{}/tokens".format(vidio_url, code), data=payload, headers=headers).json()

        token = '?{}'.format(get['token'])
    except:
        token = ''

    try:
        headers['Authority'] = "etslive-app.{}".format(vidio_url)
        headers['Origin'] = "https://www.{}".format(vidio_url)
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        headers['Dnt'] = '1'
        headers['Accept'] = '*/*'
        headers['Sec-Fetch-Site'] = 'same-site'
        headers['Sec-Fetch-Mode'] = 'cors'
        headers['Referer'] = "https://www.{}".format(vidio_url)
        headers['Accept-Encoding'] = 'gzip,deflate,br'
        headers['Accept-Language'] = 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'

        result = s.get("https://etslive-app.{}/live/{}/master.m3u8{}".format(vidio_url, code, token), headers=headers)
        result.raise_for_status()

        mesg = 'Create file successfully: {}'.format(args.output)
        return result.text
    except:
        mesg = 'Token not found. Create no signal redirect.'
        return nosignal()

s = requests.Session()
result = grab(args.channel_code, args.channel_name)
if args.output:
    open(args.output, "w").write(result)
    print(mesg)
else:
    print(result)
