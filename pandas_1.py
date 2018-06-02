import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s=pd.Series([1,3,4,np.nan,6,8])
print(s)
dates=pd.date_range('20130101', periods=6)
print(dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)
df2 = pd.DataFrame({ 'A' : 1.,
	'B' : pd.Timestamp('20130102'),
	'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
	'D' : np.array([3] * 4,dtype='int32'),
	'E' : pd.Categorical(["test","train","test","train"]),
	'F' : 'foo' })
print(df2)
print("head")
print(df.head(2));
print(df.tail(3));
print(df.index);
print(df.columns);
print(df.values);
print(df.describe());
print(df.T);
df.sort_index(axis=1,ascending=False);
print(df.sort_values(by='B'));
print(df['A']);
print(df[0:3]);
print(df['20130102':'20130104']);
print(df.loc[dates[0]])
#print(df.loc['A'])  
print(df.loc[dates[0]].loc['A']);
print(df.loc[dates[0],['A','B']]);
print(df.iloc[3:5,1:4])
print(df.iloc[1,1])
print(df.iat[1,1])
print(df[df>0]);
df2=df.copy();
print(df2);
df2['E']=['one', 'one','two','three','four','three'];
print(df2[df2['E'].isin(['two','four'])])
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print(df1)
df1.loc[dates[0]:dates[1],'E'] = 1
print(df1)
print(df1.dropna(how='any'))
print(df1.fillna(value=5))
print(pd.isna(df1))
print(df.mean())
print(df.mean(1))
s1=pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
print(df.sub(s1,axis='index'))
df.apply(np.cumsum);
df.apply(lambda x:x.max()-x.min())
s2=pd.Series(np.random.randint(0,7,size=10))
print(s2.value_counts())
s3=pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat']);
print(s3.str.lower());
df3=pd.DataFrame(np.random.randn(10,4));
pieces = [df3[:3], df3[3:7], df3[7:]]
print(pd.concat(pieces))
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]});
print(left);
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key')
df4=pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
ts=ts.cumsum()
plt.figure();
ts.plot();
plt.show()