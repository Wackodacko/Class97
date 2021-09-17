
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
    
def main():
    access_token='sl.A4qBSURM69j1wFRfne4P9uHkK7NMvqVS22gSvUCvhGuPDljU-eH6dPwKkYeBmMJzp6x9DxCtTywopkDvecd7PcqOtYjRPw8xBtLwIm-exKkZ1Zih_Tez6PUJNHFju-96-WBhq-8'
    transferData=TransferData(access_token)

    file_from=input('Enter The File Path To Transfer: ')
    file_to=input('Enter The Full Path To upload To DropBox: ')

    transferData.upload_file(file_from, file_to)
    print('File Has Been Moved')

main()