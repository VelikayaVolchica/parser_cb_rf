import argparse
import requests
import xml.etree.ElementTree as ET

def formatting_date(date):
    date_list = date.split('-')
    format_date = f'{date_list[2]}/{date_list[1]}/{date_list[0]}'
    return format_date

def get_exchange_rate(code, date):
    date = formatting_date(date)
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Ошибка при получении данных. Код ошибки: {response.status_code}")
    except requests.RequestException as e:
        print(f"Произошла ошибка: {e}")

def parse_exchange_rate(xml_content, code):
    root = ET.fromstring(xml_content)
    
    for currency in root.findall('Valute'):
        currency_code = currency.find('CharCode').text
        if currency_code == code:
            name = currency.find('Name').text
            rate = currency.find('Value').text
            return {'name': name, 'rate': rate}

def display_exchange_rate(exchange_rate, code, date):
    if exchange_rate:
        print(f"{code} ({exchange_rate['name']}): {exchange_rate['rate']}")
    else:
        print(f"Информация о валюте {code} на дату {date} не найдена.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Утилита для получения курса валют ЦБ РФ за определенную дату")
    parser.add_argument("--code", type=str, help="Код валюты в формате ISO 4217", required=True)
    parser.add_argument("--date", type=str, help="Дата в формате YYYY-MM-DD", required=True)
    args = parser.parse_args()

    xml_content = get_exchange_rate(args.code, args.date)
    exchange_rate = parse_exchange_rate(xml_content, args.code)
    display_exchange_rate(exchange_rate, args.code, args.date)
