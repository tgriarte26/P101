import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
                for filename in files:
                    local_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(local_path, file_from)
                    dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
        
def main():
    access_token = 'sl.BKIj-PbxcV9M8ic4JkhlwFqpDCRtjRZwHg6Sg-IGnQWNkfJc_JEfFn7sToYH0gfyJI-qnoBJeSwCXR1wEj3g4_bt3uIsKE06xL31GNXhwD5sVceWPigBfl7nylZmBa_P97S01eM'
    transferData = TransferData(access_token)

    file_from = str(input("Enter folder path:-"))
    file_to = input("Enter full path that will be uploaded to dropbox:-")

    transferData.upload_file(file_from,file_to)
    print("File has been moved")

main()