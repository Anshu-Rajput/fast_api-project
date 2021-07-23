from .route import account
from ..shared.db import return_connection
from .forms.changepassword import ChangepasswordRequestBody
from fastapi import Depends
from .response import fetch_multiple


@account.post('/changepassword')
async def changepassword(body_data:ChangepasswordRequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        sql=f" EXEC SP_ResetPassword '{body_data.mode}','{body_data.email}','{body_data.oldpassword}','{body_data.password}','{body_data.userid}','{body_data.verifycode}'  "
        result=fetch_multiple(sql,cursor)
        conn.commit()
        return result
        # cursor.callproc('SP_ResetPassword', (body_data.mode,body_data.email,body_data.oldpassword,body_data.password,body_data.userid,body_data.verifycode,))
        # result = []
        # for i in cursor:
        #     result = [*i]
        #     conn.commit()

    except Exception as e:
        print(e)
