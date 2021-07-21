from .route import account
from ..shared.db import return_connection
from .forms.verify_mail import VerifymailRequestBody
from fastapi import Depends


@account.post("//verifymail")
async def verifymail(body_data:VerifymailRequestBody=Depends()):
    try:
        conn=return_connection()
        cursor=conn.cursor()
        cursor.callproc('SP_MemberRegister',(body_data.mode,body_data.email,body_data.fname,
                            body_data.lname,body_data.mobile,body_data.loginid,body_data.password,body_data.refloginid,body_data.actype,
                            body_data.verifycode,body_data.isverify,body_data.userid,body_data.loginby,body_data.country,body_data.countrycode))
        result=[]
        for i in cursor:
            result=[*i]

        conn.commit()
        return result
    except Exception as e:
        print(e)