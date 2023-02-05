from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from art import *
import time

tprint("-------------")
tprint("Magor Software")
tprint("                NGL BOT")
tprint("-------------")
time.sleep(3)

link = input("link:")
be = input("message:")
azanyi = int(input("how many messages:"))
wat = int(input("add watermark?(0, 1)"))

driver = webdriver.Chrome()
driver.get(link)

for i in range(azanyi):
    try:
        
        elem = driver.find_element("name" ,"question")
        if wat == 0:
            elem.send_keys(be)
        else:
            elem.send_keys(f"{be} (github.com/kalandor122/ngl_bot)")
        but = driver.find_element("xpath", "/html/body/div[1]/form/button").click()
        time.sleep(1)
        butt = driver.find_element("xpath", "/html/body/div[2]/a[2]").click()
        time.sleep(2)
        
    except:
        driver.close()
        driver = webdriver.Chrome()
        time.sleep(25)
        driver.get(link)
        
