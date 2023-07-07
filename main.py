# This is a sample Python script.
name='SPAN-BLR-740'
paswd='Jayram@1990'
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from faker import Faker
f=Faker()
f.name()
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains
import time
service_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service_obj)
driver.get("https://spanidea.greythr.com/uas/portal/auth/login?login_challenge=c72e64ec5ee14b8ebcd3acf02642c2e9")
time.sleep(3)
driver.find_element(By.ID,'username').send_keys(name)
driver.find_element(By.ID,'password').send_keys(paswd)
#driver.find_element(By.TAG_NAME,'button').click()
