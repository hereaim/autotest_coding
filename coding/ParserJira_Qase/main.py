import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import config
""" Просто запрос в жиру
statusCategory = done AND project = 10600 AND type = Задача 
and (fixVersion in ("Запланировать в kuz-rc-1","Запланировать в rc-12","RC-11")) 
and (summary !~  "Релиз" and summary !~"%MAIN%" and  summary !~ "%regress%") 
ORDER BY key DESC, priority DESC
"""


#Тестовый апи токен e8ea74c870083e7c28c5d89482853e1c1b3d2dd6bde465354480cdc7804fabbd
#Реальный апи токен 5dad3438e15f52f629379ce51ca4d16504e27ef9c58a01b99865a8f6dda934dd
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)



def GetIdSuite():
    url = config.base_url_case
    headers = {
        "accept": "application/json",
        "Token": config.token
    }
    response = requests.get(url, headers=headers)
    print(response.text)

def MiniParserJira():
    list_summary, list_summary_url, list_href, list_name, list_priority, list_fix_versions, full_list_sprint, list_last_sprint = [], [], [], [], [], [], [], []
    driver.get('file:///C:/Users/Sayonara/Downloads/SmartCityCloud%20JIRA%202024-06-11T17_58_43+0600.html')
    getUrl = driver.find_elements(By.CLASS_NAME, 'issue-link')
    getSummary = driver.find_elements(By.CLASS_NAME, 'summary')
    getName = driver.find_elements(By.CLASS_NAME, 'issue-link')
    getPriority = driver.find_elements(By.CLASS_NAME, 'priority')
    getFixVersions = driver.find_elements(By.CLASS_NAME, 'fixVersions')
    getSprint = driver.find_elements(By.CLASS_NAME, 'customfield_10101')
    for summary in getSummary:#Получение наименования тикета
        list_summary.append(summary.text)
    for getHref in getUrl:#Получение ссылки на тикет
        list_href.append(getHref.get_attribute('href'))
    for name in getName:#Получение номера тикета
        list_name.append(name.text)
    for priority in getPriority: #Получение приоритета тикета
        list_priority.append(priority.text)
    for versions in getFixVersions:
        list_fix_versions.append(versions.text)
    for sprint in getSprint:
        text = sprint.text
        last_value = text.split(',')[-1].strip()
        list_last_sprint.append(last_value)
    return list_summary, list_href, list_name, list_priority, list_fix_versions, list_last_sprint

def get_existing_titles():
    base_url = config.base_url_case
    headers = {
        "accept": "application/json",
        "Token": config.token
    }

    titles = set()
    offset = 0
    limit = 100

    while True:
        url = f"{base_url}?limit={limit}&offset={offset}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Ошибка получения наименований: {response.status_code}")
            break

        data = response.json()
        cases = data.get('result', {}).get('entities', [])
        for case in cases:
            titles.add(case.get('title'))

        offset += limit
        if offset >= data.get('result', {}).get('total', 0):
            break
    return titles

def fetch_all_cases():
    base_url = config.base_url_case
    headers = {
        "accept": "application/json",
        "Token": config.token
    }

    existing_titles = get_existing_titles()
    print(f"Всего задач: {len(existing_titles)}")

    # Получаем общее количество записей
    initial_response = requests.get(f"{base_url}?limit=1", headers=headers)
    if initial_response.status_code != 200:
        print(f"Ошибка получения данных: {initial_response.status_code}")
        return []

    total = initial_response.json().get('result', {}).get('total', 0)

    all_cases = []
    offset = 0
    limit = 100

    while offset < total:
        url = f"{base_url}?limit={limit}&offset={offset}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Ошибка получения данных: {response.status_code}")
            break

        data = response.json()
        cases = data.get('result', {}).get('entities', [])

        for case in cases:
            if case.get('title') not in existing_titles:
                all_cases.append(case)
                existing_titles.add(case.get('title'))

        offset += limit
    return all_cases

def AddInQase():
    # Вызов мини-парсера Jira
    mini_parser = MiniParserJira()
    list_summary, list_href, list_name, list_priority, list_fix_versions, list_last_sprint = mini_parser

    count_title = 0
    url = config.base_url_case

    # Словари для приоритетов и критичности
    priority_map = {
        "Low": 3,
        "Lowest": 3,
        "Medium": 2,
        "High": 1,
        "Highest": 1
    }

    severity_map = {
        "Lowest": 6,
        "Low": 5,
        "Medium": 4,
        "High": 3,
        "Highest": 2
    }

    # Словарь для suite_id в зависимости от fix_versions
    # fix_versions в Jira: id suite в Qase
    fix_version_suite_map = {
        "Запланировать в rc-12, Запланировать в kuz-rc-1": 1,
        "Запланировать в kuz-rc-1": 2,
        "RC-11": 3,
        "Запланировать в rc-12": 4,
        "RC-11, Запланировать в rc-12": 4,
        "RC-11, Запланировать в rc-12, Запланировать в kuz-rc-1": 4,
        "": 5
    }

    def create_payload(i, suite_id):
        priority = priority_map.get(list_priority[i], 0)
        severity = severity_map.get(list_priority[i], 0)
        return {
            "suite_id": suite_id,
            "tags": [f"{list_last_sprint[i]}"],
            "title": f"[{list_name[i]}] - {list_summary[i]}",
            "description": f"[{list_href[i]}]({list_href[i]})",
            "priority": priority,
            "severity": severity
        }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Token": config.token
    }

    # Получаем существующие заголовки
    existing_titles = get_existing_titles()

    for i in range(len(list_priority)):
        title = f"[{list_name[i]}] - {list_summary[i]}"
        if title in existing_titles:
            continue

        suite_id = fix_version_suite_map.get(list_fix_versions[i])
        if suite_id is not None:
            payload = create_payload(i, suite_id)
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f"'{title}' - добавлен в Qase")
                # Добавляем заголовок в set после успешного добавления
                existing_titles.add(title)
                count_title += 1
            else:
                print(f"Ошибка добавления '{title}': {response.status_code}")
    if count_title == 0:
        print("Новых задач нет")
    else:
        print(f"Добавление задач завершено. Всего добавлено - {count_title}")


# Вызов функции для добавления задач в Qase
all_cases = fetch_all_cases()
AddInQase()