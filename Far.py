import pandas as pd
from datetime import date
from nsepy import get_history

expiry_dates=[date(2017,9,28),date(2017,10,26),date(2017,11,30),date(2017,12,28),date(2018,1,25),date(2018,2,22),date(2018,3,28),date(2018,4,26),date(2018,5,31),date(2018,6,28),date(2018,7,26),date(2018,8,30),date(2018,9,27),date(2018,10,25)]

start_dat=[date(2017,9,1),date(2017,9,29),date(2017,10,27),date(2017,12,1),date(2017,12,29),date(2018,1,29),date(2018,2,23),date(2018,4,2),date(2018,4,27),date(2018,6,1),date(2018,6,29),date(2018,7,27)]
end_dat=[date(2017,9,28),date(2017,10,26),date(2017,11,30),date(2017,12,28),date(2018,1,25),date(2018,2,22),date(2018,3,28),date(2018,4,26),date(2018,5,31),date(2018,6,28),date(2018,7,26),date(2018,8,30)]

df=pd.DataFrame()

for i in range(0,12):
    stock_fut=get_history(symbol="TVSMOTOR",
                        start=start_dat[i],
                        end=end_dat[i],
                        futures=True,
                        expiry_date=expiry_dates[i+2])
    df=df.append(stock_fut)
    
df.to_csv(r'C:\Users\KUNAL V\Downloads\TVSMOTOR_far.csv')