# AUTHOR: RITESH PRAMANIK
# IMPORTING ALL REQUIRED PACKAGES
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from getpass4 import getpass
# THIS IS THE TEXT MESSAGE WHICH IS GOING TO SEND TO THE TARGETED PEOPLE
msg = "Hi!\nI'm a bot programmed by Ritesh Pramanik. I send messages to particular people. This was a demonstration of my functionality. Thank you.\nGood Night!"
count = int(input("Enter number of friends: ")) # ENTER THE NUMBER OF PEOPLE YOU WANT TO SEND THIS MESSAGE
friends = []
for i in range(count):
    friend = input("Enter name: ")  # IT WILL PROMPT TO YOU TO ENTER THE USERNAMES OF THE RECEIVERS
    friends.append(friend)
print(friends)
browser = webdriver.Chrome(ChromeDriverManager().install())  # THIS LINE DOWNLOAD CHROME DRIVER EACH TIME
password = 'xyz'  # WRITE YOUR INSTA ACCOUNT PASSWORD 
browser.get('https://www.instagram.com/')  # THIS LINE CREATE A REQUEST FOR INSTAGRAM LOGIN PAGE
time.sleep(3)
browser.find_element(By.NAME, 'username').send_keys('xyz')  # YOUR USERNAME
browser.find_element(By.NAME, 'password').send_keys(password)
browser.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
# browser.find_element(By.CLASS_NAME, '_acan _acap _acas _aj1-').click()
time.sleep(5)
# CLICK YOUR PROFILE VIEW ICON
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a/div/div[1]/div/div').click() 
time.sleep(7)
# CLICK TO THE MESSANGER ICON
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div/div[1]/div/div').click()
time.sleep(5)
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[3]/div/button').click()
time.sleep(3)
# SEARCH FOR ENTERED USERNAME AND SELECT THEM FOR SENDING MESSAGES
for friend in friends:    
    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys(friend)
    time.sleep(5)
    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button').click()
    time.sleep(5)
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button').click()
time.sleep(5)
# TYPE THE DESIRED MESSAGE IN THE TEXT SECTION
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(msg)
# SEND THE MESSAGE
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(Keys.RETURN)
time.sleep(5)