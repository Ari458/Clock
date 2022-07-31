from datetime import datetime



class SystemTime:
    def __init__(self):
        self.hour=""
        self.min=""
        self.sec=""
        self.day=""
        self.month=""
        self.year=""
        self.today_in_words=""
        self.month_in_words=""
        self.days={6:"Sunday",
            0:"Monday",
            1:"Tuesday",
            2:"Wednesday",
            3:"Thursday",
            4:"Friday",
            5:"Saturday"}
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
    def generateTime(self):
        data=str(datetime.now())
        
        self.hour=data[11:13]
        self.min=data[14:16]
        self.sec=data[17:19]
        
        self.day=data[8:10]
        self.month=data[5:7]
        self.year=data[:4]
        
        self.today_in_words=self.days[datetime.now().weekday()]
        self.month_in_words=self.months[str(self.month)]
    def getHour(self):
        x=self.hour
        return x
    def getSec(self):
        x=self.sec
        return x
    def getMin(self):
        x=self.min
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
   
   
   