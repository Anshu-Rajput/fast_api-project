from fastapi import Body
from typing import Optional

class VerifymailRequestBody():
    def __init__(self,
                 email:Optional[str]=Body(...),
                 fname:Optional[str]=Body(...),
                 lname:Optional[str]=Body(...),
                 mobile:Optional[str]=Body(...),
                 password:Optional[str]=Body(...),
                 country:Optional[str]=Body(...),
                 countrycode:Optional[str] = Body(...),
                 mode:Optional[str]=Body('VERIFYEMAIL'),
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
