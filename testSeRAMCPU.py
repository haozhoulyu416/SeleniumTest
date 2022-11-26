#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import time
import psutil
from datetime import datetime
from pprint import pprint as pp
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# In[28]:


import psutil
import win32process
import win32gui

#获取前台窗口的句柄
handle = win32gui.GetForegroundWindow()
print(handle)
#根据前台窗口的句柄获取线程tid和进程pid
tid, pid = win32process.GetWindowThreadProcessId(handle)
print(tid, pid)
#根据前台窗口的进程pid获取进程名称
process_name = psutil.Process(67612).name()
print(process_name)


# In[107]:


windows_list = []
win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), windows_list)
for window in windows_list:
    classname = win32gui.GetClassName(window)
    title = win32gui.GetWindowText(window)
    print(f'classname:{classname} title:{title}')


# In[110]:


hwnd = win32gui.FindWindow(None, "Expanding Cards - Google Chrome")

hread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)
print(process_id)


# In[36]:


from win32 import win32gui,win32process
import time
import sys

def get_PID(point):
    try:
        p=win32gui.WindowFromPoint(point)    
        p_name=win32gui.GetWindowText(p)
        _,p_id=win32process.GetWindowThreadProcessId(p)
        process = psutil.Process('进程ID').name() 
        print(p_name,p_id)
    except:
        print("win32获取窗体信息失败 error")
        sys.exit(1)

def main():
    while True:
        point1 =win32gui.GetCursorPos()#获取鼠标坐标
        time.sleep(2)
        point2 =win32gui.GetCursorPos()#获取鼠标坐标
        if point2 == point1:
           get_PID(point2)


# In[123]:


p=win32gui.WindowFromPoint(win32gui.GetCursorPos())  
print(type(p))
print(p)
hread_id, process_id = win32process.GetWindowThreadProcessId(p) 
print(process_id)
print(win32gui.GetForegroundWindow())


# In[95]:


hwnd = win32gui.GetForegroundWindow()
hread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)
process_id
classname = win32gui.GetClassName(hwnd)
title = win32gui.GetWindowText(hwnd)
print(classname)


# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


# 创建 WebDriver 对象，指明使用chrome浏览器驱动
# 放入环境变量path里了
#wd = webdriver.Chrome(service=Service(r'e:\Selenium\chromedriver.exe'))
wd = webdriver.Chrome()
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
#wd.get('https://haozhoulyu.com.cn/')
wd.delete_all_cookies()
wd.get('file:///E:/WebProject/company-main/index.html')


# In[62]:


def webTestAuto():    

    wd.implicitly_wait(3)
    #time.sleep(2)
    js = "window.scrollTo(0, document.body.scrollHeight)"
    wd.execute_script(js)
    #time.sleep(2)
    js = "window.scrollTo(0, 0)"
    wd.execute_script(js)

    # 点击标题栏    
    #time.sleep(2)
    element_feature = wd.find_element(By.ID, 'feature')
    element_feature.click()
    #time.sleep(2)
    element_feature = wd.find_element(By.ID, 'project')
    element_feature.click()
    #time.sleep(2)
    
    # 输入Contact内容
    elements = wd.find_elements(By.TAG_NAME, 'input')
    elements[0].clear()
    elements[1].clear()
    elements[2].clear()
    elements[0].send_keys('Haozhou')
    #time.sleep(2)
    elements[1].send_keys('haozhoulyu@gmail.com')
    #time.sleep(2)
    elements[2].send_keys('764318872')
    elements[3].click()

    element_text = wd.find_elements(By.TAG_NAME, 'textarea')
    element_text[0].clear()
    element_text[0].send_keys('Answer')
    #time.sleep(2)
    
    element_feature = wd.find_element(By.ID, 'price_title')
    element_feature.click()
    #time.sleep(2)

    # 退出自动化
    # we.quit()


# In[4]:


import binascii

