import pandas as pd
import pyarrow as pa


df=pd.DataFrame({
    'name':pd.Series(dtype='str'),
    'empno':pd.Series(dtype='int'),
    'sal':pd.Series(dtype='float'),
    'dob':pd.Series(dtype='datetime64[ns]')
    })

print(df.dtypes)

df.to_parquet('Documents/schematest.parquet')
