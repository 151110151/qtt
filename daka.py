# -*-coding:utf-8-*-
"""天体打卡领积分"""
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

requests.packages.urllib3.disable_warnings()

headers = {'vary': 'accept-encoding', 'Connection': 'keep-alive',
           'User-Agent': 'GZSportsWaiter/4.0.1 (iPhone; iOS 14.2; Scale/3.00)'}


def get_resourceId():
    url = 'https://tytapp.quntitong.cn/sportinterNew/androidaccount/userAll.do'
    requests.packages.urllib3.disable_warnings()
    data = {
        'citys': '440100',
        'loginId': '13302565423', 'loginType': 'ios',
        'password': 'A370BC6B6DCF28D3ECC150127FD8B84A', 'service': 'hn'
    }
    res = requests.post(url=url, headers=headers, data=data, verify=False)
    content = eval(res.text)
    resourceId = content[0]['resourceId']
    print(resourceId)
    return resourceId


def daka():
    url = 'https://tytapp.quntitong.cn/sportinterNew/androidsignscore/saveSignDate.do'
    data = {
        'cityName': '广州市', 'citys': '440100',
        # 'deviceid': '22D513B6-7C2F-46D7-A5AC-083A8742BFB8',
        # 'imsi': 'DF1FD6FB4EDF4B96AAD0B296DF741336',
        'mobilephone': '13560376644',
        # 'os': 'ios', 'service': 'hn',
        # 'timestamp': '1620101183',
        'userId': '8a42f49274a48e760174ba3d88b421e9'
    }
    res = requests.post(url, headers=headers, data=data, verify=False)
    print(res.text)


def get_signDate():
    url = 'https://tytapp.quntitong.cn/sportinterNew/androidsignscore/getSignDate.do'
    data = {
        'cityName': '广州市', 'citys': '440100',
        # 'deviceid': '22D513B6-7C2F-46D7-A5AC-083A8742BFB8',
        # 'imsi': 'DF1FD6FB4EDF4B96AAD0B296DF741336',
        'mobilephone': '13560376644',
        # 'os': 'ios', 'service': 'hn',
        # 'timestamp': '1620101180',
        'userId': '8a42f49274a48e760174ba3d88b421e9'
    }
    res = requests.post(url=url, headers=headers, data=data, verify=False)
    print(res.text)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(daka, 'cron', day='*', hour=8, minute=1)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
