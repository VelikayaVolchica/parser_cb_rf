# Сurrency parser

## Что делает это приложение
Выводит курсы валют ЦБ РФ за определенную дату.

### Инициализация приложения
```bash
git clone https://github.com/VelikayaVolchica/parser_cb_rf
# Переходим в директорию проекта, устанавливаем необходимые библиотеки
cd <Название проекта>
pip install -r requirements.txt
```

### Запуск приложения
```bash
python3 currency_rates.py --code=<код валюты в формате ISO 4217> --date=<дата в формате YYYY-MM-DD>
```
