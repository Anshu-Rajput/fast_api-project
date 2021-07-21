from fastapi import Body
from typing import Optional
class ForgotpasswordRequestBody:

    def __init__(self,
                 email:str=Body(...),
                 mode:str=Body('FORGOTPASSWORD'),
                 oldpassword:Optional[str]=Body(...),
                 password:Optional[str]=Body(...),
                 userid:Optional[int]=Body(0),
                 verifycode:Optional[str]=Body(...)):

        self.mode=mode
        self.email=email
        self.oldpassword=oldpassword
        self.password=password
        self.userid=userid
        self.verifycode=verifycode
