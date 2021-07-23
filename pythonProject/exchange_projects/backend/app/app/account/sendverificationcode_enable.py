from .route import account
from ..shared.db import return_connection
from .forms.sendverificationcode_enable import SendVerifycodeEnable2FaRequestBody
from fastapi import Depends
from .response import fetch_multiple

@account.post('/account/sendverifycodetoenable2fa')
async  def send_verifycode_enable2fa(body_data:SendVerifycodeEnable2FaRequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        sql = sql = f"EXEC SP_enable_disable_2fa'{body_data.mode}','{body_data.userid}','{body_data.privatekey}','{body_data.publickey}','{body_data.verifycode}'"
        result = fetch_multiple(sql, cursor)
        conn.commit()
        return result
    except Exception as e:
        print(e)
