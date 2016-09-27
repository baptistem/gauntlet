
import gnupg
import json

gpg = gnupg.GPG
gpg.encoding= 'UTF-8'
owner_fingerprint=[]
data={}

def new_key(gpg):
    return gpg.gen_key_input(key_type='RSA',key_length=4096)

def load_JSON(JSON_content):
    data=json.loads(JSON_content)

def update_file(file_obj):
    json.dump(data,file_obj)

def read_file(path):
    with open(path) as json_file:
        load_JSON(json_file)

def get_password(key):
    if key not in data:
        print("key not find : "+key)
        return
    encrypted=data[key]
    
def update_password(key,password):
    data[key]=gpg.encrypt(data,owner_fingerprint)

def list_keys():
    if data is not {}:
        print data.keys
    else:
        print "no data loaded yet"


