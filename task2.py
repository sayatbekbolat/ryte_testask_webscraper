import os
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import pandas as pd


def scrap_website(base_link: str, pages_num: int, columns: list) -> pd.DataFrame: 
    """Return scrapped data from a website

    Parameters
    ----------
    base_link : str
        The main link where web scrapping starts
    pages_num : int
        The number of pages needed to scrap
    columns : List[str]
        The names dataframe columns
        
    """
    

    chrome_path = "utl/chromedriver"
    driver = webdriver.Chrome(chrome_path)

    df = pd.DataFrame(
            columns = columns
            )

    for i in range(pages_num):
        driver.get(base_link+str(i+1))
        time.sleep(1)
        article_list = driver.find_element_by_id('new-article-list')
        articles = article_list.find_elements_by_class_name('app-article-list-row__item')

        for article in articles:
            date  = article.find_elements_by_class_name('c-meta__item.c-meta__item--block-at-lg')[-1].get_attribute('datetime')
            topic_name = article.find_element_by_class_name('c-card__title').text
            topic_link = article.find_element_by_class_name('c-card__link.u-link-inherit').get_attribute('href')
            
            try: 
                desc = article.find_element_by_class_name('c-card__summary.u-mb-16.u-hide-sm-max').text
            except NoSuchElementException:
                desc = None

            auth_list = article.find_element_by_class_name('c-author-list.c-author-list--compact.u-mb-4.u-mt-auto')
            authors = [auth.text for auth in auth_list.find_elements_by_tag_name('li')]
            authors = ", ".join(authors)

            # print(date, topic_name, topic_link, desc, authors)
            
            df.loc[df.shape[0]+1] = [
                date, 
                topic_name, 
                topic_link, 
                desc, 
                authors
                ]
        
    driver.close()

    return df 


if __name__ == "__main__":
    base_link = 'https://www.nature.com/nature/research-articles?searchType=journalSearch&sort=PubDate&page='
    result_dir = 'results'
    columns = [
        'date', 
        'topic_name', 
        'topic_url', 
        'description', 
        'authors'
    ]

    df = scrap_website(base_link, 3, columns)
    df.to_csv(os.path.join(result_dir, 'task2_output.csv'), index=None)

