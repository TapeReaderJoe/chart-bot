"""Module for scraping"""

import time
from bs4 import BeautifulSoup, Tag
import requests


def scrape_finviz(ticker):
    status_code = 0
    result = {}
    url = f"https://finviz.com/quote.ashx?t={ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=5)
    while status_code != 200:
        response = requests.get(url, headers=headers, timeout=5)
        status_code = response.status_code
        if status_code != 200:
            print(f"Received status code: {status_code} for ticker: {ticker}")
            time.sleep(10)
        if status_code == 404:
            return result
    soup = BeautifulSoup(response.content, "html.parser")
    tab_body = soup.find("table", {"class": "snapshot-table2"})
    if isinstance(tab_body, Tag):
        rows = tab_body.find_all("tr")
        scrape = []
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                scrape.append(col.text.strip())
        scrape_dict = {}
        for i in range(0, len(scrape), 2):
            k = _replace(scrape[i])
            v = scrape[i + 1]
            scrape_dict[k] = v

        result["ticker"] = ticker.lower()
        result["sales_surprise"] = _format_pct(scrape_dict["sales_surprise"])
        result["eps_surprise"] = _format_pct(scrape_dict["eps_surprise"])
        result["forward_pe"] = _format_float(scrape_dict["forward_pe"])
        result["pe"] = _format_float(scrape_dict["pe"])
        result["peg"] = _format_float(scrape_dict["peg"])
        result["ps"] = _format_float(scrape_dict["ps"])
        result["pb"] = _format_float(scrape_dict["pb"])
        result["pfcf"] = _format_float(scrape_dict["pfcf"])
        result["insider_own"] = _format_pct(scrape_dict["insider_own"])
        result["inst_own"] = _format_pct(scrape_dict["inst_own"])
        result["inst_trans"] = _format_pct(scrape_dict["inst_trans"])
        result["shares_float"] = _format_shares_float(scrape_dict["shs_float"])
        result["short_float"] = _format_pct(scrape_dict["short_float"])
        result["roa"] = _format_pct(scrape_dict["roa"])
        result["roe"] = _format_pct(scrape_dict["roe"])
        result["roi"] = _format_pct(scrape_dict["roi"])
        result["gross_margin"] = _format_pct(scrape_dict["gross_margin"])
        result["oper_margin"] = _format_pct(scrape_dict["oper_margin"])
        result["profit_margin"] = _format_pct(scrape_dict["profit_margin"])
    return result


def _replace(s):
    return (
        s.replace("(", "")
        .replace(")", "")
        .replace("/", "")
        .replace(" ", "_")
        .replace(".", "")
        .lower()
    )


def _format_pct(value):
    try:
        ret = float(value.replace("%", "")) / 100
    except:
        ret = 0
    return ret


def _format_float(value):
    try:
        ret = float(value)
    except:
        ret = 0
    return ret


def _format_shares_float(value: str):
    ret = 0
    try:
        if value.endswith("M"):
            ret = float(value.replace("M", ""))
        elif value.endswith("B"):
            ret = float(value.replace("B", "")) * 1000
    except:
        ret = 0
    return ret
