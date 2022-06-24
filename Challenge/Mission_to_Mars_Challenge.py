# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images
# 

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

time.sleep(1)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

#links
links = browser.find_by_css("a.product-item img")

#img_hemi = h_soup.find_all("div", class_="item")
#print(img_hemi[0])
#img_link = img_hemi[0].find('a').get('href')
#print(img_link)


#img_title = h_soup.find_all("h2", class_="title")
#print(img_title)


#img_title = h_soup.find('h2', class_='title')
#img_title = h_soup.find_all("h2", class_ = title)
#print(img_title)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for result in range(len(links)):
    
    #Create dict
    hemispheres = {}
    
    #find elements in each loop
    browser.find_by_css("a.product-item img")[result].click() 
        
    #find image
    image = browser.find_by_text('Sample').first
    hemispheres['image_url'] = image['href']
    
    #Get title for the image
    hemispheres['title'] = browser.find_by_css('h2.title').text
    
    #Add url and title to list
    hemisphere_image_urls.append(hemispheres)
    
    #Navigate back to click on next image
    browser.back()
       


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the browser
browser.quit()





