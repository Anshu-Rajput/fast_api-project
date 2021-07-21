from typing import Optional
from fastapi import Body

class Forget2FADisableRequestBody:
    def __init__(self,
                 userid: int = Body(...),
                 verifycode:str = Body(''),
                 privatekey: Optional[str] = Body(""),
                 publickey: Optional[str] = Body(""),
                 mode: Optional[str] = Body('FORGOT2FADISABLE'),
                 email:Optional[str]=Body('')
                 ):

        self.mode=mode
        self.userid = userid
        self.privatekey=privatekey
        self.publickey = publickey
        self.verifycode = verifycode
        self.email=email




