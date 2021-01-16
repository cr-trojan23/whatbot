from selenium import webdriver
import time

firefox_driver = webdriver.Firefox(executable_path="/home/kiaria/Downloads/geckodriver")
firefox_driver.get("https://web.whatsapp.com")

time.sleep(5)
msgs = []
for i in range(11):
    temp = "Test Message " + str(i)
    msgs.append(temp)

contact_name = "sudo apt-get update"
contact_box = firefox_driver.find_element_by_xpath('//span[@title="sudo apt-get update"]')
contact_box.click()

text_box = firefox_driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
for msg in msgs:
    text_box.send_keys(msg)
    time.sleep(2)
    send_button = firefox_driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]')
    send_button.click()