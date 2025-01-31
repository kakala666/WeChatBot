import sys,subprocess,time,socket,configparser,threading,os
from time import sleep
from xml.etree.ElementTree import XMLParser

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def up_data(money:int,url:str):
    chromedriver_path = "./Config/chromedriver.exe"

    # 设置 Chrome 浏览器选项
    chrome_options = Options()
    # chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--headless")  # 设置无头模式

    # Setup Chrome options
    # chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument(r'--user-data-dir=C:\Users\byby4\AppData\Local\Google\Chrome\User Data')  # 指定用户数据目录
    # 初始化 WebDriver
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)
    driver.get('https://console.cli.im/center?activeTab=code')
    driver.implicitly_wait(10)
    M_list = []
    father = driver.find_element(By.XPATH, '//*[@id="recentUpdateBlock"]/div/div[2]/div[1]/div[2]')
    for i in range(1, 5):
        M_list.append([father.find_element(By.XPATH, f'.//div[{i}]/div[2]/div[2]/div[1]/div[1]/div/p').text,
                       father.find_element(By.XPATH,f'.//div[{i}]/div[2]/div[2]/div[1]/div[2]/span[2]/i')])
    for i in range(4):
        print(M_list[i])
    for i,j in M_list:
        if i == str(money):
            j.click()
            sleep(1.5)
            windows = driver.window_handles

            # 切换到新打开的窗口
            driver.switch_to.window(windows[-1])

            # 在新窗口中进行操作
            # 例如，获取页面标题
            print(driver.title)
            sleep(0.2)
            url_text = driver.find_element(By.XPATH,'//*[@id="jump_url"]')
            url_text.clear()
            url_text.send_keys(url)
            sleep(0.1)
            updata = driver.find_element(By.XPATH,'//*[@id="save_btn"]')
            updata.click()
            sleep(1)


