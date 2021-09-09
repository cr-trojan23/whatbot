from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import platform as _platform

# check the operating system
gecko = ""
if _platform == "linux" or _platform == "linux2":
    gecko = "./geckos/geckodriver_linux"
elif _platform == "darwin":
    gecko = "./geckos/geckodriver_mac"
elif _platform == "win32":
    gecko = "./geckos/geckodriver_win32.exe"
elif _platform == "win64":
    gecko = "./geckos/geckodriver_win64.exe"

# create a new instance of the Firefox driver
firefox_driver = webdriver.Firefox(executable_path=gecko)

# open whatsapp web
firefox_driver.get("https://web.whatsapp.com")

# get the xpath of the text box
text_box = firefox_driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')

# message to send
msg = input("enter message to be spammed\n")

# number of times to send the message
for i in range(int(input("enter number of msgs to be spammed\n"))):

    # enter the message in the text box
    text_box.send_keys(msg)

    # press enter
    text_box.send_keys(Keys.ENTER)