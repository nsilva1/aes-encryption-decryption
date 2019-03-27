import base64
from Crypto.Cipher import AES
from Crypto import Random
import os

#AES key must be either 16(128bits), 24(192bits), or 32(256bits) bytes long
#IV(Initialisation Vector) must be at least 16 bytes long
#suite = AES.new(Key,Mode,IV)
#text = suite.[encrypt/decrypt](text)

BLOCK_SIZE = 16
PADDING = '#'
key = Random.new().read(AES.block_size)
IV = os.urandom(16)

def pad(data, pad_with=PADDING):
    
    # Data to be encrypted must be in multiples of the BLOCK_SIZE.
    # if the data is less than the block size, the pad function fills it up to the block size
    # if the data is more than 16bytes, the data is filled up to the next multiple of 16, which is 32 bytes.
    
    return data + (BLOCK_SIZE - len(data) % BLOCK_SIZE) * PADDING

def encrypt(data):
    encryption_suite = AES.new(key, AES.MODE_CBC, IV)
    encrypted_text = encryption_suite.encrypt(pad(data))
    return(encrypted_text)

def decrypt(data):
    decryption_suite = AES.new(key, AES.MODE_CBC, IV)
    decrypted_text = decryption_suite.decrypt(data).rstrip(PADDING)
    return(decrypted_text)


def getData():
    user_file = raw_input("Enter path of ordinary text file: ")
    assert os.path.exists(user_file), "File not found at " + str(user_file)
    f = open(user_file,'r')
    text = f.readline()
    return text

text = getData()

fh = open('EncryptedFile.txt','w')
fh.write(encrypt(text))    
fh.close()

def getEncryptedData():
    g = open('EncryptedFile.txt', 'r')
    line = g.readline()
    return line

line = getEncryptedData


fg = open('DecryptedFile.txt','w')
fg.write(decrypt(encrypt(text)))             
fg.write("\n")
fg.write("IV :%s" %(IV))
fg.write("\n")
fg.write("key :%s" %(key))
fg.close()

