from fastapi import Body
from typing import Optional

class Disable2FaRequestBody:
    def __init__(self,mode:str=Body('DISABLE2FA'),
                 userid:str=Body(...),
                 privatekey:Optional[str]=Body(''),
                 publickey:Optional[str]=Body('')
                 ):
        self.mode=mode
        self.userid=userid
        self.privatekey=privatekey
        self.publickey=publickey

