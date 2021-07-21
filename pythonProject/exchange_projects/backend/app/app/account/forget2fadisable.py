from .route import account
from ..shared.db import return_connection
from .forms.forget2FAdisable import Forget2FADisableRequestBody
from fastapi import Depends

@account.post('/account/Forget2faDisable')
async  def forget2faDisable(body_data:Forget2FADisableRequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        cursor.callproc('SP_enable_disable_2fa',(body_data.mode,body_data.userid,body_data.privatekey,body_data.publickey,body_data.verifycode,body_data.email))
        result=[]
        for i in cursor:
            result=[*i]

        conn.commit()
        return result

    except Exception as e:
        print(e)

