from typing import Optional
from fastapi import Body

class Login2FARequestBody:
    def __init__(self,
                 mode:str=Body('LOGIN2FA'),
                 email:str=Body(...),
                 password:str=Body(...),
                 loginip:Optional[str]=Body(''),
                 loginbrowser:Optional[str]=Body(''),
                 loglocation:Optional[str]=Body(''),
                 userid:Optional[int]=Body(0)):
        self.mode=mode
        self.email=email
        self.password=password
        self.loginip=loginip
        self.loginbrowser=loginbrowser
        self.loglocation=loglocation
        self.userid=userid