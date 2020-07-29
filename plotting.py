#from matplotlib import pyplot as plt
from matplotlib import style
#doing histograms
#plt.title("My Histogram")
#ages = [18 , 19 ,21 , 25 , 26 , 30 , 32 , 38, 45 , 55]
#plt.hist(ages, bins =5 , edgecolor='black')
#bins are like the divisional categories , the number of ages in the range of the bins is plotted with the
#plt.hist() , bins can be declared explicitly as the following example:
#bins= [10 ,20 , 30 , 40 , 50 ,60]# length of this list is the number of bins plotted
#plt.hist(ages , bins= bins , edgecolor ='black')


#plt.xlabel("X-Axis")
#plt.ylabel("Y-Axis")


#plt.tight_layout()

#real world example:

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
plt.style.use('fivethirtyeight')

data = pd.read_csv('D:\\1.csv')
print(type(data))