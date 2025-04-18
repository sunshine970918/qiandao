# !/usr/bin/python3
""#line:8
import hashlib #line:11
import json #line:12
import os #line:13
import random #line:14
import time #line:15
import re #line:16
from datetime import datetime ,timedelta #line:17
from sys import exit #line:18
import requests #line:19
from requests .packages .urllib3 .exceptions import InsecureRequestWarning #line:20
requests .packages .urllib3 .disable_warnings (InsecureRequestWarning )#line:23
IS_DEV =False #line:25
if os .path .isfile ('推送配置.py'):#line:27
    from 推送配置 import send #line:28
    print ("加载通知服务成功！")#line:29
else :#line:30
    print ("加载通知服务失败!")#line:31
send_msg =''#line:32
one_msg =''#line:33
def Log (cont =''):#line:36
    global send_msg ,one_msg #line:37
    print (cont )#line:38
    if cont :#line:39
        one_msg +=f'{cont}\n'#line:40
        send_msg +=f'{cont}\n'#line:41
inviteId =['7B0443273B2249CB9CDB7B48B94DEC13','809FAF1E02D045D7A0DB185E5C91CFB1','','','']#line:47
class RUN :#line:50
    def __init__ (O00OOOOOO0OOOOO00 ,OOO00O0O0000O0OO0 ,O00OO0OOOO0O00O00 ):#line:51
        global one_msg #line:52
        one_msg =''#line:53
        O000OO0O000O0O00O =OOO00O0O0000O0OO0 .split ('@')#line:54
        O00OO0OO0OO0OO0OO =O000OO0O000O0O00O [0 ]#line:55
        O0OOOO0O0000000OO =len (O000OO0O000O0O00O )#line:56
        O0OO000O0OOO0O0O0 =O000OO0O000O0O00O [O0OOOO0O0000000OO -1 ]#line:57
        O00OOOOOO0OOOOO00 .send_UID =None #line:58
        if O0OOOO0O0000000OO >0 and "UID_"in O0OO000O0OOO0O0O0 :#line:59
            O00OOOOOO0OOOOO00 .send_UID =O0OO000O0OOO0O0O0 #line:60
        O00OOOOOO0OOOOO00 .index =O00OO0OOOO0O00O00 +1 #line:61
        Log (f"\n---------开始执行第{O00OOOOOO0OOOOO00.index}个账号>>>>>")#line:62
        if not O00OO0OO0OO0OO0OO :#line:65
            Log (f"账号信息为空，请检查第{O00OOOOOO0OOOOO00.index}个账号")#line:66
            return #line:67
        O00OOOOOO0OOOOO00 .s =requests .session ()#line:68
        O00OOOOOO0OOOOO00 .s .verify =False #line:69
        O00OOOOOO0OOOOO00 .headers ={'Host':'mcs-mimp-web.sf-express.com','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090551) XWEB/6945 Flue','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'none','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','accept-language':'zh-CN,zh','platform':'MINI_PROGRAM',}#line:82
        O00OOOOOO0OOOOO00 .anniversary_black =False #line:83
        O00OOOOOO0OOOOO00 .member_day_black =False #line:84
        O00OOOOOO0OOOOO00 .member_day_red_packet_drew_today =False #line:85
        O00OOOOOO0OOOOO00 .member_day_red_packet_map ={}#line:86
        O00OOOOOO0OOOOO00 .login_res =O00OOOOOO0OOOOO00 .login (O00OO0OO0OO0OO0OO )#line:87
        O00OOOOOO0OOOOO00 .today =datetime .now ().strftime ('%Y-%m-%d')#line:88
        O00OOOOOO0OOOOO00 .answer =False #line:89
        O00OOOOOO0OOOOO00 .max_level =8 #line:90
        O00OOOOOO0OOOOO00 .packet_threshold =1 <<(O00OOOOOO0OOOOO00 .max_level -1 )#line:91
    def get_deviceId (O00O0OOO0O000O0O0 ,characters ='abcdef0123456789'):#line:93
        O0O0O00O0000OO000 =''#line:94
        for OO00O0O00O0O00OO0 in 'xxxxxxxx-xxxx-xxxx':#line:95
            if OO00O0O00O0O00OO0 =='x':#line:96
                O0O0O00O0000OO000 +=random .choice (characters )#line:97
            elif OO00O0O00O0O00OO0 =='X':#line:98
                O0O0O00O0000OO000 +=random .choice (characters ).upper ()#line:99
            else :#line:100
                O0O0O00O0000OO000 +=OO00O0O00O0O00OO0 #line:101
        return O0O0O00O0000OO000 #line:102
    def login (OO0O00O000O0O000O ,OOO00OO0O00O0O0OO ):#line:104
        OOO0O000O0O0O0O00 =OO0O00O000O0O000O .s .get (OOO00OO0O00O0O0OO ,headers =OO0O00O000O0O000O .headers )#line:105
        OO0O00O000O0O000O .user_id =OO0O00O000O0O000O .s .cookies .get_dict ().get ('_login_user_id_','')#line:107
        OO0O00O000O0O000O .phone =OO0O00O000O0O000O .s .cookies .get_dict ().get ('_login_mobile_','')#line:108
        OO0O00O000O0O000O .mobile =OO0O00O000O0O000O .phone [:3 ]+"*"*4 +OO0O00O000O0O000O .phone [7 :]#line:109
        if OO0O00O000O0O000O .phone !='':#line:110
            Log (f'用户:【{OO0O00O000O0O000O.mobile}】登陆成功')#line:111
            return True #line:112
        else :#line:113
            Log (f'获取用户信息失败')#line:114
            return False #line:115
    def getSign (O0000O0OOO0OO0OOO ):#line:117
        OOOOOOO0O0O0OO000 =str (int (round (time .time ()*1000 )))#line:118
        OO0OO000O0000O0O0 ='wwesldfs29aniversaryvdld29'#line:119
        OOOOO000O0000OOOO ='MCS-MIMP-CORE'#line:120
        OOO0OOOOO0OO0OO00 =f'token={OO0OO000O0000O0O0}&timestamp={OOOOOOO0O0O0OO000}&sysCode={OOOOO000O0000OOOO}'#line:121
        OOOO0O000OOOO00O0 =hashlib .md5 (OOO0OOOOO0OO0OO00 .encode ()).hexdigest ()#line:122
        OOO0OOOOO0OO0OO00 ={'sysCode':OOOOO000O0000OOOO ,'timestamp':OOOOOOO0O0O0OO000 ,'signature':OOOO0O000OOOO00O0 }#line:127
        O0000O0OOO0OO0OOO .headers .update (OOO0OOOOO0OO0OO00 )#line:128
        return OOO0OOOOO0OO0OO00 #line:129
    def do_request (O0O0O0O0OOOO0O0O0 ,O00O00000OO00O000 ,data ={},req_type ='post'):#line:131
        O0O0O0O0OOOO0O0O0 .getSign ()#line:132
        try :#line:133
            if req_type .lower ()=='get':#line:134
                OOO0O0O0OOO0O0O0O =O0O0O0O0OOOO0O0O0 .s .get (O00O00000OO00O000 ,headers =O0O0O0O0OOOO0O0O0 .headers )#line:135
            elif req_type .lower ()=='post':#line:136
                OOO0O0O0OOO0O0O0O =O0O0O0O0OOOO0O0O0 .s .post (O00O00000OO00O000 ,headers =O0O0O0O0OOOO0O0O0 .headers ,json =data )#line:137
            else :#line:138
                raise ValueError ('Invalid req_type: %s'%req_type )#line:139
            OO000OOOO0OOOO0O0 =OOO0O0O0OOO0O0O0O .json ()#line:140
            return OO000OOOO0OOOO0O0 #line:141
        except requests .exceptions .RequestException as O0000OOO0000O0O0O :#line:142
            print ('Request failed:',O0000OOO0000O0O0O )#line:143
            return None #line:144
        except json .JSONDecodeError as O0000OOO0000O0O0O :#line:145
            print ('JSON decoding failed:',O0000OOO0000O0O0O )#line:146
            return None #line:147
    def sign (O000000O0O0OOO0OO ):#line:149
        print (f'>>>>>>开始执行签到')#line:150
        OOO0OOO0O0O0OOO0O ={"comeFrom":"vioin","channelFrom":"WEIXIN"}#line:151
        OOOO0O0O00O00OO00 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~integralTaskSignPlusService~automaticSignFetchPackage'#line:152
        O0000O0O0O0OOOOOO =O000000O0O0OOO0OO .do_request (OOOO0O0O00O00OO00 ,data =OOO0OOO0O0O0OOO0O )#line:153
        if O0000O0O0O0OOOOOO .get ('success')==True :#line:155
            O0OO00O0O0O0OOO0O =O0000O0O0O0OOOOOO .get ('obj',{}).get ('countDay',0 )#line:156
            if O0000O0O0O0OOOOOO .get ('obj')and O0000O0O0O0OOOOOO ['obj'].get ('integralTaskSignPackageVOList'):#line:157
                O000OOO00O0000OO0 =O0000O0O0O0OOOOOO ["obj"]["integralTaskSignPackageVOList"][0 ]["packetName"]#line:158
                Log (f'>>>签到成功，获得【{O000OOO00O0000OO0}】，本周累计签到【{O0OO00O0O0O0OOO0O + 1}】天')#line:159
            else :#line:160
                Log (f'今日已签到，本周累计签到【{O0OO00O0O0O0OOO0O + 1}】天')#line:161
        else :#line:162
            print (f'签到失败！原因：{O0000O0O0O0OOOOOO.get("errorMessage")}')#line:163
    def superWelfare_receiveRedPacket (OOOOOOOO00O0O00OO ):#line:165
        print ('>>>>>>超值福利签到')#line:166
        OO00O0OO000000OO0 ={'channel':'czflqdlhbxcx'}#line:169
        O00OOO00O00OO00OO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberActLengthy~redPacketActivityService~superWelfare~receiveRedPacket'#line:170
        O0O0O00000000OOOO =OOOOOOOO00O0O00OO .do_request (O00OOO00O00OO00OO ,data =OO00O0OO000000OO0 )#line:171
        if O0O0O00000000OOOO .get ('success')==True :#line:173
            O0OOO00000O0OO000 =O0O0O00000000OOOO .get ('obj',{}).get ('giftList',[])#line:174
            O00OO00OOO000OOOO =O0O0O00000000OOOO .get ('obj',{}).get ('extraGiftList',[])#line:175
            if O00OO00OOO000OOOO :#line:176
                O0OOO00000O0OO000 .extend (O00OO00OOO000OOOO )#line:177
            if O0OOO00000O0OO000 :#line:178
                for O00O0O0000OO0OOOO in O0OOO00000O0OO000 :#line:179
                    print (f"礼物名称: {O00O0O0000OO0OOOO['giftName']}")#line:180
                OOOOOO0OO0O0OOOOO =O0O0O00000000OOOO .get ('obj',{}).get ('receiveStatus')#line:181
                O0O00OO0OO0OO00O0 ='领取成功'if OOOOOO0OO0O0OOOOO ==1 else '已领取过'#line:182
                Log (f'超值福利签到[{O0O00OO0OO0OO00O0}]')#line:183
            else :#line:184
                Log ('没有可领取的礼物')#line:185
        else :#line:186
            O0O00O0O0000O000O =O0O0O00000000OOOO .get ('errorMessage')or json .dumps (O0O0O00000000OOOO )or '无返回'#line:187
            print (f'超值福利签到失败: {O0O00O0O0000O000O}')#line:188
    def get_SignTaskList (O000O00O00O000OOO ,END =False ):#line:190
        if not END :print (f'>>>开始获取签到任务列表')#line:191
        O00000OO0O0O0O000 ={'channelType':'3','deviceId':O000O00O00O000OOO .get_deviceId (),}#line:195
        O0O0O0O0OO000O0O0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~integralTaskStrategyService~queryPointTaskAndSignFromES'#line:196
        O0O0O0OOOO0O0000O =O000O00O00O000OOO .do_request (O0O0O0O0OO000O0O0 ,data =O00000OO0O0O0O000 )#line:197
        if O0O0O0OOOO0O0000O .get ('success')==True and O0O0O0OOOO0O0000O .get ('obj')!=[]:#line:199
            OOOO0OO000000O000 =O0O0O0OOOO0O0000O ["obj"]["totalPoint"]#line:200
            if END :#line:201
                Log (f'当前积分：【{OOOO0OO000000O000}】')#line:202
                return #line:203
            Log (f'执行前积分：【{OOOO0OO000000O000}】')#line:204
            for OOO00O0OOOOOOO00O in O0O0O0OOOO0O0000O ["obj"]["taskTitleLevels"]:#line:205
                O000O00O00O000OOO .taskId =OOO00O0OOOOOOO00O ["taskId"]#line:206
                O000O00O00O000OOO .taskCode =OOO00O0OOOOOOO00O ["taskCode"]#line:207
                O000O00O00O000OOO .strategyId =OOO00O0OOOOOOO00O ["strategyId"]#line:208
                O000O00O00O000OOO .title =OOO00O0OOOOOOO00O ["title"]#line:209
                O0OOOO000O0O0OO00 =OOO00O0OOOOOOO00O ["status"]#line:210
                OOO0O00O0OOO0OO00 =['用行业模板寄件下单','去新增一个收件偏好','参与积分活动']#line:211
                if O0OOOO000O0O0OO00 ==3 :#line:212
                    print (f'>{O000O00O00O000OOO.title}-已完成')#line:213
                    continue #line:214
                if O000O00O00O000OOO .title in OOO0O00O0OOO0OO00 :#line:215
                    print (f'>{O000O00O00O000OOO.title}-跳过')#line:216
                    continue #line:217
                else :#line:218
                    O000O00O00O000OOO .doTask ()#line:222
                    time .sleep (3 )#line:223
                O000O00O00O000OOO .receiveTask ()#line:224
    def doTask (OOO000O0O0OO0O0O0 ):#line:226
        print (f'>>>开始去完成【{OOO000O0O0OO0O0O0.title}】任务')#line:227
        O0O000O00O00OO0O0 ={'taskCode':OOO000O0O0OO0O0O0 .taskCode ,}#line:230
        O000OO000O000000O ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonRoutePost/memberEs/taskRecord/finishTask'#line:231
        OOO00OOOO0O0O0000 =OOO000O0O0OO0O0O0 .do_request (O000OO000O000000O ,data =O0O000O00O00OO0O0 )#line:232
        if OOO00OOOO0O0O0000 .get ('success')==True :#line:233
            print (f'>【{OOO000O0O0OO0O0O0.title}】任务-已完成')#line:234
        else :#line:235
            print (f'>【{OOO000O0O0OO0O0O0.title}】任务-{OOO00OOOO0O0O0000.get("errorMessage")}')#line:236
    def receiveTask (OOO000OOO00OOO0OO ):#line:238
        print (f'>>>开始领取【{OOO000OOO00OOO0OO.title}】任务奖励')#line:239
        O0O00000O0000O000 ={"strategyId":OOO000OOO00OOO0OO .strategyId ,"taskId":OOO000OOO00OOO0OO .taskId ,"taskCode":OOO000OOO00OOO0OO .taskCode ,"deviceId":OOO000OOO00OOO0OO .get_deviceId ()}#line:245
        OOO0OO0O0000OO0OO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~integralTaskStrategyService~fetchIntegral'#line:246
        O0O000O00OOOOO0O0 =OOO000OOO00OOO0OO .do_request (OOO0OO0O0000OO0OO ,data =O0O00000O0000O000 )#line:247
        if O0O000O00OOOOO0O0 .get ('success')==True :#line:248
            print (f'>【{OOO000OOO00OOO0OO.title}】任务奖励领取成功！')#line:249
        else :#line:250
            print (f'>【{OOO000OOO00OOO0OO.title}】任务-{O0O000O00OOOOO0O0.get("errorMessage")}')#line:251
    def do_honeyTask (OOO0OO0OOOO00OO0O ):#line:253
        O00O00000OO00O0O0 ={"taskCode":OOO0OO0OOOO00OO0O .taskCode }#line:255
        O0O000000O00O00OO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberEs~taskRecord~finishTask'#line:256
        OOOO00OO0OOOOOO00 =OOO0OO0OOOO00OO0O .do_request (O0O000000O00O00OO ,data =O00O00000OO00O0O0 )#line:257
        if OOOO00OO0OOOOOO00 .get ('success')==True :#line:258
            print (f'>【{OOO0OO0OOOO00OO0O.taskType}】任务-已完成')#line:259
        else :#line:260
            print (f'>【{OOO0OO0OOOO00OO0O.taskType}】任务-{OOOO00OO0OOOOOO00.get("errorMessage")}')#line:261
    def receive_honeyTask (O000O0O0O00000000 ):#line:263
        print ('>>>执行收取丰蜜任务')#line:264
        O000O0O0O00000000 .headers ['syscode']='MCS-MIMP-CORE'#line:266
        O000O0O0O00000000 .headers ['channel']='wxwdsj'#line:267
        O000O0O0O00000000 .headers ['accept']='application/json, text/plain, */*'#line:268
        O000O0O0O00000000 .headers ['content-type']='application/json;charset=UTF-8'#line:269
        O000O0O0O00000000 .headers ['platform']='MINI_PROGRAM'#line:270
        OO00O0O0O0000OO0O ={"taskType":O000O0O0O00000000 .taskType }#line:271
        O00OO0O0OOOO00OOO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~receiveExchangeIndexService~receiveHoney'#line:273
        O0O0000OOO0OOO00O =O000O0O0O00000000 .do_request (O00OO0O0OOOO00OOO ,data =OO00O0O0O0000OO0O )#line:274
        if O0O0000OOO0OOO00O .get ('success')==True :#line:275
            print (f'收取任务【{O000O0O0O00000000.taskType}】成功！')#line:276
        else :#line:277
            print (f'收取任务【{O000O0O0O00000000.taskType}】失败！原因：{O0O0000OOO0OOO00O.get("errorMessage")}')#line:278
    def get_coupom (OO0O00O00OOO000O0 ):#line:280
        print ('>>>执行领取生活权益领券任务')#line:281
        OO0OO000OOOOO0OOO ={"from":"Point_Mall","orderSource":"POINT_MALL_EXCHANGE","goodsNo":OO0O00O00OOO000O0 .goodsNo ,"quantity":1 ,"taskCode":OO0O00O00OOO000O0 .taskCode }#line:291
        O00OO0000OOO0OOOO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberGoods~pointMallService~createOrder'#line:292
        OOOOOO000O00O0OO0 =OO0O00O00OOO000O0 .do_request (O00OO0000OOO0OOOO ,data =OO0OO000OOOOO0OOO )#line:293
        if OOOOOO000O00O0OO0 .get ('success')==True :#line:294
            print (f'>领券成功！')#line:295
        else :#line:296
            print (f'>领券失败！原因：{OOOOOO000O00O0OO0.get("errorMessage")}')#line:297
    def get_coupom_list (O0O00OOO0000O00O0 ):#line:299
        print ('>>>获取生活权益券列表')#line:300
        OO00000OO0O00O000 ={"memGrade":1 ,"categoryCode":"SHTQ","showCode":"SHTQWNTJ"}#line:308
        OOOOO0OO0OOOOOOO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberGoods~mallGoodsLifeService~list'#line:309
        O00OO0OOO0000OO0O =O0O00OOO0000O00O0 .do_request (OOOOO0OO0OOOOOOO0 ,data =OO00000OO0O00O000 )#line:310
        if O00OO0OOO0000OO0O .get ('success')==True :#line:312
            OO0OO0O00O00O00OO =O00OO0OOO0000OO0O ["obj"][0 ]["goodsList"]#line:313
            for O00OOOOOO0000OOO0 in OO0OO0O00O00O00OO :#line:314
                O0000OOO0O00OO0O0 =O00OOOOOO0000OOO0 ['exchangeTimesLimit']#line:315
                if O0000OOO0O00OO0O0 >=7 :#line:316
                    O0O00OOO0000O00O0 .goodsNo =O00OOOOOO0000OOO0 ['goodsNo']#line:317
                    print (f'当前选择券号：{O0O00OOO0000O00O0.goodsNo}')#line:318
                    O0O00OOO0000O00O0 .get_coupom ()#line:319
                    break #line:320
        else :#line:321
            print (f'>领券失败！原因：{O00OO0OOO0000OO0O.get("errorMessage")}')#line:322
    def get_honeyTaskListStart (OO00O0O0000OOO00O ):#line:324
        print ('>>>开始获取采蜜换大礼任务列表')#line:325
        OOOO000O0OO0OOOOO ={}#line:327
        OO00O0O0000OOO00O .headers ['channel']='wxwdsj'#line:328
        O00OOOOO0O0000O0O ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~receiveExchangeIndexService~taskDetail'#line:329
        OOOOOO0O00OOOOO0O =OO00O0O0000OOO00O .do_request (O00OOOOO0O0000O0O ,data =OOOO000O0OO0OOOOO )#line:331
        if OOOOOO0O00OOOOO0O .get ('success')==True :#line:333
            for O00O0OOO00OOO00OO in OOOOOO0O00OOOOO0O ["obj"]["list"]:#line:334
                OO00O0O0000OOO00O .taskType =O00O0OOO00OOO00OO ["taskType"]#line:335
                OO00OO00O0OOOOOO0 =O00O0OOO00OOO00OO ["status"]#line:336
                if OO00OO00O0OOOOOO0 ==3 :#line:337
                    print (f'>【{OO00O0O0000OOO00O.taskType}】-已完成')#line:338
                    if OO00O0O0000OOO00O .taskType =='BEES_GAME_TASK_TYPE':#line:339
                        OO00O0O0000OOO00O .bee_need_help =False #line:340
                    continue #line:341
                if "taskCode"in O00O0OOO00OOO00OO :#line:342
                    OO00O0O0000OOO00O .taskCode =O00O0OOO00OOO00OO ["taskCode"]#line:343
                    if OO00O0O0000OOO00O .taskType =='DAILY_VIP_TASK_TYPE':#line:344
                        OO00O0O0000OOO00O .get_coupom_list ()#line:345
                    else :#line:346
                        OO00O0O0000OOO00O .do_honeyTask ()#line:347
                if OO00O0O0000OOO00O .taskType =='BEES_GAME_TASK_TYPE':#line:348
                    OO00O0O0000OOO00O .honey_damaoxian ()#line:349
                time .sleep (2 )#line:350
    def honey_damaoxian (O0O0OO00000O00O00 ):#line:352
        print ('>>>执行大冒险任务')#line:353
        OOOO0OO0OOO0OO0O0 =5 #line:355
        for OO0O00O000OOO000O in range (1 ,OOOO0OO0OOO0OO0O0 ):#line:356
            OO000O00O00O00000 ={'gatherHoney':20 ,}#line:359
            if OOOO0OO0OOO0OO0O0 <0 :break #line:360
            print (f'>>开始第{OO0O00O000OOO000O}次大冒险')#line:361
            OO00OOO0OO00OOOOO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~receiveExchangeGameService~gameReport'#line:362
            OO0OO0OOO0OOOO00O =O0O0OO00000O00O00 .do_request (OO00OOO0OO00OOOOO ,data =OO000O00O00O00000 )#line:363
            O00O00000O0O000OO =OO0OO0OOO0OOOO00O .get ('success')#line:365
            if O00O00000O0O000OO :#line:366
                OOOO0OO0OOO0OO0O0 =OO0OO0OOO0OOOO00O .get ('obj')['gameNum']#line:367
                print (f'>大冒险成功！剩余次数【{OOOO0OO0OOO0OO0O0}】')#line:368
                time .sleep (2 )#line:369
                OOOO0OO0OOO0OO0O0 -=1 #line:370
            elif OO0OO0OOO0OOOO00O .get ("errorMessage")=='容量不足':#line:371
                print (f'> 需要扩容')#line:372
                O0O0OO00000O00O00 .honey_expand ()#line:373
            else :#line:374
                print (f'>大冒险失败！【{OO0OO0OOO0OOOO00O.get("errorMessage")}】')#line:375
                break #line:376
    def honey_expand (O0O0O0O0000OO00O0 ):#line:378
        print ('>>>容器扩容')#line:379
        O0OOOO00OOO00O0O0 =5 #line:381
        O0O000OOO0OO0OOO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~receiveExchangeIndexService~expand'#line:383
        OOOO0OO00000OO0OO =O0O0O0O0000OO00O0 .do_request (O0O000OOO0OO0OOO0 ,data ={})#line:384
        OOO00O00O00O0O000 =OOOO0OO00000OO0OO .get ('success',False )#line:386
        if OOO00O00O00O0O000 :#line:387
            O0000O00O0OO00OO0 =OOOO0OO00000OO0OO .get ('obj')#line:388
            print (f'>成功扩容【{O0000O00O0OO00OO0}】容量')#line:389
        else :#line:390
            print (f'>扩容失败！【{OOOO0OO00000OO0OO.get("errorMessage")}】')#line:391
    def honey_indexData (OO0O0OOO0O0O0000O ,END =False ):#line:393
        if not END :print ('\n>>>>>>>开始执行采蜜换大礼任务')#line:394
        O0O0000O0OO00OOOO =random .choice ([OO00OO00000OO0000 for OO00OO00000OO0000 in inviteId if OO00OO00000OO0000 !=OO0O0OOO0O0O0000O .user_id ])#line:396
        OO0O0OOO0O0O0000O .headers ['channel']='wxwdsj'#line:397
        O0O00O000O0000O0O ={"inviteUserId":O0O0000O0OO00OOOO }#line:398
        OOO000O00O0O0OOO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~receiveExchangeIndexService~indexData'#line:399
        O0O0000000O00OOO0 =OO0O0OOO0O0O0000O .do_request (OOO000O00O0O0OOO0 ,data =O0O00O000O0000O0O )#line:400
        if O0O0000000O00OOO0 .get ('success')==True :#line:401
            O000O0O0O00OOO000 =O0O0000000O00OOO0 .get ('obj').get ('usableHoney')#line:402
            if END :#line:403
                Log (f'当前丰蜜：【{O000O0O0O00OOO000}】')#line:404
                return #line:405
            Log (f'执行前丰蜜：【{O000O0O0O00OOO000}】')#line:406
            OOOOOOOOOOOOOO00O =O0O0000000O00OOO0 .get ('obj').get ('taskDetail')#line:407
            O0O0OOOO0O0OOO0OO =O0O0000000O00OOO0 .get ('obj').get ('activityEndTime','')#line:408
            O0O0O00000O000O0O =datetime .strptime (O0O0OOOO0O0OOO0OO ,"%Y-%m-%d %H:%M:%S")#line:409
            OOOO0OOO000OOOO00 =datetime .now ()#line:410
            if OOOO0OOO000OOOO00 .date ()==O0O0O00000O000O0O .date ():#line:412
                Log ("本期活动今日结束，请及时兑换")#line:413
            else :#line:414
                print (f'本期活动结束时间【{O0O0OOOO0O0OOO0OO}】')#line:415
            if OOOOOOOOOOOOOO00O !=[]:#line:417
                for O0OOOO0OOO00O0OOO in OOOOOOOOOOOOOO00O :#line:418
                    OO0O0OOO0O0O0000O .taskType =O0OOOO0OOO00O0OOO ['type']#line:419
                    OO0O0OOO0O0O0000O .receive_honeyTask ()#line:420
                    time .sleep (2 )#line:421
    def EAR_END_2023_TaskList (O000O00O000OO00O0 ):#line:423
        print ('\n>>>>>>开始年终集卡任务')#line:424
        OOOO0O00OOOO0O0O0 ={"activityCode":"YEAR_END_2023","channelType":"MINI_PROGRAM"}#line:429
        O000O00O000OO00O0 .headers ['channel']='xcx23nz'#line:430
        O000O00O000OO00O0 .headers ['platform']='MINI_PROGRAM'#line:431
        O000O00O000OO00O0 .headers ['syscode']='MCS-MIMP-CORE'#line:432
        O0O0O0OOO00OO0OO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~activityTaskService~taskList'#line:434
        OOO00OOOO0O0000O0 =O000O00O000OO00O0 .do_request (O0O0O0OOO00OO0OO0 ,data =OOOO0O00OOOO0O0O0 )#line:436
        if OOO00OOOO0O0000O0 .get ('success')==True :#line:438
            for O000O0O00OO00O0O0 in OOO00OOOO0O0000O0 ["obj"]:#line:439
                O000O00O000OO00O0 .title =O000O0O00OO00O0O0 ["taskName"]#line:440
                O000O00O000OO00O0 .taskType =O000O0O00OO00O0O0 ["taskType"]#line:441
                O0000OO0O00O00000 =O000O0O00OO00O0O0 ["status"]#line:442
                if O0000OO0O00O00000 ==3 :#line:443
                    print (f'>【{O000O00O000OO00O0.taskType}】-已完成')#line:444
                    continue #line:445
                if O000O00O000OO00O0 .taskType =='INTEGRAL_EXCHANGE':#line:446
                    O000O00O000OO00O0 .EAR_END_2023_ExchangeCard ()#line:447
                elif O000O00O000OO00O0 .taskType =='CLICK_MY_SETTING':#line:448
                    O000O00O000OO00O0 .taskCode =O000O0O00OO00O0O0 ["taskCode"]#line:449
                    O000O00O000OO00O0 .addDeliverPrefer ()#line:450
                if "taskCode"in O000O0O00OO00O0O0 :#line:451
                    O000O00O000OO00O0 .taskCode =O000O0O00OO00O0O0 ["taskCode"]#line:452
                    O000O00O000OO00O0 .doTask ()#line:453
                    time .sleep (3 )#line:454
                    O000O00O000OO00O0 .EAR_END_2023_receiveTask ()#line:455
                else :#line:456
                    print (f'暂时不支持【{O000O00O000OO00O0.title}】任务')#line:457
        O000O00O000OO00O0 .EAR_END_2023_getAward ()#line:460
        O000O00O000OO00O0 .EAR_END_2023_GuessIdiom ()#line:461
    def addDeliverPrefer (O0O0000OO0000OO0O ):#line:463
        print (f'>>>开始【{O0O0000OO0000OO0O.title}】任务')#line:464
        O0OOO000OO00OOO00 ={"country":"中国","countryCode":"A000086000","province":"北京市","provinceCode":"A110000000","city":"北京市","cityCode":"A111000000","county":"东城区","countyCode":"A110101000","address":"1号楼1单元101","latitude":"","longitude":"","memberId":"","locationCode":"010","zoneCode":"CN","postCode":"","takeWay":"7","callBeforeDelivery":'false',"deliverTag":"2,3,4,1","deliverTagContent":"","startDeliverTime":"","selectCollection":'false',"serviceName":"","serviceCode":"","serviceType":"","serviceAddress":"","serviceDistance":"","serviceTime":"","serviceTelephone":"","channelCode":"RW11111","taskId":O0O0000OO0000OO0O .taskId ,"extJson":"{\"noDeliverDetail\":[]}"}#line:497
        OOOO00O000OOOO0O0 ='https://ucmp.sf-express.com/cx-wechat-member/member/deliveryPreference/addDeliverPrefer'#line:498
        OOO0O00OO0OO00O0O =O0O0000OO0000OO0O .do_request (OOOO00O000OOOO0O0 ,data =O0OOO000OO00OOO00 )#line:499
        if OOO0O00OO0OO00O0O .get ('success')==True :#line:500
            print ('新增一个收件偏好，成功')#line:501
        else :#line:502
            print (f'>【{O0O0000OO0000OO0O.title}】任务-{OOO0O00OO0OO00O0O.get("errorMessage")}')#line:503
    def EAR_END_2023_ExchangeCard (OOO000000OOOO000O ):#line:505
        print (f'>>>开始积分兑换年卡')#line:506
        O0OO0OOOOO0O00OO0 ={"exchangeNum":2 ,"activityCode":"YEAR_END_2023","channelType":"MINI_PROGRAM"}#line:511
        O00OO00OOOOOOO00O ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonNoLoginPost/~memberNonactivity~yearEnd2023TaskService~integralExchange'#line:512
        O0OO00OO00000O000 =OOO000000OOOO000O .do_request (O00OO00OOOOOOO00O ,data =O0OO0OOOOO0O00OO0 )#line:513
        if O0OO00OO00000O000 .get ('success')==True :#line:514
            OO00O00OOO000OOOO =O0OO00OO00000O000 ['obj']['receivedAccountList']#line:515
            for O0O000000O0OOO00O in OO00O00OOO000OOOO :#line:516
                print (f'>获得：【{O0O000000O0OOO00O["urrency"]}】卡【{O0O000000O0OOO00O["amount"]}】张！')#line:517
        else :#line:518
            print (f'>【{OOO000000OOOO000O.title}】任务-{O0OO00OO00000O000.get("errorMessage")}')#line:519
    def EAR_END_2023_getAward (OOOOOO0OOO000OO00 ):#line:521
        print (f'>>>开始抽卡')#line:522
        OOO000O0O00O0OOO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~yearEnd2023GardenPartyService~getAward'#line:523
        for O00000O0OOOOOOO0O in range (10 ):#line:524
            for OOO000O0O0O0OOOOO in range (0 ,3 ):#line:525
                O0O0O0OO0OO00OO00 ={"cardType":OOO000O0O0O0OOOOO }#line:528
                OO0OOO0OO0O0OO0OO =OOOOOO0OOO000OO00 .do_request (OOO000O0O00O0OOO0 ,data =O0O0O0OO0OO00OO00 )#line:529
                if OO0OOO0OO0O0OO0OO .get ('success')==True :#line:531
                    OO00OO00O0O0OOOO0 =OO0OOO0OO0O0OO0OO ['obj']['receivedAccountList']#line:532
                    for O0O0O0O00000OOO0O in OO00OO00O0O0OOOO0 :#line:533
                        print (f'>获得：【{O0O0O0O00000OOO0O["currency"]}】卡【{O0O0O0O00000OOO0O["amount"]}】张！')#line:534
                elif OO0OOO0OO0O0OO0OO .get ('errorMessage')=='达到限流阈值，请稍后重试':#line:535
                    break #line:536
                elif OO0OOO0OO0O0OO0OO .get ('errorMessage')=='用户信息失效，请退出重新进入':#line:537
                    break #line:538
                else :#line:539
                    print (f'>抽卡失败：{OO0OOO0OO0O0OO0OO.get("errorMessage")}')#line:540
                time .sleep (3 )#line:541
    def EAR_END_2023_GuessIdiom (OOOOOOO0000OOOOOO ):#line:543
        print (f'>>>开始猜成语')#line:544
        OOO000OOO00OOOOO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~yearEnd2023GuessIdiomService~win'#line:545
        for O0OO0O0O00OOO0OO0 in range (1 ,11 ):#line:546
            O00OOO0000O00000O ={"index":O0OO0O0O00OOO0OO0 }#line:549
            OO000OO0OOOO0O000 =OOOOOOO0000OOOOOO .do_request (OOO000OOO00OOOOO0 ,data =O00OOO0000O00000O )#line:550
            if OO000OO0OOOO0O000 .get ('success')==True :#line:551
                print (f'第{O0OO0O0O00OOO0OO0}关成功！')#line:552
            else :#line:556
                print (f'第{O0OO0O0O00OOO0OO0}关失败！')#line:557
    def EAR_END_2023_receiveTask (OO0O0OOO0OO000000 ):#line:559
        print (f'>>>开始领取【{OO0O0OOO0OO000000.title}】任务奖励')#line:560
        OOO000O0O000OOO00 ={"taskType":OO0O0OOO0OO000000 .taskType ,"activityCode":"YEAR_END_2023","channelType":"MINI_PROGRAM"}#line:565
        OO0OO00OO00OOO0O0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonNoLoginPost/~memberNonactivity~yearEnd2023TaskService~fetchMixTaskReward'#line:566
        OO00O0O00O0000OO0 =OO0O0OOO0OO000000 .do_request (OO0OO00OO00OOO0O0 ,data =OOO000O0O000OOO00 )#line:567
        if OO00O0O00O0000OO0 .get ('success')==True :#line:568
            print (f'>【{OO0O0OOO0OO000000.title}】任务奖励领取成功！')#line:569
        else :#line:570
            print (f'>【{OO0O0OOO0OO000000.title}】任务-{OO00O0O00O0000OO0.get("errorMessage")}')#line:571
    def anniversary2024_weekly_gift_status (O0O000O0O000O00OO ):#line:573
        print (f'\n>>>>>>>开始周年庆任务')#line:574
        O000OO00OO00O00O0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024IndexService~weeklyGiftStatus'#line:575
        OO00OO0OOO0O0O00O =O0O000O0O000O00OO .do_request (O000OO00OO00O00O0 )#line:576
        if OO00OO0OOO0O0O00O .get ('success')==True :#line:577
            OO000OOO00O0OO00O =OO00OO0OOO0O0O00O .get ('obj',{}).get ('weeklyGiftList',[])#line:578
            for O0OO00O000O0O00O0 in OO000OOO00O0OO00O :#line:579
                if not O0OO00O000O0O00O0 .get ('received'):#line:580
                    OOOO00O0OOOO00O0O =datetime .strptime (O0OO00O000O0O00O0 ['receiveStartTime'],'%Y-%m-%d %H:%M:%S')#line:581
                    OOOOO0O0OO0O0O0O0 =datetime .strptime (O0OO00O000O0O00O0 ['receiveEndTime'],'%Y-%m-%d %H:%M:%S')#line:582
                    OO0OO0OO0OO0O00OO =datetime .now ()#line:583
                    if OOOO00O0OOOO00O0O <=OO0OO0OO0OO0O00OO <=OOOOO0O0OO0O0O0O0 :#line:587
                        O0O000O0O000O00OO .anniversary2024_receive_weekly_gift ()#line:588
        else :#line:589
            O00000000O0O00OO0 =OO00OO0OOO0O0O00O .get ('errorMessage')or json .dumps (OO00OO0OOO0O0O00O )or '无返回'#line:590
            print (f'查询每周领券失败: {O00000000O0O00OO0}')#line:591
            if '系统繁忙'in O00000000O0O00OO0 or '用户手机号校验未通过'in O00000000O0O00OO0 :#line:592
                O0O000O0O000O00OO .anniversary_black =True #line:593
    def anniversary2024_receive_weekly_gift (O00OOOO0O00000O00 ):#line:595
        print (f'>>>开始领取每周领券')#line:596
        OOO0O0OOO00O00OOO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024IndexService~receiveWeeklyGift'#line:597
        OO0OO000O000OO0OO =O00OOOO0O00000O00 .do_request (OOO0O0OOO00O00OOO )#line:598
        if OO0OO000O000OO0OO .get ('success'):#line:599
            O00000OOOOO000000 =[OO0000000OO0OOO0O ['productName']for OO0000000OO0OOO0O in OO0OO000O000OO0OO .get ('obj',[])]#line:600
            print (f'每周领券: {O00000OOOOO000000}')#line:601
        else :#line:602
            O0OOOOO00OO0OO000 =OO0OO000O000OO0OO .get ('errorMessage')or json .dumps (OO0OO000O000OO0OO )or '无返回'#line:603
            print (f'每周领券失败: {O0OOOOO00OO0OO000}')#line:604
            if '系统繁忙'in O0OOOOO00OO0OO000 or '用户手机号校验未通过'in O0OOOOO00OO0OO000 :#line:605
                O00OOOO0O00000O00 .anniversary_black =True #line:606
    def anniversary2024_taskList (O00OO0OOO00O00O00 ):#line:608
        O000O000O0O0OO0OO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~activityTaskService~taskList'#line:609
        O0OO0O00O0O0O0000 ={'activityCode':'ANNIVERSARY_2024','channelType':'MINI_PROGRAM'}#line:613
        O0000000000OOO0OO =O00OO0OOO00O00O00 .do_request (O000O000O0O0OO0OO ,O0OO0O00O0O0O0000 )#line:614
        if O0000000000OOO0OO and O0000000000OOO0OO .get ('success'):#line:615
            OOO0OO0O00O000OOO =O0000000000OOO0OO .get ('obj',[])#line:616
            for OO00O0O000000O00O in filter (lambda O0O0000O0000O00OO :O0O0000O0000O00OO ['status']==1 ,OOO0OO0O00O000OOO ):#line:618
                if O00OO0OOO00O00O00 .anniversary_black :#line:619
                    return #line:620
                for _OO000OO000OOOOO00 in range (OO00O0O000000O00O ['canReceiveTokenNum']):#line:621
                    O00OO0OOO00O00O00 .anniversary2024_fetchMixTaskReward (OO00O0O000000O00O )#line:622
            for OO00O0O000000O00O in filter (lambda O0OOO0O00OOOO0000 :O0OOO0O00OOOO0000 ['status']==2 ,OOO0OO0O00O000OOO ):#line:624
                if O00OO0OOO00O00O00 .anniversary_black :#line:625
                    return #line:626
                if OO00O0O000000O00O ['taskType']in ['PLAY_ACTIVITY_GAME','PLAY_HAPPY_ELIMINATION','PARTAKE_SUBJECT_GAME']:#line:627
                    pass #line:628
                elif OO00O0O000000O00O ['taskType']=='FOLLOW_SFZHUNONG_VEDIO_ID':#line:629
                    pass #line:630
                elif OO00O0O000000O00O ['taskType']in ['BROWSE_VIP_CENTER','GUESS_GAME_TIP','CREATE_SFID','CLICK_MY_SETTING','CLICK_TEMPLATE','REAL_NAME','SEND_SUCCESS_RECALL','OPEN_SVIP','OPEN_FAST_CARD','FIRST_CHARGE_NEW_EXPRESS_CARD','CHARGE_NEW_EXPRESS_CARD','INTEGRAL_EXCHANGE']:#line:634
                    pass #line:635
                else :#line:636
                    for _OO000OO000OOOOO00 in range (OO00O0O000000O00O ['restFinishTime']):#line:637
                        if O00OO0OOO00O00O00 .anniversary_black :#line:638
                            break #line:639
                        O00OO0OOO00O00O00 .anniversary2024_finishTask (OO00O0O000000O00O )#line:640
    def anniversary2024_finishTask (O0O0O00OOOO00000O ,OOO00O0000O00OOOO ):#line:642
        OOO00OOO00O0OOOOO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonRoutePost/memberEs/taskRecord/finishTask'#line:643
        O000O0OOO0O0OO0O0 ={'taskCode':OOO00O0000O00OOOO ['taskCode']}#line:644
        O0O0OO00OO0O0000O =O0O0O00OOOO00000O .do_request (OOO00OOO00O0OOOOO ,O000O0OOO0O0OO0O0 )#line:645
        if O0O0OO00OO0O0000O and O0O0OO00OO0O0000O .get ('success'):#line:646
            print ('完成任务[%s]成功'%OOO00O0000O00OOOO ['taskName'])#line:647
            O0O0O00OOOO00000O .anniversary2024_fetchMixTaskReward (OOO00O0000O00OOOO )#line:649
        else :#line:650
            print ('完成任务[%s]失败: %s'%(OOO00O0000O00OOOO ['taskName'],O0O0OO00OO0O0000O .get ('errorMessage')or (json .dumps (O0O0OO00OO0O0000O )if O0O0OO00OO0O0000O else '无返回')))#line:652
    def anniversary2024_fetchMixTaskReward (O0OOO0O00OOOO0OOO ,OO0OO0OOO0OO00OOO ):#line:654
        O0O000000000O0O0O ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024TaskService~fetchMixTaskReward'#line:655
        OOO000O00OOOOO0O0 ={'taskType':OO0OO0OOO0OO00OOO ['taskType'],'activityCode':'ANNIVERSARY_2024','channelType':'MINI_PROGRAM'}#line:660
        OO0OOOOOOOO0OOOOO =O0OOO0O00OOOO0OOO .do_request (O0O000000000O0O0O ,OOO000O00OOOOO0O0 )#line:661
        if OO0OOOOOOOO0OOOOO and OO0OOOOOOOO0OOOOO .get ('success'):#line:662
            O0OOO00000OOO0000 =OO0OOOOOOOO0OOOOO .get ('obj',{}).get ('account',{})#line:663
            O000OO00OO00OO000 =[f"[{OOOOOOO0OO0OO0OOO['currency']}]X{OOOOOOO0OO0OO0OOO['amount']}"for OOOOOOO0OO0OO0OOO in O0OOO00000OOO0000 .get ('receivedAccountList',[])]#line:665
            O0O0O0OO00OO00OOO =O0OOO00000OOO0000 .get ('turnedAward',{})#line:666
            if O0O0O0OO00OO00OOO .get ('productName'):#line:667
                O000OO00OO00OO000 .append (f"[优惠券]{O0O0O0OO00OO00OOO['productName']}")#line:668
            print ('领取任务[%s]奖励: %s'%(OO0OO0OOO0OO00OOO ['taskName'],', '.join (O000OO00OO00OO000 )))#line:669
        else :#line:670
            O0OOOO0000000OOO0 =OO0OOOOOOOO0OOOOO .get ('errorMessage')or json .dumps (OO0OOOOOOOO0OOOOO )or '无返回'#line:671
            print ('领取任务[%s]奖励失败: %s'%(OO0OO0OOO0OO00OOO ['taskName'],O0OOOO0000000OOO0 ))#line:672
            if '用户手机号校验未通过'in O0OOOO0000000OOO0 :#line:673
                O0OOO0O00OOOO0OOO .anniversary_black =True #line:674
    def anniversary2024_unbox (OOO000OO0O00OOO00 ):#line:676
        OO0OOO00O00OOO0O0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024CardService~unbox'#line:677
        OOOO000OO00O0O0OO =OOO000OO0O00OOO00 .do_request (OO0OOO00O00OOO0O0 ,{})#line:678
        if OOOO000OO00O0O0OO and OOOO000OO00O0O0OO .get ('success'):#line:679
            OOOOO00OO0O0O00O0 =OOOO000OO00O0O0OO .get ('obj',{}).get ('account',{})#line:680
            OO0OOO00O0O00OOO0 =[f"[{O00O0O00O00OO0OO0['currency']}]X{O00O0O00O00OO0OO0['amount']}"for O00O0O00O00OO0OO0 in OOOOO00OO0O0O00O0 .get ('receivedAccountList',[])]#line:682
            print ('拆盒子: %s'%', '.join (OO0OOO00O0O00OOO0 )or '空气')#line:683
        else :#line:684
            OOO0OOO0O00OO0OO0 =OOOO000OO00O0O0OO .get ('errorMessage')or json .dumps (OOOO000OO00O0O0OO )or '无返回'#line:685
            print ('拆盒子失败: %s'%OOO0OOO0O00OO0OO0 )#line:686
            if '用户手机号校验未通过'in OOO0OOO0O00OO0OO0 :#line:687
                OOO000OO0O00OOO00 .anniversary_black =True #line:688
    def anniversary2024_game_list (OOO0OO00OOO00O0O0 ):#line:690
        O000O000O0O0O0000 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024GameParkService~list'#line:691
        OO0O000O00OOOOO00 =OOO0OO00OOO00O0O0 .do_request (O000O000O0O0O0000 ,{})#line:692
        try :#line:693
            if OO0O000O00OOOOO00 ['success']:#line:694
                OO00O0000O000O00O =OO0O000O00OOOOO00 ['obj'].get ('topicPKInfo',{})#line:695
                O00OO00000OO0O0O0 =OO0O000O00OOOOO00 ['obj'].get ('searchWordInfo',{})#line:696
                O0OO0O00OO0OO000O =OO0O000O00OOOOO00 ['obj'].get ('happyEliminationInfo',{})#line:697
                if not OO00O0000O000O00O .get ('isPassFlag'):#line:699
                    print ('开始话题PK赛')#line:700
                    OOO0OO00OOO00O0O0 .anniversary2024_TopicPk_topicList ()#line:702
                if not O00OO00000OO0O0O0 .get ('isPassFlag')or not O00OO00000OO0O0O0 .get ('isFinishDailyFlag'):#line:704
                    print ('开始找字游戏')#line:705
                    for O0O000OO0OO0O0OO0 in range (1 ,11 ):#line:706
                        O0000OO00OO00OO00 =random .randint (1000 ,3000 )/1000.0 #line:707
                        time .sleep (O0000OO00OO00OO00 )#line:708
                        if not OOO0OO00OOO00O0O0 .anniversary2024_SearchWord_win (O0O000OO0OO0O0OO0 ):#line:709
                            break #line:710
                if not O0OO0O00OO0OO000O .get ('isPassFlag')or not O0OO0O00OO0OO000O .get ('isFinishDailyFlag'):#line:712
                    print ('开始消消乐')#line:713
                    for O0O000OO0OO0O0OO0 in range (1 ,31 ):#line:714
                        O0000OO00OO00OO00 =random .randint (2000 ,4000 )/1000.0 #line:715
                        time .sleep (O0000OO00OO00OO00 )#line:716
                        if not OOO0OO00OOO00O0O0 .anniversary2024_HappyElimination_win (O0O000OO0OO0O0OO0 ):#line:717
                            break #line:718
            else :#line:719
                O0OO0O0OOOO000OOO =OO0O000O00OOOOO00 ['errorMessage']or json .dumps (OO0O000O00OOOOO00 )or '无返回'#line:720
                print ('查询游戏状态失败: '+O0OO0O0OOOO000OOO )#line:721
                if '用户手机号校验未通过'in O0OO0O0OOOO000OOO :#line:722
                    OOO0OO00OOO00O0O0 .anniversary_black =True #line:723
        except Exception as OOOOO00OOO0OOOO00 :#line:724
            print (str (OOOOO00OOO0OOOO00 ))#line:725
    def anniversary2024_SearchWord_win (O00O0OOOOO0OO0O0O ,O000000O0O000O00O ):#line:727
        OO00OOO000O0O0O00 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024SearchWordService~win'#line:728
        O00OOO0O0O0O0O0O0 =True #line:729
        try :#line:730
            O000OO0O0OOO0OO00 ={'index':O000000O0O000O00O }#line:731
            OOO00OO0O0O00O000 =O00O0OOOOO0OO0O0O .do_request (OO00OOO000O0O0O00 ,O000OO0O0OOO0OO00 )#line:732
            if OOO00OO0O0O00O000 and OOO00OO0O0O00O000 .get ('success'):#line:733
                OO0000O00000OOO00 =OOO00OO0O0O00O000 .get ('obj',{}).get ('currencyDTOList',[])#line:734
                OO0OOOOOOOO00O000 =', '.join ([f"[{OO0O0O0O0OOOO000O.get('currency')}]X{OO0O0O0O0OOOO000O.get('amount')}"for OO0O0O0O0OOOO000O in OO0000O00000OOO00 ])#line:735
                print (f'找字游戏第{O000000O0O000O00O}关通关成功: {OO0OOOOOOOO00O000 if OO0OOOOOOOO00O000 else "未获得奖励"}')#line:736
            else :#line:737
                OOOOO000O0O00O000 =OOO00OO0O0O00O000 .get ('errorMessage')or json .dumps (OOO00OO0O0O00O000 )or '无返回'#line:738
                print (f'找字游戏第{O000000O0O000O00O}关失败: {OOOOO000O0O00O000}')#line:739
                if '系统繁忙'in OOOOO000O0O00O000 :#line:740
                    O00OOO0O0O0O0O0O0 =False #line:741
        except Exception as O0OOO0OO000O0O00O :#line:742
            print (O0OOO0OO000O0O00O )#line:743
        finally :#line:744
            return O00OOO0O0O0O0O0O0 #line:745
    def anniversary2024_HappyElimination_win (O000OO0O0O0OO00OO ,O00OO0OO0OO0O00OO ):#line:747
        OO0000OO00000O0OO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024HappyEliminationService~win'#line:748
        O0OOOO000O00O0000 =True #line:749
        OO000O00O0OO0O000 ={'index':O00OO0OO0OO0O00OO }#line:750
        O0000O0O0OOO000O0 =O000OO0O0O0OO00OO .do_request (OO0000OO00000O0OO ,OO000O00O0OO0O000 )#line:751
        try :#line:752
            if O0000O0O0OOO000O0 and O0000O0O0OOO000O0 .get ('success'):#line:753
                O000O0O00OO0000O0 =O0000O0O0OOO000O0 ['obj'].get ('isAward')#line:754
                OOO0O0OOO000OOO0O =O0000O0O0OOO000O0 ['obj'].get ('currencyDTOList',[])#line:755
                OO0OOO00OO0OOO0OO =', '.join ([f"[{O00OO0O0O0O0OOOOO.get('currency')}]X{O00OO0O0O0O0OOOOO.get('amount')}"for O00OO0O0O0O0OOOOO in OOO0O0OOO000OOO0O ])#line:756
                print (f'第{O00OO0OO0OO0O00OO}关通关: {OO0OOO00OO0OOO0OO if OO0OOO00OO0OOO0OO else "未获得奖励"}')#line:757
            else :#line:758
                O0OOO00O0OO00O000 =O0000O0O0OOO000O0 .get ('errorMessage')or json .dumps (O0000O0O0OOO000O0 )or '无返回'#line:759
                print (f'第{O00OO0OO0OO0O00OO}关失败: {O0OOO00O0OO00O000}')#line:760
                if '系统繁忙'in O0OOO00O0OO00O000 :#line:761
                    O0OOOO000O00O0000 =False #line:762
        except Exception as O0OOO00OO0O0OO0O0 :#line:763
            print (O0OOO00OO0O0OO0O0 )#line:764
            O0OOOO000O00O0000 =False #line:765
        finally :#line:766
            return O0OOOO000O00O0000 #line:767
    def anniversary2024_TopicPk_chooseSide (OOOO000OOOOOOO00O ,OO0000OOO0OO0OOO0 ):#line:769
        OO0OO000O000O00O0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024TopicPkService~chooseSide'#line:770
        O00OOO0O0OO000OO0 =True #line:771
        O000OO0000OOOOOOO ={'index':OO0000OOO0OO0OOO0 ,'choose':0 }#line:772
        OOO0OOO000O0O00O0 =OOOO000OOOOOOO00O .do_request (OO0OO000O000O00O0 ,O000OO0000OOOOOOO )#line:773
        try :#line:774
            if OOO0OOO000O0O00O0 and OOO0OOO000O0O00O0 .get ('success'):#line:775
                O0OOO0OO00OOOO0O0 =OOO0OOO000O0O00O0 ['obj'].get ('currencyDTOList',[])#line:776
                O0OOOO0OOOOO00000 =', '.join ([f"[{OOOO000O0O00OOOOO.get('currency')}]X{OOOO000O0O00OOOOO.get('amount')}"for OOOO000O0O00OOOOO in O0OOO0OO00OOOO0O0 ])#line:777
                print (f'话题PK赛选择话题{OO0000OOO0OO0OOO0}成功： {O0OOOO0OOOOO00000 if O0OOOO0OOOOO00000 else "未获得奖励"}')#line:778
            else :#line:779
                O000O000O00000O0O =OOO0OOO000O0O00O0 ['errorMessage']or json .dumps (OOO0OOO000O0O00O0 )or '无返回'#line:780
                print (f'话题PK赛选择话题{OO0000OOO0OO0OOO0}失败： {O000O000O00000O0O}')#line:781
                if '系统繁忙'in O000O000O00000O0O :#line:782
                    O00OOO0O0OO000OO0 =False #line:783
        except Exception as OOO0OO0OO0OOO0O00 :#line:784
            print (OOO0OO0OO0OOO0O00 )#line:785
            O00OOO0O0OO000OO0 =False #line:786
        finally :#line:787
            return O00OOO0O0OO000OO0 #line:788
    def anniversary2024_TopicPk_topicList (OOO00O0000OO000OO ):#line:790
        OO00OOOOOO0O0OOOO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024TopicPkService~topicList'#line:791
        O000OO0O00OO0OOOO =OOO00O0000OO000OO .do_request (OO00OOOOOO0O0OOOO ,{})#line:792
        try :#line:793
            if O000OO0O00OO0OOOO and O000OO0O00OO0OOOO .get ('success'):#line:794
                OO00O00OO00OOO00O =O000OO0O00OO0OOOO ['obj'].get ('topics',[])#line:795
                for OO0OOO0O0O0000OO0 in OO00O00OO00OOO00O :#line:796
                    if not OO0OOO0O0O0000OO0 .get ('choose'):#line:797
                        OO000O00OO0O0O0O0 =OO0OOO0O0O0000OO0 .get ('index',1 )#line:798
                        O0OOO0O0O0OOO0000 =random .randint (2000 ,4000 )/1000.0 #line:799
                        time .sleep (O0OOO0O0O0OOO0000 )#line:800
                        if not OOO00O0000OO000OO .anniversary2024_TopicPk_chooseSide (OO000O00OO0O0O0O0 ):#line:801
                            break #line:802
            else :#line:803
                O00O0O0O0000OOOOO =O000OO0O00OO0OOOO ['errorMessage']or json .dumps (O000OO0O00OO0OOOO )or '无返回'#line:804
                print (f'查询话题PK赛记录失败： {O00O0O0O0000OOOOO}')#line:805
        except Exception as OO0000O0OOO00O0O0 :#line:806
            print (OO0000O0OOO00O0O0 )#line:807
    def anniversary2024_queryAccountStatus_refresh (O000OO00OO0O00OO0 ):#line:809
        O00O000O0OO0OOOO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024CardService~queryAccountStatus'#line:810
        OOOO000OOOO0O000O =O000OO00OO0O00OO0 .do_request (O00O000O0OO0OOOO0 ,{})#line:811
        try :#line:812
            if not OOOO000OOOO0O000O or not OOOO000OOOO0O000O .get ('success'):#line:813
                OOOOOOOO0O00O0OOO =OOOO000OOOO0O000O ['errorMessage']or json .dumps (OOOO000OOOO0O000O )or '无返回'#line:814
                print (f'查询账户状态失败： {OOOOOOOO0O00O0OOO}')#line:815
        except Exception as O0OOOO000O0OO0O00 :#line:816
            print (O0OOOO000O0OO0O00 )#line:817
    def anniversary2024_TopicPk_chooseSide (O00OO00O0O00O0000 ,O0O00O000OOO0OOOO ):#line:819
        O0O0O00OO0OO0OOOO =True #line:820
        OO000OOO00O0O0O00 ={'index':O0O00O000OOO0OOOO ,'choose':0 }#line:824
        O00OO00O0O00O0000 .headers ['channel']='31annizyw'#line:825
        OO0OO0OO00O0O0OO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024TopicPkService~chooseSide'#line:826
        OOO00O0O000OO0000 =O00OO00O0O00O0000 .do_request (OO0OO0OO00O0O0OO0 ,OO000OOO00O0O0O00 ,'post')#line:827
        if OOO00O0O000OO0000 and OOO00O0O000OO0000 .get ('success'):#line:829
            OOO000O0000O0O00O =OOO00O0O000OO0000 .get ('obj',{}).get ('currencyDTOList',[])#line:830
            if OOO000O0000O0O00O :#line:831
                OO0O000O000OOOOO0 =[f"[{O00O000O0O00OOOOO['currency']}]{O00O000O0O00OOOOO['amount']}次"for O00O000O0O00OOOOO in OOO000O0000O0O00O ]#line:832
                print (f'话题PK赛第{O0O00O000OOO0OOOO}个话题选择成功: {", ".join(OO0O000O000OOOOO0)}')#line:833
            else :#line:834
                print (f'话题PK赛第{O0O00O000OOO0OOOO}个话题选择成功')#line:835
        else :#line:836
            OOO00O00OO0OO00O0 =OOO00O0O000OO0000 .get ('errorMessage')if OOO00O0O000OO0000 else '无返回'#line:837
            print (f'话题PK赛第{O0O00O000OOO0OOOO}个话题失败: {OOO00O00OO0OO00O0}')#line:838
            if OOO00O00OO0OO00O0 and '系统繁忙'in OOO00O00OO0OO00O0 :#line:839
                O0O0O00OO0OO0OOOO =False #line:840
        return O0O0O00OO0OO0OOOO #line:842
    def anniversary2024_titleList (O000OO000OOOO0OOO ):#line:844
        O0000O00O0000OOO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024GuessService~titleList'#line:845
        OOO0O0OO00O00000O =O000OO000OOOO0OOO .do_request (O0000O00O0000OOO0 )#line:846
        if OOO0O0OO00O00000O and OOO0O0OO00O00000O .get ('success'):#line:848
            OOO0O0O0O0O0O00OO =OOO0O0OO00O00000O .get ('obj',{}).get ('guessTitleInfoList',[])#line:850
            O0OOO0000OO0O0OO0 =[OO00OOO0000000O0O for OO00OOO0000000O0O in OOO0O0O0O0O0O00OO if OO00OOO0000000O0O ['gameDate']==O000OO000OOOO0OOO .today ]#line:851
            for OO00000000OOOO0O0 in O0OOO0000OO0O0OO0 :#line:852
                if OO00000000OOOO0O0 ['answerStatus']:#line:853
                    print ('今日已回答过竞猜')#line:854
                else :#line:855
                    O000OO0OO00O000O0 =O000OO000OOOO0OOO .answer #line:856
                    if O000OO0OO00O000O0 :#line:857
                        O000OO000OOOO0OOO .anniversary2024_answer (OO00000000OOOO0O0 ,O000OO0OO00O000O0 )#line:858
                        print (f'进行了答题: {O000OO0OO00O000O0}')#line:859
        else :#line:860
            O000O0O000O0OO0OO =OOO0O0OO00O00000O .get ('errorMessage')if OOO0O0OO00O00000O else '无返回'#line:861
            print (f'查询每日口令竞猜失败: {O000O0O000O0OO0OO}')#line:862
    def anniversary2024_titleList_award (O0OO0000O000OOOOO ):#line:864
        OO000OO00OO0O0OO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024GuessService~titleList'#line:865
        OO0O00OO00O0OOO00 =O0OO0000O000OOOOO .do_request (OO000OO00OO0O0OO0 )#line:866
        if OO0O00OO00O0OOO00 and OO0O00OO00O0OOO00 .get ('success'):#line:868
            OO0OOO000OOO00O0O =OO0O00OO00O0OOO00 .get ('obj',{}).get ('guessTitleInfoList',[])#line:870
            O00O000O000O0000O =[OO000OOOOO0000OOO for OO000OOOOO0000OOO in OO0OOO000OOO00O0O if OO000OOOOO0000OOO ['gameDate']==O0OO0000O000OOOOO .today ]#line:871
            for O0O0OOO0OO0O0OO00 in O00O000O000O0000O :#line:873
                if O0O0OOO0OO0O0OO00 ['answerStatus']:#line:874
                    OOOO0OOO00000O000 =O0O0OOO0OO0O0OO00 .get ('awardList',[])+O0O0OOO0OO0O0OO00 .get ('puzzleList',[])#line:875
                    O00OOOO00O00OOO00 =', '.join ([f"{OOOOO0OO000OOOOOO['productName']}"for OOOOO0OO000OOOOOO in OOOO0OOO00000O000 ])#line:876
                    print (f'口令竞猜奖励: {O00OOOO00O00OOO00}'if O00OOOO00O00OOO00 else '今日无奖励')#line:877
                else :#line:878
                    print ('今日还没回答竞猜')#line:879
        else :#line:880
            OOO0O000O0OO0OOO0 =OO0O00OO00O0OOO00 .get ('errorMessage')if OO0O00OO00O0OOO00 else '无返回'#line:881
            print (f'查询每日口令竞猜奖励失败: {OOO0O000O0OO0OOO0}')#line:882
    def anniversary2024_answer (OO0000000O00O00OO ,O00OOO000OOOOO0O0 ):#line:885
        OO000OO000OO00O00 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024GuessService~answer'#line:886
        O0O00O0OOOOO000O0 ={'period':O00OOO000OOOOO0O0 ['period'],'answerInfo':O00OOO000OOOOO0O0 }#line:887
        OOO0O0O0000O00OOO =OO0000000O00O00OO .do_request (OO000OO000OO00O00 ,O0O00O0OOOOO000O0 )#line:888
        if OOO0O0O0000O00OOO and OOO0O0O0000O00OOO .get ('success'):#line:889
            print ('口令竞猜回答成功')#line:890
            OO0000000O00O00OO .anniversary2024_titleList_award ()#line:891
        else :#line:892
            OO0O0O0000000OO0O =OOO0O0O0000O00OOO .get ('errorMessage')if OOO0O0O0000O00OOO else '无返回'#line:893
            print (f'口令竞猜回答失败: {OO0O0O0000000OO0O}')#line:894
    def anniversary2024_queryAccountStatus (O0O0000O0000OOOO0 ):#line:897
        O00OOO0000OO00OO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024CardService~queryAccountStatus'#line:898
        OOOO00OO0OOOO0OOO =O0O0000O0000OOOO0 .do_request (O00OOO0000OO00OO0 )#line:899
        if OOOO00OO0OOOO0OOO .get ('success'):#line:900
            OO00OO0O00OO0OOO0 =OOOO00OO0OOOO0OOO .get ('obj',{}).get ('accountCurrencyList',[])#line:901
            O0O00OO0O0000000O =[O000O0000OOO0OO00 for O000O0000OOO0OO00 in OO00OO0O00OO0OOO0 if O000O0000OOO0OO00 .get ('currency')=='UNBOX_CHANCE']#line:903
            OOOO0000OO0OO0OOO =O0O00OO0O0000000O [0 ].get ('balance')if O0O00OO0O0000000O else 0 #line:904
        else :#line:910
            O0000O000O0O0O00O =OOOO00OO0OOOO0OOO .get ('errorMessage')or json .dumps (OOOO00OO0OOOO0OOO )or '无返回'#line:911
            print ('查询已收集拼图失败: '+O0000O000O0O0O00O )#line:912
        OOOO00OO0OOOO0OOO =O0O0000O0000OOOO0 .do_request (O00OOO0000OO00OO0 )#line:914
        if OOOO00OO0OOOO0OOO .get ('success'):#line:915
            OO00OO0O00OO0OOO0 =OOOO00OO0OOOO0OOO .get ('obj',{}).get ('accountCurrencyList',[])#line:916
            OO00OO0O00OO0OOO0 =[OOOO0O0O0O0O0OO0O for OOOO0O0O0O0O0OO0O in OO00OO0O00OO0OOO0 if OOOO0O0O0O0O0OO0O .get ('currency')!='UNBOX_CHANCE']#line:918
            if OO00OO0O00OO0OOO0 :#line:919
                OOOOO0000O0000OOO =OO00OO0O00OO0OOO0 #line:920
                O0O0000OO00OO0000 =[]#line:921
                O0O0000O0000OOOO0 .cards ={'CARD_1':0 ,'CARD_2':0 ,'CARD_3':0 ,'CARD_4':0 ,'CARD_5':0 ,'CARD_6':0 ,'CARD_7':0 ,'CARD_8':0 ,'CARD_9':0 ,'COMMON_CARD':0 }#line:933
                for OOOOO0OOO00O00O00 in OOOOO0000O0000OOO :#line:934
                    O000O0000000O00OO =OOOOO0OOO00O00O00 .get ('currency')#line:935
                    if O000O0000000O00OO in O0O0000O0000OOOO0 .cards :#line:936
                        O0O0000O0000OOOO0 .cards [O000O0000000O00OO ]=int (OOOOO0OOO00O00O00 .get ('balance'))#line:937
                    O0O0000OO00OO0000 .append ('['+OOOOO0OOO00O00O00 .get ('currency')+']X'+str (OOOOO0OOO00O00O00 .get ('balance')))#line:938
                Log (f'已收集拼图: {O0O0000OO00OO0000}')#line:940
                OOOOO0000O0000OOO .sort (key =lambda OOOOOOOO00000OO00 :OOOOOOOO00000OO00 .get ('balance'),reverse =True )#line:941
            else :#line:943
                print ('还没有收集到拼图')#line:944
        else :#line:945
            O0000O000O0O0O00O =OOOO00OO0OOOO0OOO .get ('errorMessage')or json .dumps (OOOO00OO0OOOO0OOO )or '无返回'#line:946
            print ('查询已收集拼图失败: '+O0000O000O0O0O00O )#line:947
    def do_draw (OO00O0O00OOOOO000 ,OOOO00O0O0000O0O0 ):#line:949
        OOO00OO0OOOO0000O ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~anniversary2024CardService~collectDrawAward'#line:950
        O000O0OO0OOO0O0O0 ={"accountList":OOOO00O0O0000O0O0 }#line:951
        O00O0OO0OOO0O0OO0 =OO00O0O00OOOOO000 .do_request (OOO00OO0OOOO0000O ,O000O0OO0OOO0O0O0 )#line:952
        if O00O0OO0OOO0O0OO0 and O00O0OO0OOO0O0OO0 .get ('success'):#line:953
            O000O0OO0OOO0O0O0 =O00O0OO0OOO0O0OO0 .get ('obj',{})#line:954
            OOO0OOOOOOO0OO00O =O000O0OO0OOO0O0O0 .get ('productName','')#line:955
            Log (f'抽奖成功,获得{OOO0OOOOOOO0OO00O}')#line:956
            return True #line:957
        else :#line:958
            O00O0OOOO000OO00O =O00O0OO0OOO0O0OO0 .get ('errorMessage')if O00O0OO0OOO0O0OO0 else '无返回'#line:959
            print (f'抽奖失败: {O00O0OOOO000OO00O}')#line:960
            return False #line:961
    def convert_common_card (OO00OOOO00OOO0OO0 ,OO00O000O0OO00O0O ,OO00OO0OO000O0O00 ):#line:963
        if OO00O000O0OO00O0O ['COMMON_CARD']>0 :#line:965
            OO00O000O0OO00O0O ['COMMON_CARD']-=1 #line:966
            OO00O000O0OO00O0O [OO00OO0OO000O0O00 ]+=1 #line:967
            return True #line:968
        return False #line:969
    def can_draw (OO0O0OO00O0O000O0 ,O00OO00OO0O0O0OO0 ,OO0OO0O0O0000OO0O ):#line:971
        OOOOOOO0OO00O0OO0 =sum (1 for O0OO000O00OOOO0OO ,OOOOO0O0O00OOOO0O in O00OO00OO0O0O0OO0 .items ()if O0OO000O00OOOO0OO !='COMMON_CARD'and OOOOO0O0O00OOOO0O >0 )#line:973
        return OOOOOOO0OO00O0OO0 >=OO0OO0O0O0000OO0O #line:974
    def draw (O0OOOOO00O0000O00 ,O0OO0OOOOO0OO0OOO ,O0OO0O00O0O000O0O ):#line:976
        OO00O0OOOO00OOOOO =[]#line:977
        for OOOO00OOO00OO000O ,OO0OOOO00OO00OO0O in sorted (O0OO0OOOOO0OO0OOO .items (),key =lambda O00000O0OO0O000O0 :O00000O0OO0O000O0 [1 ]):#line:978
            if OOOO00OOO00OO000O !='COMMON_CARD'and OO0OOOO00OO00OO0O >0 :#line:979
                O0OO0OOOOO0OO0OOO [OOOO00OOO00OO000O ]-=1 #line:980
                OO00O0OOOO00OOOOO .append (OOOO00OOO00OO000O )#line:981
                if len (OO00O0OOOO00OOOOO )==O0OO0O00O0O000O0O :#line:982
                    break #line:983
        if len (OO00O0OOOO00OOOOO )==O0OO0O00O0O000O0O :#line:984
            "没有足够的卡进行抽奖"#line:985
        if O0OOOOO00O0000O00 .do_draw (OO00O0OOOO00OOOOO ):#line:986
            return OO00O0OOOO00OOOOO #line:987
        else :#line:988
            return None #line:989
    def simulate_lottery (O0O000000O0OO000O ,OOOO0OOO0O0OO0O00 ):#line:991
        while O0O000000O0OO000O .can_draw (OOOO0OOO0O0OO0O00 ,9 ):#line:992
            OOO00O00OOO0O00O0 =O0O000000O0OO000O .draw (OOOO0OOO0O0OO0O00 ,9 )#line:993
            print ("进行了一次9卡抽奖，消耗卡片: ",OOO00O00OOO0O00O0 )#line:994
        while O0O000000O0OO000O .can_draw (OOOO0OOO0O0OO0O00 ,7 )or O0O000000O0OO000O .convert_common_card (OOOO0OOO0O0OO0O00 ,'CARD_1'):#line:995
            if not O0O000000O0OO000O .can_draw (OOOO0OOO0O0OO0O00 ,7 ):#line:996
                continue #line:997
            OOO00O00OOO0O00O0 =O0O000000O0OO000O .draw (OOOO0OOO0O0OO0O00 ,7 )#line:998
            print ("进行了一次7卡抽奖，消耗卡片: ",OOO00O00OOO0O00O0 )#line:999
        while O0O000000O0OO000O .can_draw (OOOO0OOO0O0OO0O00 ,5 )or O0O000000O0OO000O .convert_common_card (OOOO0OOO0O0OO0O00 ,'CARD_1'):#line:1000
            if not O0O000000O0OO000O .can_draw (OOOO0OOO0O0OO0O00 ,5 ):#line:1001
                continue #line:1002
            OOO00O00OOO0O00O0 =O0O000000O0OO000O .draw (OOOO0OOO0O0OO0O00 ,5 )#line:1003
            print ("进行了一次5卡抽奖，消耗卡片: ",OOO00O00OOO0O00O0 )#line:1004
        while O0O000000O0OO000O .can_draw (OOOO0OOO0O0OO0O00 ,3 )or O0O000000O0OO000O .convert_common_card (OOOO0OOO0O0OO0O00 ,'CARD_1'):#line:1005
            if not O0O000000O0OO000O .can_draw (OOOO0OOO0O0OO0O00 ,3 ):#line:1006
                continue #line:1007
            OOO00O00OOO0O00O0 =O0O000000O0OO000O .draw (OOOO0OOO0O0OO0O00 ,3 )#line:1008
            print ("进行了一次3卡抽奖，消耗卡片: ",OOO00O00OOO0O00O0 )#line:1009
    def anniversary2024_task (O00OOOO00O0O00O00 ):#line:1011
        O00OOOO00O0O00O00 .anniversary2024_weekly_gift_status ()#line:1012
        if O00OOOO00O0O00O00 .anniversary_black :#line:1013
            return #line:1014
        O00OOOO00O0O00O00 .anniversary2024_queryAccountStatus ()#line:1018
        O00O0OOO0000OO000 =datetime (2024 ,4 ,3 ,14 ,0 )#line:1019
        if datetime .now ()>O00O0OOO0000OO000 :#line:1021
            print ('周年庆活动即将结束，开始自动抽奖')#line:1022
            O00OOOO00O0O00O00 .simulate_lottery (O00OOOO00O0O00O00 .cards )#line:1023
        else :#line:1024
            print ('未到自动抽奖时间')#line:1025
    def member_day_index (OO0O0O00O0OOOOO0O ):#line:1027
        print ('====== 会员日活动 ======')#line:1028
        try :#line:1029
            O00OO00O0OO0OOOOO =random .choice ([OOOOOOO00OO0OO000 for OOOOOOO00OO0OO000 in inviteId if OOOOOOO00OO0OO000 !=OO0O0O00O0OOOOO0O .user_id ])#line:1030
            O0OOOO00OO00O0000 ={'inviteUserId':O00OO00O0OO0OOOOO }#line:1031
            O0OO0O0O0000OO00O ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~memberDayIndexService~index'#line:1032
            O000O0000OOOO0O00 =OO0O0O00O0OOOOO0O .do_request (O0OO0O0O0000OO00O ,data =O0OOOO00OO00O0000 )#line:1034
            if O000O0000OOOO0O00 .get ('success'):#line:1035
                OO00OOOO0OO0OO000 =O000O0000OOOO0O00 .get ('obj',{}).get ('lotteryNum',0 )#line:1036
                O0OO000OO00O0O0OO =O000O0000OOOO0O00 .get ('obj',{}).get ('canReceiveInviteAward',False )#line:1037
                if O0OO000OO00O0O0OO :#line:1038
                    OO0O0O00O0OOOOO0O .member_day_receive_invite_award (O00OO00O0OO0OOOOO )#line:1039
                OO0O0O00O0OOOOO0O .member_day_red_packet_status ()#line:1040
                Log (f'会员日可以抽奖{OO00OOOO0OO0OO000}次')#line:1041
                for _OO000O00OOO0O0O0O in range (OO00OOOO0OO0OO000 ):#line:1042
                    OO0O0O00O0OOOOO0O .member_day_lottery ()#line:1043
                if OO0O0O00O0OOOOO0O .member_day_black :#line:1044
                    return #line:1045
                OO0O0O00O0OOOOO0O .member_day_task_list ()#line:1046
                if OO0O0O00O0OOOOO0O .member_day_black :#line:1047
                    return #line:1048
                OO0O0O00O0OOOOO0O .member_day_red_packet_status ()#line:1049
            else :#line:1050
                OO00O00O0OO0OO0O0 =O000O0000OOOO0O00 .get ('errorMessage','无返回')#line:1051
                Log (f'查询会员日失败: {OO00O00O0OO0OO0O0}')#line:1052
                if '没有资格参与活动'in OO00O00O0OO0OO0O0 :#line:1053
                    OO0O0O00O0OOOOO0O .member_day_black =True #line:1054
                    Log ('会员日任务风控')#line:1055
        except Exception as O00O0O0OO000000O0 :#line:1056
            print (O00O0O0OO000000O0 )#line:1057
    def member_day_receive_invite_award (OOO0OO0O0OOOO00OO ,OO000OO00O0O0O000 ):#line:1059
        try :#line:1060
            OOO000OOO00OO00OO ={'inviteUserId':OO000OO00O0O0O000 }#line:1061
            OOO0O0O0O00O00OOO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~memberDayIndexService~receiveInviteAward'#line:1063
            OO00O0O0OO0000O00 =OOO0OO0O0OOOO00OO .do_request (OOO0O0O0O00O00OOO ,OOO000OOO00OO00OO )#line:1065
            if OO00O0O0OO0000O00 .get ('success'):#line:1066
                O0OO0OOO00O00OOO0 =OO00O0O0OO0000O00 .get ('obj',{}).get ('productName','空气')#line:1067
                Log (f'会员日奖励: {O0OO0OOO00O00OOO0}')#line:1068
            else :#line:1069
                O0OO0O00O0000OOOO =OO00O0O0OO0000O00 .get ('errorMessage','无返回')#line:1070
                Log (f'领取会员日奖励失败: {O0OO0O00O0000OOOO}')#line:1071
                if '没有资格参与活动'in O0OO0O00O0000OOOO :#line:1072
                    OOO0OO0O0OOOO00OO .member_day_black =True #line:1073
                    Log ('会员日任务风控')#line:1074
        except Exception as OOOO00000O0OOO0OO :#line:1075
            print (OOOO00000O0OOO0OO )#line:1076
    def member_day_lottery (O0OOO00OO00000000 ):#line:1078
        try :#line:1079
            O00O000OO0O000O00 ={}#line:1080
            O0O00O0O0000OO0OO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~memberDayLotteryService~lottery'#line:1081
            O00O00O000OOOO00O =O0OOO00OO00000000 .do_request (O0O00O0O0000OO0OO ,O00O000OO0O000O00 )#line:1083
            if O00O00O000OOOO00O .get ('success'):#line:1084
                OO0OO0O000O0O000O =O00O00O000OOOO00O .get ('obj',{}).get ('productName','空气')#line:1085
                Log (f'会员日抽奖: {OO0OO0O000O0O000O}')#line:1086
            else :#line:1087
                OOOO000OOO00O00O0 =O00O00O000OOOO00O .get ('errorMessage','无返回')#line:1088
                Log (f'会员日抽奖失败: {OOOO000OOO00O00O0}')#line:1089
                if '没有资格参与活动'in OOOO000OOO00O00O0 :#line:1090
                    O0OOO00OO00000000 .member_day_black =True #line:1091
                    Log ('会员日任务风控')#line:1092
        except Exception as OOO00O0OOOOOO0O0O :#line:1093
            print (OOO00O0OOOOOO0O0O )#line:1094
    def member_day_task_list (O0OOO0OOOO0O0OOO0 ):#line:1096
        try :#line:1097
            O0O0OO0OO0OO0O0O0 ={'activityCode':'MEMBER_DAY','channelType':'MINI_PROGRAM'}#line:1098
            OOO0OO0OO0O0O0OO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~activityTaskService~taskList'#line:1099
            O00000O000000OO00 =O0OOO0OOOO0O0OOO0 .do_request (OOO0OO0OO0O0O0OO0 ,O0O0OO0OO0OO0O0O0 )#line:1101
            if O00000O000000OO00 .get ('success'):#line:1102
                O0OOOOO0O0OO0O000 =O00000O000000OO00 .get ('obj',[])#line:1103
                for O0000O000OOOOOO00 in O0OOOOO0O0OO0O000 :#line:1104
                    if O0000O000OOOOOO00 ['status']==1 :#line:1105
                        if O0OOO0OOOO0O0OOO0 .member_day_black :#line:1106
                            return #line:1107
                        O0OOO0OOOO0O0OOO0 .member_day_fetch_mix_task_reward (O0000O000OOOOOO00 )#line:1108
                for O0000O000OOOOOO00 in O0OOOOO0O0OO0O000 :#line:1109
                    if O0000O000OOOOOO00 ['status']==2 :#line:1110
                        if O0OOO0OOOO0O0OOO0 .member_day_black :#line:1111
                            return #line:1112
                        if O0000O000OOOOOO00 ['taskType']in ['SEND_SUCCESS','INVITEFRIENDS_PARTAKE_ACTIVITY','OPEN_SVIP','OPEN_NEW_EXPRESS_CARD','OPEN_FAMILY_CARD','CHARGE_NEW_EXPRESS_CARD','INTEGRAL_EXCHANGE']:#line:1115
                            pass #line:1116
                        else :#line:1117
                            for _OOO00O00OO00O00OO in range (O0000O000OOOOOO00 ['restFinishTime']):#line:1118
                                if O0OOO0OOOO0O0OOO0 .member_day_black :#line:1119
                                    return #line:1120
                                O0OOO0OOOO0O0OOO0 .member_day_finish_task (O0000O000OOOOOO00 )#line:1121
            else :#line:1122
                OOOO0O00OO0OOO000 =O00000O000000OO00 .get ('errorMessage','无返回')#line:1123
                Log ('查询会员日任务失败: '+OOOO0O00OO0OOO000 )#line:1124
                if '没有资格参与活动'in OOOO0O00OO0OOO000 :#line:1125
                    O0OOO0OOOO0O0OOO0 .member_day_black =True #line:1126
                    Log ('会员日任务风控')#line:1127
        except Exception as OO0OO0OOO000O0O00 :#line:1128
            print (OO0OO0OOO000O0O00 )#line:1129
    def member_day_finish_task (OOOOOO00O00O0O0O0 ,O0OO000O000O000OO ):#line:1131
        try :#line:1132
            OOOOO0000OOO0O00O ={'taskCode':O0OO000O000O000OO ['taskCode']}#line:1133
            O00O0OOOOO0O0OOOO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberEs~taskRecord~finishTask'#line:1135
            O00O00O0000O00O00 =OOOOOO00O00O0O0O0 .do_request (O00O0OOOOO0O0OOOO ,OOOOO0000OOO0O00O )#line:1137
            if O00O00O0000O00O00 .get ('success'):#line:1138
                Log ('完成会员日任务['+O0OO000O000O000OO ['taskName']+']成功')#line:1139
                OOOOOO00O00O0O0O0 .member_day_fetch_mix_task_reward (O0OO000O000O000OO )#line:1140
            else :#line:1141
                OOO00OO0O0O0OO0OO =O00O00O0000O00O00 .get ('errorMessage','无返回')#line:1142
                Log ('完成会员日任务['+O0OO000O000O000OO ['taskName']+']失败: '+OOO00OO0O0O0OO0OO )#line:1143
                if '没有资格参与活动'in OOO00OO0O0O0OO0OO :#line:1144
                    OOOOOO00O00O0O0O0 .member_day_black =True #line:1145
                    Log ('会员日任务风控')#line:1146
        except Exception as OO000OO00OOO0O00O :#line:1147
            print (OO000OO00OOO0O00O )#line:1148
    def member_day_fetch_mix_task_reward (O00OOO0O00OO0OOO0 ,OOOO000OO0O0OOOOO ):#line:1150
        try :#line:1151
            O00O00O0OO0OO0OOO ={'taskType':OOOO000OO0O0OOOOO ['taskType'],'activityCode':'MEMBER_DAY','channelType':'MINI_PROGRAM'}#line:1152
            O0O00OOO00OOOOOO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~activityTaskService~fetchMixTaskReward'#line:1154
            O0OOO000O00O0OO0O =O00OOO0O00OO0OOO0 .do_request (O0O00OOO00OOOOOO0 ,O00O00O0OO0OO0OOO )#line:1156
            if O0OOO000O00O0OO0O .get ('success'):#line:1157
                Log ('领取会员日任务['+OOOO000OO0O0OOOOO ['taskName']+']奖励成功')#line:1158
            else :#line:1159
                OOO0OO0OO0O0O00O0 =O0OOO000O00O0OO0O .get ('errorMessage','无返回')#line:1160
                Log ('领取会员日任务['+OOOO000OO0O0OOOOO ['taskName']+']奖励失败: '+OOO0OO0OO0O0O00O0 )#line:1161
                if '没有资格参与活动'in OOO0OO0OO0O0O00O0 :#line:1162
                    O00OOO0O00OO0OOO0 .member_day_black =True #line:1163
                    Log ('会员日任务风控')#line:1164
        except Exception as OO0OOO00O0OOO0OO0 :#line:1165
            print (OO0OOO00O0OOO0OO0 )#line:1166
    def member_day_receive_red_packet (O0000OO00000OO000 ,O00O0O0OOO000OO0O ):#line:1168
        try :#line:1169
            O0OOO0000OO0OO00O ={'receiveHour':O00O0O0OOO000OO0O }#line:1170
            OO0000OOO00OO0O0O ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~memberDayTaskService~receiveRedPacket'#line:1171
            OO0000O0O00O0OOO0 =O0000OO00000OO000 .do_request (OO0000OOO00OO0O0O ,O0OOO0000OO0OO00O )#line:1173
            if OO0000O0O00O0OOO0 .get ('success'):#line:1174
                print (f'会员日领取{O00O0O0OOO000OO0O}点红包成功')#line:1175
            else :#line:1176
                OO00O0O000000O0OO =OO0000O0O00O0OOO0 .get ('errorMessage','无返回')#line:1177
                print (f'会员日领取{O00O0O0OOO000OO0O}点红包失败: {OO00O0O000000O0OO}')#line:1178
                if '没有资格参与活动'in OO00O0O000000O0OO :#line:1179
                    O0000OO00000OO000 .member_day_black =True #line:1180
                    Log ('会员日任务风控')#line:1181
        except Exception as OOOOO0OOOOO000O00 :#line:1182
            print (OOOOO0OOOOO000O00 )#line:1183
    def member_day_red_packet_status (OO0O0OO0OOO0O0O0O ):#line:1185
        try :#line:1186
            O0OO0O0O00OOOOOO0 ={}#line:1187
            O0O00OO0OOO00OO00 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~memberDayPacketService~redPacketStatus'#line:1188
            O0OOO0O0OOOOO00O0 =OO0O0OO0OOO0O0O0O .do_request (O0O00OO0OOO00OO00 ,O0OO0O0O00OOOOOO0 )#line:1189
            if O0OOO0O0OOOOO00O0 .get ('success'):#line:1190
                OOOOOOO0O0000O0O0 =O0OOO0O0OOOOO00O0 .get ('obj',{}).get ('packetList',[])#line:1191
                for O0OOO00000000O0OO in OOOOOOO0O0000O0O0 :#line:1192
                    OO0O0OO0OOO0O0O0O .member_day_red_packet_map [O0OOO00000000O0OO ['level']]=O0OOO00000000O0OO ['count']#line:1193
                for OO0OO00OOO0000O00 in range (1 ,OO0O0OO0OOO0O0O0O .max_level ):#line:1195
                    O0OO00OO000OOO0O0 =OO0O0OO0OOO0O0O0O .member_day_red_packet_map .get (OO0OO00OOO0000O00 ,0 )#line:1196
                    while O0OO00OO000OOO0O0 >=2 :#line:1197
                        OO0O0OO0OOO0O0O0O .member_day_red_packet_merge (OO0OO00OOO0000O00 )#line:1198
                        O0OO00OO000OOO0O0 -=2 #line:1199
                OO00OO00OOOO00O0O =[]#line:1200
                OO00OO0O0000O0OOO =0 #line:1201
                for OO0OO00OOO0000O00 ,O0OO00OO000OOO0O0 in OO0O0OO0OOO0O0O0O .member_day_red_packet_map .items ():#line:1203
                    if O0OO00OO000OOO0O0 ==0 :#line:1204
                        continue #line:1205
                    OO00OO00OOOO00O0O .append (f"[{OO0OO00OOO0000O00}级]X{O0OO00OO000OOO0O0}")#line:1206
                    OO0O00OO0OO0OO000 =int (OO0OO00OOO0000O00 )#line:1207
                    if OO0O00OO0OO0OO000 <OO0O0OO0OOO0O0O0O .max_level :#line:1208
                        OO00OO0O0000O0OOO +=1 <<(OO0O00OO0OO0OO000 -1 )#line:1209
                Log ("会员日合成列表: "+", ".join (OO00OO00OOOO00O0O ))#line:1211
                if OO0O0OO0OOO0O0O0O .member_day_red_packet_map .get (OO0O0OO0OOO0O0O0O .max_level ):#line:1213
                    Log (f"会员日已拥有[{OO0O0OO0OOO0O0O0O.max_level}级]红包X{OO0O0OO0OOO0O0O0O.member_day_red_packet_map[OO0O0OO0OOO0O0O0O.max_level]}")#line:1214
                    OO0O0OO0OOO0O0O0O .member_day_red_packet_draw (OO0O0OO0OOO0O0O0O .max_level )#line:1215
                else :#line:1216
                    OO0O0O0OO0O0OOOO0 =OO0O0OO0OOO0O0O0O .packet_threshold -OO00OO0O0000O0OOO #line:1217
                    Log (f"会员日距离[{OO0O0OO0OOO0O0O0O.max_level}级]红包还差: [1级]红包X{OO0O0O0OO0O0OOOO0}")#line:1218
            else :#line:1220
                OO0OOO0000O0OOO00 =O0OOO0O0OOOOO00O0 .get ('errorMessage','无返回')#line:1221
                Log (f'查询会员日合成失败: {OO0OOO0000O0OOO00}')#line:1222
                if '没有资格参与活动'in OO0OOO0000O0OOO00 :#line:1223
                    OO0O0OO0OOO0O0O0O .member_day_black =True #line:1224
                    Log ('会员日任务风控')#line:1225
        except Exception as OO00O000O0OOO0O0O :#line:1226
            print (OO00O000O0OOO0O0O )#line:1227
    def member_day_red_packet_merge (OOO0O00O0OO0OOOOO ,O00O00O000O0OOO00 ):#line:1229
        try :#line:1230
            OOOOOO0000O0000OO ={'level':O00O00O000O0OOO00 ,'num':2 }#line:1233
            O0OOOOOOO0O0O0O00 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~memberDayPacketService~redPacketMerge'#line:1234
            OOO00OOO0OOO00O00 =OOO0O00O0OO0OOOOO .do_request (O0OOOOOOO0O0O0O00 ,OOOOOO0000O0000OO )#line:1236
            if OOO00OOO0OOO00O00 .get ('success'):#line:1237
                Log (f'会员日合成: [{O00O00O000O0OOO00}级]红包X2 -> [{O00O00O000O0OOO00 + 1}级]红包')#line:1238
                OOO0O00O0OO0OOOOO .member_day_red_packet_map [O00O00O000O0OOO00 ]-=2 #line:1239
                if not OOO0O00O0OO0OOOOO .member_day_red_packet_map .get (O00O00O000O0OOO00 +1 ):#line:1240
                    OOO0O00O0OO0OOOOO .member_day_red_packet_map [O00O00O000O0OOO00 +1 ]=0 #line:1241
                OOO0O00O0OO0OOOOO .member_day_red_packet_map [O00O00O000O0OOO00 +1 ]+=1 #line:1242
            else :#line:1243
                O0OO00O0O00OOOO00 =OOO00OOO0OOO00O00 .get ('errorMessage','无返回')#line:1244
                Log (f'会员日合成两个[{O00O00O000O0OOO00}级]红包失败: {O0OO00O0O00OOOO00}')#line:1245
                if '没有资格参与活动'in O0OO00O0O00OOOO00 :#line:1246
                    OOO0O00O0OO0OOOOO .member_day_black =True #line:1247
                    Log ('会员日任务风控')#line:1248
        except Exception as OO0O000O0O000O0OO :#line:1249
            print (OO0O000O0O000O0OO )#line:1250
    def member_day_red_packet_draw (OO000000O0000O000 ,OOOO0OOO000OOOOO0 ):#line:1252
        try :#line:1253
            OOOOOOO00O00O0000 ={'level':str (OOOO0OOO000OOOOO0 )}#line:1254
            O00OOO000000000O0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~memberDayPacketService~redPacketDraw'#line:1255
            OO0000O0OOOO0O0O0 =OO000000O0000O000 .do_request (O00OOO000000000O0 ,OOOOOOO00O00O0000 )#line:1256
            if OO0000O0OOOO0O0O0 and OO0000O0OOOO0O0O0 .get ('success'):#line:1257
                O0OOO0OOO000OOO0O =[OO00OO00OO000OOO0 ['couponName']for OO00OO00OO000OOO0 in OO0000O0OOOO0O0O0 .get ('obj',[])]or []#line:1258
                Log (f"会员日提取[{OOOO0OOO000OOOOO0}级]红包: {', '.join(O0OOO0OOO000OOO0O) or '空气'}")#line:1260
            else :#line:1261
                O000OOO0O0OO0OOO0 =OO0000O0OOOO0O0O0 .get ('errorMessage')if OO0000O0OOOO0O0O0 else "无返回"#line:1262
                Log (f"会员日提取[{OOOO0OOO000OOOOO0}级]红包失败: {O000OOO0O0OO0OOO0}")#line:1263
                if "没有资格参与活动"in O000OOO0O0OO0OOO0 :#line:1264
                    OO000000O0000O000 .memberDay_black =True #line:1265
                    print ("会员日任务风控")#line:1266
        except Exception as OO0OO0000O00OO0O0 :#line:1267
            print (OO0OO0000O00OO0O0 )#line:1268
    def MIDAUTUMN_2024_index (O0000OO000000OO0O ):#line:1270
        print ('====== 查询活动状态 ======')#line:1271
        OOO0O0O0O000OO0OO =random .choice ([OOOOO0OO0O00O00O0 for OOOOO0OO0O00O00O0 in inviteId if OOOOO0OO0O00O00O0 !=O0000OO000000OO0O .user_id ])#line:1272
        try :#line:1273
            O0000OO000000OO0O .headers ['channel']='newExpressWX'#line:1274
            O0000OO000000OO0O .headers ['referer']=f'https://mcs-mimp-web.sf-express.com/origin/a/mimp-activity/midAutumn2024?mobile={O0000OO000000OO0O.mobile}&userId={O0000OO000000OO0O.user_id}&path=/origin/a/mimp-activity/midAutumn2024&supportShare=&inviteUserId={OOO0O0O0O000OO0OO}&from=newExpressWX'#line:1276
            OO0OOOOOOOO0O0OOO ={}#line:1277
            OOO0OO0O0O000O0OO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonNoLoginPost/~memberNonactivity~midAutumn2024IndexService~index'#line:1278
            OO00OOOOOO000OOOO =O0000OO000000OO0O .do_request (OOO0OO0O0O000O0OO ,OO0OOOOOOOO0O0OOO )#line:1280
            if OO00OOOOOO000OOOO .get ('success'):#line:1282
                OO0O0O0O0000OO0OO =OO00OOOOOO000OOOO .get ('obj',[{}])#line:1283
                OO0O0O00OO000O00O =OO0O0O0O0000OO0OO .get ('acEndTime','')#line:1284
                O0OOOO0OO000OOO00 =datetime .now ().strftime ("%Y-%m-%d %H:%M:%S")#line:1286
                OOOOOOO00O0O0OOOO =datetime .strptime (OO0O0O00OO000O00O ,"%Y-%m-%d %H:%M:%S")#line:1287
                OOOOO000OO0OO00O0 =datetime .now ()<OOOOOOO00O0O0OOOO #line:1289
                if OOOOO000OO0OO00O0 :#line:1290
                    print ('活动进行中....')#line:1291
                    return True #line:1292
                else :#line:1293
                    print ('活动已结束')#line:1294
                    return False #line:1295
            else :#line:1296
                OOOO00O0OOOO00OO0 =OO00OOOOOO000OOOO .get ('errorMessage','无返回')#line:1297
                if '没有资格参与活动'in OOOO00O0OOOO00OO0 :#line:1298
                    O0000OO000000OO0O .MIDAUTUMN_2024_black =True #line:1299
                    Log ('会员日任务风控')#line:1300
                return False #line:1301
        except Exception as OOOOOO00OO0O00000 :#line:1302
            print (OOOOOO00OO0O00000 )#line:1303
            return False #line:1304
    def MIDAUTUMN_2024_Game_indexInfo (OO00O000OO0OO0000 ):#line:1306
        Log ('====== 开始游戏 ======')#line:1307
        try :#line:1308
            O0OOO0OO00O0O0OO0 ={}#line:1309
            OOO0OOO0O0OO000OO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~midAutumn2024GameService~indexInfo'#line:1310
            OOO0OO0000000O0OO =OO00O000OO0OO0000 .do_request (OOO0OOO0O0OO000OO ,O0OOO0OO00O0O0OO0 )#line:1312
            if OOO0OO0000000O0OO .get ('success'):#line:1314
                O0OO00O0OOO0OOOO0 =OOO0OO0000000O0OO .get ('obj',[{}])#line:1315
                OOOO0OO00OO000O00 =O0OO00O0OOO0OOOO0 .get ('maxPassLevel','')#line:1316
                O0000OO00O0OO0OO0 =O0OO00O0OOO0OOOO0 .get ('ifPassAllLevel','')#line:1317
                if OOOO0OO00OO000O00 !=30 :#line:1318
                    OO00O000OO0OO0000 .MIDAUTUMN_2024_win (OOOO0OO00OO000O00 )#line:1319
                else :#line:1320
                    OO00O000OO0OO0000 .MIDAUTUMN_2024_win (0 )#line:1321
            else :#line:1323
                O0000OO000OO000O0 =OOO0OO0000000O0OO .get ('errorMessage','无返回')#line:1324
                if '没有资格参与活动'in O0000OO000OO000O0 :#line:1325
                    OO00O000OO0OO0000 .MIDAUTUMN_2024_black =True #line:1326
                    Log ('会员日任务风控')#line:1327
                return False #line:1328
        except Exception as OOO00O0OO0OOOO00O :#line:1329
            print (OOO00O0OO0OOOO00O )#line:1330
            return False #line:1331
    def MIDAUTUMN_2024_Game_init (OOOO000O0OO0000OO ):#line:1333
        Log ('====== 开始游戏 ======')#line:1334
        try :#line:1335
            O00OOO000O00O0000 ={}#line:1336
            OOO0000OO000O0O0O ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~midAutumn2024GameService~init'#line:1337
            OO00000O0O00OOOOO =OOOO000O0OO0000OO .do_request (OOO0000OO000O0O0O ,O00OOO000O00O0000 )#line:1339
            if OO00000O0O00OOOOO .get ('success'):#line:1341
                OOO0OOOOOOO000000 =OO00000O0O00OOOOO .get ('obj',[{}])#line:1342
                O0000O0OOO0OOO000 =OOO0OOOOOOO000000 .get ('currentIndex','')#line:1343
                OO000OOOO0O0O0OOO =OOO0OOOOOOO000000 .get ('ifPassAllLevel','')#line:1344
                if O0000O0OOO0OOO000 !=30 :#line:1345
                    OOOO000O0OO0000OO .MIDAUTUMN_2024_win (O0000O0OOO0OOO000 )#line:1346
                else :#line:1347
                    OOOO000O0OO0000OO .MIDAUTUMN_2024_win (0 )#line:1348
            else :#line:1350
                O0O0O000OO0000OO0 =OO00000O0O00OOOOO .get ('errorMessage','无返回')#line:1351
                if '没有资格参与活动'in O0O0O000OO0000OO0 :#line:1352
                    OOOO000O0OO0000OO .MIDAUTUMN_2024_black =True #line:1353
                    Log ('会员日任务风控')#line:1354
                return False #line:1355
        except Exception as O0O000000000O000O :#line:1356
            print (O0O000000000O000O )#line:1357
            return False #line:1358
    def MIDAUTUMN_2024_weeklyGiftStatus (O0000OOO0OO000OO0 ):#line:1360
        print ('====== 查询每周礼包领取状态 ======')#line:1361
        try :#line:1362
            O0OO000OOO0OO0OO0 ={}#line:1363
            OOOOOOOOOOOO0OO00 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~midAutumn2024IndexService~weeklyGiftStatus'#line:1364
            O0OO00OOOO0OOOO0O =O0000OOO0OO000OO0 .do_request (OOOOOOOOOOOO0OO00 ,O0OO000OOO0OO0OO0 )#line:1366
            if O0OO00OOOO0OOOO0O .get ('success'):#line:1368
                O00OO00OO0O0OO00O =O0OO00OOOO0OOOO0O .get ('obj',[{}])#line:1369
                for OOO000O0O0O000OOO in O00OO00OO0O0OO00O :#line:1370
                    OO00O00O0000OO0OO =OOO000O0O0O000OOO ['received']#line:1371
                    OO0O00000000OOO00 =OOO000O0O0O000OOO ['receiveStartTime']#line:1372
                    O00OO0O0O0OOOOO00 =OOO000O0O0O000OOO ['receiveEndTime']#line:1373
                    print (f'>>> 领取时间：【{OO0O00000000OOO00} 至 {O00OO0O0O0OOOOO00}】')#line:1374
                    if OO00O00O0000OO0OO :#line:1375
                        print ('> 该礼包已领取')#line:1376
                        continue #line:1377
                    OO0O0OO0OOOO00OOO =datetime .strptime (OO0O00000000OOO00 ,"%Y-%m-%d %H:%M:%S")#line:1378
                    O0OOOO00O00O00O0O =datetime .strptime (O00OO0O0O0OOOOO00 ,"%Y-%m-%d %H:%M:%S")#line:1379
                    O0O00O0000O0O0OOO =OO0O0OO0OOOO00OOO <=datetime .now ()<=O0OOOO00O00O00O0O #line:1380
                    if O0O00O0000O0O0OOO :#line:1381
                        print (f'>> 开始领取礼包：')#line:1382
                        O0000OOO0OO000OO0 .MIDAUTUMN_2024_receiveWeeklyGift ()#line:1383
            else :#line:1384
                O0OO00O0O00OO000O =O0OO00OOOO0OOOO0O .get ('errorMessage','无返回')#line:1385
                if '没有资格参与活动'in O0OO00O0O00OO000O :#line:1386
                    O0000OOO0OO000OO0 .MIDAUTUMN_2024_black =True #line:1387
                    Log ('会员日任务风控')#line:1388
        except Exception as O0O000OO0OOOOO0O0 :#line:1389
            print (O0O000OO0OOOOO0O0 )#line:1390
    def MIDAUTUMN_2024_receiveWeeklyGift (O00O00000OOO0OOOO ):#line:1392
        O0000000O0O000000 =random .choice ([OO0OOOO0OOO00000O for OO0OOOO0OOO00000O in inviteId if OO0OOOO0OOO00000O !=O00O00000OOO0OOOO .user_id ])#line:1393
        try :#line:1394
            OO000O000OO0OO00O ={"inviteUserId":O0000000O0O000000 }#line:1395
            O000OOO00000O00O0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~midAutumn2024IndexService~receiveWeeklyGift'#line:1396
            O00O00OOOOO0OOO0O =O00O00000OOO0OOOO .do_request (O000OOO00000O00O0 ,OO000O000OO0OO00O )#line:1398
            if O00O00OOOOO0OOO0O .get ('success'):#line:1400
                O000O0O000O0OOOO0 =O00O00OOOOO0OOO0O .get ('obj',[{}])#line:1401
                if O000O0O000O0OOOO0 ==[{}]:#line:1402
                    print ('> 领取失败')#line:1403
                    return False #line:1404
                for OO00000000O00OO00 in O000O0O000O0OOOO0 :#line:1405
                    OOO00OO0OO0000OO0 =OO00000000O00OO00 ['productName']#line:1406
                    OO0OOOOOO00OO00O0 =OO00000000O00OO00 ['amount']#line:1407
                    print (f'> 领取【{OOO00OO0OO0000OO0} x {OO0OOOOOO00OO00O0}】成功')#line:1408
            else :#line:1409
                OOO0OOO000OO000O0 =O00O00OOOOO0OOO0O .get ('errorMessage','无返回')#line:1410
                if '没有资格参与活动'in OOO0OOO000OO000O0 :#line:1411
                    O00O00000OOO0OOOO .MIDAUTUMN_2024_black =True #line:1412
                    Log ('会员日任务风控')#line:1413
        except Exception as OO0O00O0O0O000OOO :#line:1414
            print (OO0O00O0O0O000OOO )#line:1415
    def MIDAUTUMN_2024_taskList (OOOOO00000OO0000O ):#line:1417
        print ('====== 查询推币任务列表 ======')#line:1418
        try :#line:1419
            O000O0O00000O0O0O ={"activityCode":"MIDAUTUMN_2024","channelType":"MINI_PROGRAM"}#line:1423
            O00000O0OO000O0OO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~activityTaskService~taskList'#line:1424
            OO0O0O00000O000OO =OOOOO00000OO0000O .do_request (O00000O0OO000O0OO ,O000O0O00000O0O0O )#line:1426
            if OO0O0O00000O000OO .get ('success'):#line:1428
                O0OO0O0O00O0OOOO0 =OO0O0O00000O000OO .get ('obj',[{}])#line:1429
                for O0O0O00OOO0O0O000 in O0OO0O0O00O0OOOO0 :#line:1430
                    O0OO00OOOO0O000O0 =O0O0O00OOO0O0O000 ['taskType']#line:1431
                    OOOOO00000OO0000O .taskName =O0O0O00OOO0O0O000 ['taskName']#line:1432
                    OOOOOOOO0OO000OO0 =O0O0O00OOO0O0O000 ['status']#line:1433
                    if OOOOOOOO0OO000OO0 ==3 :#line:1434
                        Log (f'> 任务【{OOOOO00000OO0000O.taskName}】已完成')#line:1435
                        continue #line:1436
                    OOOOO00000OO0000O .taskCode =O0O0O00OOO0O0O000 .get ('taskCode',None )#line:1437
                    if OOOOO00000OO0000O .taskCode :#line:1438
                        OOOOO00000OO0000O .MIDAUTUMN_2024_finishTask ()#line:1439
                    if O0OO00OOOO0O000O0 =='PLAY_ACTIVITY_GAME':#line:1440
                        OOOOO00000OO0000O .MIDAUTUMN_2024_Game_init ()#line:1441
            else :#line:1442
                OOOOO00O0OO00OOO0 =OO0O0O00000O000OO .get ('errorMessage','无返回')#line:1443
                if '没有资格参与活动'in OOOOO00O0OO00OOO0 :#line:1444
                    OOOOO00000OO0000O .MIDAUTUMN_2024_black =True #line:1445
                    Log ('会员日任务风控')#line:1446
        except Exception as O00OOO00000OO00OO :#line:1447
            print (O00OOO00000OO00OO )#line:1448
    def MIDAUTUMN_2024_coinStatus (O0OOOOOO00OO00OOO ,END =False ):#line:1450
        Log ('====== 查询金币信息 ======')#line:1451
        O0OO0000000OO0OO0 ={}#line:1453
        O00OO00OOOOO00000 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~midAutumn2024CoinService~coinStatus'#line:1454
        O0O0O00OO0OOOOOO0 =O0OOOOOO00OO00OOO .do_request (O00OO00OOOOO00000 ,O0OO0000000OO0OO0 )#line:1456
        if O0O0O00OO0OOOOOO0 .get ('success'):#line:1458
            O0O0OO0OO00OOO00O =O0O0O00OO0OOOOOO0 .get ('obj',None )#line:1459
            if O0O0OO0OO00OOO00O ==None :return False #line:1460
            OOOO000O0OOOO00OO =O0O0OO0OO00OOO00O .get ('accountCurrencyList',[])#line:1461
            O0000OO000000000O =O0O0OO0OO00OOO00O .get ('pushedTimesToday','')#line:1462
            OO00O00O0O0OO0O00 =O0O0OO0OO00OOO00O .get ('pushedTimesTotal','')#line:1463
            OO000O0OOOOO00OOO =0 #line:1464
            O0OOOOOO00OO00OOO .COIN_balance =0 #line:1465
            OO0000000O000O0O0 =0 #line:1466
            for OO0O0O000OOO00O00 in OOOO000O0OOOO00OO :#line:1467
                if OO0O0O000OOO00O00 ['currency']=='PUSH_TIMES':#line:1468
                    OO000O0OOOOO00OOO =OO0O0O000OOO00O00 ['balance']#line:1469
                if OO0O0O000OOO00O00 ['currency']=='COIN':#line:1470
                    O0OOOOOO00OO00OOO .COIN_balance =OO0O0O000OOO00O00 ['balance']#line:1471
                if OO0O0O000OOO00O00 ['currency']=='WELFARE_CARD':#line:1472
                    OO0000000O000O0O0 =OO0O0O000OOO00O00 ['balance']#line:1473
            OO00OOOO0000OO00O =OO000O0OOOOO00OOO #line:1475
            if END :#line:1476
                if OO000O0OOOOO00OOO >0 :#line:1477
                    for OOOO00OO00O0O000O in range (OO000O0OOOOO00OOO ):#line:1478
                        print (f'>> 开始第【{OO000O0OOOOO00OOO + 1}】次推币')#line:1479
                        O0OOOOOO00OO00OOO .MIDAUTUMN_2024_pushCoin ()#line:1480
                        OO00OOOO0000OO00O -=1 #line:1481
                        O0000OO000000000O +=1 #line:1482
                        OO00O00O0O0OO0O00 +=1 #line:1483
                Log (f'> 剩余推币次数：【{OO00OOOO0000OO00O}】')#line:1484
                Log (f'> 当前金币：【{O0OOOOOO00OO00OOO.COIN_balance}】')#line:1485
                Log (f'> 今日推币：【{O0000OO000000000O}】次')#line:1487
                Log (f'> 总推币：【{OO00O00O0O0OO0O00}】次')#line:1488
            else :#line:1489
                print (f'> 剩余推币次数：【{OO000O0OOOOO00OOO}】')#line:1490
                print (f'> 当前金币：【{O0OOOOOO00OO00OOO.COIN_balance}】')#line:1491
                print (f'> 今日推币：【{O0000OO000000000O}】次')#line:1493
                print (f'> 总推币：【{OO00O00O0O0OO0O00}】次')#line:1494
            O0OOOOOO00OO00OOO .MIDAUTUMN_2024_givePushTimes ()#line:1496
        else :#line:1497
            O0O0O0OOO0OOO0OOO =O0O0O00OO0OOOOOO0 .get ('errorMessage','无返回')#line:1498
            if '没有资格参与活动'in O0O0O0OOO0OOO0OOO :#line:1499
                O0OOOOOO00OO00OOO .MIDAUTUMN_2024_black =True #line:1500
                Log ('会员日任务风控')#line:1501
    def MIDAUTUMN_2024_pushCoin (O000O00O000OO0O00 ):#line:1505
        try :#line:1506
            O00OO00O0000OO00O ={"plateToken":None }#line:1507
            OO00000OOOOO00OO0 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~midAutumn2024CoinService~pushCoin'#line:1508
            O000O00O00O00O0O0 =O000O00O000OO0O00 .do_request (OO00000OOOOO00OO0 ,O00OO00O0000OO00O )#line:1510
            if O000O00O00O00O0O0 .get ('success'):#line:1512
                O0O0O0O00O0O00O00 =O000O00O00O00O0O0 .get ('obj',[{}])#line:1513
                OO00000O0O00OOOO0 =O0O0O0O00O0O00O00 .get ('drawAward','')#line:1514
                O000O00O000OO0O00 .COIN_balance +=OO00000O0O00OOOO0 #line:1515
                print (f'> 获得：【{OO00000O0O00OOOO0}】金币')#line:1516
            else :#line:1518
                OOOOOO0OOOO0O000O =O000O00O00O00O0O0 .get ('errorMessage','无返回')#line:1519
                if '没有资格参与活动'in OOOOOO0OOOO0O000O :#line:1520
                    O000O00O000OO0O00 .MIDAUTUMN_2024_black =True #line:1521
                    Log ('会员日任务风控')#line:1522
        except Exception as O00OO00O0O00O0O0O :#line:1523
            print (O00OO00O0O00O0O0O )#line:1524
    def MIDAUTUMN_2024_givePushTimes (O000000O00OO000O0 ):#line:1526
        Log ('====== 领取赠送推币次数 ======')#line:1527
        try :#line:1528
            OOOO0O0000OOO0O00 ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~midAutumn2024CoinService~givePushTimes'#line:1529
            OOO00OOO00OO000OO =O000000O00OO000O0 .do_request (OOOO0O0000OOO0O00 )#line:1531
            if OOO00OOO00OO000OO .get ('success'):#line:1533
                OO000000O0O00OOOO =OOO00OOO00OO000OO .get ('obj',0 )#line:1534
                print (f'> 获得：【{OO000000O0O00OOOO}】次推币机会')#line:1535
            else :#line:1536
                OO00OOO0OO0OOOOO0 =OOO00OOO00OO000OO .get ('errorMessage','无返回')#line:1537
                if '没有资格参与活动'in OO00OOO0OO0OOOOO0 :#line:1538
                    O000000O00OO000O0 .MIDAUTUMN_2024_black =True #line:1539
                    Log ('> 会员日任务风控')#line:1540
                print (OO00OOO0OO0OOOOO0 )#line:1541
        except Exception as O0000O0OO00O0O0O0 :#line:1542
            print (O0000O0OO00O0O0O0 )#line:1543
    def MIDAUTUMN_2024_finishTask (O0O00000O000O0O0O ):#line:1545
        try :#line:1546
            O0OOO0OOO00OO0O00 ={"taskCode":O0O00000O000O0O0O .taskCode }#line:1549
            OO0OOO00O0OO0OOOO ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberEs~taskRecord~finishTask'#line:1550
            O000O0000OOO0O0O0 =O0O00000O000O0O0O .do_request (OO0OOO00O0OO0OOOO ,O0OOO0OOO00OO0O00 )#line:1552
            if O000O0000OOO0O0O0 .get ('success'):#line:1554
                O00OOO00O0OOO00OO =O000O0000OOO0O0O0 .get ('obj',False )#line:1555
                Log (f'> 完成任务【{O0O00000O000O0O0O.taskName}】成功')#line:1556
            else :#line:1557
                O0O000O0O000O0OOO =O000O0000OOO0O0O0 .get ('errorMessage','无返回')#line:1558
                if '没有资格参与活动'in O0O000O0O000O0OOO :#line:1559
                    O0O00000O000O0O0O .MIDAUTUMN_2024_black =True #line:1560
                    Log ('会员日任务风控')#line:1561
        except Exception as OO0000O0OO00O00OO :#line:1562
            print (OO0000O0OO00O00OO )#line:1563
    def MIDAUTUMN_2024_win (O00OO0OOO00O000O0 ,OO000OO0OOO0OO0OO ):#line:1565
        try :#line:1566
            for O0OOO00OO00O0000O in range (OO000OO0OOO0OO0OO ,31 ):#line:1567
                print (f'开始第【{O0OOO00OO00O0000O}】关')#line:1568
                OOO0OO00O0O0O00OO ={"levelIndex":O0OOO00OO00O0000O }#line:1569
                OOO0OO0O0OO00O00O ='https://mcs-mimp-web.sf-express.com/mcs-mimp/commonPost/~memberNonactivity~midAutumn2024GameService~win'#line:1570
                O000O0OOO0O0OOO0O =O00OO0OOO00O000O0 .do_request (OOO0OO0O0OO00O00O ,OOO0OO00O0O0O00OO )#line:1572
                if O000O0OOO0O0OOO0O .get ('success'):#line:1574
                    OOO0O0000O0OO0OO0 =O000O0OOO0O0OOO0O .get ('obj',[{}])#line:1575
                    O0O000000OO000OO0 =OOO0O0000O0OO0OO0 .get ('currentAwardList',[])#line:1576
                    if O0O000000OO000OO0 !=[]:#line:1577
                        for OO00OOOOOO00OO000 in O0O000000OO000OO0 :#line:1578
                            O00OOO00000OOOOOO =OO00OOOOOO00OO000 .get ('currency','')#line:1579
                            O0OO0O00OOOO00O00 =OO00OOOOOO00OO000 .get ('amount','')#line:1580
                            print (f'> 获得：【{O00OOO00000OOOOOO}】x{O0OO0O00OOOO00O00}')#line:1581
                    else :#line:1582
                        print (f'> 本关无奖励')#line:1583
                else :#line:1587
                    OOOO0O00000000O0O =O000O0OOO0O0OOO0O .get ('errorMessage','无返回')#line:1588
                    print (OOOO0O00000000O0O )#line:1589
                    if '没有资格参与活动'in OOOO0O00000000O0O :#line:1590
                        O00OO0OOO00O000O0 .MIDAUTUMN_2024_black =True #line:1591
                        Log ('会员日任务风控')#line:1592
        except Exception as OO0O0O000000000OO :#line:1593
            print (OO0O0O000000000OO )#line:1594
    def main (OOOOOO0O0000O0O00 ):#line:1596
        global one_msg #line:1597
        O0OOO00000OOOOO00 =random .randint (1000 ,3000 )/1000.0 #line:1598
        time .sleep (O0OOO00000OOOOO00 )#line:1599
        one_msg =''#line:1600
        if not OOOOOO0O0000O0O00 .login_res :return False #line:1601
        OOOOOO0O0000O0O00 .sign ()#line:1603
        OOOOOO0O0000O0O00 .superWelfare_receiveRedPacket ()#line:1604
        OOOOOO0O0000O0O00 .get_SignTaskList ()#line:1605
        OOOOOO0O0000O0O00 .get_SignTaskList (True )#line:1606
        OOOOOO0O0000O0O00 .honey_indexData ()#line:1609
        OOOOOO0O0000O0O00 .get_honeyTaskListStart ()#line:1611
        OOOOOO0O0000O0O00 .honey_indexData (True )#line:1612
        OOO0000OO0OO0OOOO =datetime .now ().day #line:1628
        if 26 <=OOO0000OO0OO0OOOO <=28 :#line:1629
            OOOOOO0O0000O0O00 .member_day_index ()#line:1630
        else :#line:1632
            print ('未到指定时间不执行会员日任务')#line:1633
        if OOOOOO0O0000O0O00 .MIDAUTUMN_2024_index ():#line:1635
            OOOOOO0O0000O0O00 .MIDAUTUMN_2024_weeklyGiftStatus ()#line:1636
            OOOOOO0O0000O0O00 .MIDAUTUMN_2024_coinStatus ()#line:1637
            OOOOOO0O0000O0O00 .MIDAUTUMN_2024_taskList ()#line:1638
            OOOOOO0O0000O0O00 .MIDAUTUMN_2024_coinStatus (True )#line:1640
        OOOOOO0O0000O0O00 .sendMsg ()#line:1642
        return True #line:1643
    def sendMsg (OO0000O000O0OO00O ,help =False ):#line:1645
        if OO0000O000O0OO00O .send_UID :#line:1646
            O0OOOO000OO00O000 =CHERWIN_TOOLS .wxpusher (OO0000O000O0OO00O .send_UID ,one_msg ,APP_NAME ,help )#line:1647
            print (O0OOOO000OO00O000 )#line:1648
def get_quarter_end_date ():#line:1651
    OO00O0OO0O0O0OOOO =datetime .now ()#line:1652
    OO0O00OOOO000O000 =OO00O0OO0O0O0OOOO .month #line:1653
    O0OOOOOO0O0O0O0O0 =OO00O0OO0O0O0OOOO .year #line:1654
    O00OOOOOO000OO0OO =datetime (O0OOOOOO0O0O0O0O0 ,((OO0O00OOOO000O000 -1 )//3 +1 )*3 +1 ,1 )#line:1657
    OO0O0O0O0O00OO00O =O00OOOOOO000OO0OO -timedelta (days =1 )#line:1660
    return OO0O0O0O0O00OO00O .strftime ("%Y-%m-%d")#line:1662
def is_activity_end_date (OO0O000OOO00OOOOO ):#line:1665
    OO00O0OO00OOO000O =datetime .now ().date ()#line:1666
    OO0O000OOO00OOOOO =datetime .strptime (OO0O000OOO00OOOOO ,"%Y-%m-%d").date ()#line:1667
    return OO00O0OO00OOO000O ==OO0O000OOO00OOOOO #line:1669
if __name__ =='__main__':#line:1671
    APP_NAME ='顺丰速运'#line:1672
    ENV_NAME ='SFSY'#line:1673
    CK_NAME ='url'#line:1674
    print (f'''
✨✨✨ {APP_NAME}脚本✨✨✨
    ''')#line:1677
    tokens =[
    'https://mcs-mimp-web.sf-express.com/mcs-mimp/share/weChat/shareGiftReceiveRedirect?source=CX&scene=6&unionId=28UdSjbXLEjOtRDH89Bly5Lt%2BAOnfXQ7HClcLvGeUso%3D&openId=FVzQyjuAAFek%2FTlMGj9na8MLM26JqxYf7Vu5%2FcvFdng%3D&memId=pDZc55C1L%2FcJ0%2FY%2B%2BAMrW8Xl%2FB14n7qrYF3nOr92PcoDdjSr%2F6X0WoiZtgGzs7sG&memNo=6tB15T6k0ZvyroDMcHJm6cVfaQL5mlxoo4xlXDLvS2YDdjSr%2F6X0WoiZtgGzs7sG&mobile=ucVfOZ3hHiPzJJA6MqKhTw%3D%3D&bizCode=692&mediaCode=wxapp',
    
    ]#line:1683
    print (f"\n>>>>>>>>>>共获取到{len(tokens)}个账号<<<<<<<<<<")#line:1686
    for index ,token in enumerate (tokens ):#line:1689
        run_result =RUN (token ,index ).main ()#line:1690
        if not run_result :#line:1691
            continue #line:1692
    if send :#line:1695
        send (f'{APP_NAME}挂机通知',send_msg )