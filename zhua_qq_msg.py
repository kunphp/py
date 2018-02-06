# -*- coding: utf-8 -*-
# @Author: Wykun
# @Date:   2018-02-02 11:06:14
# @Last Modified by:   Wykun
# @Last Modified time: 2018-02-06 17:01:31
# 抓取QQ空间留言
from bs4 import BeautifulSoup
from selenium import webdriver
import time
# 使用selenium
driver = webdriver.Chrome()
driver.maximize_window()

# 传入QQ，需要抓取留言的页数
def get_words(qq,npage=5):
    driver.get('https://user.qzone.qq.com/{}/334'.format(qq))
    time.sleep(3)
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if(a == True):
        driver.switch_to.frame('login_frame')
        # 1、电脑没有登录自己QQ时
        # driver.find_element_by_id('switcher_plogin').click()
        # driver.find_element_by_id('u').clear()#选择用户名框
        # driver.find_element_by_id('u').send_keys({QQ号})
        # driver.find_element_by_id('p').clear()
        # driver.find_element_by_id('p').send_keys({QQ密码})
        # driver.find_element_by_id('login_button').click()
        # 2、电脑已登录QQ时换成快捷登录直接点击
        driver.find_element_by_id('img_out_自己的QQ').click()

        time.sleep(4)
    driver.switch_to.frame('tgb')
    driver.implicitly_wait(4)
    num = 1
    while (num < npage):
        num += 1
        time.sleep(3)
        menu = driver.find_element_by_id('ulCommentList')
        logToFile(menu.text)
        p = 'QZBlog.Util.PageIndexManager.goDirectPage('+str(num)+')'
        driver.execute_script(p+';return false;')
    if num == npage:
        time.sleep(2)
        memu = driver.find_element_by_id('ulCommentList')
        logToFile(memu.text)

    driver.close()
    driver.quit()
# 读取内容写入文件
def logToFile(content,name='menu.txt'):
    f = open(name,'a+',encoding='utf8')
    try:
        print(content)
        f.write(content+'\n')
    except:
        print('error1')
    finally:
        f.close()


if __name__ == '__main__':
    get_words('好友QQ',20)
