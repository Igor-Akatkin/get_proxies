# ENG
## Description:
The script collects and outputs a list of proxies (http/https) from https://free-proxy-list.net

## How to use/description of script functions:
* Function **get_all_proxies**  
Allows to get all available proxies on the resource without binding to the scheme and save them to txt and json files
* Function **get_https_proxies**  
Allows to get all https proxies available on the resource and save them to txt and json files
* Function **get_one_random_proxy**  
Allows to get one random proxy without binding to a scheme
* Function **get_one_random_https_proxy**  
Allows to get one https proxy

## Result output format:
The data is written in two formats:
- ssl_proxies.txt - list in {ip}:{port} format
- ssl_proxies.json - list of dictionaries in json format
___

# RUS
## Описание:
Скрипт собирает и выдает список proxies (http/https) с сайта https://free-proxy-list.net  

## Как пользоваться/описание функций скрипта:
* Функция **get_all_proxies**  
Позволяет получить все доступные на ресурсе прокси без привязки к схеме и сохранить в файлы txt и json
* Функция **get_https_proxies**  
Позволяет получить все доступные на ресурсе https прокси и сохранить в файлы txt и json
* Функция **get_one_random_proxy**  
Позволяет получить один рандомный прокси без привязки к схеме
* Функция **get_one_random_https_proxy**  
Позволяет получить один https прокси
    
## Формат выдачи результата:
Данные записываются в двух форматах:
- ssl_proxies.txt – список в формате {ip}:{port}
- ssl_proxies.json – список словарей в json