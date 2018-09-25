from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import datetime
def main():
    if datetime.datetime.now().weekday() == 2:
        print ('Knock Knock')
        ####################################################################
        base = "https://www.sportyhq.com/authentication/login"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.get(base)
        time.sleep(1)
        elem = driver.find_element_by_xpath("//input[@placeholder='Email or Username']")
        elem.send_keys('email')
        time.sleep(random.triangular(1, 3,2))
        elem2 = driver.find_element_by_xpath("//input[@placeholder='Password']")
        elem2.send_keys('password')
        driver.find_element_by_xpath("//*[contains(@class,'btn btn-lg btn-primary btn-block')]").click()
        #driver.find_element_by_css_selector(".btn btn-lg btn-primary btn-block").click()
        ####################################################################
        #court
        date = datetime.datetime.now()
        date = date + datetime.timedelta(days=7)
        date = str(date)[:10]
        court = 'https://www.sportyhq.com/book/index/390/%s' % (date,)
        driver.get(court)
        time.sleep(8)
        ####################################################################  
        courttobook= driver.find_element_by_xpath("//a[contains(@href,'time=19:00:00&club_id=390&club_asset_id=415')]")
        courttobook.click()
        time.sleep(5)
        opponent = driver.find_element_by_xpath("//input[@placeholder='Search for a player']")
        time.sleep(3)
        opponent.send_keys('AName')
        time.sleep(3)
        opponent.send_keys(u'\ue007')
        time.sleep(1)
        driver.find_element_by_css_selector(".btn-primary").click()
        time.sleep(5)
        driver.quit()
    else:
        print ('Bye!')
if __name__ == "__main__":
    main()
