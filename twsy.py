#!/usr/local/bin/python3.4

FILE_MSG = './twsdata.txt'
U_LIST = './twsul.txt'
import cgi
import os

# デバッグ用
import cgitb
cgitb.enable()

#userlistの取り込み
ulist = ""
with open(U_LIST, mode='r') as g:
  for attd in g:
    ulist = ulist + "," + attd[0:6]
ulist = ulist[1:]
#ulist = ulist[:-1]
#print(ulist)

#twsdataの取り込み
tdata = ""
with open(FILE_MSG, mode='r') as h:
  for pref in h:
    #pref = re.sub(r'(\r\n|\r|\n)', "\n", pref)
    tdata=tdata + "," + pref[6:-1]
tdata=tdata[1:]
#print (tdata)

print ("Content-Type: text/html\n")
print ("<html><body><head>")
print ("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print ("</head>")

form = cgi.FieldStorage()
form_check = 0

# formでの変数有無チェック

if "name" not in form:
  form_check = 1

if "WineA" not in form:
  form_check = 1

if "WineB" not in form:
  form_check = 1

if "WineC" not in form:
  form_check = 1

if "WineD" not in form:
  form_check = 1

if "WineE" not in form:
  form_check = 1

if "WineF" not in form:
  form_check = 1

if form["name"].value not in ulist:
  form_check = 2

if form["name"].value in tdata:
  form_check = 3

print ("<FORM action='twsy.html' method='post'>")

# パラメータエラー時の対応 
if form_check == 1 :
  print ("<h2>Missing info!</h2>")
  print("Please try again by using Back Button, or ")
  print("<a href='http://www.tokyowine.org/twscalc/twsy.html'>Re-Input</a>")
  
elif form_check == 2 :
  print ("Your name is not in the list. Or spelled wrong?")
  print("Please try again by pushing Back Button, or ")
  print("<a href='http://www.tokyowine.org/twscalc/twsy.html'>Re-Input</a>")

elif form_check == 3 :  
  print ("You have already submitted the preferances!")
  print("Please check ")
  print("<a href='http://www.tokyowine.org/twscalc/twsr.html'>Result</a>")

else :
  if 21 == int(form["WineA"].value) + int(form["WineB"].value) + int(form["WineC"].value) + int(form["WineD"].value) +int(form["WineE"].value) + int(form["WineF"].value):
    msg=form["WineA"].value + form["WineB"].value + form["WineC"].value + form["WineD"].value +form["WineE"].value + form["WineF"].value + form["name"].value + "\n"
    with open(FILE_MSG, "a", encoding="utf-8") as f:
      f.write(msg)
    print ("Rating registered")
    print ("<a href='http://www.tokyowine.org/twscalc/twsr.py'>Result</a>")

  else :
    print("Wrong Input! Please check ABCDEF are ")
    print((form["WineA"].value) + (form["WineB"].value) + (form["WineC"].value) + (form["WineD"].value) +(form["WineE"].value) + (form["WineF"].value))
    print("Please try again by Back Button or ")
    print("<a href='http://www.tokyowine.org/twscalc/twsy.html'>Re-Input</a>")
  
print ("</body></html>")
