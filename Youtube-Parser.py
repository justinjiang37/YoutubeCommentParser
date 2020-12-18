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

import tkinter as tk
import tkinter.font as font
# UI import

def YoutubeParser (keywords, link):

    # if keywords.get() == None or link == None:
    #     root = tk.Tk()
    #     root.title("error")
    #     error_output = tk.Label(root, text = "Either keywords or link not filled out")
    #     error_output.place(relx=0.5, rely=0.5, anchor='center')
    #     tk.mainloop()

    options = Options()
    # options.add_argument("--headless")

    keywords = keywords.get()
    keywords = str(keywords).split(' ')
    with Chrome(options = options) as driver:
        wait = WebDriverWait(driver, 1)
        print("========================")
        # print(link.get())
        # driver = webdriver.Chrome()
        driver.get(link.get())
        # assert "Python" in driver.title

        for item in range(5): #by increasing the highest range you can get more content
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(1)

        # print(keywords)

        root = tk.Tk()
        root.title("ALL Comments")

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
            if any(temp in comment.text for temp in keywords):
                text = tk.Label(root, text = comment.text)
                text.pack()
                # print(comment.text)
                # print("")

        root.mainloop()


def UI():
    root = tk.Tk()
    root.title("Youtube Parser Tool")
    init = tk.Canvas(root, width=600, height=600)

    init.pack()

    #keywords
    keywordTextBox = tk.Canvas(root, width = 400, height = 300)
    keywordTextBox.place(relx=0.5, rely=0.3, anchor='center')

    keyboardLabel = tk.Label(root, text = "Keywords")
    keyboardLabel.config(font=("Courier bold", 13))
    keyboardLabel.place(relx=0.325, rely=0.4165, anchor='center')

    keywords = tk.Entry(root)
    keywordTextBox.create_window(200, 225, window = keywords)

    #link
    linkTextBox = tk.Canvas(root, width = 400, height = 300)
    linkTextBox.place(relx=0.5, rely=0.85, anchor='center')

    linkLabel = tk.Label(root, text = "Link")
    linkLabel.config(font=("Courier bold", 13))
    linkLabel.place(relx=0.35, rely=0.6, anchor='center')

    link = tk.Entry(root)
    linkTextBox.create_window(200, 0, window = link)

    #button
    button1 = tk.Button(text='Get all comments', command=lambda : YoutubeParser(keywords, link))
    button1.config(font=("Courier bold", 13, 'bold', 'underline'))
    button1.config(height = 2, width = 15)
    button1.config(foreground = 'red')
    button1.place(relx=0.5, rely=0.75, anchor='s')

    #title
    titleLabel = tk.Label(root, text="Welcome To The Youtube Comment Parser!")
    titleLabel.config(font=("Courier bold", 15))
    titleLabel.place(relx=0.5, rely=0.25, anchor='center')


    root.mainloop()

if __name__ == "__main__":
    UI()