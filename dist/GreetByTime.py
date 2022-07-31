class GreetByTime:
    def __init__(self):
        self.greet=["Morning","Afternoon","Evening","Night","Noon","Mid-night"]
    def getGreet(self,time="",meridiem=""):
        meridiem=meridiem.upper()
        hour=int(time.split(":")[0])
        min=int(time.split(":")[1])
        if len(meridiem)!=0:
            if (((hour>=1 and hour <=3  and meridiem=="AM")  or (hour>=9 and hour<=11 and meridiem=="PM")) and min>=0 and min<=59) or (hour==12 and min>=1 and min<=59 and meridiem=="AM"):
                return self.greet[3]
            elif hour>=5 and hour<=8 and min>=0 and min<=59 and meridiem=="PM":
                return self.greet[2]
            elif ((hour>=1 and hour<=4 and min>=0 and min<=59) or (hour==12 and min>=1 and min<=59)) and meridiem=="PM":
                return self.greet[1]
            elif hour>=4 and hour<=11 and min>=0 and min<=59 and meridiem=="AM":
                return self.greet[0]
            elif hour==12 and min==0 and meridiem=="AM":
                return self.greet[5]
            elif hour==12 and min==0 and meridiem=="PM":
                return self.greet[4]
        else:
            if hour==0 and min==0:
                return self.greet[5]
            elif ((hour>=21 and hour<=23 and min>=0) or (hour==0 and hour<=3 and min>=1)) and min<=59:
                return self.greet[3]
            elif hour>=4 and hour<=11 and min>=0 and min<=59:
                return self.greet[0]
            elif hour==12 and min==0:
                return self.greet[4]
            elif hour>=12 and hour<=16 and min>=1 and min<=59:
                return self.greet[1]
            elif hour>=17 and hour<=23 and min>=0 and min<=59:
                return self.greet[2]
                 