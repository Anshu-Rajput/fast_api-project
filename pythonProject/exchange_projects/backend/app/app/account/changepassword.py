from .route import account
from ..shared.db import return_connection
from .forms.changepassword import ChangepasswordRequestBody
from fastapi import Depends


@account.post('/changepassword')
async def changepassword(body_data:ChangepasswordRequestBody=Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()
        cursor.callproc('SP_ResetPassword', (body_data.mode,body_data.email,body_data.oldpassword,body_data.password,body_data.userid,body_data.verifycode,))
        result = []
        for i in cursor:
            result = [*i]
            conn.commit()
        return result
    except Exception as e:
        print(e)
