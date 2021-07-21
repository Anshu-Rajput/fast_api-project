from typing import Optional
from fastapi import Body

class Forget2FARequestBody:
    def __init__(self,
                 userid: int = Body(...),
                 privatekey: Optional[str] = Body(""),
                 publickey: Optional[str] = Body(""),
                 mode: Optional[str] = Body('FORGOT2FA'),
                 verifycode: Optional[str] = Body(''),
                 email:str=Body(...)
                 ):

        self.mode=mode
        self.userid = userid
        self.privatekey=privatekey
        self.publickey = publickey
        self.verifycode=verifycode
        self.email=email




