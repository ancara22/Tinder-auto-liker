from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


MY_EMAIL = "*******"
MY_PASS = "*****"

chrome_driver_path = "/Users/dinisbarcari/Documents/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get("https://tinder.onelink.me/9K8a/3d4abb81")

sleep(3)
b3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
b3.click()

login = driver.find_element(By.XPATH, '//*[@id="t-831228276"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
login.click()

f_window = driver.window_handles[1]
driver.switch_to.window(f_window)

sleep(2)
fb_login = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]')
fb_login.click()

email = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
passw = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
email.send_keys(MY_EMAIL)
passw.send_keys(MY_PASS)
passw.send_keys(Keys.ENTER)


sleep(7)
driver.switch_to.window(driver.window_handles[0])
b1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
b1.click()
b2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
b2.click()

sleep(7)
b4 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/button[2]/span')
b4.click()

sleep(2)
like1 = driver.find_element(By.XPATH,
                           '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
like1.click()

for n in range(30):
    try:
        sleep(2)
        like2 = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like2.click()
    except:
        b5 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button[2]')
        b5.click()




# driver.quit()



