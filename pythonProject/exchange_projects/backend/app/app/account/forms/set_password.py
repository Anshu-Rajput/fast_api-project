from typing import Optional
from fastapi import Body

class SetpasswordRequestBody:
    def __init__(self,
                 email:str=Body(...),
                 mode:str=Body('CHANGEFORGOTPASSWORD'),
                 password: str = Body(...),
                 oldpassword:Optional[str]=Body(''),
                 userid:Optional[str]=Body(''),
                 verifycode:Optional[str]=Body(''),





                 ):



        self.mode=mode
        self.email=email
        self.oldpassword = oldpassword
        self.password=password
        self.userid=userid
        self.verifycode=verifycode