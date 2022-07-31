from tkinter import *
from dist.InternetTime import *
from dist.SystemTime import *
from dist.ConvertTime import *
from dist.GreetByTime import *



hour=""
min=""
sec=""
day=""
month=""
year=""
today_str=""
month_str=""
greet=""


it=InternetTime()
st=SystemTime()
ct=ConvertTime()
gt=GreetByTime()

def genT():
    if it.connection()==200:
        it.genarateTime()
        hour=it.getHour()
        min=it.getMin()
        sec=it.getSec()
        day=it.getDay()
        month=it.getMonth()
        year=it.getYear()
        today_str=it.getToday_in_words()
        month_str=it.getMonth_in_words()
        LABEL_TIME=hour+":"+min+":"+sec
            
    else:
        st.generateTime()
        hour=st.getHour()
        min=st.getMin()
        sec=st.getSec()
        day=st.getDay()
        month=st.getMonth()
        year=st.getYear()
        today_str=st.getToday_in_words()
        month_str=st.getMonth_in_words()
        LABEL_TIME=hour+":"+min+":"+sec
        

    greet=gt.getGreet(LABEL_TIME)
    
    return LABEL_TIME,"Good "+greet.lower(),day,month,year,today_str,month_str
    
    
 
#tkinter        
top= Tk()

height=108
width=260

top.geometry(str(width)+"x"+str(height))
top.minsize(width,height)
top.maxsize(width,height)
top.iconbitmap("C:/Users/Ari/Desktop/Clock/images/clock.ico")


my_greet= Label(top,text= "",font=("Courier", 10))
my_greet.grid(sticky="W",column=0,row=0,padx=0,pady=0)

my_time= Label(top,text= "",font=("Courier", 40))
my_time.grid(column=0,row=1,padx=0,pady=0)

my_date= Label(top,text= "",font=("Courier", 12))
my_date.grid(column=0,row=2,padx=0,pady=0)




def clock():
    my_greet.config(text=genT()[1])
    my_time.config(text=genT()[0])
    my_date.config(text=genT()[2]+" "+genT()[6]+" "+genT()[4])
    top.title(genT()[5])
    my_time.after(200,clock)
    
clock()
top.mainloop()


  



