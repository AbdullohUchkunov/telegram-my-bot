import requests
from bs4 import BeautifulSoup
import time

named_tuple = time.localtime()
time_string = time.strftime("%H:%M:%S", named_tuple)
num = ""
list_1 = [11600]

# if time_string == "09:00:00" or time_string == "11:33:00":
response = requests.get("https://bank.uz/uz/currency/dollar-ssha")
bs = BeautifulSoup(response.text, 'html.parser')
dollar_rate = bs.find_all(class_='semibold-text')
num += dollar_rate[7].text[1:3]
num += dollar_rate[7].text[4:7]
num_1 = int(num)
list_1.append(num_1)
print(list_1)







