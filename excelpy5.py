import pandas as pd

df=pd.read_csv('Online-retail.csv')
df.head()

print(df)
df['LinePrice']=df['Quantity'] * df['UnitPrice']
df.head()

print(df)

df_customers = df.groupby('CustomerID').agg(
    orders=('invoiceNo','nunique'),
    skus=('StockCode' , 'nunique'),
    quantity=('Quantity' ,'sum'),
    revenue=('LinePrice' , 'sum'),
).reset_index()
    
df_customers.head()
    
print(df_customers)