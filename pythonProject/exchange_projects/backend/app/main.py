import uvicorn
from fastapi import FastAPI
from app.account.route import account
from app.market.route import market


app=FastAPI()
app.include_router(account)
app.include_router(market)


@app.get("/first")
async def trial():
    return "successfull"



if __name__ == "__main__":
    uvicorn.run(app, port=8000)
