#import the libraries pandas, numpy and matplotlib
# if you still don´t have them in your VSCode then got o terminal and pip3 install (librery)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# here I´m making the variables for the files I have in my computer folder. Excel file 1 there are two sheets, with shift 1 and 2, the other excel there is the shift 3:
excel_file_1 = "shift-data.xlsx"
excel_file_2 = "third-shift-data.xlsx"

#here i´m passing the comands to read the files I want to, which I explained in the comments above. 
df_first_shift = pd.read_excel(excel_file_1, sheet_name="first")
df_second_shift = pd.read_excel(excel_file_1, sheet_name="second")
df_third_shift = pd.read_excel(excel_file_2)

#here is just to check:
print(df_first_shift)
#here is just to print a specific column:
print(df_first_shift["Product"])

#here is to put all the files and sheets into a single excel file:
df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])
print(df_all)

#here i´m making the group for the each shift and calculating the mean
pivot = df_all.groupby(["Shift"]).mean()
#here i´m getting the 3 shifts and having the mean for the colums to check the results, i specificated the columns i want to have the resuls to compare. the : in the beginning is to say I want all the rows. 
shift_productivity = pivot.loc[:,"Production Run Time (Min)": "Products Produced (Units)"]

print(shift_productivity)

#this below is to have the graphic:
#shift_productivity.plot(kind="bar")
#plt.show()

#This below is to save the new excel file:
#df_all.to_excel("output.xlsx")


