from .route import account
from ..shared.db import return_connection
from .forms.login2FA import Login2FARequestBody
from fastapi import Depends

@account.post('/account/Login2fa')
async  def login2fa(body_data:Login2FARequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        cursor.callproc('SP_Login',(body_data.mode,body_data.email,body_data.password,body_data.loginip,body_data.loginbrowser,body_data.loglocation,body_data.userid))
        result=[]
        for i in cursor:
            result=[*i]

        conn.commit()
        return result

    except Exception as e:
        print(e)

