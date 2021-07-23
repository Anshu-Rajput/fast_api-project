from .route import account
from ..shared.db import return_connection
from .forms.registration import RegisterRequestBody
from fastapi import Depends
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


@account.post("/registration")
async def register(bodydata: RegisterRequestBody = Depends()):
    try:
        conn = return_connection()
        cursor = conn.cursor()

        cursor.callproc('SP_MemberRegister',(bodydata.mode, bodydata.email, bodydata.fname,
                                              bodydata.lname, bodydata.mobile, bodydata.loginid, bodydata.password,
                                              bodydata.refloginid, bodydata.actype,bodydata.verifycode,
                                             bodydata.isverify, bodydata.userid,bodydata.loginby, bodydata.country, bodydata.countrycode))

        # result=cursor.fetchall()
        result = []

        for i in cursor:
            result = [*i]
            break
        conn.commit()
        html = result[3]
        print(result)

        return result
    except Exception as e:
        print(e)

# sendmail---->

def sendmail(email, html):
    print("sendmail is working")
    sender_mail = "anshu.rajput452000@gmail.com"
    reciever_mail = email
    subject = "verification code"
    html_content = html
    message = Mail(sender_mail, email, subject, html_content)
    try:
        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print("Exiting send mail")

    except Exception as e:
        print(e.message)
    #---->show all data
@account.post("/account/register/showall")
async def display():
     conn=return_connection()
     cursor=conn.cursor()
     cursor.execute("select * from membermaster")  # temp_membermaster
     result = cursor.fetchall()
     return result


     # rows = cursor.fetchall()
     # columns = [column[0] for column in cursor.description]
     # for i in rows:
     #     list.append(dict(zip(columns, i)))
     # return list
