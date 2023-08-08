import smtplib
from windows_toasts import WindowsToaster, ToastText1, ToastDuration


def desktop_notification():
    wintoaster = WindowsToaster('SRT Sniper')
    newToast = ToastText1()
    newToast.SetBody('Train Found!')
    newToast.SetDuration(ToastDuration(ToastDuration.Short))
    wintoaster.show_toast(newToast)


def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        body = f'Subject: {subject}\n\n{message}'
        server.sendmail(sender_email, receiver_email, body.encode('utf-8'))
        server.quit()

        print('Message sent successfully!')

    except Exception as e:
        print(f'Failed to send message. Error: {e}')
