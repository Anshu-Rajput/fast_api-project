from fastapi import Body
from typing import Optional

class Enable2FaRequestBody:
    def __init__(self,mode:str=Body('ENABLE2FA'),
                 userid:str=Body(...),
                 privatekey:Optional[str]=Body(''),
                 publickey:Optional[str]=Body(''),
                 verifycode:str=Body(...),
                 email:str=Body(...)
                 ):
        self.mode=mode
        self.userid=userid
        self.privatekey=privatekey
        self.publickey=publickey
        self.verifycode=verifycode
        self.email=email

