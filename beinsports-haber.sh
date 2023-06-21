#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/scripts/

python3 beinsports-haber.py > ../beinsports-haber.m3u8
python3 BernamaTV.py > ../BernamaTV.m3u8
python3 supercross.py > ../supercrossTV.m3u8

echo m3u8 grabbed
