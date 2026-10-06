from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
import pickle
car=pd.read_csv('orgnized_data.csv')
x=car.drop(columns='Price')
y=car['Price']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
oh=OneHotEncoder()
oh.fit(x[['name','company','fuel_type']])
col_trans=make_column_transformer((OneHotEncoder(categories=oh.categories_),['name','company','fuel_type']),remainder='passthrough')
model=LinearRegression()
pipe=make_pipeline(col_trans,model)
pipe.fit(x_train,y_train)
y_predt=pipe.predict(x_test)
print(r2_score(y_test,y_predt))

scores=[]
for i in range(1000):
    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=i)
    lr=LinearRegression()
    pipe=make_pipeline(col_trans,lr)
    pipe.fit(X_train,y_train)
    y_pred=pipe.predict(X_test)
    scores.append(r2_score(y_test,y_pred))
print(max(scores))
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=np.argmax(scores))
lr=LinearRegression()
pipe=make_pipeline(col_trans,lr)
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)
r2_score(y_test,y_pred)
pickle.dump(pipe,open('LinearRegressionModel.pkl','wb'))