print(wd.current_window_handle)      # 用于获取当前窗口句柄
print(wd.current_url)
string = '065A89E0340657BD50BC8B330FB1D7D0'
print(wd.window_handles)
print(wd.title)


# In[117]:


tabs = wd.window_handles
for window_handle in tabs:
     if window_handle == wd.current_window_handle:
          tab = tabs.index(window_handle)
          print(tab)


# In[14]:


# Bytes conversion

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


# In[15]:


if len(sys.argv) < 2:
    print ("missing pid arg")
    sys.exit()


# In[16]:


def get_process_list(process_name):
    # 获取所有正在运行的进程PID
    pid_list = psutil.pids()
    process_list = []
    for pid in pid_list:
        try:
            pid_process = psutil.Process(pid)
        except Exception as e:
            continue
        pid_name = pid_process.name()
        if process_name == pid_name:
            process_list.append(pid_process)
    return process_list


# In[63]:


process_list = get_process_list("chrome.exe")
print(len(process_list))
iteration = 1
chrome_cpu_percent = 0
chrome_mem_uss = 0
pid = 103900
for pid_process in process_list:
    if(pid_process.pid == pid):
        for i in range(iteration):
            #print(pid_process)
            # 获取 RAM memory, USS(唯一集大小)是进程专有的内存
            chrome_mem_uss += pid_process.memory_full_info().uss 
            
            # 获取 CPU utilization as percentage
            pid_process.cpu_percent(None)
            time.sleep(2)
            
            # 模拟测试用户网页浏览点击输入操作
            [webTestAuto() for _ in range(5)]
            
             # 第一次调用pid_process.cpu_percent(None)得到的是0
            # 第二次调用pid_process.cpu_percent(None)得到的是从上一次调用同一个进程对象的cpu_percent(None)方法到第二次调用之间的cpu利用率
            #(cpu利用率是计算一段时间内cpu计算时间/总时间)
            chrome_cpu_percent += pid_process.cpu_percent(None)
            chrome_mem_uss_str = str(round(chrome_mem_uss / 1024 / 1024, 2))
            chrome_cpu_percent_str = str(round(chrome_cpu_percent, 2))
            #print("RAM: ", chrome_mem_uss/1024, "浏览器内存占用：",chrome_mem_uss_str,"cpu使用率：",chrome_cpu_percent_str)

            with open("mem_and_cpu", 'a') as mem_file:
                now_time = datetime.fromtimestamp(round(time.time(), 0))
                mem_file.write(str(now_time) + ",RAM " + chrome_mem_uss_str + "," + chrome_cpu_percent_str +"\n")

avg_chrome_mem_uss_str = (round(chrome_mem_uss /1024 /iteration, 2))
avg_chrome_cpu_percent_str = (round(chrome_cpu_percent/iteration, 2))
print("RAM：",avg_chrome_mem_uss_str," CPU Usage Percentage：",avg_chrome_cpu_percent_str)


# In[74]:


# 查看正在运行的process信息

pp([(p.pid, p.info) for p in psutil.process_iter(['name', 'status']) if p.info['status'] == psutil.STATUS_RUNNING and p.info['name']=='chrome.exe'])


# In[64]:


wd.delete_all_cookies()


# In[4]:


psutil.pid_exists(24260)


# In[29]:


p = psutil.Process(82664)
print(p.name())


# In[ ]:


pid = 21076
p = psutil.Process(21076)
print(p.name)
# monitor process and write data to file
interval = 3 # polling seconds
with open("process_monitor_" + p.name() + '_' + str(pid) + ".csv", "a+") as f:
    f.write("time,cpu%,mem%\n") # titles
    while True:
        current_time = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
        cpu_percent = p.cpu_percent() # better set interval second to calculate like:  p.cpu_percent(interval=0.5)
        mem_percent = p.memory_percent()
        line = current_time + ',' + str(cpu_percent) + ',' + str(mem_percent)
        print (line)
        f.write(line + "\n")
        time.sleep(interval)


# In[ ]:




