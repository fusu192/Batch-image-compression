# Batch-image-compression
python3 selenium squoosh(网页版) 批量压缩图片

- 本项目运行前，需先配置好selenium环境，以及python3环境，确保浏览器驱动已安装好。
- 笔者运行环境为：mac，python3.6，selenium3.141.0

# 使用方法
- 安装好selenium环境以及python3环境
- 下载项目
```git clone git@github.com:fusu192/Batch-image-compression.git```
- 切换目录
<br>```cd Batch-image-compression```<br>
工作目录结构，目标文件夹pic中有两个相册，每个相册中有3张图片，我们需要压缩所有相册里面的图片
<img src="https://img2020.cnblogs.com/blog/1011634/202009/1011634-20200923205316536-1982696890.png" width = "90%" height = "90%" alt="图片名称" />
- 运行代码，下面的是输出日志<br>
```shell
macname@MacdeMacBook-Pro Interface-automation-test % ./run.sh 
host: default host
task id: not specific, so all case will be test
Service URL: https://baike.baidu.com
======================================================== test session starts ========================================================
platform darwin -- Python 3.6.3, pytest-5.1.0, py-1.8.0, pluggy-0.12.0
rootdir: /Users/macname/Desktop/interface_automation/Interface-automation-test/case
plugins: allure-pytest-2.7.1
collected 8 items                                                                                                                   

test_HY-112.py .                                                                                                              [ 12%]
test_HY-174_189.py .                                                                                                          [ 25%]
test_HY-218.py .                                                                                                              [ 37%]
test_HY-34.py .                                                                                                               [ 50%]
test_HY-380.py .                                                                                                              [ 62%]
test_HY-50.py .                                                                                                               [ 75%]
test_HY-55.py .                                                                                                               [ 87%]
test_HY-66.py .                                                                                                               [100%]

========================================================= 8 passed in 0.79s =========================================================
Report successfully generated to ../html
macname@MacdeMacBook-Pro Interface-automation-test % 
```
- 压缩过程视频链接（https://v.kuaishou.com/60ZJzZ）
<br>
- 具体步骤可参考以下博客（https://www.cnblogs.com/sea-stream/p/13721105.html）
