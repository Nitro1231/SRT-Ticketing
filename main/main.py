import time
import json
from SRT import SRT
from windows_toasts import WindowsToaster, ToastText1, ToastDuration


USER_INFO = './user_info.json'
WINDOW_SEAT = True


def search_trains(srt: SRT, params: dict) -> list['SRTTrain']:
    return srt.search_train(params['dep'], params['arr'], params['date'], params['time'], params['time_limit'], params['available_only'])


def notification():
    wintoaster = WindowsToaster('SRT Sniper')
    newToast = ToastText1()
    newToast.SetBody('Train Found!')
    newToast.SetDuration(ToastDuration(ToastDuration.Short))
    wintoaster.show_toast(newToast)


if __name__ == '__main__':
    # Get user info from user_info.json
    with open(USER_INFO, encoding='utf8') as fp:
        user_info = json.load(fp)

    login_info = user_info['login_info']
    search_params = user_info['search_params']

    srt = SRT(login_info['username'], login_info['password'], False)

    reserved = False
    while not reserved:
        for params in search_params:
            trains = srt.search_train(params['dep'], params['arr'], params['date'], params['time'], params['time_limit'], params['available_only'])
            print(trains)

            if len(trains) > 0:
                print('Seat Avaiable!')
                srt.login()
                srt.reserve(trains[0], window_seat=True)
                srt.logout()

                while True:
                    notification()
                    time.sleep(10)
            time.sleep(3)
