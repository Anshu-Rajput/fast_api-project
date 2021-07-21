from fastapi.params import Depends

from .route import  account
from ..shared.db import return_connection
from .forms.profile_verification_update import BasicProfileVerificationUpdateRequestForm


@account.post('/account/profile_verification_update')
async def profile_verification_update(body_data:BasicProfileVerificationUpdateRequestForm=Depends()):
    try:
        conn=return_connection()
        cursor=conn.cursor()
        cursor.callproc('Sp_basicprofileinfo',(body_data.mode, body_data.id, body_data.userid, body_data.nationality, body_data.fullname, body_data.birthdate, body_data.address, body_data.city, body_data.pin, body_data.pan))

        result = []
        for i in cursor:
            result = [*i]
        conn.commit(

        )
        return result

    except Exception as e:
        print(e)