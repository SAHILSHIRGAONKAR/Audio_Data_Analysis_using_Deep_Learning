"""

The following code classifies piece of music as one of 
the four emotions mentioned in the document
performs k-NN classification for different numbers of neighbors,
calculates and stores accuracy scores,
and then creates a plot to visualize the results.
The accuracy scores are used to evaluate the model's performance with varying k values.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


data = pd.read_csv('Data/Emotion_features.csv')
feature = data.loc[:, 'tempo':] #Extract the columns from 'tempo' to the end of the DataFrame as the feature data
featureName = list(feature)
color = ['red' if l==1 else 'green' if l==2 else 'blue' if l==3 else 'orange' for l in data['label']]

for name in featureName:
    feature[name] = (feature[name]-feature[name].min())/(feature[name].max()-feature[name].min())

plt.style.use('ggplot')

array = np.array(data)

features = feature.values
labels = data.loc[:, 'class'].dropna()
test_size = 0.20 #The size of the testing set is set to 20% of the entire dataset,
                 # and a random seed is used for reproducibility.
random_seed = 2

train_d, test_d, train_l, test_l = train_test_split(features, labels, test_size=test_size, random_state=random_seed)

result = []
xlabel = [i for i in range(1, 11)]
for neighbors in range(1, 11):
    kNN = KNeighborsClassifier(n_neighbors=neighbors)
    kNN.fit(train_d, train_l)
    prediction = kNN.predict(test_d)
    result.append(accuracy_score(prediction, test_l)*100)

plt.figure(figsize=(10, 10))
plt.xlabel('kNN Neighbors for k=1,2...20')
plt.ylabel('Accuracy Score')
plt.title('kNN Classifier Results')
plt.ylim(0, 100)
plt.xlim(0, xlabel[len(xlabel)-1]+1)
plt.plot(xlabel, result)
plt.savefig('1-fold 10NN Result.png')
plt.show()