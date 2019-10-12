from selenium import webdriver
from time import sleep
import pytesseract






def write(a):
    t = 3
    browser.find_element_by_xpath('//a[text()="个人中心"]').click()
    print('成功进入个人中心')
    sleep(t)
    browser.find_element_by_xpath('//*[@id="user_main"]/div/div[2]/div[2]/div[2]/ul/li/a').click()
    print('成功进入班级')

    sleep(t)
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])
    sleep(t)
    browser.find_element_by_xpath('//*[@id="sm_header"]/div/div[2]/ul/li[1]').click()
    print('成功进入首页')
    sleep(t)
    browser.find_element_by_xpath('//*[@id="sm_center"]/div[1]/div/dl/dd[1]/ul/li[8]/a').click()
    print('成功进入实践教学')
    sleep(t)
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[2])
    #sleep(10)
    #browser.find_element_by_xpath('//*[@id="sm_center_cover"]/div/div[1]/div[1]').click()
    #print('成功进入实践教学平台')
    sleep(t)
    browser.find_element_by_xpath('//*[@id="sm_center_cover"]/div/div[1]/div[1]').click()
    print('成功进入课题')
    sleep(t)
    if a==1:#品牌教学活动
        browser.find_element_by_xpath(' // *[ @ id = "sm_center"] / div[2] / div[1] / ul / li[3] / a').click()
        print("进入实验报告")
        sleep(t)
        browser.find_element_by_xpath('//*[@id="218"]').send_keys(tx)
        browser.find_element_by_xpath('//*[@id="218"]').send_keys(tx2)
        browser.find_element_by_xpath('//*[@id="218"]').send_keys(tx3)
        browser.find_element_by_xpath('//*[@id="218"]').send_keys(tx4)
        browser.find_element_by_xpath('//*[@id="218"]').send_keys(tx5)
        browser.find_element_by_xpath('//*[@id="218"]').send_keys(tx6)
        browser.find_element_by_xpath('//*[@id="218"]').send_keys(tx7)
        #browser.find_element_by_xpath('//*[@id="218"]').send_keys(tx9)
        #browser.find_element_by_xpath('//*[@id="218"]').send_keys(tx10)
        browser.find_element_by_xpath('//*[@id="218"]').send_keys(' ')

        sleep(3)

        print('成功')











if __name__ == '__main__':
    #username = input('请输入你的用户名：')
    username = '13350001157'

    #pwd = input('请输入你的密码：')
    pwd = 'adaM3131'
    '''
    with open("test", 'r') as x:
        line = x.readlines()
        tx = line[0]
        tx1 = line[1]
        tx2 = line[2]
        tx3 = line[3]
        tx4 = line[4]
        tx5 = line[5]
        tx6 = line[6]
        tx7 = line[7]
        tx8 = line[8]
        tx9 = line[9]
        tx10 = line[10]
    '''



    tx = input('请输入文本1：')
    tx2 = input('请输入文本2：')
    tx3 = input('请输入文本3：')
    tx4 = input('请输入文本4：')
    tx5 = input('请输入文本5：')
    tx6 = input('请输入文本6：')
    tx7 = input('请输入文本7：')


    url = 'http://www.attop.com/index.htm'

    browser = webdriver.Chrome()
    url = 'http://www.attop.com/index.htm'
    browser.get(url)
    browser.find_elements_by_xpath('//li[@class="logon-bar"]/a')[0].click()
    browser.switch_to.frame(browser.find_element_by_id('pageiframe'))
    browser.find_element_by_id('username').send_keys(username)
    browser.find_element_by_id('password').send_keys(pwd)

    print('请在8秒钟内完成验证并登录')
    sleep(10)


    write()


