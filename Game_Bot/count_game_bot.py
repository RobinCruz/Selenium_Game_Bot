'''
This is a bot for the game that i came across in github and thought would be fun to make a bot for it!
This game is to click numbers from 1 to 30 which are randomly positioned in a 6x5 grid in the fastest possible time.
'''
try:
        from selenium import webdriver
        import time
        class game_bot():
                def __init__(self):
                        self.driver = webdriver.Chrome("C:/Users/robin/Downloads/chromedriver_win32/chromedriver.exe")
                        self.driver.get("https://bkspurgeon.github.io/numberCounter/")

                def start_game(self):
                        i = 1
                        while(i<=30):
                                start_bot = self.driver.find_element_by_xpath("//button[text()='{}']".format(i))
                                start_bot.click()
                                time.sleep(0.001)
                                i = i+1
                        
                
        Bot = game_bot()
        time.sleep(1)
        Bot.start_game()
        Bot.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
except:
        print("Download Chrome Driver \nInstall Selenium \nVerify Driver Location in the code")
        
