from .route import account
from ..shared.db import  return_connection
from .forms.login import LoginRequestBody
from fastapi import Depends
from .response import fetch_multiple
@account.post("//login")
async def login(body_data:LoginRequestBody=Depends()):
    try:
        sql=f"EXEC SP_Login '{body_data.mode}','{body_data.username}','{body_data.password}','{body_data.login_ip}','{body_data.login_browser}'"
        conn=return_connection()
        cursor=conn.cursor()
        result=fetch_multiple(sql,cursor)
        conn.commit()
        return result
        #cursor.callproc('SP_Login',('LOGIN', body_data.username, body_data.password, body_data.login_ip, body_data.login_browser))
        # result=[]
        # for i in cursor:
        #     result=[*i]


    except Exception as e:
        print(e)

