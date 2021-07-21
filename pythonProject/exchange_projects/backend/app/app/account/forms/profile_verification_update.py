from fastapi.param_functions import Body
from typing import Optional


class BasicProfileVerificationUpdateRequestForm:
    def __init__(
            self,
            userid: int = Body(0),
            nationality: int = Body(0),
            fullname: str = Body(...),
            birthdate: str = Body(...),
            address: str = Body(...),
            city: str = Body(...),
            pin: str = Body(...),
            pan: str = Body(...),
            mode: Optional[str] = Body('UPDATE'),
            id: Optional[int] = Body(0)

    ):
        self.mode = mode
        self.id = id
        self.userid = userid
        self.nationality = nationality
        self.fullname = fullname
        self.birthdate = birthdate
        self.address = address
        self.city = city
        self.pin = pin
        self.pan = pan
