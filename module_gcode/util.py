import datetime

class Util():

    def get_current_time(self):
        return str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

