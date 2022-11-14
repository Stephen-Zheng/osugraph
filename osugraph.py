import os
from time import sleep
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By


id = str(input("What is your osu Ign: "))
timezone = str(input("what timezone are you in?(in caps): "))

match timezone:
  case "PST":
    zone = -8
  case "AST":
    zone = -4
  case "EST":
    zone = -5
  case "AKST":
    zone = -9
  case "CT":
    zone = -6
  case "MT":
    zone = -7
#zone = -8
path = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options = options)
driver.get("https://osu.ppy.sh/users/" + id)

my_element = driver.find_element(By.CLASS_NAME, value = "show-more-link__label-text")
my_element.click()
sleep(1)
my_element = driver.find_element(By.CLASS_NAME, value ="show-more-link__label-text")
my_element.click()
sleep(1)

html = driver.page_source
htmls = html.split()

i = 0
YN = False
arr_num = [0] * 24

for line in htmls:

  if "datetime" in str(line) and YN == True:
    lines = line.split('T')
    hour = lines[1].split(':')

    realtime = int(hour[0]) + zone

    if realtime > 23:
      realtime -= 24
    
    elif realtime < 0:
      realtime += 24

    arr_num[realtime] += 1
  
    i += 1

  elif ">100</span>" in str(line):
    YN = True

  if i == 100:
    break

driver.quit()

hours = []
hours = [j for j in range(24)]
plt.xticks(hours, hours)
plt.yticks(hours)
plt.xlabel("Hour")
plt.ylabel("n of scores")
plt.bar(hours, arr_num)
dir_path = os.path.dirname(os.path.realpath(__file__))
plt.savefig(dir_path + "/save.png")
plt.show()