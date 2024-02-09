from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os,threading,csv

def get_list(newsList):
    contents = []
    for idx,news in enumerate(newsList):
        link=news.find_element(By.XPATH,f'//*[@id="news_List"]/ul/li[{idx+1}]/a').get_attribute('href')
        img = news.find_element(By.XPATH, f'//*[@id="news_List"]/ul/li[{idx+1}]/a/div[1]/img').get_attribute('src')
        title = news.find_element(By.XPATH, f'//*[@id="news_List"]/ul/li[{idx+1}]/a/div[2]/h3').get_attribute('textContent')
        summary = news.find_element(By.XPATH, f'//*[@id="news_List"]/ul/li[{idx+1}]/a/div[2]/p').get_attribute('textContent')
        content = {'img': img, 'title': title, 'summary': summary,'link':link}
        contents.append(content)
        print(link)
    print(contents)
    return contents
def save_csv(contents):
    csv_folder_path=os.path.join(os.getcwd(),'csv')
    filename = 'corona19.csv'
    if not os.path.isdir(csv_folder_path):
        os.mkdir('csv')
    contents_csv=[]
    col=['이미지','제목','요약','링크']
    for content in contents:
        content_csv={}
        for idx,(key,value) in enumerate(content.items()):
            content_csv[col[idx]]=value
        contents_csv.append(content_csv)
    with open(os.path.join(csv_folder_path,filename),'w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=col)
        writer.writeheader()
        writer.writerows(contents_csv)

def crawling(args):
    driver=None
    try:
        driver_path=f'{os.path.join(os.path.dirname(__file__),"chromedriver.exe")}'
        service = Service(executable_path=driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1920x1080')
        options.add_argument(
            'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/120.0.0.0 Safari/537.36')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://mediahub.seoul.go.kr/corona19/news/keywordNewsList.do')

        category=args['category']
        if category:
            if category=='8':
                driver.find_element(By.CSS_SELECTOR,'#content > div > div.news_cate > div > button.slick-next.slick-arrow').click()
                driver.implicitly_wait(2)
            path='#content > div > div.news_cate > div > div > div > div '
            category_ec=EC.presence_of_all_elements_located((By.CSS_SELECTOR,path))
            category_btns=WebDriverWait(driver, 10).until(category_ec)
            driver.execute_script(f'arguments[0].ariaHidden="false";arguments[0].style.display="inline-block";',category_btns[int(category)-1])
            category_btns[int(category)-1].click()

        content_xpath='#news_List > ul > li'
        # newsList = driver.find_elements(By.XPATH,content_xpath)
        newsList=WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, content_xpath)))
        contents=get_list(newsList)
        thread = threading.Thread(target=save_csv,args=(contents,))
        thread.start()
        return contents
    except Exception as e:
        print(e)
        return contents
    finally:
        if driver:
            driver.quit()

