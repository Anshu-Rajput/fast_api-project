from .route import account
from ..shared.db import return_connection
from .forms.set_password import SetpasswordRequestBody
from fastapi import Depends
@account.post('/setpassword')
async  def setpassword(body_data:SetpasswordRequestBody=Depends()):
    try:
        conn=return_connection()
        cursor=conn.cursor()
        cursor.callproc('SP_ResetPassword',(body_data.mode,body_data.email,body_data.oldpassword,body_data.password,body_data.userid,body_data.verifycode))
        result=[]
        for i in cursor:
            result=[*i]
            conn.commit()
        return result
    except Exception as e:
        print(e)