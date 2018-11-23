import ftplib, ftputil, os
from ftplib import FTP, all_errors
import sys
import codecs

import top as top

HOST = 'ftp.someserver.net'
ftp = FTP(HOST)

user = 'user'
psw = 'pass'
ftp.login(user, psw)
ftp.cwd('www')

dst = 'X:/Files/FTP_test/'
src = '/www'
site = 'sitename.dns'
os.chdir(dst)
try:
    os.mkdir(site)
except FileExistsError:
    pass

dst = dst + site
os.chdir(dst)

filenames = ftp.nlst()
for filename in filenames:
    host_file = os.path.join(
        dst, filename
        )
    try:
        with open(host_file, 'wb') as local_file:
            ftp.retrbinary('RETR ' + filename, local_file.write)
        print('Копируется файл', filename)
    except ftplib.all_errors as e:
        print('Error FTP:', e)

ftp.quit()
