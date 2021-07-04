import datetime as d
from selenium import webdriver
import time as t
import Users as u
driver = webdriver.Firefox()#Calls Firefox
driver.get('http://web.whatsapp.com')#Call WebWhatsapp
print('Please Scan the QR Code and press enter')
input()#Pause To scan QR Code
while True:
    user=u.Users()
    register=driver.find_elements_by_class_name("OUeyt")# The green dot tells us that the message is new
    date=d.date.today().isoformat()#Register Date and Time Of Entering And Leaving Bot
    if len(register) > 0:
        ele = register[-1]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(ele, 0, -20)# move a bit to the left from the green dot
        # Clicking couple of times because sometimes whatsapp web responds after two clicks
        try:
            action.click()
            action.perform()
            action.click()
            action.perform()
        except Exception as e:
            pass
        try:
            name = driver.find_element_by_class_name("_16vzP").text #Name Of Contact/Group
            message = driver.find_elements_by_class_name("vW7d1")[-1].text.lower()# Last Message Recieved
            if 'garbage.exe' in message.lower():#To Summon Bot To A Chat
                if name not in user:#New User
                    u.ArriveUser(name,date)
                    textbox = driver.find_element_by_class_name("_2S1VP")
                    response='Hello, This Is Garbage, Thank You For Calling Me, '+name+'. If you need help, Say "!help", If you want me to leave say "bye garb" and please no enter keys(\\n)\n'
                    textbox.send_keys(response)
                    pass
                elif name in user and 'false' in user[name].lower():#Old User
                    u.ArriveUser(name,date)
                    textbox = driver.find_element_by_class_name("_2S1VP")
                    response='Hello, This Is Garbage, Thank You For Calling Me Again, '+name+'. If you need help, Say "!help", If you want me to leave say "bye garb" and please no enter keys(\\n)\n'
                    textbox.send_keys(response)
                    pass
                else:#Already In Chat
                    textbox = driver.find_element_by_class_name("_2S1VP")
                    response='I am already here\n'
                    textbox.send_keys(response)
                    pass
            if name in user:#Commands
                assert '\n' in message, 'Please No \\n(Enter Key)'#Sometimes, The Bot Errors Out With '\n' keys
                textbox = driver.find_element_by_class_name("_2S1VP")
                #Here you add an if Condition and then code the basic code for the system
                #Conside Importing Them As Libraries
                #and putting the if condition and call the function
                #My Thoughts Anyway
                if '!help' in message.lower():#For Interface Help
                    response='Commands:\n'
                    textbox.send_keys(response)
                    pass
                if 'bye garb' in message.lower():#For Bot To Leave
                    response='Goodbye\n'
                    textbox.send_keys(response)
                    u.LeaveUser(name,date)
                if 'killswitch' in message.lower():#Developer Emergency Kill(Not Offical Command In Help[I don't advice putting there])
                    break
        except Exception as e:#Sends Error To Both IDLE and Users
            print (e)
            textbox = driver.find_element_by_class_name("_2S1VP")
            response=str(e)[0].upper()+str(e)[1:]+'\n'
            textbox.send_keys(response)
        t.sleep(1)