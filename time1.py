from datetime import datetime , timedelta
class Time_l:
    def __init__(self):
        self.today = datetime.now()

    def access (self , year , mounth , day):
        date = datetime(year , mounth , day)
        return date
    
    def _next_day(self):
        self.today = self.today + timedelta(day = 1)
        return self.today