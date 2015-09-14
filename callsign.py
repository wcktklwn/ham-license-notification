name = 'Lastname, Firstname Initial'
address = '123 Street Blvd'

fromemail = 'from@email.net'
frompassword = 'supersecurepassword'
toemail = 'to@email.net'


import urllib, zipfile, os, datetime, smtplib

now = datetime.datetime.now()
now = now.strftime("%a")
now = now.lower()

fcclist = 'http://wireless.fcc.gov/uls/data/daily/l_am_' + now + '.zip'

urllib.urlretrieve (fcclist, "ham_daily.zip")

is_zip = zipfile.is_zipfile('ham_daily.zip')
if is_zip:
        zf = zipfile.ZipFile('ham_daily.zip', 'r')
        zf.extract("EN.dat")

with open('EN.dat', 'r') as searchfile:
        for line in searchfile:
                if name and address in line:
                        line = line.split('|', 26 )
                        callsign = 'Your new call sign is: ' + line[4]
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(fromemail, frompassword)
                        message = """\From: %s\nTo: %s\nSubject: Callsign\n\n%s""" % (fromemail, toemail, callsign)
                        server.sendmail(fromemail, toemail, message)
                        server.close()

os.remove("ham_daily.zip")
os.remove("EN.dat")