import requests
import re
import argparse

main = """
团队：Thirteen Team
作者：crazy
使用方法：
python main.py -i 文件名
工具支持：LayuiMin系统的未授权漏洞批量扫描
"""
print(main)
parser = argparse.ArgumentParser(description="可选参数列表")
parser.add_argument("-i", type=str, default=None, help="文件名")
args = parser.parse_args()

lass = []

if args.i is not None:
    with open(args.i, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i = i.strip()
            a = ("http://"+i)
            # print(a)
            try:
                resp = requests.get(a)
                if resp.status_code == 200:
                    # print(a + "站点存活")
                    resp_s = requests.get(a)
                    resp_s.encoding = 'utf-8'
                    obj = re.compile(r'iniUrl: "(?P<poc>.*?)",')
                    for ii in obj.finditer(resp_s.text):
                        # print(ii.group("poc"))
                        if ii.group("poc") == "api/init.json":
                            print(a + "存在未授权漏洞")
                            with open('扫描结果.txt', 'a') as file0:
                                print(a, file=file0)
                            continue
                        else:
                            print(ii + "不存在未授权漏洞")
                            continue
                else:
                    print(a + "站点错误")
            except:
                print(a+"站点问题")
        print("扫描完成")
