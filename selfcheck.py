#자가진단 자동화 프로그램
from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

slave = wb.Chrome("D:\chromedriver.exe")
slave.get("https://hcs.eduro.go.kr/#/loginHome")

elem = slave.find_element_by_id("btnConfirm2")
elem.click()
bt1 = slave.find_element_by_id("schul_name_input")
bt1.click()

select = Select(slave.find_element_by_id('sidolabel'))
select.select_by_value(value='03')
select = Select(slave.find_element_by_id('crseScCode'))
select.select_by_value(value='4')

ip = slave.find_element_by_id('orgname')
ip.send_keys("대륜고등학교")

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
ip2.send_keys("이재윤")

ip3 = slave.find_element_by_id('birthday_input')
ip3.send_keys("040324")

sel6 = slave.find_element_by_id('btnConfirm')
sel6.send_keys(Keys.ENTER)
time.sleep(3)
password = slave.find_element_by_tag_name('input')
password.send_keys(Keys.NUMPAD0)
password.send_keys(Keys.NUMPAD2)
password.send_keys(Keys.NUMPAD0)
password.send_keys(Keys.NUMPAD3)

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

########################################################

slave = wb.Chrome("D:\chromedriver.exe")
slave.get("https://hcs.eduro.go.kr/#/loginHome")

elem = slave.find_element_by_id("btnConfirm2")
elem.click()
bt1 = slave.find_element_by_id("schul_name_input")
bt1.click()

select = Select(slave.find_element_by_id('sidolabel'))
select.select_by_value(value='03')
select = Select(slave.find_element_by_id('crseScCode'))
select.select_by_value(value='4')

ip = slave.find_element_by_id('orgname')
ip.send_keys("대륜고등학교")

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
ip2.send_keys("심재원")

ip3 = slave.find_element_by_id('birthday_input')
ip3.send_keys("040217")

sel6 = slave.find_element_by_id('btnConfirm')
sel6.send_keys(Keys.ENTER)
time.sleep(3)
password = slave.find_element_by_tag_name('input')
password.send_keys(Keys.NUMPAD1)
password.send_keys(Keys.NUMPAD9)
password.send_keys(Keys.NUMPAD5)
password.send_keys(Keys.NUMPAD0)

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

###############################################

slave = wb.Chrome("D:\chromedriver.exe")
slave.get("https://hcs.eduro.go.kr/#/loginHome")

elem = slave.find_element_by_id("btnConfirm2")
elem.click()
bt1 = slave.find_element_by_id("schul_name_input")
bt1.click()

select = Select(slave.find_element_by_id('sidolabel'))
select.select_by_value(value='03')
select = Select(slave.find_element_by_id('crseScCode'))
select.select_by_value(value='4')

ip = slave.find_element_by_id('orgname')
ip.send_keys("대륜고등학교")

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
ip2.send_keys("서유성")

ip3 = slave.find_element_by_id('birthday_input')
ip3.send_keys("041204")

sel6 = slave.find_element_by_id('btnConfirm')
sel6.send_keys(Keys.ENTER)
time.sleep(3)
password = slave.find_element_by_tag_name('input')
password.send_keys(Keys.NUMPAD1)
password.send_keys(Keys.NUMPAD2)
password.send_keys(Keys.NUMPAD0)
password.send_keys(Keys.NUMPAD4)

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

#########################################
slave = wb.Chrome("D:\chromedriver.exe")
slave.get("https://hcs.eduro.go.kr/#/loginHome")

elem = slave.find_element_by_id("btnConfirm2")
elem.click()
bt1 = slave.find_element_by_id("schul_name_input")
bt1.click()

select = Select(slave.find_element_by_id('sidolabel'))
select.select_by_value(value='03')
select = Select(slave.find_element_by_id('crseScCode'))
select.select_by_value(value='4')

ip = slave.find_element_by_id('orgname')
ip.send_keys("대륜고등학교")

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
ip2.send_keys("남윤성")

ip3 = slave.find_element_by_id('birthday_input')
ip3.send_keys("040102")

sel6 = slave.find_element_by_id('btnConfirm')
sel6.send_keys(Keys.ENTER)
time.sleep(3)
password = slave.find_element_by_tag_name('input')
password.send_keys(Keys.NUMPAD1)
password.send_keys(Keys.NUMPAD2)
password.send_keys(Keys.NUMPAD1)
password.send_keys(Keys.NUMPAD4)

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
##################################################

slave = wb.Chrome("D:\chromedriver.exe")
slave.get("https://hcs.eduro.go.kr/#/loginHome")

elem = slave.find_element_by_id("btnConfirm2")
elem.click()
bt1 = slave.find_element_by_id("schul_name_input")
bt1.click()

select = Select(slave.find_element_by_id('sidolabel'))
select.select_by_value(value='04')
select = Select(slave.find_element_by_id('crseScCode'))
select.select_by_value(value='4')

ip = slave.find_element_by_id('orgname')
ip.send_keys("인천예술고등학교")

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
ip2.send_keys("김서현")

ip3 = slave.find_element_by_id('birthday_input')
ip3.send_keys("040125")

sel6 = slave.find_element_by_id('btnConfirm')
sel6.send_keys(Keys.ENTER)
time.sleep(3)
password = slave.find_element_by_tag_name('input')
password.send_keys(Keys.NUMPAD1)
password.send_keys(Keys.NUMPAD3)
password.send_keys(Keys.NUMPAD0)
password.send_keys(Keys.NUMPAD3)

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
####################################################


slave = wb.Chrome("D:\chromedriver.exe")
slave.get("https://hcs.eduro.go.kr/#/loginHome")

elem = slave.find_element_by_id("btnConfirm2")
elem.click()
bt1 = slave.find_element_by_id("schul_name_input")
bt1.click()

select = Select(slave.find_element_by_id('sidolabel'))
select.select_by_value(value='10')
select = Select(slave.find_element_by_id('crseScCode'))
select.select_by_value(value='4')

ip = slave.find_element_by_id('orgname')
ip.send_keys("영신여자고등학교")

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
ip2.send_keys("배은빈")

ip3 = slave.find_element_by_id('birthday_input')
ip3.send_keys("040317")

sel6 = slave.find_element_by_id('btnConfirm')
sel6.send_keys(Keys.ENTER)
time.sleep(3)
password = slave.find_element_by_tag_name('input')
password.send_keys(Keys.NUMPAD0)
password.send_keys(Keys.NUMPAD3)
password.send_keys(Keys.NUMPAD1)
password.send_keys(Keys.NUMPAD7)

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

