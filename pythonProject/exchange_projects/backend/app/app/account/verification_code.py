from .route import account
from ..shared.db import return_connection
from .forms.verification_code import VerifycodeRequestBody
from fastapi import Depends

@account.post('/ forgotpassword/verification_code')
async def verifycode(bodydata:VerifycodeRequestBody=Depends()):
    conn=return_connection()
    cursor=conn.cursor()
    cursor.callproc('SP_MemberRegister',(bodydata.mode, bodydata.email,  bodydata.verifycode,bodydata.fname,
                                              bodydata.lname, bodydata.mobile, bodydata.loginid, bodydata.password,
                                              bodydata.refloginid, bodydata.actype,
                                              bodydata.refid, bodydata.isverify, bodydata.userid,
                                              bodydata.loginby, bodydata.country, bodydata.countrycode))
    result=[]
    for i in cursor:
        result=[*i]
        print(result)
    conn.commit()
    return result