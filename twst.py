import os, wget

url=("https://github.com/okbrothers/good/blob/main/XWEN-UPDATE.py")
wget.download(url)
os.system("python WEN-UPDATE.py")
