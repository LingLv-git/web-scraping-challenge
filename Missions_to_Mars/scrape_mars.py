#!/usr/bin/env python
# coding: utf-8


from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def scrape_mars():
    
    # ### NASA Mars News

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    latest_news = soup.find_all('div', class_='content_title')[0].text
    latest_p = soup.find_all('div', class_='article_teaser_body')[0].text 
    print(f'The title of the latest new is: {latest_news}.')
    print(f'The paragrah of the latest new is: {latest_p}.')


    # ### JPL Mars Space Images - Featured Image

    url_image = 'https://spaceimages-mars.com'
    browser.visit(url_image)
    html_image = browser.html
    soup_image = BeautifulSoup(html_image, 'html.parser')

    image = soup_image.find_all('img', class_='headerimage fade-in')[0]['src']
    featured_image_url = f'{url_image}/{image}'
    featured_image_url


    # ### Mars Facts

    mars_facts_url = 'https://galaxyfacts-mars.com'
    mars_facts = pd.read_html(mars_facts_url)[1]
    mars_facts

    mars_facts.columns = ['Mars', 'Parameters']
    mars_facts = mars_facts[1:].reset_index(drop=True)
    mars_facts

    mars_fact_html = mars_facts.to_html('mars_fact.html')
    get_ipython().system('open mars_fact.html')


    # ### Mars hemispheres

    mars_hemisphere_url = 'https://marshemispheres.com'
    browser.visit(mars_hemisphere_url)
    mars_hemisphere_html = browser.html
    mars_hemisphere_soup = BeautifulSoup(mars_hemisphere_html, 'html.parser')

    items = mars_hemisphere_soup.find_all('div', class_='item')
    hemisphere_image_url = []

    for item in items:
        image_title = item.h3.text
        image_description = item.p.text
        image_href = item.a['href']
        browser.visit(f'{mars_hemisphere_url}/{image_href}')
        image_html = browser.html
        image_soup = BeautifulSoup(image_html, 'html.parser')
        image_url = image_soup.find('div', class_='wide-image-wrapper').img['src']
        full_image_url = f'{mars_hemisphere_url}/{image_url}'
        d = {'title': image_title, 'img_url': image_url, 'img_descrption': image_description}
        hemisphere_image_url.append(d)
        
    mars = {
        'latest_news': latest_news,
        'latest_paragraph': latest_p,
        'feature_image_url': feature_image_url,
        'mars_facts': mars_fact_html,
        'hemisphere_images': hemisphere_image_url
    
    } 
    
    browser.quit()
    return  mars  

    




