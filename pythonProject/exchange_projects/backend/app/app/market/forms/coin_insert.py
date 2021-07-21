from fastapi import Body
#from typing import Optional
class CoinInsertRequestBody:
    def __init__(self,
                 mode:str=Body('INSERT'),
                 id:int=Body(0),
                 coinname:str=Body(...),
                 coinprefix:str=Body(...),
                 cointype:str=Body(...),
                 isdepositactive:int=Body(0),
                 iswithdrawactive:int=Body(0),
                 iactive:int=Body(0),
                 istradeactive:int=Body(0),
                 ondate:str=Body(...),
                 cointransferaddress:str=Body(...),
                 withdrawfee:int=Body(0),
                 coindecimal:int=Body(0),
                 userid:int=Body(0)



                 ):

        self.mode=mode
        self.id=id
        self.coinname=coinname
        self.coinprefix=coinprefix
        self.cointype=cointype
        self.isdepositactive=isdepositactive
        self.iswithdrawactive=iswithdrawactive
        self.iactive=iactive
        self.istradeactive=istradeactive
        self.ondate=ondate
        self.cointransferaddress=cointransferaddress
        self.withdrawfee=withdrawfee
        self.coindecimal=coindecimal
        self.userid=userid
