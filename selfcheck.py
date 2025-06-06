#자가진단 자동화 프로그램 V.3.3
from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
import time
import datetime


def selfcheck_h_f(local, school, name, birthday, password, q1_a, q2_a, q3_a):
    options= EdgeOptions()
    options.use_chromium= True
    
    if True:
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
    
    slave = wb.Edge("D:\msedgedriver.exe")
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

    sel2 = WebDriverWait(slave,10).until(
    
    EC.presence_of_element_located((By.CLASS_NAME, "searchBtn"))

    ).click()

    sel4 = WebDriverWait(slave,10).until(
    
    EC.presence_of_element_located((By.CLASS_NAME, "layerSchoolArea"))

    ).click()

    sel5 = WebDriverWait(slave,10).until(
    
    EC.presence_of_element_located((By.TAG_NAME, "a"))

    ).click()

    sel3 = WebDriverWait(slave,10).until(
    
    EC.presence_of_element_located((By.CLASS_NAME, "layerFullBtn"))

    ).click()


    ip2 = slave.find_element_by_id('user_name_input')
    ip2.send_keys(str(name))
    
    ip3 = slave.find_element_by_id('birthday_input')
    ip3.send_keys(str(birthday))
    sel6 = slave.find_element_by_id('btnConfirm')
    sel6.send_keys(Keys.ENTER)
    ## 개인 정보 입력 부분 
    time.sleep(4)
    pass_input_box = WebDriverWait(slave, 10).until(
    
    EC.presence_of_element_located((By.CLASS_NAME, "input_text_common"))

    )
    
    
    pass_input_box.click()


    for num in password:
        kk = num
        if kk == '0':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='0']")
            password_key0.click()
        if kk == '1':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='1']")
            password_key0.click()
        if kk == '2':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='2']")
            password_key0.click()
        if kk == '3':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='3']")
            password_key0.click()
        if kk == '4':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='4']")
            password_key0.click()
        if kk == '5':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='5']")
            password_key0.click()
        if kk == '6':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='6']")
            password_key0.click()
        if kk == '7':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='7']")
            password_key0.click()
        if kk == '8':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='8']")
            password_key0.click()
        if kk == '9':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='9']")
            password_key0.click()
        kk == "str" 
    ######################

    sel7 = slave.find_element_by_id('btnConfirm')
    sel7.send_keys(Keys.ENTER)
    time.sleep(3)
    
        
    sel8 = WebDriverWait(slave,10).until(
    
    EC.presence_of_element_located((By.CLASS_NAME, "btn"))

    )

    slave.implicitly_wait(5)
    sel8.click()

    try:
        if len(slave.find_element_by_class_name('active').text) > 0:
            pass
        elif len(slave.find_element_by_class_name('caution').text) > 0:
            pass
        
        print(name,"success")
        slave.close()
    
    except:
        
        if q1_a == 'n':

            q1 = WebDriverWait(slave, 10).until(
                
                EC.presence_of_element_located((By.ID, "survey_q1a1"))

                ).click()
        
        elif q1_a == 'y':

            q1 = WebDriverWait(slave,10).until(
                    
                    EC.presence_of_element_located((By.ID, "survey_q1a2"))

                    ).click()
        
        if q2_a == 'n':

            q2 = WebDriverWait(slave,10).until(
                    
                    EC.presence_of_element_located((By.ID, "survey_q2a1"))

                    ).click()

        if q2_a == 'y':

            q2 = WebDriverWait(slave,10).until(
                    
                    EC.presence_of_element_located((By.ID, "survey_q2a2"))

                    ).click()

        if q3_a == 'n':

            q3 = WebDriverWait(slave,10).until(
                    
                    EC.presence_of_element_located((By.ID, "survey_q3a1"))

                    ).click()

        if q3_a == 'y':

            q3 = WebDriverWait(slave,10).until(
                    
                    EC.presence_of_element_located((By.ID, "survey_q3a2"))

                    ).click()

        sel9 = slave.find_element_by_id('btnConfirm')
        sel9.click()
    



    

