from typing import Optional
from fastapi import Body


class ChangepasswordRequestBody:
    def __init__(self,
                 email: str = Body(...),

                 oldpassword: str = Body(...),
                 password: str = Body(...),
                 userid: int = Body(...),
                 mode: Optional[str] = Body('CHANGEPASSWORD'),
                 verifycode: Optional[str] = Body(''),

                 ):
        self.mode = mode
        self.email = email
        self.oldpassword = oldpassword
        self.password = password
        self.userid = userid
        self.verifycode = verifycode
