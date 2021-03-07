'''
Every single import that's needed to run Selenium.
These are default copied from online tutorials (randomly pieced together)
We really only are using:
time:                   Lets us control wait method which is a pause in the automation. You'll see it used to create pauses in the code.
import Chrome:          Lets us use Chrome as the webdriver for web testing. I assume if we wanted firefox/safari/edge we'd import those instead.
import Options:         Lets us set the --headless tag. This lets us run the code without having a window popup. I have it commented out right now so you can see the cool stuff.
                        When you want to run it quicker, just comment it out again when you run the code.
import Keys:            Lets the program use keys such as ASDF, TAB, RETURN. In our case, we use the END key to hit the bottom of the comments each time.
                        Our code goes down 10 times, so 10 times it will go downwards to gather comments. You can probably set a while loop that keeps going down
                        until you don't have comments.
import WebDriverWait:   In case of an issue, it will let the web automation driver wait for a certain amount of time before firing off code.
import EC:              Lets us set the selectors. You can see on line 37 that it uses the CSS selector tags of #comment and #content-text. You can change that for whatever
                        you actually want to get.
1. Improve the UI
2. Add a new screen to go to to list out all of the relevant comments in a pretty way.
3. Increase the range from 5 to a higher number.
4. Disable the Chrome Tester rom loading the UI so that the tests run faster
'''

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
import io
from PIL import Image
import PIL
import requests
from PIL import Image, ImageTk
# UI import


def YoutubeParser(keywords, link):

    options = Options()
    options.add_argument("--headless")

    keywords = keywords.get()
    keywords = str(keywords).split(' ')

    with Chrome(options=options) as driver:
        wait = WebDriverWait(driver, 1)
        print("========================")
        driver.get(link.get())

        for item in range(10):  # by increasing the highest range you can get more content
            wait.until(EC.visibility_of_element_located(
                (By.TAG_NAME, "body"))).send_keys(Keys.END) # end moves page down
            time.sleep(1)

        root = tk.Tk()
        root.title("ALL Comments")

        # creating out put frame
        outputFrame1 = Frame(root)
        outputFrame1.pack(fill = BOTH, expand = 1)

        # creating out put canvas in side frame
        outputCanvas = Canvas(outputFrame1)
        outputCanvas.pack(side = LEFT, fill = BOTH, expand = 1)

        # adding the scroll bar
        scrollBar = ttk.Scrollbar(outputFrame1, orient = VERTICAL, command = outputCanvas.yview)
        scrollBar.pack(side = RIGHT, fill = Y)

        # configuring canvas
        outputCanvas.configure(yscrollcommand = scrollBar.set)
        outputCanvas.bind('<Configure>', lambda e: outputCanvas.configure(
            scrollregion = outputCanvas.bbox("all")))

        # create new frame in side canvas
        outputFrame2 = Frame(outputCanvas)

        # add second frame in canvas
        outputCanvas.create_window((0,0), window = outputFrame2, anchor = "nw")

        for i in range(len(wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))))):
            comment = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#comment #content-text")))[i]

            username = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#comment #author-text")))[i].text

            pfpLink = str(wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#comment #img")))[i].get_attribute("src"))

            print(wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#comment #img")))[i].get_attribute("src"))

            words = []
            temp_sentence = ""
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

            for i in comment.text:
                if i not in punctuations:
                    temp_sentence = temp_sentence + i

            words = temp_sentence.split()
            for j in range(len(words)):
                words[j] = words[j].lower()

            if any(temp in words for temp in keywords):
                response = requests.get(pfpLink)
                image_bytes = io.BytesIO(response.content)
                img = PIL.Image.open(image_bytes)
                tkimage = ImageTk.PhotoImage(img)
                pfp = tk.Label(root, image=tkimage)

                temp_comment = comment.text
                temp_comment_list = temp_comment.split(' ')
                new_string = ""
                line = ""

                for i in range(0, len(temp_comment_list), 7):
                    if i + 7 < len(temp_comment_list):
                        for j in range(i, i+7):
                            line = line + temp_comment_list[j] + ' '
                        line += "\n"
                        new_string += line
                        line = ""
                    else:
                        for j in range(i, len(temp_comment_list)):
                            line = line + temp_comment_list[j] + ' '
                        new_string += line

                pfp.pack(side = TOP)
                username = tk.Label(outputFrame2, text=username + "\n___________________")
                username.pack(side = TOP)

                text = tk.Label(outputFrame2, text=new_string)
                text.pack()
                space = tk.Label(
                    outputFrame2, text="\n\n  ")
                space.pack(side = TOP)

        driver.quit()
        root.mainloop()


def UI():
    root = tk.Tk()
    root.title("Youtube Parser Tool")

    init = tk.Canvas(root, width=600, height=600)
    init.configure(bg='white')
    init.pack()

    # keywords
    keywordTextBox = tk.Canvas(root, width=300, height=80,
                               bd=0, highlightthickness=0)
    keywordTextBox.place(relx=0.5, rely=0.60, anchor='center')
    keywordTextBox.configure(bg="white")
    keywordTextBox.config(borderwidth=0)

    img = PhotoImage(file="C:/Users/Justi/Keyword.png")
    keyboardLabel = tk.Label(root, image=img)
    keyboardLabel.config(borderwidth=0)
    keyboardLabel.place(relx=0.36, rely=0.595, anchor='center')

    keywords = tk.Entry(root)
    keywordTextBox.create_window(170, 40, window=keywords)

    # link
    linkTextBox = tk.Canvas(root, width=300, height=80,
                            bd=0, highlightthickness=0)
    linkTextBox.place(relx=0.5, rely=0.45, anchor='center')
    linkTextBox.configure(bg="white")
    linkTextBox.config(borderwidth=1)

    img1 = PhotoImage(file="C:/Users/Justi/link.png")
    linkLabel = tk.Label(root, image=img1)
    linkLabel.place(relx=0.365, rely=0.449, anchor='center')
    linkLabel.config(borderwidth=0)

    link = tk.Entry(root)
    linkTextBox.create_window(170, 40, window=link)

    # button
    button1 = tk.Button(text='Get all comments',
                        command=lambda: YoutubeParser(keywords, link))
    imga = PhotoImage(file="C:/Users/Justi/button.png")
    button1.config(image=imga)
    button1.config(borderwidth=0)
    button1.place(relx=0.5, rely=0.75, anchor='s')

    # title
    titleLabel = tk.Label(root, text = "Welcome to the YouTube Comment Parser")
    titleLabel.configure(background = "white")
    titleLabel.config(font=("Helvetica", 15))
    titleLabel.place(relx=0.5, rely=0.3, anchor='center')
    root.mainloop()


if __name__ == "__main__":
    UI()

# TODO:
#   add image - test code copy

# use https://www.youtube.com/watch?v=FSGeskFzE0s as example - jack and rose
