import requests

from bs4 import BeautifulSoup as bs


def get_ssl_proxies():
    url = "https://free-proxy-list.net/"
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


def main():
    proxy = get_ssl_proxies()
    print(proxy)

if __name__ == "__main__":
    main()