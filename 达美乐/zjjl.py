import re
from datetime import datetime
import sys

def find_openid(account, time_str, log_filename):
    """
    在日志文件中查找指定账号的 OpenID
    """
    try:
        with open(log_filename, 'r', encoding='utf-8') as file:
            content = file.read()
            # 查找该账号最近的请求信息块
            pattern = rf'请求信息:\n账号: {account}.*?"openid":\s*"([^"]+)"'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"查找OpenID时出错: {str(e)}")
    return None

def extract_prizes(log_filename='dml.log', output_filename='中奖日志.log'):
    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(f"提取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            outfile.write("一等奖中奖记录:\n" + "="*50 + "\n\n")
            
            prize_stats = {
                "一等奖": {"count": 0},
                "二等奖": {"count": 0}
            }
            
            # 使用集合来存储已处理的记录，避免重复
            processed_records = set()
            
            with open(log_filename, 'r', encoding='utf-8') as file:
                for line in file:
                    if '抽中' in line and ('一等奖' in line or '二等奖' in line):
                        # 提取关键信息
                        match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*?(\S+)\s+抽中\s+(.*?),\s+使用分数:\s+(\d+)', line)
                        if match:
                            time_str, account, prize, score = match.groups()
                            
                            # 创建唯一标识
                            record_id = f"{account}_{prize}"  # 只用账号和奖品类型作为唯一标识
                            
                            # 如果已经处理过这条记录，跳过
                            if record_id in processed_records:
                                continue
                                
                            processed_records.add(record_id)
                            
                            prize_type = "一等奖" if "一等奖" in prize else "二等奖"
                            
                            # 写入中奖记录
                            outfile.write(f"时间: {time_str}\n")
                            outfile.write(f"账号: {account}\n")
                            
                            # 查找对应的 OpenID
                            openid = find_openid(account, time_str, log_filename)
                            if openid:
                                outfile.write(f"OpenID: {openid}\n")
                            
                            outfile.write(f"奖品: {prize}\n")
                            outfile.write(f"使用分数: {score}\n")
                            outfile.write("-"*50 + "\n\n")
                            
                            # 更新统计信息
                            prize_stats[prize_type]["count"] += 1
            
            # 写入统计信息
            outfile.write("\n统计信息:\n" + "="*50 + "\n")
            for prize_type, stats in prize_stats.items():
                outfile.write(f"\n{prize_type}:\n")
                outfile.write(f"总次数: {stats['count']}\n")
                
        print(f"中奖记录已提取到: {output_filename}")
        return True
        
    except Exception as e:
        print(f"提取中奖记录时出错: {str(e)}")
        return False

if __name__ == "__main__":
    success = extract_prizes()
    sys.exit(0 if success else 1)