from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 
 
import pandas as pd
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
print (df.head(10))
print (df.describe(include='all'))
df.plot.scatter(x='sepal length (cm)', y='sepal width (cm)', c='target', colormap='viridis')
import matplotlib.pyplot as plt
plt.show()
df. plot(x='sepal length (cm)', y='sepal width (cm)', c='target', colormap='viridis', kind='scatter')
kind='line')
plt.show()
df.plot(x='column_x(cm)', y='column_y (cm)', c='target', colormap='viridis', kind='bar')
