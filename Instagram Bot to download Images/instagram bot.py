#imports here
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget # this is to save the image to your device
import random
import time


#the usename ,password and the profile whose id we want is saved in a variable
uname=input("Enter Insta username : ")
passw=input("Enter insta Password : ")
keyword = input("Enter Insta Id : ")

#the instance of Chrome WebDriver is created
driver = wd.Chrome(executable_path='C:/Users/anany/.wdm/drivers/chromedriver/win32/91.0.4472.101/chromedriver.exe')
driver.get("http://www.instagram.com")

#this is to locate username and input feilds
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))


# this is to clear if any exsisting values are persent
username.clear()

#we are sending keys, this is similar to entering keys from the keyboard
username.send_keys(uname) #"test___113"

# this is to clear if any exsisting values are persent
password.clear()

#we are sending keys, this is similar to entering keys from the keyboard
password.send_keys(passw) #"admin113"

#this is to loacte and click the submit button
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


#this is to click on not now on pop ups
#this one asks to save profile info
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
#this asks to turn on notifications
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()



#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
#clear if any values are present
searchbox.clear()


#this is to search the id whose profile picture we want

searchbox.send_keys(keyword)
keyword=keyword+"'s profile piture"
# Wait for 5 seconds to make sure all profiles are loaded
time.sleep(5)
#this clicks on the top profile
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
#this finally opens the profile
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

# so ids can be private or public class for private is "rkEop" and public is "_6q-tv"
present=False
try:
    driver.find_element_by_class_name("rkEop")
    present = True 
except:
   present = False 

if present:
    images = driver.find_elements_by_css_selector('img[alt="Profile photo"]')
    #checks if The account to be scraped is private or not
    check= driver.find_elements_by_class_name('rkEop')
    
else:
    images = driver.find_elements_by_tag_name('img')
    #checks if The account to be scraped is private or not
    check= driver.find_elements_by_class_name('_6q-tv')   
    print(check)

#images are saved in an array
if  check:        
    images = [image.get_attribute('src') for image in images]
    images = images[:1]
else:
    images = [image.get_attribute('src') for image in images]
    images = images[:-2]


#this part gets the path and folder name
path = os.getcwd()
path = os.path.join(path, keyword[0:] + str(random.randint(1,10000)))
print(path)
#create the directory
os.mkdir(path)

#this part finally downloads and saves the image to the device
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[0:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

# Web diver waits for this much time 

time.sleep(2)

# to close the browser window 

driver.close()