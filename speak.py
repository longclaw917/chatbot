from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--log-level-3')
chrome_options.headless=True
path = "C:\\Users\\dhruba jyoti ghosh\\PycharmProjects\\AIProject\\driver\\chromedriver.exe"
driver=webdriver.Chrome(path,options=chrome_options)
driver.maximize_window()

website = f"https://ttsmp3.com/"

driver.get(website)
buttonselection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
buttonselection.select_by_visible_text('British English / Brian')

def tell(text):
    # print("")
    # print(f"Ai : {text}")
    # print("")
    data = str(text)
    xpathtxa = '/html/body/div[4]/div[2]/form/textarea'
    driver.find_element(by=By.XPATH,value=xpathtxa).send_keys(data)
    driver.find_element(by=By.XPATH,value='//*[@id="vorlesenbutton"]').click()
    driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()
    sleep(2)

