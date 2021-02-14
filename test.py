import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import ttk
from tkinter import Entry
import tkinter as tk
import tkinter.font as font
from tkinter import *

path = "E:\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.youtube.com/watch?v=FSGeskFzE0s")
wait = WebDriverWait(driver, 1)

for item in range(10):  # by increasing the highest range you can get more content
    wait.until(EC.visibility_of_element_located(
        (By.TAG_NAME, "body"))).send_keys(Keys.END)  # end moves page down
    time.sleep(1)

pfp_list = wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, "#comment #img")))

print(username_list[0].text)
