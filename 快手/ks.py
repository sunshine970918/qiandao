#!/usr/bin/python
# coding=utf-8
import sys
import os
import traceback
import requests
import json
import hashlib

SIGN_LOG = 'logs/kuaishou_sign.log'

work_path = os.path.dirname(os.path.abspath(__file__))
SIGN_LOG_FILE = os.path.join(work_path, SIGN_LOG)


def get_baoxiang(token, __NS_sig3):
    print('💎💎💎💎开始领取宝箱💎💎💎💎')
    access_token = ''
    try:
        url = "https://nebula.kuaishou.com/rest/wd/encourage/unionTask/treasureBox/report?__NS_sig3=" + __NS_sig3 + "&sigCatVer=1"

        # 定义请求头
        headers = {
            "Host": "nebula.kuaishou.com",
            "Connection": "keep-alive",
            "Content-Length": "2",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://nebula.kuaishou.com",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://nebula.kuaishou.com/nebula/task/earning?source=timer&layoutType=4&hyId=nebula_earning",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }

        # 发送 POST 请求
        resp = requests.post(url, headers=headers, data=json.dumps({}))
        resp_json = resp.json()
        if resp_json['result'] == 1:
            title_reward_count = resp_json['data']['title']['rewardCount']
            print(f"得到金币：{title_reward_count}")
        else:
            print(resp_json['error_msg'])
    except:
        print(f"获取异常:{traceback.format_exc()}")

    return access_token


def get_fanbu(token, __NS_sig4):
    print("🍱🍱🍱🍱开始领取饭补🍱🍱🍱🍱")
    try:
        url = "https://encourage.kuaishou.com/rest/wd/encourage/unionTask/dish/report?__NS_sig4=" + __NS_sig4 + "&sigCatVer=1"

        # 定义请求头
        headers = {
            "Host": "encourage.kuaishou.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://encourage.kuaishou.com",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://encourage.kuaishou.com/activity/dish?layoutType=4&encourageEventTracking=W3siZW5jb3VyYWdlX3Rhc2tfaWQiOjIwMDA4LCJlbmNvdXJhZ2VfcmVzb3VyY2VfaWQiOiJlYXJuUGFnZV90YXNrTGlzdF8xNyIsImV2ZW50VHJhY2tpbmdMb2dJbmZvIjpbeyJldmVudFRyYWNraW5nVGFza0lkIjoyMDAwOCwicmVzb3VyY2VJZCI6ImVhcm5QYWdlX3Rhc2tMaXN0XzE3IiwiZXh0UGFyYW1zIjp7fX1dfV0",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }

        # 发送 POST 请求
        resp = requests.post(url, headers=headers, data=json.dumps({}))

        resp_json = resp.json()
        if resp_json['result'] == 1:
            title = resp_json['data']['title']
            dsd = resp_json['data']['amount']
            print(f"{title} 共计: {dsd}")
        else:
            print(resp_json['error_msg'])

    except:
        print(f"获取异常:{traceback.format_exc()}")


def get_money(token):
    print('🥰🥰🥰🥰🥰开始获取当前的现金💰️💰️💰️💰️💰️')
    money = ''
    try:
        url = "https://nebula.kuaishou.com/rest/n/nebula/activity/earn/overview/basicInfo"

        # 定义请求头
        headers = {
            "Host": "nebula.kuaishou.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://nebula.kuaishou.com/nebula/task/earning?source=timer&layoutType=4&hyId=nebula_earning",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }

        # 发送 POST 请求
        resp = requests.get(url, headers=headers)

        resp_json = resp.json()
        money = resp_json['data']['allCash']
        print(f"现在的钱总共：{money}")
    except:
        print(f"获取异常:{traceback.format_exc()}")

    return money


def get_walk(token, __NS_sig4):
    print('🏃🏃🏃🏃🏃开始执行步数换金币🏃🏃🏃🏃🏃')
    try:

        url = "https://encourage.kuaishou.com/rest/wd/encourage/unionTask/walking/detail?__NS_sig4=" + __NS_sig4 + "&sigCatVer=1"
        headers = {
            "Host": "encourage.kuaishou.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.700 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha34 ksNebula/12.5.40.8118 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://encourage.kuaishou.com",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://encourage.kuaishou.com/activity/walk?layoutType=4&source=new_task_center&encourageEventTracking=W3siZW5jb3VyYWdlX3Rhc2tfaWQiOjIwMDQ4LCJlbmNvdXJhZ2VfcmVzb3VyY2VfaWQiOiJlYXJuUGFnZV90YXNrTGlzdF8yMiIsImV2ZW50VHJhY2tpbmdMb2dJbmZvIjpbeyJldmVudFRyYWNraW5nVGFza0lkIjoyMDA0OCwicmVzb3VyY2VJZCI6ImVhcm5QYWdlX3Rhc2tMaXN0XzIyIiwiZXh0UGFyYW1zIjp7fX1dfV0",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }

        data = {"reportCount": 56060, "authorized": True, "stepDataStatus": 1, "updateStepInfo": True}
        # 将 data 转换为 json 字符串，并计算其长度，设置 Content-Length

        data_json = json.dumps(data)
        headers['Content-Length'] = str(len(data_json))

        resp = requests.post(url, headers=headers, json=data)
        # print(resp.text)
        resp_json = resp.json()
        if resp_json['result'] == 1:
            walking_info = resp_json['data']['walkingInfo']
            rewarded = True
            for item in walking_info:
                if item['rewarded'] == False:
                    rewarded = False

            if rewarded == False:
                title = resp_json['data']['button']['text']
                print(f"可以领取:  {title}")

                url = "https://encourage.kuaishou.com/rest/wd/encourage/unionTask/reward?taskId=20048&rewardType=1&__NS_sig4=" + __NS_sig4 + "&sigCatVer=1"
                headers = {
                    "Host": "encourage.kuaishou.com",
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
                    "content-type": "application/json",
                    "Accept": "*/*",
                    "Origin": "https://encourage.kuaishou.com",
                    "X-Requested-With": "com.kuaishou.nebula",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://encourage.kuaishou.com/activity/dish?layoutType=4&encourageEventTracking=W3siZW5jb3VyYWdlX3Rhc2tfaWQiOjIwMDA4LCJlbmNvdXJhZ2VfcmVzb3VyY2VfaWQiOiJlYXJuUGFnZV90YXNrTGlzdF8xNyIsImV2ZW50VHJhY2tpbmdMb2dJbmZvIjpbeyJldmVudFRyYWNraW5nVGFza0lkIjoyMDAwOCwicmVzb3VyY2VJZCI6ImVhcm5QYWdlX3Rhc2tMaXN0XzE3IiwiZXh0UGFyYW1zIjp7fX1dfV0",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cookie": token
                }
                resp = requests.get(url, headers=headers)
                resp_json = resp.json()
                if resp_json['result'] == 1:
                    desc = resp_json['data']['popup']['desc']
                    title = resp_json['data']['popup']['title']
                    print(f"{title} {desc}")
                else:
                    print(resp_json['error_msg'])
            else:
                print(resp_json['data']['button']['text'])
        else:
            print(resp_json['error_msg'])
    except:
        print(f"获取异常:{traceback.format_exc()}")


def get_qiandao(token, __NS_sig3):
    print('❤❤❤❤❤开始执行签到❤❤❤❤❤')
    try:
        url = "https://nebula.kuaishou.com/rest/wd/encourage/unionTask/signIn/report?__NS_sig3=" + __NS_sig3 + "&sigCatVer=1"

        # 定义请求头
        headers = {
            "Host": "nebula.kuaishou.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://nebula.kuaishou.com/nebula/task/earning?source=timer&layoutType=4&hyId=nebula_earning",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }

        # 发送 POST 请求
        resp = requests.get(url, headers=headers)
        resp_json = resp.json()

        # print(resp.text)

        if resp_json['result'] == 1:
            if 'reportRewardResult' in resp_json['data']:
                title = resp_json['data']['reportRewardResult']['awardToast']['title']
                print(f"{title}")
                bsd1 = resp_json['data']['reportRewardResult']['awardToast']['basicSignInAwardResultShow']['bottomText']
                bsd2 = resp_json['data']['reportRewardResult']['awardToast']['basicSignInAwardResultShow']['bottomText']
                print(f"正常：{bsd1}  额外：{bsd2}")
            elif 'signInUnionSpecialAreaData' in resp_json['data']:
                subtitle = resp_json['data']['signInUnionSpecialAreaData']['subtitle']
                todaySignInAmount = resp_json['data']['signInUnionSpecialAreaData']['todaySignInAmount']
                print(f"{subtitle}")
                print(f"今日签到得到：{todaySignInAmount}元")
        else:
            print(resp_json['error_msg'])
    except:
        print(f"获取异常:{traceback.format_exc()}")


# 获取环境变量
_cookie = os.getenv('KSJSB_COOKIE')

# 检查变量是否存在
if _cookie == '':
    print("请先在环境变量里添加 \"KS_COOKIE\" 填写对应快手的 cookie 值")
    exit(0)


def gen_tokensig(sig, salt=""):
    v = sig + salt
    return hashlib.sha256(v.encode('utf-8')).hexdigest()


def gen_sig(params, data):
    dd = dict(params, **data)
    dict_sort_res = dict(sorted(dd.items(), key=lambda x: x[0]))
    ss = ""
    for key, value in dict_sort_res.items():
        if key not in ["sig", "__NS_sig3", "sig2"]:
            ss += f"{key}={value}"
    ss += "ca8e86efb32e"
    return hashlib.md5(ss.encode()).hexdigest()


def main():
    _cookie=""
    get_baoxiang(_cookie, "填写宝箱")
    get_fanbu(_cookie, "饭补")
    get_qiandao(_cookie, "签到")
    get_money(_cookie)


if __name__ == '__main__':
    main()