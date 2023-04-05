#자가진단 자동화 프로그램 V.3.1
from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import datetime

def selfcheck_h_f(local, school, name, birthday, password):

    options = wb.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("window-size=1920x1080") # 화면크기(전체화면)
    options.add_argument("disable-gpu") 
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    # 속도 향상을 위한 옵션 해제
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    options.add_experimental_option('prefs', prefs)

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
    slave.implicitly_wait(3)
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
    
    time.sleep(0.5)

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
        kk == "str" 
    ######################
    
    sel7 = slave.find_element_by_id('btnConfirm')
    sel7.send_keys(Keys.ENTER)

    time.sleep(2)
    
    sel8 = slave.find_element_by_class_name('btn')
    sel8.click()

    q1 = slave.find_element_by_id('survey_q1a1')
    q1.click()
    q2 = slave.find_element_by_id('survey_q2a1')
    q2.click()
    q3 = slave.find_element_by_id('survey_q3a1')
    q3.click()

    sel9 = slave.find_element_by_id('btnConfirm')
    sel9.click()

    slave.close()
    print(name,"success")
    
    fl = open("D:\selfcheck-checking\checklist.txt", "a")

    now = datetime.datetime.now()

    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    fl.write(nowDatetime)
    fl.write('\t\n')
    fl.write(name)
    fl.close()
def selfcheck_m_f(local, school, name, birthday, password):
    
    options = wb.ChromeOptions() # 크롬 옵션 객체 생성
    options.add_argument('headless') # headless 모드 설정
    options.add_argument("window-size=1920x1080") # 화면크기(전체화면)
    options.add_argument("disable-gpu") 
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    # 속도 향상을 위한 옵션 해제
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    options.add_experimental_option('prefs', prefs)


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
    slave.implicitly_wait(3)
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
    
    time.sleep(0.5)
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
        kk == 'str'  
    ######################
    
    sel7 = slave.find_element_by_id('btnConfirm')
    sel7.send_keys(Keys.ENTER)
    sel8 = slave.find_element_by_class_name('btn')
    sel8.click()


    q1 = slave.find_element_by_id('survey_q1a1')
    q1.click()
    q2 = slave.find_element_by_id('survey_q2a1')
    q2.click()
    q3 = slave.find_element_by_id('survey_q3a1')
    q3.click()

    sel9 = slave.find_element_by_id('btnConfirm')
    sel9.click()
    slave.close()
    print(name,"success")
    fl = open("D:\selfcheck-checking\checklist.txt", "a")

    now = datetime.datetime.now()

    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    fl.write(nowDatetime)
    fl.write('\t')
    fl.write(name)
    fl.close()

def selfcheck_h(local, school, name, birthday, password):
    try:
        selfcheck_h_f(local, school, name, birthday, password)
    except:
        time.sleep(2)
        selfcheck_h_f(local, school, name, birthday, password)
    finally:
        time.sleep(0.3)

def selfcheck_m(local, school, name, birthday, password):
    try:
        selfcheck_m_f(local, school, name, birthday, password)
    except:
        timel.sleep(2)
        selfcheck_m_f(local, school, name, birthday, password)
    finally:
        time.sleep(0.3)

selfcheck_h("대구", "대륜고등학교", "이재윤", "040324", "0203")
selfcheck_h("대구", "대륜고등학교", "심재원", "040217", "1950")
selfcheck_h("대구", "대륜고등학교", "서유성", "041204", "1204")
selfcheck_h("대구", "대륜고등학교", "남윤성", "040102", "1214")
selfcheck_h("대구", "대륜고등학교", "박주연", "040308", "4308")
selfcheck_h("대구", "대륜고등학교", "이민성", "040720", "0720")
selfcheck_h("대구", "대륜고등학교", "전주원", "040326", "2059")
selfcheck_h("대구", "대륜고등학교", "이예준", "040427", "3216")
selfcheck_h("대구", "대륜고등학교", "허재원", "040607", "1907")
selfcheck_h("대구", "대륜고등학교", "김동욱", "040818", "0818")
time.sleep(5)
selfcheck_h("대구", "대륜고등학교", "이유준", "040427", "0401")
selfcheck_h("대구", "대륜고등학교", "김민규", "041112", "6238")
selfcheck_h("대구", "대륜고등학교", "이유찬", "040115", "5087")
selfcheck_h("대구", "대륜고등학교", "이재균", "781011"," 1404")
selfcheck_h("대구", "대륜고등학교", "최연우", "040224", "5250")
selfcheck_h("대구", "대륜고등학교", "이도헌", "041209", "1207")
selfcheck_h("대구", "대륜고등학교", "김태경", "040116", "1604")
selfcheck_h("대구", "대륜고등학교", "차승민", "040222", "5013")
selfcheck_h("대구", "대륜고등학교", "박진수", "040320", "0320")
selfcheck_h("대구", "대륜고등학교", "김수찬", "041115", "0513")
time.sleep(5)
selfcheck_h("대구", "대륜고등학교", "권준혁", "041226", "1226")
selfcheck_h("대구", "경신고등학교", "전현욱", "040916", "5898")
selfcheck_h("대구", "대륜고등학교", "김연우", "041215", "1215")
selfcheck_h("대구", "현풍고등학교", "최세빈", "040319", "0319") 
selfcheck_h("대구", "현풍고등학교", "손윤지", "040605", "1234")
selfcheck_h("대구", "현풍고등학교", "이유나", "041125", "1369")
selfcheck_h("대구", "중앙고등학교", "이승진", "040119", "1234")
selfcheck_h("대구", "경신고등학교", "윤지민", "040103", "1850")
selfcheck_h("부산", "부산중앙고등학교", "김준", "041019", "1019")
selfcheck_h("인천", "인천예술고등학교", "김서현", "040125", "1303")
time.sleep(5)
selfcheck_h("경기", "영신여자고등학교", "배은빈", "040317", "0317")
selfcheck_h("경기", "인창고등학교", "송서연", "040502", "7482")
selfcheck_h("서울", "진선여자고등학교", "방수연", "040409", "0409")
selfcheck_m("경기", "은가람중학교", "김서은", "070502", "0502")


f = open("D:\selfcheck-checking\check.txt", "a")

now = datetime.datetime.now()

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
f.write("\n")
f.write(nowDatetime)

f.close()

fl2 = open("D:\selfcheck-checking\checklist.txt", "a")

now = datetime.datetime.now()

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
  
fl2.write(nowDatetime)
fl2.write('\n')
fl2.close()
