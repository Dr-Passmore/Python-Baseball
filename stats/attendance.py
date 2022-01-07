import pandas as pd
import matplotlib.pyplot as plt
from data import games

attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'),{'year', 'multi3'}]
#print(attendance)
attendance.columns = ['year', 'attendance']

attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')
plt.xlabel('Year')
plt.ylabel('attendance')

plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')
#print(attendance)
plt.show()