import datetime
def dateAndTime():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    hour=datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
    second=datetime.datetime.now().second
    dateAndTime=str(year)+"-"+str(month)+"-"+str(day)+"-"+str(hour)+"-"+str(minute)+"-"+str(second)
    
    return dateAndTime
    