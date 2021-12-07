# BDynamicToWechat

详细博客介绍：[《转发 B 站 UP 主动态到微信 python 脚本》](https://blog.tangspoon.cn/2021/12/06/%E5%8E%9F%E5%88%9B%EF%BD%9C%E8%BD%AC%E5%8F%91B%E7%AB%99UP%E4%B8%BB%E5%8A%A8%E6%80%81%E5%88%B0%E5%BE%AE%E4%BF%A1python%E8%84%9A%E6%9C%AC/)

<img src="https://picbed.tangspoon.cn/uPic/image-20211206213430058.png" alt="image-20211206213430058" style="zoom:40%;" />

## 一、需求背景

B站关注了非常多up主，每天动态99+，但其实绝大部分的UP主我都不感兴趣。我每天都得手动寻找那些必看的UP。在寻找的过程中，大数据推荐让我忍不住看了一个又一个的视频，浪费时间不够专注。

所以，需要开发一个**每天定时把我每天必看的UP主的动态转发到微信**，这样避免了手动寻找和被大数据推荐的干扰，专注力大大提高。

## 二、部署到vps

## 1. 克隆仓库

```
cd /home && git clone https://github.com/tangspoon66/BDynamicToWechat.git
```

### 2. 修改server酱的sendkey

```
vi BDynamicToWechat.py
```

![image-20211207170834662](https://picbed.tangspoon.cn/uPic/image-20211207170834662.png)

### 2. 建立uid.txt

```
touch /home/uid.txt
# 添加uid
vi /home/uid.txt
```

### 3. 安装requests模块

```linux
# debian9
apt-get install python-requests -y
# centos
yum install python-requests -y
```

### 4. 换成python3

部署到vps可能会出现如下错误

```
“UnicodeDecodeError: 'ascii' codec can't decode byte 0xc0 in position 7: ordi”
```

这是因为出现系统中默认使用python2，换成python3就可以解决问题

```python
# 删除/usr/bin目录下的python link文件
sudo **rm** -rf /usr/bin/python

# 删除后再建立新的链接关系：
sudo **ln** -s /usr/bin/python3.5 /usr/bin/python
```

```python
# 如果想切换回python2.7
sudo **rm** -rf /usr/bin/pythonsudo **ln** -s /usr/bin/ptyhon2.7 /usr/bin/python
```

### 5. 设置crontab定时任务

```
00 22 * * * python BDynamicToWechat.py
# 每天晚上10点执行任务
```

## 三、效果

<img src="https://picbed.tangspoon.cn/uPic/IMG_3761.jpg" alt="IMG_3761" style="zoom:33%;" />

<img src="https://picbed.tangspoon.cn/uPic/IMG_3762.jpg" alt="IMG_3762" style="zoom:33%;" />

