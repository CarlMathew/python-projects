from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service("Users\Carlito\Desktop\ProgramThesis\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
grandma = 0
factory = 0
while True:
    clicker1 = driver.find_element(By.ID, "buyGrandma")
    clicker2 = driver.find_element(By.ID, "buyFactory")
    price1 = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
    price_grandma = int(price1.text.split(" ")[2])
    price2 = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
    price_factory = int(price2.text.split(" ")[2])
    money = int(driver.find_element(By.ID, "money").text)
    print(money)
    clicker = driver.find_element(By.ID, "cookie")
    clicker.click()
    if money >= price_grandma and grandma <= 4:
        print(price_grandma)
        clicker1.click()
        grandma += 1
    elif money >= price_factory and factory <= 5:
        clicker2.click()
        factory += 1





