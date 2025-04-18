import os
import csv
from requests import post
from datetime import datetime
from time import time
from base64 import b64encode
from json import dumps
from Crypto.Cipher import AES, DES, DES3
from binascii import b2a_hex
from decimal import Decimal, ROUND_HALF_UP
import requests
import os
def upload_to_gist(file_path, note, platform="github"):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    if platform == "github":
        url = "https://api.github.com/gists"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        }
        payload = {
            "description": f"联通话费统计 - {note}",
            "public": True,
            "files": {os.path.basename(file_path): {"content": content}}
        }
    else:
        url = "https://gitee.com/api/v5/gists"
        payload = {
            "access_token": os.getenv("GITEE_TOKEN"),
            "description": f"联通话费统计 - {note}",
            "public": "true",
            "files": {os.path.basename(file_path): {"content": content}}
        }
        headers = {}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 201:
            return response.json().get("html_url")
        print(f"{platform} 上传失败: {response.text}")
    except Exception as e:
        print(f"{platform} 上传异常: {str(e)}")
    return None

class Crypt:
    def __init__(self, crypt_type: str, key, iv=None, mode="ECB"):
        if crypt_type.upper() not in ["AES", "DES", "DES3"]:
            raise Exception("加密类型错误, 请重新选择 AES/DES/DES3")
        self.crypt_type = AES if crypt_type.upper() == "AES" else DES if crypt_type.upper() == "DES" else DES3
        self.block_size = self.crypt_type.block_size
        if self.crypt_type == DES:
            self.key_size = self.crypt_type.key_size
        elif self.crypt_type == DES3:
            self.key_size = self.crypt_type.key_size[1]
        else:
            if len(key) <= 16:
                self.key_size = self.crypt_type.key_size[0]
            elif len(key) > 24:
                self.key_size = self.crypt_type.key_size[2]
            else:
                self.key_size = self.crypt_type.key_size[1]
        if len(key) > self.key_size:
            key = key[:self.key_size]
        else:
            if len(key) % self.key_size != 0:
                key = key + (self.key_size - len(key) % self.key_size) * chr(0)
        self.key = key.encode("utf-8")
        if mode == "ECB":
            self.mode = self.crypt_type.MODE_ECB
        elif mode == "CBC":
            self.mode = self.crypt_type.MODE_CBC
        
        if iv is None:
            self.cipher = self.crypt_type.new(self.key, self.mode)
        else:
            if isinstance(iv, str):
                iv = iv[:self.block_size]
                self.cipher = self.crypt_type.new(self.key, self.mode, iv.encode("utf-8"))
            elif isinstance(iv, bytes):
                iv = iv[:self.block_size]
                self.cipher = self.crypt_type.new(self.key, self.mode, iv)
            else:
                raise Exception("偏移量不为字符串")
    def encrypt(self, data, padding="pkcs7", b64=False):
        pkcs7_padding = lambda s: s + (self.block_size - len(s.encode()) % self.block_size) * chr(
            self.block_size - len(s.encode()) % self.block_size)
        zero_padding = lambda s: s + (self.block_size - len(s) % self.block_size) * chr(0)
        pad = pkcs7_padding if padding == "pkcs7" else zero_padding
        data = self.cipher.encrypt(pad(data).encode("utf8"))
        encrypt_data = b64encode(data) if b64 else b2a_hex(data)  
        return encrypt_data.decode('utf8')

