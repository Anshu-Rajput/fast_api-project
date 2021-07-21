from fastapi.params import Depends
from ..shared.db import return_connection
from .route import market
from .forms.coin_insert import CoinInsertRequestBody

@market.post('/insert_coin')
async def insert_coin(
        coinname: str,
        coinprefix: str,
        cointype: str,
        isdepositactive: bool,
        iswithdrawactive: bool,
        iactive: bool,
        istradeactive: bool,
        ondate: str = "",
        cointransferaddress: str = "",
        withdrawfee: int = "",
        coindecimal: int = "",
        userid: int = ""):
        #body_data:CoinInsertRequestBody=Depends()):
    try:
        id:str=""
        mode:str="INSERT"
        conn=return_connection()
        cursor=conn.cursor()
        cursor.callproc('Sp_coin',(mode, id, coinname, coinprefix, cointype, isdepositactive, iswithdrawactive,
                                    iactive, istradeactive, ondate, cointransferaddress, withdrawfee, coindecimal, userid))
        for row in cursor:
            result=[*row]
        conn.commit()

        return result

    except Exception as e:
        print(e)


        #
        # for row in cursor:
        #     result=row
        # conn.commit()
        # return result



        # body_data.mode,
        # body_data.id,
        # body_data.coinname,
        # body_data.coinprefix,
        # body_data.cointype,
        # body_data.isdepositactive,
        # body_data.iswithdrawactive,
        # body_data.iactive,
        # body_data.istradeactive,
        # body_data.ondate,
        # body_data.cointransferaddress,
        # body_data.withdrawfee,
        # body_data.coindecimal,
        # body_data.userid



