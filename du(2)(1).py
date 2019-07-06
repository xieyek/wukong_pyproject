import random

from selenium import webdriver
import time
import os
from selenium.webdriver.support.select import Select
driver=webdriver.Firefox()
driver.get('https://vip6.99xbgg.com/?s=/WebPublic/login')
time.sleep(2)
driver.find_element_by_id('user_account').send_keys('991491658')
driver.find_element_by_id('user_password').send_keys()
# driver.maximize_window()
# driver.save_screenshot(r'C:\test\aa.png')
# img=driver.find_element_by_id('captcha_img')
# location=img.location
# size=img.size
# png=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
# i=Image.open(r'C:\test\aa.png')
# i1=i.crop(png)
# i1.save(r'C:\test\bb.png')
# i2=Image.open(r'C:\test\bb.png')
# text=pytesseract.image_to_string(i2)
# print(text)
# driver.find_element_by_id('captcha').send_keys(text)
time.sleep(15)
driver.find_element_by_id('submit').click()
time.sleep(5)
windows=driver.window_handles
driver.switch_to.window(windows[0])

# driver.find_element_by_class_name('provision-agree-btn').click()
driver.find_element_by_css_selector('.provision-agree-btn').click()
time.sleep(5)
driver.find_element_by_class_name('close').click()

time.sleep(3)
windows=driver.window_handles
driver.switch_to.window(windows[0])
driver.find_element_by_css_selector('.icon-menu-1').click()
time.sleep(2)
driver.find_element_by_css_selector('.lottery-game > li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)').click()
time.sleep(5)
windows=driver.window_handles
driver.switch_to.window(windows[0])
driver.find_element_by_css_selector('#index-menu > li:nth-child(6) > a:nth-child(1)').click()
time.sleep(5)
driver.find_element_by_css_selector('#show_hid_font').click()
time.sleep(5)
#刷新
while 1==1:
    try:
        driver.find_element_by_css_selector('.uil-reload').click()
        time.sleep(1)
        money=driver.find_element_by_css_selector('#header_lottery_balance').text
        print(money)
        # a = random.randint(1, 5)
        a = random.randint(0, 1)
        if a == 0:
            b = random.randrange(3, 9, 3)
        if a == 1:
            b = random.randrange(1, 7, 3)
        b += 1
        d=[1,2,5]
        for i in d:
            print('****************')
            a = random.randint(0, 1)
            if a == 0:
                b = random.randrange(3, 9, 3)
            if a == 1:
                b = random.randrange(1, 7, 3)
            b += 1
            print(b)
            driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div[4]/div/div/div[1]/div[3]/span[%r]/i'%b).click()
            driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div[4]/div/div/div[2]/div[3]/span[%r]/i' % b).click()
            driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div[4]/div/div/div[3]/div[3]/span[%r]/i' % b).click()
            driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div[4]/div/div/div[4]/div[3]/span[%r]/i' % b).click()
            driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div[2]/div[4]/div/div/div[5]/div[3]/span[%r]/i' % b).click()

            se=driver.find_element_by_css_selector('#bet_mode')
            Select(se).select_by_index(2)
            t=driver.find_element_by_css_selector('#bet_multi')
            t.clear()
            t.send_keys(i)
            driver.find_element_by_css_selector('a.play-now-btn:nth-child(2)').click()
            time.sleep(3)
            driver.find_element_by_css_selector('.btn-default').click()
            time.sleep(50)
            driver.find_element_by_css_selector('.uil-reload').click()
            time.sleep(1)
            money1=driver.find_element_by_css_selector('#header_lottery_balance').text
            print(money1)
            if money1>money:
                print('----------')
                break
        print('///////////////////')
        time.sleep(59)
    except Exception as a:
        print(a)


# /html/body/div[5]/section/div/div/div[2]/div[4]/div/div/div[1]/div[4]/a[2]
# /html/body/div[5]/section/div/div/div[2]/div[4]/div/div/div[1]/div[4]/a[3]
# /html/body/div[5]/section/div/div/div[2]/div[4]/div/div/div[2]/div[4]/a[2]
# /html/body/div[5]/section/div/div/div[2]/div[4]/div/div/div[3]/div[4]/a[2]

# driver.find_element_by_xpath('/html/body/div[5]/div[1]/header/div[1]/div/div[2]/div/div/nav/div/div[2]/ul[2]/li[1]/ul/li/div/div/div/div[1]/div[2]/ul/li[2]/a')
# driver.close()


