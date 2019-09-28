import os
ku=input("输入你要安装的第三方库：")
cmd="pip install "+ku+" -i https://pypi.douban.com/simple"
os.system(cmd)
