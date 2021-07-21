from .route import account
from ..shared.db import  return_connection
from .forms.login import LoginRequestBody
from fastapi import Depends
@account.post("//login")
async def login(body_data:LoginRequestBody=Depends()):
    try:
        conn=return_connection()
        cursor=conn.cursor()
        cursor.callproc('SP_Login',('LOGIN', body_data.username, body_data.password, body_data.login_ip, body_data.login_browser))
        result=[]
        for i in cursor:
            result=[*i]
        return result

    except Exception as e:
        print(e)

