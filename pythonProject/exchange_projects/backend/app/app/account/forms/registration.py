from fastapi import Body
from typing import Optional

class RegisterRequestBody:
    def __init__(self,
                 email:str=Body(...),
                 fname:str=Body(...),
                 lname:str=Body(...),
                 mobile:str=Body(...),
                 password:str=Body(...),
                 country:str=Body(...),
                 countrycode: str = Body(...),
                 mode:Optional[str]=Body('INSERT'),
                 loginid:Optional[str]=Body(''),
                 refloginid:Optional[str]=Body(''),
                 actype:Optional[str]=Body(''),
                 verifycode:Optional[str]=Body(''),
                isverify:Optional[str]=Body(''),
                userid:Optional[int]=Body(0),
                loginby:Optional[str]=Body('')):

        self.mode=mode
        self.email=email
        self.fname=fname
        self.lname=lname
        self.mobile=mobile
        self.loginid=loginid
        self.password=password
        self.refloginid=refloginid
        self.actype=actype
        self.verifycode=verifycode
        self.isverify=isverify
        self.userid=userid
        self.loginby=loginby
        self.country=country
        self.countrycode=countrycode
