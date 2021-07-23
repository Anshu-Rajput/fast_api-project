from .route import account
from ..shared.db import return_connection
from .forms.forget2FAdisable import Forget2FADisableRequestBody
from fastapi import Depends
from .response import fetch_multiple

@account.post('/account/Forget2faDisable')
async  def forget2faDisable(body_data:Forget2FADisableRequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        sql = f" EXEC SP_enable_disable_2fa'{body_data.mode}','{body_data.userid}','{body_data.privatekey}','{body_data.publickey}','{body_data.verifycode}','{body_data.email}'  "
        result = fetch_multiple(sql, cursor)
        conn.commit()
        return result
        # cursor.callproc('SP_enable_disable_2fa',(body_data.mode,body_data.userid,body_data.privatekey,body_data.publickey,body_data.verifycode,body_data.email))
        # result=[]
        # for i in cursor:
        #     result=[*i]


    except Exception as e:
        print(e)

