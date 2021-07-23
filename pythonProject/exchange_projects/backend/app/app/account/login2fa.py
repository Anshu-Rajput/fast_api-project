from .route import account
from ..shared.db import return_connection
from .forms.login2FA import Login2FARequestBody
from fastapi import Depends
from .response import fetch_multiple

@account.post('/account/Login2fa')
async  def login2fa(body_data:Login2FARequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        sql = f"EXEC SP_Login '{body_data.mode}','{body_data.email}',,'{body_data.password}','{body_data.login_ip}','{body_data.login_browser}',{body_data.loglocation},'{body_data.userid}'"
        result = fetch_multiple(sql, cursor)
        conn.commit()
        return result
        # cursor.callproc('SP_Login',(body_data.mode,body_data.email,body_data.password,body_data.loginip,body_data.loginbrowser,body_data.loglocation,body_data.userid))
        # result=[]
        # for i in cursor:
        #     result=[*i]


    except Exception as e:
        print(e)

