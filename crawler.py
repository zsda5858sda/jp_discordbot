from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import datetime
import time
from news import News
import logging
import os

logger = logging.getLogger(__name__)
def get_title(news):
    _title = news.find_element(By.TAG_NAME, "h2")
    return _title.text.replace("\n", "")

def get_url(news):
    _url = news.find_element(By.TAG_NAME, "a")
    return _url.get_attribute("href")

def get_time(news):
    _time = news.find_element(By.TAG_NAME, "time")
    return datetime.datetime.strptime(_time.get_attribute('datetime'), '%Y-%m-%d %H:%M:%S')

def read_file():
    f = open("news.txt", 'r', encoding='utf-8')
    previos_news = f.read().split(',')
    f.close()
    return previos_news

def write_file(s):
    f = open("news.txt", 'w', encoding='utf-8')
    f.write(s)
    f.close()

def start_crawler():
    if not os.path.exists('news.txt'):
        open("news.txt", "x")

    previos_news = read_file()
    logger.info("開始爬蟲")

    options = Options()
    options.add_argument("-inprivate")
    options.add_argument("--headless")
    #create chrome driver
    driver = webdriver.Edge(options=options)
    driver.get("https://www3.nhk.or.jp/news/easy/")
    time.sleep(3)
    driver.execute_script("""
        var rt = document.getElementsByTagName('rt');
        while(rt.length > 10) {
            rt[0].remove();
        }
    """)
    news_list = driver.find_elements(By.CLASS_NAME, "news-list__item")

    results = []
    for news in news_list:
        news_title = get_title(news)
        if news_title in previos_news:
            break
        previos_news.append(news_title)

        news_url = get_url(news)
        news_time = get_time(news)
    
        news = News(news_title, news_url, news_time)
        results.append(news)
    
    logger.info("爬蟲結束，回傳文章")
    write_file(','.join(previos_news))
    return results