class China_Unicom:
    def __init__(self, phone_num):
        self.phone_num = phone_num
        self.masked_phone = phone_num
        self.headers = {
            "Host": "10010.woread.com.cn",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json;charset=utf-8",
            'accesstoken': "ODZERTZCMjA1NTg1MTFFNDNFMThDRDYw",
            "Origin": "https://10010.woread.com.cn",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 unicom{{version:iphone_c@11.000}}",
            "Connection": "keep-alive",
            "Referer": "https://10010.woread.com.cn/ng_woread/",
        }

    def timestamp(self):
        return round(time() * 1000)

    def perform_request(self, url, crypt_text, retry_num=1):
        while retry_num > 0:
            body = {"sign": b64encode(
                Crypt(crypt_type="AES", key="woreadst^&*12345", iv="16-Bytes--String", mode="CBC").encrypt(
                    crypt_text).encode()).decode()}
            self.headers["Content-Length"] = str(len(dumps(body).replace(" ", "")))
            try:
                res = post(url, headers=self.headers, json=body)
                return res.json()
            except Exception as e:
                retry_num -= 1
                if retry_num == 0:
                    print(f"请求失败: {e}")
        return None

    def get_userinfo(self):
        date = datetime.today().strftime("%Y%m%d%H%M%S")
        num3 = b64encode(
                Crypt(crypt_type="AES", key="woreadst^&*12345", iv="16-Bytes--String", mode="CBC").encrypt(
                    self.phone_num).encode()).decode()
        url = "https://10010.woread.com.cn/ng_woread_service/rest/account/login"
        crypt_text = f'{{"phone":"{num3}","timestamp":"{date}"}}'
        data = self.perform_request(url, crypt_text)
        if data["code"] == "0000":
            self.userinfo = data["data"]
        else:
            print(f"登录失败{data}")
            exit(0)
    
    def cxye(self):
        url = "https://10010.woread.com.cn/ng_woread_service/rest/phone/vouchers/queryTicketAccount"
        timestamp = self.timestamp()
        date = datetime.today().__format__("%Y%m%d%H%M%S")
        crypt_text = f'{{"timestamp":"{date}","token":"{self.userinfo["token"]}","userId":"{self.userinfo["userid"]}","userIndex":{self.userinfo["userindex"]},"userAccount":"{self.userinfo["phone"]}","verifyCode":"{self.userinfo["verifycode"]}"}}'
        data = self.perform_request(url, crypt_text)
        if (data['code']) == "0000":
            hbcx = data['data']['usableNum'] / 100
            return hbcx 
        return 0 

    def tongji(self, max_pages=1, filter_months=None):
        url = "https://10010.woread.com.cn/ng_woread_service/rest/phone/vouchers/queryPhoneTicketRecord"
        timestamp = self.timestamp()
        date = datetime.today().strftime("%Y%m%d%H%M%S")  
        page_num = 1
        page_size = 260
        all_data = []

        while page_num <= max_pages:
            crypt_text = f'{{"type":"1","timestamp":"{date}","token":"{self.userinfo["token"]}","userId":"{self.userinfo["userid"]}","userIndex":{self.userinfo["userindex"]},"userAccount":"{self.userinfo["phone"]}","verifyCode":"{self.userinfo["verifycode"]}","pageNum":{page_num},"pageSize":{page_size}}}'
            data = self.perform_request(url, crypt_text)
            # print(data['data'])
            if data['code'] == '0000' and data['data']['list']:
                all_data.extend(data['data']['list'])
                page_num += 1
            else:
                break
        current_month = datetime.now().month
        current_year = datetime.now().year
        day = datetime.today().day  
        if filter_months is None:
            filter_months = [current_month]

        filter_months = [month for month in filter_months if 1 <= month <= 12]

        if not filter_months:
            print("没有有效的月份设置，使用当前月份查询")
            filter_months = [current_month]

        print(f"查询月份: {', '.join(map(str, filter_months))}月")

        filtered_data = [record for record in all_data if datetime.strptime(record['gaintime'], "%Y%m%d%H%M%S").month in filter_months and datetime.strptime(record['gaintime'], "%Y%m%d%H%M%S").year == current_year]

        reason_mapping = {
            "120": "阅读120分钟",
            "240": "阅读240分钟",
            "360": "阅读360分钟",
            "480": "阅读480分钟",
            "50元": "每日---红包",
            "2分钟": "阅读---红包"
        }

        month_totals = {month: Decimal(0) for month in filter_months}

        for record in filtered_data:
            reason = record['reason']
            matched_reason = None
            for key, value in reason_mapping.items():
                if key in reason:
                    matched_reason = value
                    break
            month = datetime.strptime(record['gaintime'], "%Y%m%d%H%M%S").month
            if matched_reason:
                gaintime_date = datetime.strptime(record['gaintime'], "%Y%m%d%H%M%S").strftime("%Y-%m-%d") 
                print(f"账号:【{self.masked_phone}】：领取时间: {gaintime_date} 任务:【{matched_reason}】 面值: {record['facevalue'] / 100} 元")
            else:
                gaintime_date = datetime.strptime(record['gaintime'], "%Y%m%d%H%M%S").strftime("%Y-%m-%d") 
                print(f"账号:【{self.masked_phone}】：领取时间: {gaintime_date} 任务:【未知】 面值: {record['facevalue'] / 100} 元")
            month_totals[month] += Decimal(record['facevalue']) / 100

        for month in filter_months:
            total_amount = month_totals[month].quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
            print(f"账号:【{self.masked_phone}】：截止今日：{month}月{day}日 共获得【 {total_amount} 元话费】")

        return all_data, month_totals

