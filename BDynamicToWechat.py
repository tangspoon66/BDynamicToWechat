#coding=UTF-8

import requests
import time

dynamic_api = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history'
msg_api = 'https://sctapi.ftqq.com/SCT94144TuDEe5IYr9NNt9vRWbw07TIoV.send'
# # demo3需要先手动输入uid
# uid = ['487425891', '44571203', '31880257', '99157282', '482508159']

# 更新up主的timestamp转str
struct_time = []
timeString = []
uid = []

update_content = []
update_uid = []
space_url = []


# 动态参数

def read_uid():
    with open('/home/uid.txt', 'r') as f:
        uid = f.readlines()
    for i in range(0, len(uid)):
        uid[i] = uid[i].strip('\n')
    return uid


# 用于获取dynamic的时间戳，使用dynamic_api
def get_timestamp():
    for i in range(0, len(uid)):
        # 组合成 host_uid=xxxx 的形式
        params = 'host_uid' + '=' + uid[i]
        # 开始发送get请求
        # html = requests.post(dynamic_api, params=params).json()
        all_content.append((requests.post(dynamic_api, params)).json())
        timestamp.append(all_content[i]['data']['cards'][0]['desc']['timestamp'])
        # 给msg的title参数使用
        uname_list.append(all_content[i]['data']['cards'][0]['desc']['user_profile']['info']['uname'])
        # 获取所有的uid

    return timestamp, uname_list, all_content


# dynamic和system的时间戳转化为20210101的string形式
def format_time():
    # 更新up主的timestamp转20200101格式
    for i in range(0, len(uid)):
        struct_time.append(time.localtime(timestamp[i]))
        # print('struct_time:', struct_time[i])
        timeString.append(time.strftime("%Y%m%d", struct_time[i]))
        # print(timeString[i])

    # systemTime的timestamp转为str
    nowTime = int(time.time())
    nowStruct_time = time.localtime(nowTime)
    nowTimeString = time.strftime("%Y%m%d", nowStruct_time)
    # print(nowTimeString)
    return timeString, nowTimeString


def get_spaceurl():
    nowTimeString = format_time()[1]
    timeString = format_time()[0]
    # 获得update的name和uid

    for i in range(0, len(uname_list)):
        if timeString[i] == nowTimeString:
            update_list.append(uname_list[i])
            # update_uid.append()
            space_url.append('https://space.bilibili.com/' + uid[i] + '/dynamic')
        if i == len(uid) - 1:
            if len(space_url) == 0:
                print('呜呜呜，今日无更新嗷。可以看看书鸭！或者早点睡～')
    print('update_list:', update_list)
    # print(update_uid)
    # print(space_url)
    # print(len(space_url))
    return space_url


# msg to wechat
def msg():
    sendlistStr = ''
    desp_list = []
    desp_str = ''
    # 获取upadtename的字符串
    for i in range(0, len(update_list)):
        sendlistStr = sendlistStr + '，' + '《' + update_list[i] + '》' 
       	desp_list.append(update_list[i] + ' ' + space_url[i] + ' ')
        desp_str = desp_str + '\n\n' + desp_list[i]
    print(desp_str)
    title_params = '有' + str(len(update_list)) + '位你喜欢的up主更新啦!'

    msgData = {
        'title': title_params,
        'desp': desp_str
    }
    requests.post(msg_api, msgData)
    print('有' + str(len(update_list)) + '位你喜欢的up主更新啦!')


if __name__ == '__main__':
    uname_list = []
    update_list = []
    timestamp = []
    all_content = []
    nowTimeString = []
    timeString = []

    # 读取uid列表
    uid = read_uid()
    read_uid()

    timestamp, uname_list, all_content = get_timestamp()

    get_spaceurl()
    msg()
