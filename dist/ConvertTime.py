class ConvertTime:
    def format_12_hours(self,format_24):
        hour=int(format_24.split(":")[0])
        min=int(format_24.split(":")[1])
        meridiem=""
        
        if hour>=0 and hour<=11 and min>=0 and min<=59:
            meridiem="AM"
        else:
            hour=hour-12
            meridiem="PM"
            
        if hour<10:
            time="0"+str(hour)+":"+str(min)+" "+meridiem   
        else:
            time=str(hour)+":"+str(min)+" "+meridiem
            
        return time
    def format_24_hours(self,format_12,meridiem):
        hour=int(format_12.split(":")[0])
        min=int(format_12.split(":")[1])
        
        if hour<=11 and hour>=0:
            if meridiem=="PM":
                hour=hour+12
                
            if hour<10:
                time="0"+str(hour)+":"+str(min)+" "+meridiem   
            else:
                time=str(hour)+":"+str(min)+" "+meridiem    
                
            return time    
        else:
            return -1  