def load_phone_notes(file_path):
    phone_notes = {}
    push_config = {}
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  
                if not line:
                    continue 
                try:
                    parts = line.split(',')
                    if len(parts) == 3: 
                        app_token, uid, note = parts
                        push_config[note] = {"app_token": app_token, "uid": uid}
                    elif len(parts) == 2: 
                        phone, note = parts
                        phone_notes[phone] = note
                    else:
                        print(f"跳过格式不正确的行: {line}")
                except ValueError:
                    print(f"跳过格式不正确的行: {line}")

    return phone_notes, push_config

def save_phone_notes(file_path, phone_notes, push_config):
    """
    保存手机号备注和推送配置到文件
    """
    with open(file_path, 'w', encoding='utf-8') as file:    
        for note, config in push_config.items():
            file.write(f"{config['app_token']},{config['uid']},{note}\n")
        for phone, note in phone_notes.items():
            file.write(f"{phone},{note}\n")

def wxpusher_push(title, content, app_token, uids):
    url = "https://wxpusher.zjiecode.com/api/send/message"
    headers = {"Content-Type": "application/json"}
    payload = {
        "appToken": app_token,
        "content": content,
        "summary": title, 
        "contentType": 1, 
        "uids": uids if isinstance(uids, list) else [uids]
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("WxPusher 推送成功！")
    else:
        print(f"WxPusher 推送失败: {response.text}")

def start(phone, phone_notes, push_config, file_path, all_accounts_stats):
    if phone == "":
        exit(0)
    china_unicom = China_Unicom(phone)
    china_unicom.get_userinfo()
    filter_months_str = os.getenv("YF")
    filter_months = []
    if filter_months_str:
        try:
            filter_months = [int(month) for month in filter_months_str.split(",")]
        except ValueError:
            print(f"YF 环境变量值无效: {filter_months_str}")
            filter_months = None

    note = phone_notes.get(phone, "未备注")
    print(f"开始处理手机号:【{phone}】------------------【{note}】")
    all_data, month_totals = china_unicom.tongji(filter_months=filter_months)

    hbcx = china_unicom.cxye()
    print(f"账号:【{phone}】：截止今日：{datetime.now().month}月{datetime.now().day}日 阅读区话费红包余额【 {hbcx:.2f} 元】\n")

    if phone not in phone_notes:
        phone_notes[phone] = "未备注"
        save_phone_notes(file_path, phone_notes, push_config)

    if note not in all_accounts_stats:
        all_accounts_stats[note] = {"accounts": [], "details": {}}
    all_accounts_stats[note]["accounts"].append({"phone": phone, "month_totals": month_totals, "hbcx": hbcx})
    all_accounts_stats[note]["details"][phone] = all_data

    print(f"账号【{phone}】处理完成，统计信息和详细记录已存储")

def push_all_stats(all_accounts_stats, push_config):

    filter_months_str = os.getenv("YF")
    filter_months = []
    if filter_months_str:
        try:
            filter_months = [int(month) for month in filter_months_str.split(",")]
        except ValueError:
            print(f"YF 环境变量值无效: {filter_months_str}")
            filter_months = None
    if not filter_months:
        filter_months = [datetime.now().month] 

    for note, data in all_accounts_stats.items():
        if note in push_config:
            app_token = push_config[note]["app_token"]
            uid = push_config[note]["uid"]
            push_title = f"联通话费统计 - {note}"
            markdown_content = f"# 联通话费统计 - {note}\n\n"
            total_amount_all = Decimal(0) 
            account_count = len(data["accounts"]) 

            for account in data["accounts"]:
                phone = account["phone"]
                markdown_content += f"## 手机号: {phone}\n"
                for month, total_amount in account["month_totals"].items():
                    if month in filter_months: 
                        markdown_content += f"- {month}月共获得 {total_amount} 元话费\n"
                        total_amount_all += total_amount 

                hbcx = account.get("hbcx", 0)
                markdown_content += f"- 阅读区话费红包余额 {hbcx:.2f} 元\n"
                markdown_content += "\n"

                if phone in data["details"]:
                    markdown_content += f"### 详细领取记录\n"
                    for record in data["details"][phone]:
                        if isinstance(record, dict): 
                            gaintime = datetime.strptime(record['gaintime'], "%Y%m%d%H%M%S")
                            if gaintime.month in filter_months:  
                                gaintime_str = gaintime.strftime("%Y-%m-%d")
                                reason = record['reason']
                                facevalue = record['facevalue'] / 100
                                markdown_content += f"- 时间: {gaintime_str} 任务:【{reason}】 面值: {facevalue} 元\n"
                        else:
                            print(f"错误：record 不是字典，而是 {type(record)}")
                    markdown_content += "\n"

            file_path = f"{note}_statistics.md"
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(markdown_content)

            github_url = upload_to_gist(file_path, note, platform="github")
            gitee_url = upload_to_gist(file_path, note, platform="gitee")

            push_content = f"{note}--账号数--{account_count}--总共获得: {total_amount_all} 元话费\n\n"
            for account in data["accounts"]:
                phone = account["phone"]
                push_content += f"手机号: {phone}\n"
                for month, total_amount in account["month_totals"].items():
                    if month in filter_months:  
                        push_content += f"{month}月共获得 {total_amount} 元话费\n"
 
                hbcx = account.get("hbcx", 0)
                push_content += f"阅读区话费红包余额 {hbcx:.2f} 元\n"
                push_content += "\n"

            if github_url or gitee_url:
                push_content += "统计信息和详细记录链接：\n"
                if github_url:
                    push_content += f"GitHub（国外访问）: {github_url}\n"
                if gitee_url:
                    push_content += f"Gitee（国内访问）: {gitee_url}\n"
            else:
                push_content += "统计信息上传失败，请检查日志或稍后重试。"

            wxpusher_push(push_title, push_content, app_token, uid)

            os.remove(file_path)
            print(f"本地文件 {file_path} 已删除")
        else:
            print(f"未找到备注【{note}】的推送配置")

    if "总推送" in push_config:
        app_token = push_config["总推送"]["app_token"]
        uid = push_config["总推送"]["uid"]
        push_title = "联通话费统计 - 总推送"

        total_amount_all = Decimal(0) 
        account_count = 0  
        push_content = "联通话费统计 - 总推送\n\n"

        markdown_content = "# 联通话费统计 - 总推送\n\n"

        for note, data in all_accounts_stats.items():

            note_account_count = len(data["accounts"])
            note_total_amount = Decimal(0)
            for account in data["accounts"]:
                for month, total_amount in account["month_totals"].items():
                    if month in filter_months: 
                        note_total_amount += total_amount

            push_content += f"{note}--账号数--{note_account_count}--总共获得: {note_total_amount} 元话费\n\n"
            markdown_content += f"## 备注: {note}\n"
            markdown_content += f"- 账号数: {note_account_count}\n"
            markdown_content += f"- 总话费金额: {note_total_amount} 元\n\n"

            for account in data["accounts"]:
                phone = account["phone"]
                push_content += f"手机号: {phone}\n"
                markdown_content += f"### 手机号: {phone}\n"
                for month, total_amount in account["month_totals"].items():
                    if month in filter_months: 
                        push_content += f"{month}月共获得 {total_amount} 元话费\n"
                        markdown_content += f"- {month}月共获得 {total_amount} 元话费\n"

                hbcx = account.get("hbcx", 0)
                push_content += f"阅读区话费红包余额 {hbcx:.2f} 元\n"
                markdown_content += f"- 阅读区话费红包余额 {hbcx:.2f} 元\n"
                push_content += "\n"
                markdown_content += "\n"

                if phone in data["details"]:
                    markdown_content += f"#### 详细领取记录\n"
                    for record in data["details"][phone]:
                        if isinstance(record, dict): 
                            gaintime = datetime.strptime(record['gaintime'], "%Y%m%d%H%M%S")
                            if gaintime.month in filter_months: 
                                gaintime_str = gaintime.strftime("%Y-%m-%d")
                                reason = record['reason']
                                facevalue = record['facevalue'] / 100
                                markdown_content += f"- 时间: {gaintime_str} 任务:【{reason}】 面值: {facevalue} 元\n"
                        else:
                            print(f"错误：record 不是字典，而是 {type(record)}")
                    markdown_content += "\n"
            push_content += "\n"
            markdown_content += "\n"

            account_count += note_account_count
            total_amount_all += note_total_amount

        push_content += f"总账号数: {account_count}\n"
        push_content += f"总话费金额: {total_amount_all} 元\n"
        markdown_content += f"## 总账号数: {account_count}\n"
        markdown_content += f"## 总话费金额: {total_amount_all} 元\n"

        file_path = "总推送_statistics.md"
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(markdown_content)

        github_url = upload_to_gist(file_path, "总推送", platform="github")
        gitee_url = upload_to_gist(file_path, "总推送", platform="gitee")

        if github_url or gitee_url:
            push_content += "\n统计信息和详细记录链接：\n"
            if gitee_url:
                push_content += f"Gitee（国内访问）: {gitee_url}\n"
            if github_url:
                push_content += f"GitHub（国外访问）: {github_url}\n"
        else:
            push_content += "\n统计信息上传失败，请检查日志或稍后重试。"

        wxpusher_push(push_title, push_content, app_token, uid)

        os.remove(file_path)
        print(f"本地文件 {file_path} 已删除")
    else:
        print("未找到'总推送'的推送配置")

if __name__ == "__main__":
    phone_numbers = os.getenv("SJH", "").split("&")
    total_accounts = len(phone_numbers)
    print(f"总共要处理的账号数量: {total_accounts}")
    
    file_path = '联通代挂.txt'
    phone_notes, push_config = load_phone_notes(file_path)
    all_accounts_stats = {}

    for index, phone_number in enumerate(phone_numbers, start=1):
        print(f"=================================【账号{index}】=================================")
        start(phone_number, phone_notes, push_config, file_path, all_accounts_stats)

    push_all_stats(all_accounts_stats, push_config)

    print("\n所有账号的统计信息：")
    for note, data in all_accounts_stats.items():
        for i, account in enumerate(data["accounts"], start=1):
            phone = account["phone"]
            month_totals = account["month_totals"]
            for month, total_amount in month_totals.items():
                total_amount = total_amount.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                print(f"【账号{i:02d}】:【{phone}】--{month}月共获得 {total_amount} 元话费--【{note}】")