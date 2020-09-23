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
macname@MacdeMBP case %
macname@MacdeMBP case % python3 compress_pic.py
本次任务共有2个.
开始处理------->1/2----------->test1
1/1/2-------------------->test1
还没有出现结束标志---
Message: no such element: Unable to locate element: {"method":"xpath","selector":".//div[@class="hc73a"]/span/span"}
  (Session info: chrome=85.0.4183.121)

还没有出现结束标志---
Message: no such element: Unable to locate element: {"method":"xpath","selector":".//div[@class="hc73a"]/span/span"}
  (Session info: chrome=85.0.4183.121)

13% smaller
转换完成---
50
27.4
3
1.71
2/1/2-------------------->test1
72% smaller
转换完成---
50
31.6
3
1.85
3/1/2-------------------->test1
67% smaller
转换完成---
50
17.4
3
1.43
开始处理------->2/2----------->test2
1/2/2-------------------->test2
59% smaller
转换完成---
50
20.2
3
1.47
2/2/2-------------------->test2
26% smaller
转换完成---
50
30.9
3
1.86
3/2/2-------------------->test2
14% smaller
转换完成---
50
27.2
3
1.94
macname@MacdeMBP case % 
```
- 压缩过程视频链接（https://v.kuaishou.com/60ZJzZ）
<br>
- 具体步骤可参考以下博客（https://www.cnblogs.com/sea-stream/p/13721105.html）
