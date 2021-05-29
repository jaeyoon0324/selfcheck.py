#자가진단 자동화 프로그램 V.2
from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

def selfcheck_h(local, school, name, birthday, password):
    
    if local == "서울":
        loc_cod = '01'
    if local == "부산":
        loc_cod = '02'
    if local == "대구":
        loc_cod = '03'
    if local == "인천":
        loc_cod = '04'
    if local == "광주":
        loc_cod = '05'
    if local == "대전":
        loc_cod = '06'
    if local == "울산":
        loc_cod = '07'
    if local == "세종":
        loc_cod = '08'
    if local == "경기":
        loc_cod = '10'
    if local == "강원":
        loc_cod = '11'
    if local == "충북":
        loc_cod = '12'
    if local == "충남":
        loc_cod = '13'
    if local == "전북":
        loc_cod = '14'
    if local == "전남":
        loc_cod = '15'
    if local == "경북":
        loc_cod = '16'
    if local == "경남":
        loc_cod = '17'
    if local == "제주":
        loc_cod = '18'
    
    slave = wb.Chrome("D:\chromedriver.exe")
    slave.get("https://hcs.eduro.go.kr/#/loginHome")

    elem = slave.find_element_by_id("btnConfirm2")
    elem.click()
    bt1 = slave.find_element_by_id("schul_name_input")
    bt1.click()
    
    select = Select(slave.find_element_by_id('sidolabel'))
    select.select_by_value(value = loc_cod)
    select = Select(slave.find_element_by_id('crseScCode'))
    select.select_by_value(value='4')

    ip = slave.find_element_by_id('orgname')
    ip.send_keys(str(school))

    sel2 = slave.find_element_by_class_name('searchBtn')
    sel2.click()
    sel4 = slave.find_element_by_class_name("layerSchoolArea")
    sel4.click()
    time.sleep(1)
    sel5 = slave.find_element_by_tag_name('a')
    sel5.click()

    sel3 = slave.find_element_by_class_name("layerFullBtn")
    sel3.click()

    ip2 = slave.find_element_by_id('user_name_input')
    ip2.send_keys(str(name))
    
    ip3 = slave.find_element_by_id('birthday_input')
    ip3.send_keys(str(birthday))
    sel6 = slave.find_element_by_id('btnConfirm')
    sel6.send_keys(Keys.ENTER)
    time.sleep(3)
    

    pas_list = []
    for num in password:
        kk = num
        password = slave.find_element_by_tag_name('input')
        if kk == '0':
            password.send_keys(Keys.NUMPAD0)
        if kk == '1':
            password.send_keys(Keys.NUMPAD1)
        if kk == '2':
            password.send_keys(Keys.NUMPAD2)
        if kk == '3':
            password.send_keys(Keys.NUMPAD3)
        if kk == '4':
            password.send_keys(Keys.NUMPAD4)
        if kk == '5':
            password.send_keys(Keys.NUMPAD5)
        if kk == '6':
            password.send_keys(Keys.NUMPAD6)
        if kk == '7':
            password.send_keys(Keys.NUMPAD7)
        if kk == '8':
            password.send_keys(Keys.NUMPAD8)
        if kk == '9':
            password.send_keys(Keys.NUMPAD9)    
    ######################
    
    sel7 = slave.find_element_by_id('btnConfirm')
    sel7.send_keys(Keys.ENTER)
    time.sleep(3)
    sel8 = slave.find_element_by_class_name('btn')
    sel8.click()

    time.sleep(1.5)

    q1 = slave.find_element_by_id('survey_q1a1')
    q1.click()
    q2 = slave.find_element_by_id('survey_q2a1')
    q2.click()
    q3 = slave.find_element_by_id('survey_q3a1')
    q3.click()

    sel9 = slave.find_element_by_id('btnConfirm')
    sel9.click()
    time.sleep(1)
    slave.close()
    print(name,"success")

def selfcheck_m(local, school, name, birthday, password):
    if local == "서울":
        loc_cod = '01'
    if local == "부산":
        loc_cod = '02'
    if local == "대구":
        loc_cod = '03'
    if local == "인천":
        loc_cod = '04'
    if local == "광주":
        loc_cod = '05'
    if local == "대전":
        loc_cod = '06'
    if local == "울산":
        loc_cod = '07'
    if local == "세종":
        loc_cod = '08'
    if local == "경기":
        loc_cod = '10'
    if local == "강원":
        loc_cod = '11'
    if local == "충북":
        loc_cod = '12'
    if local == "충남":
        loc_cod = '13'
    if local == "전북":
        loc_cod = '14'
    if local == "전남":
        loc_cod = '15'
    if local == "경북":
        loc_cod = '16'
    if local == "경남":
        loc_cod = '17'
    if local == "제주":
        loc_cod = '18'
    
    slave = wb.Chrome("D:\chromedriver.exe")
    slave.get("https://hcs.eduro.go.kr/#/loginHome")

    elem = slave.find_element_by_id("btnConfirm2")
    elem.click()
    bt1 = slave.find_element_by_id("schul_name_input")
    bt1.click()
    
    select = Select(slave.find_element_by_id('sidolabel'))
    select.select_by_value(value = loc_cod)
    select = Select(slave.find_element_by_id('crseScCode'))
    select.select_by_value(value='3')

    ip = slave.find_element_by_id('orgname')
    ip.send_keys(str(school))

    sel2 = slave.find_element_by_class_name('searchBtn')
    sel2.click()
    sel4 = slave.find_element_by_class_name("layerSchoolArea")
    sel4.click()
    time.sleep(1)
    sel5 = slave.find_element_by_tag_name('a')
    sel5.click()

    sel3 = slave.find_element_by_class_name("layerFullBtn")
    sel3.click()

    ip2 = slave.find_element_by_id('user_name_input')
    ip2.send_keys(str(name))
    
    ip3 = slave.find_element_by_id('birthday_input')
    ip3.send_keys(str(birthday))
    sel6 = slave.find_element_by_id('btnConfirm')
    sel6.send_keys(Keys.ENTER)
    time.sleep(3)
    

    pas_list = []
    for num in password:
        kk = num
        password = slave.find_element_by_tag_name('input')
        if kk == '0':
            password.send_keys(Keys.NUMPAD0)
        if kk == '1':
            password.send_keys(Keys.NUMPAD1)
        if kk == '2':
            password.send_keys(Keys.NUMPAD2)
        if kk == '3':
            password.send_keys(Keys.NUMPAD3)
        if kk == '4':
            password.send_keys(Keys.NUMPAD4)
        if kk == '5':
            password.send_keys(Keys.NUMPAD5)
        if kk == '6':
            password.send_keys(Keys.NUMPAD6)
        if kk == '7':
            password.send_keys(Keys.NUMPAD7)
        if kk == '8':
            password.send_keys(Keys.NUMPAD8)
        if kk == '9':
            password.send_keys(Keys.NUMPAD9)    
    ######################
    
    sel7 = slave.find_element_by_id('btnConfirm')
    sel7.send_keys(Keys.ENTER)
    time.sleep(3)
    sel8 = slave.find_element_by_class_name('btn')
    sel8.click()

    time.sleep(1.5)

    q1 = slave.find_element_by_id('survey_q1a1')
    q1.click()
    q2 = slave.find_element_by_id('survey_q2a1')
    q2.click()
    q3 = slave.find_element_by_id('survey_q3a1')
    q3.click()

    sel9 = slave.find_element_by_id('btnConfirm')
    sel9.click()
    time.sleep(1)
    slave.close()
    print(name,"success")

