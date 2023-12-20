import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = 'ou_01_6.xlsx'
df = pd.read_excel(excel_file_path)
print(df)

# Assuming your DataFrame has columns 'x' and 'y'
plt.scatter( df['#CONF:'], df['#SUP:'],alpha=0.2)
plt.xlabel('X-axis #CONF Label')
plt.ylabel('Y-axis  #SUP Label')
plt.title('Sup and Conf relation')
plt.show()
