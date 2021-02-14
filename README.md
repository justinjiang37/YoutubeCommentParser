# **YouTube Comment Parser**
### **Welcome to the Youtube comment parser**

The point of this project is to let content creators on Youtube to gather ideas and opinion from their personal fanbase from their video's comment section. Using the following steps, you will be able to get all the comments that contains the keyword of your choice!

## **How to use:**
1. Select the video that you would like to use the parser on.
2. Copy (Ctrl + c) the video link on the top of the browser.
3. Run the Python program and paste the video link in the box labeled "link".
4. Enter the Keywords (ALL IN LOWERCASE) that you would like to search by with a space in between each word. (Make sure to leave no trailing spaces at the end of your key words list)

5. Press the red "Get All Comments" button and another window should pop up with all the comments containing the keywords along side with the Username and Profile photo!

***This section of code here repressents the loop that goes through each comment:***
```
        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
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
                temp_comment = comment.text
                for i in range(len(temp_comment)):
                    if i % 65 == 0:
                        temp_comment = temp_comment[:i] + "\n" + temp_comment[i:]
                text = tk.Label(OutPut_Frame_2, text=temp_comment)
                text.pack()
                space = tk.Label(
                    OutPut_Frame_2, text="=====================================")
                space.pack()
```

