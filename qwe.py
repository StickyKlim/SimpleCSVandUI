import pandas as pd
import matplotlib.pyplot as plt
Market = {'Year': [2011, 2011, 2012, 2013, 20010, 2014, 2015,2010, 2011, 2012, 2013, 2018, 2014, 2015,2010, 2011, 2012, 2013, 2019, 2014],
                'Month': [2,3,4,4,5,6,4,3,4,2,3,6, 4,12,10,5,7,2,9,1],
                'Rating': [6,8,10,2,4,6,7,2,2,6,7,8,1,7,10,9,2,1,6,8],
                'Price':[12,3,4,56,23,14,26,39,23,11,2,6,3,87,23,56,78,25,10,12]}
df=pd.DataFrame(Market,columns=['Year', 'Month', 'Rating', 'Price'])
plt.scatter(df['Price'], df['Rating'], color='red')
plt.title('Название графика', fontsize=10)
plt.xlabel('Rating',fontsize=10)
plt.ylabel('Year', fontsize = 10)
plt.grid(True)
plt.show()