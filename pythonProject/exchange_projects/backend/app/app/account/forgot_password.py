from .route import account
from ..shared.db import return_connection
from .forms.forgot_password import ForgotpasswordRequestBody
from fastapi import Depends
from .registration import sendmail

@account.post('/forgot_password')
async  def forgot_password(body_data:ForgotpasswordRequestBody=Depends()):
    try:
        conn=return_connection()
        cursor=conn.cursor()
        print("working")
        cursor.callproc('SP_ResetPassword',(body_data.mode, body_data.email, body_data.oldpassword, body_data.password))
        result=[]
        for i in cursor:
            result=[*i]

        #html=result[3]
        #sendmail(body_data.email,html)
        print(result,"hii ")

        conn.commit()
        return result
    except Exception as e:
        print(e)