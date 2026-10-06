'''DATA WE HAVE TO TRAIN IS NOT IDEAL IT HAS TO BE FILTERED AND PROCESSES BY PANDAS TO
GET THE IDEAL DATA FOR OUR MODEL'''
import pandas as pd
car=pd.read_csv('quikr_car.csv')
print(car.info())
'''
PROBLEMS IN DATA 

1) ALL THE COLOUMS ARE IN STR SO WE NEED TO CANVERT THEM IN INT IF POSSIBLE
2) values in year in not good it has non int values in it so it needs to be cleaned
3) price has string "ask for price" in it as values
4) kms_driven has "kms" in valus as string which is not sutable
5) kms also have nan valus
6) fuel type has nan value
7) name od car is so long to process 

'''  
backup=car.copy() #for safety

# clean year coloum
car=car[car['year'].str.isnumeric()]
car['year']=car['year'].astype(int)
'''so now it year has only int values and we canverted its typle to int also'''
## clean the price
'''it has either int values or a string "ask for price
   so we will delete this string data a
   and also delete commas
'''
car=car[car['Price']!="Ask For Price"]
car['Price']=car['Price'].str.replace(',','').astype(int)
## clean km driven

car['kms_driven']=car['kms_driven'].str.split(' ').str.get(0).str.replace(',','')
car=car[car['kms_driven'].str.isnumeric()]
car['kms_driven']=car['kms_driven'].astype(int)
print(car.info())

## clean fuel typle
car=car[~car['fuel_type'].isna()]

## clean name( trim to 3 world)
car['name']=car['name'].str.split(' ').str.slice(0,3).str.join(' ')
## indexes correct

car.reset_index(drop=True)
car=car[car['Price']<6e6].reset_index(drop=True)
print(car)

car.to_csv('orgnized_data.csv', index=False)