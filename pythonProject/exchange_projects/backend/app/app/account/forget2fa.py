from .route import account
from ..shared.db import return_connection
from .forms.forget2fa import Forget2FARequestBody
from fastapi import Depends
from .response import fetch_multiple

@account.post('/account/Forget2fa')
async  def forget2fa(body_data:Forget2FARequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        sql = f" EXEC SP_enable_disable_2fa'{body_data.mode}','{body_data.userid}','{body_data.privatekey}','{body_data.publickey}','{body_data.verifycode}','{body_data.email}'  "
        result = fetch_multiple(sql, cursor)
        conn.commit()
        return result
        #cursor.callproc('SP_enable_disable_2fa',(body_data.mode,body_data.userid,body_data.privatekey,body_data.publickey,body_data.verifycode,body_data.email))
        #result=[]
        #for i in cursor:
        #    result=[*i]

        #conn.commit()
        #return result

    except Exception as e:
        print(e)

