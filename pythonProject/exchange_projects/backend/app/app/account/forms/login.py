from fastapi import Body
from typing import Optional

class LoginRequestBody:
    """
       This is a dependency class, use it like:
           @app.post("/account/login")
           def login(form_data: LoginRequestForm = Depends()):


       It creates the following Form request parameters in your endpoint:

       username: username string.
       password: password string.
       login_ip: optional string. IP address of users.
       login_browser: optional string. Browser type of users.
       """
    def __init__(self,
                 username:str=Body(...),
                 password: str = Body(...),
                 mode: Optional[str] = Body('LOGIN'),
                 login_ip: Optional[str] = Body(''),
                 login_browser: Optional[str] = Body('')
                 ):
        self.username = username
        self.password = password
        self.login_ip = login_ip
        self.mode = mode
        self.login_browser = login_browser

