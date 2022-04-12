
import requests
import json
import csv
import pandas as pd
import io
from bs4 import BeautifulSoup

def main():
    url = 'http://merchant.officenexapi.com/gmc/200004228227200008518956'
    response = requests.get(url)
    html = response.text

    html = html[59:-7]
    print(html)
    # df = pd.read_csv(io.StringIO(html))
    # print(df)

if __name__ == '__main__':
    main()