#! /usr/local/bin/python3.4
import cgi

form = cgi.FieldStorage()

print 'Content-type: text/html'
print
print '<HTML>'
print '<HEAD>'
print '<TITLE>GUEST BOOK</TITLE>'
print '</HEAD>'
print '<BODY BGCOLOR="#ffffff">'

for x in form.keys():
    print '%s = %s<BR>' % (x, form[x].value)

print '</BODY>'
print '</HTML>'
