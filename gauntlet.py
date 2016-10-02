import sys
import gnupg
import json

gpg = gnupg.GPG
gpg.encoding= 'UTF-8'
owner_fingerprint=[]
data={}
file_path=""

def new_key(gpg):
    return gpg.gen_key_input(key_type='RSA',key_length=4096)

def load_JSON(JSON_content):
    data=json.loads(JSON_content)

def update_file(path):
    with open( path) as file_obj:
        json.dump(data,file_obj)

def read_file(path):
    with open(path) as json_file:
        load_JSON(json_file)

def get_password(key):
    if key not in data:
        print("key not find : "+key)
        return
    encrypted=data[key]
    
def decrypt(encrypted):
    gpg.decrypt(encrypted)

def update_password(key,password):
    data[key]=gpg.encrypt(data,owner_fingerprint)

def list_keys():
    if data is not {}:
        print data.keys
    else:
        print "no data loaded yet"

#do the main check here
if len(sys.argv)<=1:
    print "nothing to do here, print help"
    

elif sys.argv[1] is "-id" and sys.args[2] is not None:
    if data is {}:
        read_file(file_path)
    if sys.argv[3] is not None and sys.argv[3] is not "-cb":
        print(decrypt(get_password(sys.argv[2])))

elif sys.argv[1] is "-l":
    list_keys()

elif sys.argv[1] is "-u" and sys.argv[2] is not None:
    #update by hidding the new password
    update_file(file_path)


    
    

