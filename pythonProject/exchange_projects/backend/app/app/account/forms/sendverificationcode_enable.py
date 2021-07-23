from fastapi import Body
from typing import Optional

class SendVerifycodeEnable2FaRequestBody:
    def __init__(self,mode:str=Body('VERIFYCODETOENABLE2FA'),
                 userid:str=Body(...),
                 verifycode:Optional[ str] = Body(''),
                 privatekey:Optional[str]=Body(''),
                 publickey:Optional[str]=Body(''),



                 ):
        self.mode=mode
        self.userid=userid
        self.privatekey=privatekey
        self.publickey=publickey
        self.verifycode=verifycode


