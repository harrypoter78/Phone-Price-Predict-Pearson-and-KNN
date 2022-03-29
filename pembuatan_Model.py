import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

data = pd.read_csv("train.csv")

print(data.head())
print('Dataset Asal', data.shape)
# print(data.dtypes)

#PROSES PEARSON
pearson = data.corr(method='pearson')
fig = plt.subplots(figsize=(12, 12))
sns.heatmap(pearson, square=True, cbar=True, annot=True, cmap="GnBu", annot_kws={'size': 5})
plt.title('Pearson Correlations between Attributes')


#Seleksi fitur
seleksifitur = (['clock_speed', 'mobile_wt', 'touch_screen'])
data=data.drop(seleksifitur, axis=1)
print('Dataset Hasil Seleksi Fitur', data.shape)
print(data.head(3))


#Menghapus label price range
y = data['price_range']
x = data.drop('price_range', axis=1)


#Memisahkan dataset menjadi train & test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101, stratify=y)
print('Dataset x_train', x_train.shape)
print('Dataset x_test', x_test.shape)
# print(data.columns)


#PROSES KNN
#Menentukan nilai tetangga terbaik
parameters = {'n_neighbors':np.arange(1,30)}
knn = KNeighborsClassifier()
model = GridSearchCV(knn, parameters, cv=5)
model.fit(x_train, y_train)
print(model.best_params_)


#Pembuatan model dengan K=9
model_knn = KNeighborsClassifier(n_neighbors=9)
model_knn.fit(x_train, y_train)


#Prediksi akurasi KNN
y_pred_knn = model_knn.predict(x_test)
acc_knn = accuracy_score(y_test, y_pred_knn)
print('Akurasi : ', acc_knn)

model_save = model_knn
filename = 'phoneModel.pkl'
pickle.dump(model_save, open(filename, 'wb'))


print('')
print('Proses Prediksi Harga Handphone')
#Prediksi Data Testing
test_data = pd.read_csv("test.csv")
print(test_data.head())
test_data=test_data.drop('id', axis=1)
test_data=test_data.drop(seleksifitur, axis=1)
print(test_data.head())
model_load = pickle.load(open(filename, 'rb'))
predicted_price_range = model_load.predict(test_data)
print('Hasil Prediksi')
print(predicted_price_range)
test_data['price_range'] = predicted_price_range
print(test_data.head())

plt.show()

