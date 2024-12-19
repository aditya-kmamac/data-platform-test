from ftplib import FTP

with FTP(host="", user="", passwd="") as ftp:
    ftp.login()
    ftp.dir()