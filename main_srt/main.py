import time
import json
from SRT import SRT
from notification import *
from datetime import datetime


USER_INFO = './user_info.json'
WINDOW_SEAT = True


if __name__ == '__main__':
    # Get user info from user_info.json
    with open(USER_INFO, encoding='utf8') as fp:
        user_info = json.load(fp)

    login_info = user_info['login_info']
    email_info = user_info['notification']['email']
    search_params = user_info['search_params']

    srt = SRT(login_info['username'], login_info['password'], False)

    reserved = False
    while not reserved:
        for params in search_params:
            trains = srt.search_train(params['dep'], params['arr'], params['date'], params['time'], params['time_limit'], False)
            now = datetime.now()
            print(f'[{now.time()}] {trains}')

            if len(trains) > 0:
                for train in trains:
                    if train.seat_available():
                        print(' *** Seat Avaiable! *** ')
                        srt.login()
                        srt.reserve(trains[0], window_seat=True)
                        print(srt.get_reservations())
                        send_email(
                            email_info['sender_email'],
                            email_info['sender_password'],
                            email_info['receiver_email'],
                            'An SRT ticket has been reserved!',
                            srt.get_reservations()
                        )
                        srt.logout()

                        while True:
                            desktop_notification()
                            time.sleep(30)
        time.sleep(2)
