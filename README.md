# **YouTube Comment Parser**
### **Welcome to the Youtube comment parser**

The point of this project is to let content creators on Youtube to gather ideas and opinion from their personal fanbase from their video's comment section. Using the following steps, you will be able to get all the comments that contains the keyword of your choice!

## **How to use:**
1. Select the video that you would like to use the parser on.
2. Copy (Ctrl + c) the video link on the top of the browser.
3. Run the Python program and paste the video link in the box labeled "link".
4. Enter the Keywords that you would like to search by. (Make sure to leave no trailing spaces at the end of your key words list)
5. Press the red "Get All Comments" button and another window should pop up with all the comments containing the keywords along side with the Username and Profile photo!

***This section of code here repressents the loop that goes through each comment:***
```
for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
    if any(temp in comment.text for temp in keywords):
        text = tk.Label(root, text = comment.text)
        text.pack()
        space.pack()
```

