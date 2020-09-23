
import time
import sys,os
import requests
import shutil
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def formatFloat(num):
    return '{:.2f}'.format(num)

def asleep(driver):
	driver.implicitly_wait(3.5)
	time.sleep(2) 

driver = webdriver.Chrome()

asleep(driver)

#当前目录
pwd=os.getcwd()

#图片
pic_d=os.path.join(pwd,"pic")

#计数
count=0

lll=os.listdir(pic_d)

all_pic_name=[i for i in lll if((not i.startswith(".")) and (os.path.isdir(os.path.join(pic_d,i))))]

number_all=len(all_pic_name)

print("本次任务共有{}个.".format(number_all))

for i in all_pic_name:	
	pic_count=0
	count+=1
	print("开始处理------->{}/{}----------->{}".format(count,number_all,i))
	tmp_pic_d=os.path.join(pic_d,i)
	pics=os.listdir(tmp_pic_d)
	for j in pics:
		pic_count+=1
		print("{}/{}/{}-------------------->{}".format(pic_count,count,number_all,i))	
		if(j.startswith(".")):
			continue
		f=os.path.join(tmp_pic_d,j)
		# 打开 Squoosh
		driver.get('https://squoosh.app')
		# 找到输入框
		input_box = driver.find_element_by_xpath('.//input[@class="_2zg9i"]')
		# 输入图片路径
		input_box.send_keys(f)

		# 等待出现 'smaller'字样，10秒不出现则视为处理失败
		while(1):
			
			try:
				locator = driver.find_element_by_xpath('.//div[@class="hc73a"]/span/span')
				str=locator.text
				print(str)
				if("smaller" in str or "bigger" in str):
					print("页面刷新完成---")
					break
				else:
					print("等待---")
					time.sleep(2)
			except Exception as e:
				print("还没有出现结束标志---")
				print(e)

		#设置
		b= ActionChains(driver)
		c= driver.find_element_by_xpath('.//input[@class="_2x7lc"]')
		b.click_and_hold(c).perform()
		#b.reset_actions()

		while(1):
			#获取当前进度值
			style=driver.find_element_by_class_name("_1grfT").get_attribute("style")
			v=style.split("%")[0].split(":")[1]
			v=int(v)
			print(v)

			#获取大小
			locator = driver.find_elements_by_xpath('.//div[@class="hc73a"]/span')[-1].text
			num=locator.split()[0]
			num=float(num)
			print(num)

			if(v<8):
				break
			else:
				#左移
				b.move_by_offset(-120,0).perform()

			time.sleep(1)

		# 找到下载按钮
		button = driver.find_elements_by_xpath('.//a[@title="Download"]')[-1]
		# 点击下载按钮
		button.click()
time.sleep(3)		
driver.quit()
print("压缩结束！")
			


