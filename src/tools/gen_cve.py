#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import tabulate
import json
import sys

def get_cvss3(vector):
  
  try:
    res = requests.get(url)
    doc = BeautifulSoup(res.text, "html.parser")
    score = doc.find("dd", {"id": "cvss-overall-score-cell"}).text

  except:
    score = "0.0"

  return score,url



def default(d, k, v=""):
  if k in d: return d[k]
  return v

if len(sys.argv) != 2:
  sys.stderr.write(f"{sys.argv[0]} <cve.json>\n")
  sys.exit(1)

src = sys.argv[1]

indata = json.load(open(src, "r"))


table = [ ]
headers = [ "Reference", "Report", "CVSS3", "Description" ]

for entry in indata:
  cve_link = ""
  if "cve" in entry:
    cve = entry["cve"]
    cve_link = f"[{cve}](https://www.cvedetails.com/cve/{cve})"

  report_links = ""
  if "report" in entry:
    if False and len(entry["report"]) == 1:
      report_links = f"[Report]({entry['report'][0]})"
    else:
      links = [ f"[{i+1}]({url})" for i,url in enumerate(entry["report"]) ]
      report_links = " ".join(links)

  cvss = ""
  if "cvss3" in entry:
    url=""
    if "cvss_vector" in entry:
      vector = entry["cvss_vector"]
      url = f"https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector={vector}&version=3.1"
    score = entry["cvss3"]
    cvss = f"[{score}]({url})"

  table.append([ f"{cve_link}",
                 f"{report_links}",
                 f"{cvss}",
                 default(entry, "descr", "")
                ]
               )


print(tabulate.tabulate(table, headers, tablefmt="html"))
