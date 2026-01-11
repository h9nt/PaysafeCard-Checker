from requests import Session
from colorama import init
from os import system

# from threading import Thread

init(autoreset=True)
system("cls")


# 2345423423423423
class PaysafeChecker:
    def __init__(self, card_pin, debug=False):
        "Exapmle PIN: 1234567890123456"
        self.card_pin = card_pin
        self.request = Session()
        self.api_url = "https://rest.paysafecard.com/rest/card/pin/mobile"
        self.debug = debug

        if self.debug == True:
            log_mesasage = (
                f"[DEBUG] Initialized PaysafeChecker with PIN: {self.card_pin}"
            )
            print(log_mesasage)

    def check_balance(self):

        headers = {
            "cardpin": self.card_pin,
            "user-agent": "paysafecard/25.24.2 (SM-N975F; Android 9; okhttp/5.3.2)",
            "accept": "application/json",
            "accept-language": "de-DE",
            "accept-encoding": "gzip",
        }

        response = self.request.get(
            self.api_url
            + "?threatMetrixIdentifier=syokr78i2fmhge0d9w75hy4ygzxu74aq&clientApplicationKey=D4hqzBREaa349sIlNvtipsD2MoYkzXeF",
            headers=headers,
        ).json()
        if (
            "message" in response
            and response["message"]
            == "Die PaysafeCard ist bereits einem Konto zugewiesen."
        ):
            return "The PaysafeCard is already assigned to an account."
        elif (
            "message" in response
            and response["message"]
            == "Der PaysafeCard-Code exisitiert nicht. Überprüfe deine Eingabe."
        ):
            return "The entered PIN is invalid."
        return response


if __name__ == "__main__":
    print(PaysafeChecker(input("[?] Cardpin >>> ")).check_balance())
