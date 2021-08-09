from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
firefox_driver = webdriver.Firefox(executable_path="/home/kiaria/Documents/github_projects/whatbot/geckodriver")
firefox_driver.get("https://web.whatsapp.com")

input()
text_box = firefox_driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
for i in range(2001):
    msg = "enter spam text here"
    text_box.send_keys(msg)
    text_box.send_keys(Keys.ENTER)
    #time.sleep(2)