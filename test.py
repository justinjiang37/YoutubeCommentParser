import io
from PIL import Image
import PIL
import requests
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

from PIL import Image, ImageTk

path = "E:\\\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.youtube.com/watch?v=FSGeskFzE0s")
wait = WebDriverWait(driver, 1)

options = Options()
options.add_argument("--headless")

root = tk.Tk()
root.title("Youtube Parser Tool")

for item in range(5):  # by increasing the highest range you can get more content
    wait.until(EC.visibility_of_element_located(
        (By.TAG_NAME, "body"))).send_keys(Keys.END)  # end moves page down
    time.sleep(5)
    # make time wait a little longer for it to load and be more stable

pfp_list = wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, "#comment #img")))

#DIG what exactly is the element in pfp_list[0]
for element in pfp_list:
    if element is None:
        print("element is NONE...")
        continue
    print(element)
    a = element.get_attribute("src")
    if a is None:
        print("link is NONE...")
        continue
    print(a)

    # look at output
    # some times the first image works and sometimes it dosent :(
    # GET Attribute is CORRECT but it is just NOT consistent
    # request .get specifically NEEDS an Url Required. The url of the request
    response = requests.get(a)
    image_bytes = io.BytesIO(response.content)
    img = PIL.Image.open(image_bytes)
    tkimage = ImageTk.PhotoImage(img)
    print(type(tkimage))
    testimg = tk.Label(root, image=tkimage)
    testimg.pack()
    print(type(testimg))
    # w = tk.Label(root, text="Hello Tkinter!")
    # w.pack()
    # only pack very last image (with link url)

root.mainloop()

# 1: everything works - Old - Kevin Garncia
# 2: None - same thing - same code error:
'''
DevTools listening on ws://127.0.0.1:58258/devtools/browser/1896c7c4-be8c-4903-b9b1-c310da02dd23
None
Traceback (most recent call last):
  File "C:\\Users\\Justi\\OneDrive\\Desktop\\Git\\YoutubeCommentParser\\test.py", line 47, in <module>
    response = requests.get(a) #What is requests.get EXPECTING EXACTLY
  File "C:\\Python39\\lib\\site-packages\\requests\\api.py", line 76, in get
    return request('get', url, params=params, **kwargs)
  File "C:\\Python39\\lib\\site-packages\\requests\\api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\\Python39\\lib\\site-packages\\requests\\sessions.py", line 528, in request
    prep = self.prepare_request(req)
  File "C:\\Python39\\lib\\site-packages\\requests\\sessions.py", line 456, in prepare_request
    p.prepare(
  File "C:\\Python39\\lib\\site-packages\\requests\\models.py", line 316, in prepare
    self.prepare_url(url, params)
  File "C:\\Python39\\lib\\site-packages\\requests\\models.py", line 390, in prepare_url
    raise MissingSchema(error)
requests.exceptions.MissingSchema: Invalid URL 'None': No schema supplied. Perhaps you meant
'''

# 3: Works - New - Nikolia Sokolov
# 4: Works - New - Nikolia Sokolov
# 5: Time out - comment didnt load in time - (Let it load for a second?) dont make two
#    consecutively too quickly
'''
DevTools listening on ws://127.0.0.1:58429/devtools/browser/aa38781f-36cb-41a3-9a85-a01222b4f710
Traceback (most recent call last):
  File "C:\\Users\\Justi\\OneDrive\\Desktop\\Git\\YoutubeCommentParser\\test.py", line 38, in <module>
    pfp_list = wait.until(EC.presence_of_all_elements_located(
  File "C:\\Python39\\lib\\site-packages\\selenium\\webdriver\\support\\wait.py", line 80, in until
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message:
'''
# 6: Works - New - Nikolia Sokolov (let rest/load for 30 sec)
# 7: Loaded - still didnt work - None same error as attemp two
# 8: Works - New - Nikolia Sokolov (let rest/load for 30 sec)
# 9: did not let rest - didnt work
# 10: last attempt: let rest for 5 min, focused on browser(no focus on other) should work
#       Yes Works!
