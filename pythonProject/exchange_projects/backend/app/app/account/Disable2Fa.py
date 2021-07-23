from .route import account
from ..shared.db import return_connection
from .forms.disable2FA import Disable2FaRequestBody
from fastapi import Depends
from .response import fetch_multiple

@account.post('/account/disable2FA')
async  def disable2fa(body_data:Disable2FaRequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        sql=sql=f"EXEC SP_enable_disable_2fa'{body_data.mode}','{body_data.userid}','{body_data.privatekey}','{body_data.publickey}'"
        result=fetch_multiple(sql,cursor)

        conn.commit()
        return result

        # cursor.callproc('SP_enable_disable_2fa',(body_data.mode,body_data.userid,body_data.privatekey,body_data.publickey))
        # # result=[]
        # for i in cursor:
        #     result=[*i]



    except Exception as e:
        print(e)
