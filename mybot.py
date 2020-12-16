from selenium import webdriver
import time
import sys
import keyboard

class MyBot:
    def __init__(self, credentials):
        self.CREDENTIALS = credentials
        self.bot = webdriver.Chrome('chromedriver.exe')
        self.bot.get('https://teams.microsoft.com')
        time.sleep(5)

    def Login(self):
        # Inputting email in input box
        email_input = self.bot.find_element_by_xpath('//*[@id="i0116"]')
        email_input.send_keys(self.CREDENTIALS['email'])

        # Clicking Next Button
        btn_next = self.bot.find_element_by_xpath('//*[@id="idSIButton9"]')
        btn_next.click()
        time.sleep(5)

        # Inputting password in input box
        password_input = self.bot.find_element_by_xpath('//*[@id="i0118"]')
        password_input.send_keys(self.CREDENTIALS['password'])

        # Clicking SignIn button
        btn_signIn = self.bot.find_element_by_xpath('//*[@id="idSIButton9"]')
        btn_signIn.click()
        time.sleep(5)

        # Refusing Stay Signed In option
        btn_no = self.bot.find_element_by_xpath('//*[@id="idBtn_Back"]')
        btn_no.click()
        time.sleep(10)

        # Clicking Use Web App instead option
        try:
            btn_useWebApp = self.bot.find_element_by_xpath('//*[@id="download-desktop-page"]/div/a')
            btn_useWebApp.click()
        except:   
            time.sleep(15)

    def getClassSchedule(self):
        try:
            with open('classSchedule.txt') as f:
                schedule_lst = f.read().split('\n')
                return schedule_lst

        except Exception as e:
            print(e)
            sys.exit(1)

    def FindClass(self, class_name):
        available_teams = self.bot.find_elements_by_class_name('name-channel-type')
        
        for team in available_teams:
            if class_name.upper() in team.get_attribute('innerHTML').upper():
                team.click()


    def JoinClass(self):
        self.FindClass('bot testing')
        time.sleep(15)
        # Finding and Clicking Join button
        btn_join = self.bot.find_element_by_xpath('//*[@id="m1608134726965"]/calling-join-button/button')
        btn_join.click()
        time.sleep(2)

        # Blocking Camera and Mic
        for _ in range(2):
            keyboard.send('tab', do_press=True, do_release=True)
            keyboard.send('tab', do_press=True, do_release=True)
            keyboard.send('tab', do_press=True, do_release=True)
            keyboard.send('enter', do_press=True, do_release=True)
            time.sleep(2)

        # Continue without audio
        keyboard.send('tab', do_press=True, do_release=True)
        keyboard.send('enter', do_press=True, do_release=True)
        time.sleep(2)

        # Join 
        keyboard.send('enter', do_press=True, do_release=True)
        print('Class Joined')

        # Leave Class
        time.sleep(20)
        for _ in range(7):
            keyboard.send('tab', do_press=True, do_release=True)
        keyboard.send('enter', do_press=True, do_release=True)



credentials = {'email':'', 'password':''}

# Reading login credentials from text file
with open('credentials.txt') as f:
    content_lst = f.read().split(',')
    credentials['email'] = content_lst[0]
    credentials['password'] = content_lst[1]

if __name__ == '__main__':
    bot = MyBot(credentials)
    bot.Login()
    bot.JoinClass()