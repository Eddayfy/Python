from selenium import webdriver
import time
import os

# fi blasst "geckodriver.exe" ktb 'path' dyal "geckodriver.exe" li m3a had fichier.
driver = webdriver.Firefox(executable_path=r"geckodriver.exe")

# fi had list ktb smiyat dyal nass li baghi tssifat lihoum lmessage.
NameList = ["Name1","Name2","Name3"]

# fi had variable ktb lmessage li baghi tsiftou.
UserMessage = "Put your message here."

try:
    driver.get("https://web.whatsapp.com")
    input("Scan QR Code, And then click Enter: ")
except:
    print("Erore on ScanQRcode Tap")

# had loop ghada tb9a khdama hta tssifat lmessagat lga3 smiyat li dakhalti fi list.
for Name in NameList:
    SearchTextBox = driver.find_element_by_class_name('_3FRCZ')
    SearchTextBox.send_keys("")
    SearchTextBox.send_keys(Name)
    time.sleep(5)
    UserBox = driver.find_element_by_xpath('//span[@title = "{}"]'.format(Name))
    UserBox.click()
    time.sleep(2)

    try:
        MessageTextBox = driver.find_elements_by_class_name('_3FRCZ')
        MessageTextBox[1].send_keys("")
        MessageTextBox[1].send_keys(UserMessage)
        time.sleep(2)
        driver.find_element_by_class_name("_1U1xa").click()
        print(Name,"received the message.")
    except:
        print("Erore on SendTheMessage Tap, for: ",Name)

print("Done!")
#driver.quit()
