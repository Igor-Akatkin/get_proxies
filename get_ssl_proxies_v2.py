import json
import requests
import time

from bs4 import BeautifulSoup as bs


def get_ssl_proxies(url):
    soup = bs(requests.get(url).content, "lxml")
    proxies = []

    rows = soup.find("table", class_="table").find_all("tr")
    for row in rows:
        if row.find(class_="hx").text == "yes":
            ip = row.find_all("td")[0].text
            port = row.find_all("td")[1].text
            proxy = f"{ip}:{port}"
            proxies.append(proxy)
    return proxies

def save_proxies(proxies):
    # запись списка в txt
    with open("ssl_proxies.txt", "w") as file:
        print(*proxies, file=file, sep="\n")

    # запись списка словарей в json
    result_list = []
    for proxy in proxies:
        result_list.append(
            {"proxy": proxy}
        )

    with open("ssl_proxies.json", "w", encoding="utf-8") as file:
        json.dump(result_list, file, indent=4)

def main():
    url = "https://free-proxy-list.net/"
    proxies = get_ssl_proxies(url)
    save_proxies(proxies)

if __name__ == "__main__":
    main()
