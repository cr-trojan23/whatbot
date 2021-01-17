from selenium import webdriver
import time

firefox_driver = webdriver.Firefox(executable_path="/home/kiaria/Downloads/geckodriver")
firefox_driver.get("https://web.whatsapp.com")

time.sleep(5)
'''
msgs = ["He loves to play basketball.", "He goes to school.", "Does he go to school?", "She writes an e-mail to her best friend.", "He thinks he is very handsome.",
"It usually rains every day here.", "It smells very delicious in the kitchen.", "We generally sing songs all together.", "We go to a gallery every Sunday.",
"Does he write an email?", "The sun rises at the east.", "She goes to work by car.", "It doesn’t rain here in the summer.", "We cook every day.",
"We go to the gym club together.", "You have a big house.", "Do we know each other?", "They sleep in the afternoon.", "When do they usually talk to each other?",
"The children are at home.", "The earth goes round the sun.", "George brushes his teeth twice a day.", "He gets up early every day.", "They speak English in U.S.A.",
"I like reading detective stories.", "I like geography and science.", "She doesn’t study German on Monday.", "Does she live in Paris?", "He doesn’t teach math.",
"Cats hate water.", "Every child likes an icecream.", "My mother never lies.", "The Earth is spherical.", "She doesn’t use a computer.",
"It snows a lot in winter in Russia.", "We live in Texas.", "You go to holiday every summer.", "Do you like spaghetti?", "My daughter does the laundry.",
"My brother takes out the trash.", "The course starts next Sunday.", "She swims every morning.", "I don’t wash the dishes.", "We see them every week.",
"I don’t like tea.", "When does the train usually leave?", "She always forgets her purse.", "You don’t have children.", "I and my sister don’t see each other anymore.",
"They don’t go to school tomorrow.", "She wants to be a dentist.", "Cows eat grass.", "My cat runs very fast.", "She has a beehive full of bees.",
"My son lives in London.", "They don’t have any money.", "She plays basketball.", "He catches the train every morning.", "My sister works at the theater.",
"Michael doesn’t work.", "How often do you see George?", "She doesn’t see Peter every day.", "My boyfriend loves this song.", "My father doesn’t speak good English.",
"He goes to football every day.", "California is not in the United Kingdom.", "The Queen of England livesin Buckingham Palace.", "Julie talks very fast.",
"My brother’s dog barks a lot.", "Does he play tennis?", "The train leaves every morning, at 18 A.M.", "Water freezes at 0°C", "I love my new pets.",
"We drink coffee every morning.", "My Dad never works on the weekends.", "She doesn’t teach chemistry.", "I do love my new pets.",
"Mary brushes her teeth twice a day.", "He drives to work.", "Mary enjoys cooking.", "She likes bananas.", "You don’t listen to me.", "I run four miles every morning.",
"They speak English at work.", "The train does not leave at 12 A.M.", "I have no money at the moment.", "Do they talk a lot ?",
"Tomorrow early morning first I go to morning walk.", "Does she drink coffee?", "You run to the party.", "You have some schoolwork to do.", "Doyou eat ice cream?",
"The train leaves in ten minutes.", "Do pigs like milk?", "California is in America.", "Penguins live in the Antarctica.", "Nurses work in clinics and hospitals.",
"Alex works for 7 hours every day.", "I do not like meat.", "They go to a gallery every Saturday."]
'''
msgs = []
for i in range(101):
    temp = "Hey sheet! here is a test message " + str(i) + "for you"
    msgs.append(temp)

contact_name = "Q1 DS Sheet LL"
contact_box = firefox_driver.find_element_by_xpath('//span[@title="{}"]'.format(contact_name))
contact_box.click()

text_box = firefox_driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
for msg in msgs:
    text_box.send_keys(msg)
    time.sleep(2)
    send_button = firefox_driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]')
    send_button.click()