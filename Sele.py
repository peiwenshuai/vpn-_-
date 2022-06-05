from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
wd=webdriver.Chrome(service=Service('/Users/ashuai/shuai/py/chromedriver'))
a=input("请输入一个基础字符串6位英文以内")
b=input("请输入你要邀请注册的人数")
i=1
while(i<int(b)):
   x=str(i)
   name_f=a
   name_e="@gmail.com"
   wd.get('http://wmwtg.duokuai3.cc:5658/invite?code=eDeD1KbT')
   wd.find_element(By.ID,'email').send_keys(name_f+x+name_e)
   wd.find_element(By.ID,'passwd').send_keys('112233aB')
   wd.find_element(By.ID,'repasswd').send_keys('112233aB')
   wd.find_element(By.ID,'register-confirm').click()
   i=i+1
