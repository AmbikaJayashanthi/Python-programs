import pandas as pd
df=pd.read_excel("mark.xlsx")
df['MARK']=df['MARK']+10
print(df)
df.to_excel(excel_writer= "res.xlsx",index=False)