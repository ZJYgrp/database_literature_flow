import requests
import json
import pandas as pd
import urllib
import wget
import lxml
import html5lib
import bs4
from scidownl.scihub import *

DOI = "10.1016/j.jmb.2004.10.035"
out = 'paper'
sci = SciHub(DOI, out).download(3)

#for i in idlist
#r = requests.get('https://reader.elsevier.com/reader/sd/pii/S0300908414002156?token=9ACC68C41C9C47330CD5D9775A87E086238E27FD2DFAEA3D4418C88DEBAD83D1097512B0F40DC7FAB736E92FB266F8D7&originRegion=us-east-1&originCreation=20210605170135')
r=requests.get("https://pubs.acs.org/doi/10.1021/bi8010016")


r.headers['content-type']='application/json; charset=utf8'

print(r.status_code)
r.encoding='utf-8'

#json.loads(r.text)
#print(r.text)
#wget.download("https://pubs.acs.org/doi/pdf/10.1021/bi8010016")
#json.loads(r.text)

#dfs = pd.read_html("https://reader.elsevier.com/reader/sd/pii/S0300908414002156?token=9ACC68C41C9C47330CD5D9775A87E086238E27FD2DFAEA3D4418C88DEBAD83D1097512B0F40DC7FAB736E92FB266F8D7&originRegion=us-east-1&originCreation=20210605170135")
#print(dfs)