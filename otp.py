#!/usr/bin/env python3
import os,requests,time,pyotp
import hashlib,base64,uuid,random
class otp:
    def __init__(self) -> None:
        self.user="root"
        self.homePath="/root"
        self.keyPath=self.homePath+"/.otpkey"
        self.ip=requests.get('https://checkip.amazonaws.com').text.strip()
    
    def changePassword(self,password):
        os.system("echo \""+self.user+":"+password+"\" | chpasswd")

    @property
    def keyfile(self):
        if not os.path.isfile(self.keyPath):
            self.setupOtp()
        with open(self.keyPath,'r') as key:
            return key.read()

    @keyfile.setter
    def keyfile(self,content):
        with open(self.keyPath,'w',encoding='utf-8') as key:
            key.write(content)

    def key(self):
        key0=hashlib.md5(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
        key1=hashlib.sha512(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
        key2=hashlib.sha3_512(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
        keys=base64.b32encode(locals()['key'+str(random.randint(0,2))].encode(encoding="utf-8")).decode("utf-8").rstrip("=")
        return keys

    def setupOtp(self):
        self.keyfile=self.key()
        uri=pyotp.TOTP(self.keyfile).provisioning_uri(self.ip, issuer_name=self.user)
        urifileContent=uri+"\nhttps://api.qrserver.com/v1/create-qr-code/?size=1024x1024&data="+uri
        with open(self.homePath+"/.otpProvisioningUri",'w',encoding='utf-8') as urifile:
            urifile.write(urifileContent)

    def getOtpn(self):
        otp=pyotp.TOTP(self.keyfile)
        return otp.now()

if __name__ == "__main__":
    #print("helloworld")
    otp_service=otp()
    otpn_last=""
    while True:
        otpn=otp_service.getOtpn()
        print("otpn="+otpn+", otpn_last="+otpn_last)
        if otpn_last != otpn:
            otpn_last=otpn
            otp_service.changePassword(otpn_last)
        time.sleep(1)
