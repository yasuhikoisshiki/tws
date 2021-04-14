#!/usr/local/bin/python3.4

# パスワードやデータファイル名を指定 --- (*1)
PASSWORD = 'abcd'
FILE_MSG = './twsdata.txt'

# 
import os, sys, io, cgi, re

# デバッグ用
import cgitb
cgitb.enable()

out = lambda s: print(s, end="\n")

# ヘッダなどを出力 --- (*3)
out("Content-type: text/html\n")
out("<html>")
out("<head>")
out("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
out("</head>")
out("<body>")

form = cgi.FieldStorage()
if ("msg" in form):
    msg = form["msg"].value + "\n"
    with open(FILE_MSG, "wt", encoding="utf-8") as f:
        f.write(msg)
else:
    out("no data")
    
    # インプットを表示
out("TWS Rating Calc")
txt = ""
#if os.path.exists(FILE_MSG):
# ファイルから読み出して表示 --- (*7)
txt = open(FILE_MSG, "rt", encoding="utf-8").read()
txt = re.sub(r'(\r\n|\r|\n)', "\n", txt)

    # フォームを表示 --- (*8)
out("<form>")
out("")
out("<textarea cols='20' rows='20' name='msg'>" +txt + "</textarea><br>")
out("<input type= 'submit' value='Amend'>")
out("<br>")
out("</form>")

    
out("</body></html>")
