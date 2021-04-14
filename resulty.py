#!/usr/local/bin/python3.4


# パスワードやデータファイル名を指定 --- (*1)
PASSWORD = 'abcd'
FILE_MSG = './twsdata.txt'
NOB = 6

# デバッグ用
import cgitb
cgitb.enable()

# 日本語を扱うために必要な設定 --- (*2)
import os, sys, io, cgi, re
#sys.stdin, sys.stdout, sys.etderr =  [
#  open(sys.stdin.fileno(),  'r', encoding='UTF-8'),
#  open(sys.stdout.fileno(), 'w', encoding='UTF-8'),
#  open(sys.stderr.fileno(), 'w', encoding='UTF-8')]

out = lambda s: print(s, end="\n")

# ヘッダなどを出力 --- (*3)
out("Content-type: text/html; charset=utf-8")
out("")
out("<html><body bgcolor='#F7F7E0'>")

# メッセージボードを表示
out("<head>")
out("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
out("</head>")
out("--------Rating Results --------<BR>")
out("<table width='340'><tr><td width='10%'>""A""</td><td width='10%'>""B""</td><td width='10%'>""C""</td><td width='10%'>""D""</td><td width='10%'>""E""</td><td width='10%'>""F""</td><td width='40%'>"" ""</td></tr></table>")
out("======================<BR>")
#out("")
Aw = []
Bw = []
Cw = []
Dw = []
Ew = []
Fw = []
Rt = []
if os.path.exists(FILE_MSG):

    # ファイルから読み出して表示 --- (*7)
    f = open(FILE_MSG, mode="r")
    count=0
    for p in f:
        if p[0] == "\n":
            continue
        Aw.append(int(p[0]))
        Bw.append(int(p[1]))
        Cw.append(int(p[2]))
        Dw.append(int(p[3]))
        Ew.append(int(p[4]))
        Fw.append(int(p[5]))
        print("<table width='340'><tr>")
        print("<td width='10%'>" + p[0] +"</td><td width='10%'>"+p[1]+"</td><td width='10%'>"+p[2]+"</td><td width='10%'>"+p[3]+"</td><td width='10%'>"+p[4]+"</td><td width='10%'>"+p[5]+"</td><td width='40%'>" + p[6:12] + "</td>")
        count +=1        
        print("</tr></table>")
    print("========1st/2nd/Last======<BR>")
    print("<table width='340'><tr><td width='10%'>" + str(Aw.count(1)) + "</td>")
    print("<td width='10%'>" + str(Bw.count(1)) + "</td>")
    print("<td width='10%'>"+ str(Cw.count(1)) + "</td>")
    print("<td width='10%'>"+ str(Dw.count(1)) + "</td>")
    print("<td width='10%'>"+ str(Ew.count(1)) + "</td>")
    print("<td width='10%'>"+ str(Fw.count(1)) + "</td>")
    print("<td width='40%'>"+ "FIRSTs" + "</td></tr></table>")
    print("<table width='340'><tr><td width='10%'>" + str(Aw.count(2)) + "</td>")
    print("<td width='10%'>" + str(Bw.count(2)) + "</td>")
    print("<td width='10%'>" + str(Cw.count(2)) + "</td>")
    print("<td width='10%'>" + str(Dw.count(2)) + "</td>")
    print("<td width='10%'>" + str(Ew.count(2)) + "</td>")
    print("<td width='10%'>" + str(Fw.count(2)) + "</td>")
    print("<td width='40%'>" + "SECONDs" + "</td</tr></table>")
    print("<table width='340'><tr><td width='10%'>" + str(Aw.count(6)) + "</td>")
    print("<td width='10%'>" + str(Bw.count(6)) + "</td>")
    print("<td width='10%'>" + str(Cw.count(6)) + "</td>")
    print("<td width='10%'>" + str(Dw.count(6)) + "</td>")
    print("<td width='10%'>" + str(Ew.count(6)) + "</td>")
    print("<td width='10%'>" + str(Fw.count(6)) + "</td>")
    print("<td width='40%'>"+ "LASTs" + "</td></tr></table>")
    print("========Total===========<BR>")
    print("<table width='340'><tr><td width='10%'>" + str(sum(Aw))+ "</td>")
    print("<td width='10%'>" + str(sum(Bw)) + "</td>")
    print("<td width='10%'>" + str(sum(Cw)) + "</td>")
    print("<td width='10%'>" + str(sum(Dw)) + "</td>")
    print("<td width='10%'>" + str(sum(Ew)) + "</td>")
    print("<td width='10%'>" + str(sum(Fw)) + "</td>")
    print("<td width='40%'>" + " " + "</td></tr></table>")

    Rt.append(sum(Aw))
    Rt.append(sum(Bw))
    Rt.append(sum(Cw))
    Rt.append(sum(Dw))
    Rt.append(sum(Ew))
    Rt.append(sum(Fw))
    #print("<BR>")
    print("========Rating==========<BR>")
    print("<table width='340'>") 
    #print(max(Rt))
    Rl = sorted(set(Rt))

    for i in Rt:
        #print(Rt.count(i))
        print("<td width='10%'>" + str(Rl.index(i)+1) + "</td>")
        
    #print(min(Rt))
    print("<td width='40%'>" + " " + "</td>")
    out("</tr></table>")

    #print(Aw.count("1")) 
        
    # フォームを表示 --- (*8)
    out("<form>")
    #out("Code: <input type='password' name='pw'><br>")
    out("")
    out("<br>")
    #out("<textarea style='width:20%' rows='20'>" +txt + "</textarea><br>")
    out("<a href= 'https://www.tokyowine.org/'>TWS Home Page</a>")
    out("</form>")
else:
    out("oops")

out("</body></html>")
