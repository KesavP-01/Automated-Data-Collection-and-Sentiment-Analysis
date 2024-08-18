import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from scrapy.selector import Selector
import random
from dataPrep import loadData, mergeDict, processDF

proxies = ['74.208.177.198:80', '162.223.91.11:80', '43.157.8.79:8888', '41.204.63.118:80',
           '85.105.20.121:6563', '211.226.174.45:8080']

def getReviews(df):
    rating_list = []
    reviews_list = []
    reviews_df = {}
    code_list = df
    for code in code_list:
        url = "https://www.imdb.com/title/{}/reviews/?ref_=tt_ql_2".format(code)
        proxy = random.choice(proxies)
        options = webdriver.ChromeOptions()
        options.add_argument(f'--proxy-server = {proxy}')
        driver2 = webdriver.Chrome(options = options)
        driver2.get(url)
        count_reviews = driver2.find_element(By.XPATH, '//div[@class="lister"]/div/div/span')
        count = count_reviews.get_attribute('innerHTML').replace(',', '').split(' ')[0]
        clicks = round(int(int(count)/25))
        i=1
        while i < clicks:
            try:
                driver2.find_element(By.ID, 'load-more-trigger').click()
                i=i+1
            except:
                pass
        reviews = driver2.find_elements(By.CSS_SELECTOR, 'div.review-container')
        
        for r in reviews:
            sel = Selector(text= r.get_attribute('innerHTML'))
            try:
                ratings = sel.css('.rating-other-user-rating span::text').extract_first()
            except:
                ratings = np.nan
            try:
                review = sel.css('.text.show-more__control::text').extract_first()
            except:
                review = np.nan
            rating_list.append(ratings)
            reviews_list.append(review)
        reviews_df[code] = pd.DataFrame({
        'Rating': rating_list,
        'Review': reviews_list})
    driver2.quit()
    return reviews_df

if __name__ == "__main__":

    movies = loadData("data/movieNames.csv")
    movieTitles = movies['Movie_Code'].tolist()

    reviews = getReviews(movieTitles)
    movieReviews = mergeDict(reviews)

    reviews = loadData(movieReviews)

    reviews.to_csv('data/movieReviews.csv', index=False)