def selfcheck_h_f_checker(local, school, name, birthday, password, q1_a, q2_a, q3_a):
    
    options= EdgeOptions()
    options.use_chromium= True

    if True:
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
    
    slave = wb.Edge("D:\msedgedriver.exe")
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

    sel2 = WebDriverWait(slave,10).until(
    
    EC.presence_of_element_located((By.CLASS_NAME, "searchBtn"))

    ).click()

    sel4 = WebDriverWait(slave,10).until(
    
    EC.presence_of_element_located((By.CLASS_NAME, "layerSchoolArea"))

    ).click()

    sel5 = WebDriverWait(slave,10).until(
    
    EC.presence_of_element_located((By.TAG_NAME, "a"))

    ).click()

    sel3 = WebDriverWait(slave,10).until(
    
    EC.presence_of_element_located((By.CLASS_NAME, "layerFullBtn"))

    ).click()


    ip2 = slave.find_element_by_id('user_name_input')
    ip2.send_keys(str(name))
    
    ip3 = slave.find_element_by_id('birthday_input')
    ip3.send_keys(str(birthday))
    sel6 = slave.find_element_by_id('btnConfirm')
    sel6.send_keys(Keys.ENTER)
    ## 개인 정보 입력 부분 
    time.sleep(3)
    pass_input_box = WebDriverWait(slave, 10).until(
    
    EC.presence_of_element_located((By.CLASS_NAME, "input_text_common"))

    )
    
    
    pass_input_box.click()


    for num in password:
        kk = num
        if kk == '0':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='0']")
            password_key0.click()
        if kk == '1':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='1']")
            password_key0.click()
        if kk == '2':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='2']")
            password_key0.click()
        if kk == '3':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='3']")
            password_key0.click()
        if kk == '4':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='4']")
            password_key0.click()
        if kk == '5':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='5']")
            password_key0.click()
        if kk == '6':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='6']")
            password_key0.click()
        if kk == '7':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='7']")
            password_key0.click()
        if kk == '8':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='8']")
            password_key0.click()
        if kk == '9':
            password_key0 = slave.find_element_by_xpath("//a[@aria-label='9']")
            password_key0.click()
        kk == "str" 
    ######################
    
    sel7 = slave.find_element_by_id('btnConfirm')
    sel7.send_keys(Keys.ENTER)

    time.sleep(3)
    try:
        if len(slave.find_element_by_class_name('active').text) > 0:
            pass
        elif len(slave.find_element_by_class_name('caution').text) > 0:
            pass
        
        print(name,"success")
    
        fl = open("D:\selfcheck-checking\checklist.txt", "a")

        now = datetime.datetime.now()

        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

        fl.write(nowDatetime)
        fl.write('\t\n')
        fl.write(name)
        fl.close()
        slave.close()

    except:
    
        selfcheck_h(local, school, name, birthday, password)
        slave.close()

        time.sleep(1)

        try:

        	selfcheck_h_checker(local, school, name, birthday, password)
            slave.close()
            
            except:
            pass
          
def selfcheck_h(local, school, name, birthday, password, q1_a, q2_a, q3_a):

    try:
        selfcheck_h_f(local, school, name, birthday, password, q1_a, q2_a, q3_a)
        print(name,"success")
 
    except:
        try:
            print(name,"failed")
            fail = open("D:\selfcheck-checking\\faillist.txt", "a")
            now = datetime.datetime.now()

            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

            fail.write(nowDatetime)
            fail.write(name)
            fail.write("\n")
            fail.close()
        except:
            pass

def selfcheck_h_t_checker(local, school, name, birthday, password, q1_a, q2_a, q3_a):
    try:
        selfcheck_h_f_checker(local, school, name, birthday, password, q1_a, q2_a, q3_a)
        
    except:
        selfcheck_h_f_checker(local, school, name, birthday, password, q1_a, q2_a, q3_a)
        
def selfcheck_h_checker(local, school, name, birthday, password, q1_a, q2_a, q3_a):
    try:
        selfcheck_h_t_checker(local, school, name, birthday, password, q1_a, q2_a, q3_a)
    except:
        selfcheck_h_t_checker(local, school, name, birthday, password, q1_a, q2_a, q3_a)

def excute_selfcheck():

#기본값은 n, 유사시 y

    selfcheck_h("대구", "대륜고등학교", "이재윤", "040324", "0203", 'n', 'n', 'y')


def excute_selfcheck_checker():

    selfcheck_h_checker("대구", "대륜고등학교", "이재윤", "040324", "0203", 'n', 'n', 'y')


def excute_final():

    try:       
        excute_selfcheck()
        
    except:

        try:
            excute_selfcheck()
        except:
            pass


    try:
        excute_selfcheck_checker()

    except:
        try:
            excute_selfcheck_checker()
        except:
            pass

excute_final()

f = open("D:\selfcheck-checking\check.txt", "a")

now = datetime.datetime.now()

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
f.write("\n")
f.write(nowDatetime)

f.close()

f = open("D:\selfcheck-checking\checklist.txt", "a")

now = datetime.datetime.now()

nowDatetime = now.strftime('%Y-%m-%d')

f.write("\n")
f.write(nowDatetime)
f.write("finaly success")

f.close()
