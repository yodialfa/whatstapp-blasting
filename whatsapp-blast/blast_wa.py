from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os
import pandas as pd

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()

print(style.YELLOW + '\nYour Message :')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
baca_nomor = pd.read_excel("phone.xlsx")
numbers = baca_nomor['phone']
name = baca_nomor['name']
total_number=len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30

driver = webdriver.Chrome('chromedriver', options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "Press Enter if you Logged in ..." + style.RESET)
for  number, name in zip(numbers,name):
	# number = number.strip()
	number = str(number)
	pesan = f'Hi, *{name}*. {message}'
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format( name, total_number, number) + style.RESET)
	try:
		url = 'https://web.whatsapp.com/send?phone=62' + number + '&text=' + pesan
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
				except Exception as e:
					print(style.RED + f"\nFailed to send message to: {name} {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
				else:
					sleep(1)
					click_btn.click()
					sent=True
					sleep(3)
					print(style.GREEN + 'Message sent to: ' + name + number + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message to ' + name + number + str(e) + style.RESET)
driver.quit()


