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
from tkinter import ttk
from tkinter import Entry
import tkinter as tk
import tkinter.font as font
from tkinter import *
# UI import


def YoutubeParser(keywords, link):

    # if keywords.get() == None or link == None:
    #     root = tk.Tk()
    #     root.title("error")
    #     error_output = tk.Label(root, text = "Either keywords or link not filled out")
    #     error_output.place(relx=0.5, rely=0.5, anchor='center')
    #     tk.mainloop()

    options = Options()
    options.add_argument("--headless")

    keywords = keywords.get()
    keywords = str(keywords).split(' ')
    # Print out each keyword to check what's being checked here.
    with Chrome(options=options) as driver:
        wait = WebDriverWait(driver, 1)
        print("========================")
        driver.get(link.get())

        for item in range(5):  # by increasing the highest range you can get more content
            wait.until(EC.visibility_of_element_located(
                (By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(1)

        root = tk.Tk()
        root.title("ALL Comments")

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
            # Try running without if and just add all.
            if any(temp in comment.text.split(' ') for temp in keywords):
                text = tk.Label(root, text=comment.text)
                text.pack()
                space = tk.Label(
                    root, text="=====================================")
                space.pack()

        root.mainloop()


def UI():
    root = tk.Tk()
    root.title("Youtube Parser Tool")

    init = tk.Canvas(root, width=600, height=600,
                     highlightthickness=5, highlightbackground="gray")
    init.configure(bg='white')
    init.pack()

    # keywords
    keywordTextBox = tk.Canvas(root, width=400, height=300)
    keywordTextBox.place(relx=0.5, rely=0.3, anchor='center')
    keywordTextBox.configure(bg="white")
    keywordTextBox.config(borderwidth=0)

    img = PhotoImage(file="C:/Users/Justi/Keyword.png")
    keyboardLabel = tk.Label(root, image=img)
    keyboardLabel.config(borderwidth=0)
    keyboardLabel.place(relx=0.34, rely=0.4175, anchor='center')

    keywords = tk.Entry(root)
    keywordTextBox.create_window(200, 225, window=keywords)

    # link
    linkTextBox = tk.Canvas(root, width=400, height=200, borderwidth=0)
    linkTextBox.place(relx=0.5, rely=0.75, anchor='center')
    linkTextBox.configure(bg="white")
    linkTextBox.config(borderwidth=0)

    img1 = PhotoImage(file="C:/Users/Justi/link.png")
    linkLabel = tk.Label(root, image=img1)
    linkLabel.place(relx=0.36, rely=0.587, anchor='center')
    linkLabel.config(borderwidth=0)

    link = tk.Entry(root)
    linkTextBox.create_window(200, 0, window=link)

    # button
    button1 = tk.Button(text='Get all comments',
                        command=lambda: YoutubeParser(keywords, link))
    imga = PhotoImage(file="C:/Users/Justi/button.png")
    button1.config(image=imga)
    button1.config(borderwidth=0)
    button1.place(relx=0.5, rely=0.75, anchor='s')

    # title
    titleImg = PhotoImage(file="C:/Users/Justi/title.png")
    titleLabel = tk.Label(root, image=titleImg)
    titleLabel.place(relx=0.5, rely=0.25, anchor='center')
    root.mainloop()


if __name__ == "__main__":
    UI()
