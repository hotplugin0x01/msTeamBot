from selenium import webdriver
import time
import sys

class MyBot:
    # def __init__(self, credentials):
    #     self.CREDENTIALS = credentials
    #     self.bot = webdriver.Chrome('chromedriver.exe')
    #     self.bot.get('https://teams.microsoft.com')
    #     time.sleep(5)

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
        time.sleep(5)

        # Clicking Use Web App instead option
        btn_useWebApp = self.bot.find_element_by_xpath('//*[@id="download-desktop-page"]/div/a')
        btn_useWebApp.click()

    def getClassSchedule(self):
        try:
            with open('classSchedule.txt') as f:
                schedule_lst = f.read().split('\n')
                return schedule_lst

        except Exception as e:
            print(e)
            sys.exit(1)
            


credentials = {'email':'', 'password':''}

# Reading login credentials from text file
with open('credentials.txt') as f:
    content_lst = f.read().split(',')
    credentials['email'] = content_lst[0]
    credentials['password'] = content_lst[1]

if __name__ == '__main__':
    # bot = MyBot(credentials)
    bot = MyBot()
    bot.getClassSchedule()
    # bot.Login()