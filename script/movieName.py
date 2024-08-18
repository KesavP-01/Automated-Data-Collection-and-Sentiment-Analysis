import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import random


proxies = ['74.208.177.198:80', '162.223.91.11:80', '43.157.8.79:8888', '41.204.63.118:80',
           '85.105.20.121:6563', '211.226.174.45:8080']

def getMovieNames(url):
    proxy = random.choice(proxies)
    options = webdriver.ChromeOptions()
    options.add_argument(f'--proxy-server = {proxy}')


    driver = webdriver.Chrome(options=options)
    driver.get(url)
    name= driver.find_elements(By.XPATH, '//div[@class="ipc-metadata-list-summary-item__c"]/div/div/div/a/h3')
    code = driver.find_elements(By.XPATH, '//div[@class="ipc-metadata-list-summary-item__c"]/div/div/div/a')

    name_list = []
    code_list = []
    final_data = {}
    for n in name:
        Name = n.get_attribute('innerHTML').split('.')[1]
        name_list.append(Name)
    for c in code:
        codes = c.get_attribute("href")[27:36]
        code_list.append(codes)
    final_data = pd.DataFrame({
        'Name' : name_list,
        'Movie_Code' : code_list})
    driver.quit()
    final_data.to_csv('data/movieNames.csv', index=False)
    return final_data

if __name__ == "__main__":
    getMovieNames('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

