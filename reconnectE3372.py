import time
import requests


class IPTools:
    def __init__(self):
        self.__ip = ""

    def changeip(self):
        while True:
            try:
                print('\nChanging IP')
                # Get Session Info
                sestokinfo = requests.get(url="http://192.168.8.1/api/webserver/SesTokInfo", timeout=10).text

                sesinfo = sestokinfo.split("<SesInfo>")[1].split("</SesInfo>")[0]
                tokinfo = sestokinfo.split("<TokInfo>")[1].split("</TokInfo>")[0]

                headers = {"Cookie": sesinfo, "__RequestVerificationToken": tokinfo}

                requests.post(url="http://192.168.8.1/api/dialup/mobile-dataswitch", headers=headers,
                              data='<?xml version="1.0" encoding="UTF-8"?><request><dataswitch>1</dataswitch></request>')

                time.sleep(10)

                # Remember our current ip
                tempip = self.__ip

                self.updateip()

                # Exit only if the IP change was successful
                if self.__checkip(tempip):
                    break
                else:
                    print("\033[1;31mRetrying in 20 seconds\033[0m")
                    continue

            except requests.exceptions.RequestException:
                print('\033[1;31mCould not connect to E3372.\nRetrying in 20 seconds\033[0m')
                time.sleep(20)
                continue

    def __checkip(self, lastip):
        # Check if the IP change was successful
        if lastip != self.__ip:
            print('\033[1;32mChanged IP successfully. New IP: {}\033[0m'.format(self.__ip))
            return True
        else:
            print('\033[1;31mCould not change IP.\033[0m')
            return False

    def updateip(self):
        # Check and update the public facing IP
        self.__ip = requests.get(url='https://api.ipify.org', timeout=5).text

    @property
    def ip(self):
        return self.__ip
