import json
import requests
import time
from random import choice

from bs4 import BeautifulSoup as bs


def get_https_proxies():
    """
    Получить и сохранить все https прокси
    """
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "lxml")

    proxies = []

    rows = soup.find("table", class_="table table-striped table-bordered").find("tbody").find_all("tr")
    for row in rows:
        if row.find(class_="hx").text == "yes":
            ip = row.find_all("td")[0].text.strip()
            port = row.find_all("td")[1].text.strip()
            proxy = f"{ip}:{port}"
            proxies.append(proxy)

    # запись списка в txt
    with open("https_proxies.txt", "w") as file:
        print(*proxies, file=file, sep="\n")

    # запись списка словарей в json
    result_list = []
    for proxy in proxies:
        result_list.append(
            {"https": proxy}
        )
    with open("https_proxies.json", "w", encoding="utf-8") as file:
        json.dump(result_list, file, indent=4)


def get_all_proxies():
    """
    Получить и сохранить все прокси вне зависимости от схемы
    """
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "lxml")

    proxies = []

    rows = soup.find("table", class_="table table-striped table-bordered").find("tbody").find_all("tr")
    for row in rows:
        ip = row.find_all("td")[0].text.strip()
        port = row.find_all("td")[1].text.strip()
        schema = 'https' if 'yes' in row.find_all("td")[6].text.strip() else 'http'
        proxy = f'{schema}://{ip}:{port}'
        proxies.append(proxy)

    # запись списка в txt
    with open("all_proxies.txt", "w") as file:
        print(*proxies, file=file, sep="\n")

    # запись списка словарей в json
    result_list = []
    for proxy in proxies:
        schema = proxy.split('://')[0]
        proxy = proxy.split('://')[1]
        result_list.append(
            {schema: proxy}
        )
    with open("all_proxies.json", "w", encoding="utf-8") as file:
        json.dump(result_list, file, indent=4)


def get_one_random_proxy():
    """
    Получить 1 рандомный прокси вне зависимости от схемы
    Срез из 15 первых записей на момент обращения к функции
    """
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "lxml")

    proxies = []

    rows = soup.find("table", class_="table table-striped table-bordered").find("tbody").find_all("tr")
    for row in rows[:15]:
        ip = row.find_all("td")[0].text.strip()
        port = row.find_all("td")[1].text.strip()
        schema = 'https' if 'yes' in row.find_all("td")[6].text.strip() else 'http'
        proxy = f'{schema}://{ip}:{port}'
        proxies.append(proxy)

    result_list = []
    for proxy in proxies:
        schema = proxy.split('://')[0]
        proxy = proxy.split('://')[1]
        result_list.append(
            {schema: proxy}
        )
    print(f'Рандомный прокси: {choice(result_list)}')
    return choice(result_list) # {'schema': 'ip:port'}

def get_one_random_https_proxy():
    """
    Получить 1 рандомный https прокси
    """
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "lxml")

    proxies = []

    rows = soup.find("table", class_="table table-striped table-bordered").find("tbody").find_all("tr")
    for row in rows:
        if row.find(class_="hx").text == "yes":
            ip = row.find_all("td")[0].text.strip()
            port = row.find_all("td")[1].text.strip()
            proxy = f"{ip}:{port}"
            schema = "https"
            proxies.append(
                {schema: proxy}
            )
    print(f'Рандомный https прокси: {choice(proxies)}')
    return choice(proxies)  # {'schema': 'ip:port'}


def check_proxy(url):
    """
    Проверка прокси на доступность.
    В параметр proxy необходимо добавить вызов одной из функций:
    get_one_random_proxy(soup) - Получить 1 рандомный прокси вне зависимости от схемы
    get_one_random_https_proxy(soup) - Получить 1 рандомный https прокси
    """
    proxy = get_one_random_proxy(soup)
    r = requests.get(url, proxies=proxy, timeout=5)
    print(r.json())


def main():
    # Получить все прокси без привязки к схеме и сохранить в файлы:
    get_all_proxies()
    # Получить все https прокси и сохранить в файлы:
    get_https_proxies()

    # Получить один рандомный прокси без привязки к схеме
    get_one_random_proxy()
    # Получить один https прокси
    get_one_random_https_proxy()

    # Проверка
    # check_proxy('http://httpbin.org/ip')
    # check_proxy('https://api.ipify.org?format=json')

if __name__ == "__main__":
    main()
