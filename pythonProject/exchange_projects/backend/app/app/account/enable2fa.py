from .route import account
from ..shared.db import return_connection
from .forms.enable2FA import Enable2FaRequestBody
from fastapi import Depends
from .response import fetch_multiple

@account.post('/account/enable2fa')
async  def enable2fa(body_data:Enable2FaRequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        sql = sql = f"EXEC SP_enable_disable_2fa'{body_data.mode}','{body_data.userid}','{body_data.privatekey}','{body_data.publickey}','{body_data.verifycode}','{body_data.email}'"
        result = fetch_multiple(sql, cursor)
        conn.commit()
        return result
        # cursor.callproc('SP_enable_disable_2fa',(body_data.mode,body_data.userid,body_data.privatekey,body_data.publickey))
        # result=[]
        # for i in cursor:
        #     result=[*i]

        # conn.commit()
        # return result

    except Exception as e:
        print(e)
