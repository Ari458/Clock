import requests

class InternetTime:
    def __init__(self):
        self.url="https://worldtimeapi.org"
        self.param="/api/ip"
        self.days={0:"Sunday",
            1:"Monday",
            2:"Tuesday",
            3:"Wednesday",
            4:"Thursday",
            5:"Friday",
            6:"Saturday"}
        self.months={"01":"January",
            "02":"February",
            "03":"March",
            "04":"April",
            "05":"May",
            "06":"June",
            "07":"July",
            "08":"August",
            "09":"September",
            "10":"October",
            "11":"November",
            "12":"December"}
        self.hour=""
        self.min=""
        self.sec=""
        self.day=""
        self.month=""
        self.year=""
        self.today_in_words=""
        self.month_in_words=""
        self.req=""
    def connection(self):
        try:
            self.req=requests.get(self.url+self.param)
            if self.req.status_code==200:
                return 200
            else:
                return 404
        except:
            return 404
    def genarateTime(self):
        data=self.req.json()
        
        date = data["datetime"][:10]
        time = data["datetime"][11:19]
        
        self.today_in_words = self.days[data["day_of_week"]]
        self.month_in_words = self.months[str(date[5:7])]
        
        self.year = date[:4]
        self.month = date[5:7]
        self.day = date[8:]
        
        self.hour = time[0:2]
        self.min = time[3:5]
        self.sec=time[6:]
    def getHour(self):
        x=self.hour
        return x
    def getMin(self):
        x=self.min
        return x
    def getSec(self):
        x=self.sec
        return x
    def getDay(self):
        x=self.day
        return x
    def getMonth(self):
        x=self.month
        return x
    def getYear(self):
        x=self.year
        return x
    def getToday_in_words(self):
        x=self.today_in_words
        return x
    def getMonth_in_words(self):
        x=self.month_in_words
        return x





            