class Keyring:
    data={}
    owner_fingerprint=''
    has_changes=False
from getpass import getpass
import sys
try:
    import gnupg
except ImportError:
    print("missing gnupg")
    sys.exit(-1)
import json
try:
        from Tkinter import Tk
except ImportError:
        from tkinter import Tk

t=Tk()
t.withdraw()
gpg = gnupg.GPG()
gpg.encoding= 'UTF-8'

k=Keyring()


def load_JSON(JSON_content):
    crypted_id_data=json.load(JSON_content)
    passphrase=getpass("passphrase?")
    for key in crypted_id_data:
        k.data[decrypt(key,passphrase=passphrase)]=crypted_id_data[key]

def update_file(path):
    crypted_data={}
    if k.owner_fingerprint is None:
        print("No fingerprint set, cant uncrypt!")
        return
    if k.owner_fingerprint is not None:
        for key in k.data.keys():
            crypted_data[encrypt(key)]=k.data[key]
    with open( path,'w') as file_obj:
        json.dump(crypted_data,file_obj)
        k.has_changes=False

def read_file(path):
    with open(path) as json_file:
        load_JSON(json_file)

def test_key_id(key):
    if k.data is None:
        print("no data loaded yet")
        return False
    if key not in k.data:
        print("key not found")
        return False
    else:
        return True

def get_password(key):
    return k.data[key]
    
def decrypt(encrypted,passphrase=None):
    if passphrase is None:
        passphrase = getpass("passphrase? ")
    return str(gpg.decrypt(str(encrypted),passphrase=str(passphrase)))

def encrypt(clear):
    return str(gpg.encrypt(clear,k.owner_fingerprint))

def update_password(dic_id,password):
    k.data[dic_id]=encrypt(password)
    k.has_changes=True

def list_ids():
    if k.data is not {}:
        for dicid in k.data.keys():
            print(dicid)
    else:
        print("no data loaded yet")

def set_owner_fingerprint():
    print("available private keys are :")
    i=0
    keys=gpg.list_keys(True)
    for key in gpg.list_keys(True):
        print(str(i)+'\t'+key['keyid']+'\t'+key['uids'][0])
        i+=1
    print("which one should be used? ")
    index=int_input_safe("which one should be used?",set_owner_fingerprint)
    if int(index)>i-1:
        print("key : "+str(index)+" not found")
        return
    print(keys[int(index)]['fingerprint']+' is your choice')
    k.owner_fingerprint=[keys[int(index)]['fingerprint']]

def int_input_safe(message,iffail):
    i=input(message)

    try :
        i=int(i)
    except ValueError:
        print("")
        print("you must type a number")
        print("")
        iffail()
    return i

def shell():
    print("---------------------------")
    print("available actions :")
    print("1.\tset private keys")
    print("2.\tlist ids")
    print("3.\tget password")
    print("4.\tupdate password")
    print("5.\tload file")
    print("6.\tsave to file")
    print("0 \tto exit")
    choice=int_input_safe("type your choice : ",shell)
    if choice not in [0,1,2,3,4,5,6]:
        print("choice matching no option")
    elif choice is 0:
        print("exiting")
        k=None
        return
    elif choice is 1:
        set_owner_fingerprint()
    elif choice is 2:
        list_ids()
    elif choice is 3:
        print("type the id of your key")
        key_id=input()
        t.clipboard_clear()
        if test_key_id(key_id):
            t.clipboard_append(decrypt(get_password(key_id)))
            t.after(10000,t.clipboard_clear)
    elif choice is 4:
        print("type the id to update")
        id_to_update=input("id : ")
        print("type the new password")
        password=getpass("password : ")
        confirm=getpass("confirm : ")
        if password==confirm:
            update_password(id_to_update,password)
        else:
            print("passwords mismatch")
    elif choice is 5:
        print ("type the path to the encrypted json file")
        path=input()
        try:
            read_file(path)
        except ValueError:
            print ("json doesn't seems right. check file content")
        except FileNotFoundError:
            print("File not find, check path")
        except Error:
            print("unhandled error")
    elif choice is 6:
        print("type where to save the file")
        path=input()
        update_file(path)
    print("")
    a=input("press a key to continue")
    shell()


#do the main check here

if len(sys.argv)<=1:
    print("nothing to do here, print help")
elif sys.argv[1] == "-id" and sys.args[2] is not None:
    if data is {}:
        read_file(file_path)
    if sys.argv[3] is not None and sys.argv[3] is not "-cb":
        print(decrypt(get_password(sys.argv[2])))
elif sys.argv[1] == "-l":
    list_keys()
elif sys.argv[1] == "-u" and sys.argv[2] is not None:
    #update by hidding the new password
    update_file(file_path)
elif sys.argv[1] == "-s":
    try:
        shell()
    except KeyboardInterrupt:
        print("Exiting")
