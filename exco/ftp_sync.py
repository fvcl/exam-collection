import ftplib
import os

password = "4G%&R!$.}9#x,!>"
def sync_files():
    # send file to FTP server
    ftp = ftplib.FTP("fachverein-cl.ch")
    username = "u220318531"
    ftp.login(username, password)
    ftp.cwd('pdfs')
    files = os.listdir('static/data')
    full_path = os.path.join(os.getcwd(), 'static/data')
    print(full_path)
    for file in files:
        print(file)
        if file not in ftp.nlst():
            print('Sending file to FTP server: ' + file)
            with open(full_path + file, 'rb') as f:
                ftp.storbinary('STOR ' + file, f)

def send_file_to_ftp_server(file):
    # send file to FTP server
    ftp = ftplib.FTP("fachverein-cl.ch")
    username = "u220318531"
    ftp.login(username, password)
    ftp.cwd('pdfs')
    print('Sending file to FTP server: ' + file)
    file = file.split('/')[-1]
    with open(file, 'rb') as f:
        ftp.storbinary('STOR ' + file, f)

def get_files_from_ftp_server():
    # get file from FTP server
    ftp = ftplib.FTP("fachverein-cl.ch")
    username = "u220318531"
    ftp.login(username, password)
    ftp.cwd('pdfs')
    files = ftp.nlst()
    files = [file for file in files if file not in ['.', '..'] and file.lstrip("STOR ") not in os.listdir('static/data')]
    for file in files:
        with open('static/data/' + file, 'wb') as f:
            ftp.retrbinary('RETR ' + file, f.write)