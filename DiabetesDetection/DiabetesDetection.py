{
"cells": [
{
"cell_type": "markdown",
"metadata": {},
"source": [
"# DIABETES PREDICTION"
]
},
{
"cell_type": "code",
"execution_count": 2,
"metadata": {},
"outputs": [],
"source": [
"import numpy as np\n",
"import pandas as pd"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## IMPORTING DATASET"
]
},
{
"cell_type": "code",
"execution_count": 3,
"metadata": {},
"outputs": [
{
"data": {
"text/html": [
"<div>\n",
"<style scoped>\n",
"    .dataframe tbody tr th:only-of-type {\n",
"        vertical-align: middle;\n",
"    }\n",
"\n",
"    .dataframe tbody tr th {\n",
"        vertical-align: top;\n",
"    }\n",
"\n",
"    .dataframe thead th {\n",
"        text-align: right;\n",
"    }\n",
"</style>\n",
"<table border=\"1\" class=\"dataframe\">\n",
"  <thead>\n",
"    <tr style=\"text-align: right;\">\n",
"      <th></th>\n",
"      <th>Pregnancies</th>\n",
"      <th>Glucose</th>\n",
"      <th>BloodPressure</th>\n",
"      <th>SkinThickness</th>\n",
"      <th>Insulin</th>\n",
"      <th>BMI</th>\n",
"      <th>DiabetesPedigreeFunction</th>\n",
"      <th>Age</th>\n",
"      <th>Outcome</th>\n",
"    </tr>\n",
"  </thead>\n",
"  <tbody>\n",
"    <tr>\n",
"      <th>0</th>\n",
"      <td>6</td>\n",
"      <td>148</td>\n",
"      <td>72</td>\n",
"      <td>35</td>\n",
"      <td>0</td>\n",
"      <td>33.6</td>\n",
"      <td>0.627</td>\n",
"      <td>50</td>\n",
"      <td>1</td>\n",
"    </tr>\n",
"    <tr>\n",
"      <th>1</th>\n",
"      <td>1</td>\n",
"      <td>85</td>\n",
"      <td>66</td>\n",
"      <td>29</td>\n",
"      <td>0</td>\n",
"      <td>26.6</td>\n",
"      <td>0.351</td>\n",
"      <td>31</td>\n",
"      <td>0</td>\n",
"    </tr>\n",
"    <tr>\n",
"      <th>2</th>\n",
"      <td>8</td>\n",
"      <td>183</td>\n",
"      <td>64</td>\n",
"      <td>0</td>\n",
"      <td>0</td>\n",
"      <td>23.3</td>\n",
"      <td>0.672</td>\n",
"      <td>32</td>\n",
"      <td>1</td>\n",
"    </tr>\n",
"    <tr>\n",
"      <th>3</th>\n",
"      <td>1</td>\n",
"      <td>89</td>\n",
"      <td>66</td>\n",
"      <td>23</td>\n",
"      <td>94</td>\n",
"      <td>28.1</td>\n",
"      <td>0.167</td>\n",
"      <td>21</td>\n",
"      <td>0</td>\n",
"    </tr>\n",
"    <tr>\n",
"      <th>4</th>\n",
"      <td>0</td>\n",
"      <td>137</td>\n",
"      <td>40</td>\n",
"      <td>35</td>\n",
"      <td>168</td>\n",
"      <td>43.1</td>\n",
"      <td>2.288</td>\n",
"      <td>33</td>\n",
"      <td>1</td>\n",
"    </tr>\n",
"    <tr>\n",
"      <th>5</th>\n",
"      <td>5</td>\n",
"      <td>116</td>\n",
"      <td>74</td>\n",
"      <td>0</td>\n",
"      <td>0</td>\n",
"      <td>25.6</td>\n",
"      <td>0.201</td>\n",
"      <td>30</td>\n",
"      <td>0</td>\n",
"    </tr>\n",
"    <tr>\n",
"      <th>6</th>\n",
"      <td>3</td>\n",
"      <td>78</td>\n",
"      <td>50</td>\n",
"      <td>32</td>\n",
"      <td>88</td>\n",
"      <td>31.0</td>\n",
"      <td>0.248</td>\n",
"      <td>26</td>\n",
"      <td>1</td>\n",
"    </tr>\n",
"    <tr>\n",
"      <th>7</th>\n",
"      <td>10</td>\n",
"      <td>115</td>\n",
"      <td>0</td>\n",
"      <td>0</td>\n",
"      <td>0</td>\n",
"      <td>35.3</td>\n",
"      <td>0.134</td>\n",
"      <td>29</td>\n",
"      <td>0</td>\n",
"    </tr>\n",
"    <tr>\n",
"      <th>8</th>\n",
"      <td>2</td>\n",
"      <td>197</td>\n",
"      <td>70</td>\n",
"      <td>45</td>\n",
"      <td>543</td>\n",
"      <td>30.5</td>\n",
"      <td>0.158</td>\n",
"      <td>53</td>\n",
"      <td>1</td>\n",
"    </tr>\n",
"    <tr>\n",
"      <th>9</th>\n",
"      <td>8</td>\n",
"      <td>125</td>\n",
"      <td>96</td>\n",
"      <td>0</td>\n",
"      <td>0</td>\n",
"      <td>0.0</td>\n",
"      <td>0.232</td>\n",
"      <td>54</td>\n",
"      <td>1</td>\n",
"    </tr>\n",
"  </tbody>\n",
"</table>\n",
"</div>"
],
"text/plain": [
"   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
"0            6      148             72             35        0  33.6   \n",
"1            1       85             66             29        0  26.6   \n",
"2            8      183             64              0        0  23.3   \n",
"3            1       89             66             23       94  28.1   \n",
"4            0      137             40             35      168  43.1   \n",
"5            5      116             74              0        0  25.6   \n",
"6            3       78             50             32       88  31.0   \n",
"7           10      115              0              0        0  35.3   \n",
"8            2      197             70             45      543  30.5   \n",
"9            8      125             96              0        0   0.0   \n",
"\n",
"   DiabetesPedigreeFunction  Age  Outcome  \n",
"0                     0.627   50        1  \n",
"1                     0.351   31        0  \n",
"2                     0.672   32        1  \n",
"3                     0.167   21        0  \n",
"4                     2.288   33        1  \n",
"5                     0.201   30        0  \n",
"6                     0.248   26        1  \n",
"7                     0.134   29        0  \n",
"8                     0.158   53        1  \n",
"9                     0.232   54        1  "
]
},
"execution_count": 3,
"metadata": {},
"output_type": "execute_result"
}
],
"source": [
"dataset = pd.read_csv(\"diabetes.csv\")\n",
"dataset.head(10)"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## analyzing dataset "
]
},
{
"cell_type": "code",
"execution_count": 4,
"metadata": {},
"outputs": [
{
"name": "stdout",
"output_type": "stream",
"text": [
"<class 'pandas.core.frame.DataFrame'>\n",
"RangeIndex: 768 entries, 0 to 767\n",
"Data columns (total 9 columns):\n",
"Pregnancies                 768 non-null int64\n",
"Glucose                     768 non-null int64\n",
"BloodPressure               768 non-null int64\n",
"SkinThickness               768 non-null int64\n",
"Insulin                     768 non-null int64\n",
"BMI                         768 non-null float64\n",
"DiabetesPedigreeFunction    768 non-null float64\n",
"Age                         768 non-null int64\n",
"Outcome                     768 non-null int64\n",
"dtypes: float64(2), int64(7)\n",
"memory usage: 54.1 KB\n"
]
}
],
"source": [
"dataset.info()"
]
},
{
"cell_type": "code",
"execution_count": 5,
"metadata": {},
"outputs": [
{
"data": {
"text/plain": [
"Pregnancies                 0\n",
"Glucose                     0\n",
"BloodPressure               0\n",
"SkinThickness               0\n",
"Insulin                     0\n",
"BMI                         0\n",
"DiabetesPedigreeFunction    0\n",
"Age                         0\n",
"Outcome                     0\n",
"dtype: int64"
]
},
"execution_count": 5,
"metadata": {},
"output_type": "execute_result"
}
],
"source": [
"dataset.isnull().sum()"
]
},
{
"cell_type": "code",
"execution_count": 6,
"metadata": {},
"outputs": [],
"source": [
"X = dataset.iloc[:,:-1]\n",
"y = dataset.iloc[:,-1]"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## splitting data"
]
},
{
"cell_type": "code",
"execution_count": 7,
"metadata": {},
"outputs": [],
"source": [
"from sklearn.model_selection import train_test_split\n",
"X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 25,random_state = 0)"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## applying classifiers AND evaluation\n",
"### RANDOM FOREST "
]
},
{
"cell_type": "code",
"execution_count": 8,
"metadata": {},
"outputs": [],
"source": [
"from sklearn.ensemble import RandomForestClassifier\n",
"classifier = RandomForestClassifier(n_estimators = 6, criterion = 'entropy', random_state = 0)\n",
"classifier.fit(X_train, y_train)\n",
"\n",
"y_pred = classifier.predict(X_test)"
]
},
{
"cell_type": "code",
"execution_count": 9,
"metadata": {},
"outputs": [
{
"name": "stdout",
"output_type": "stream",
"text": [
"Accuracy :  88.0\n"
]
}
],
"source": [
"from sklearn.metrics import accuracy_score\n",
"acc_logreg2 = round(accuracy_score(y_pred, y_test) , 2)*100\n",
"print(\"Accuracy : \",acc_logreg2)"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"### LOGISTIC REGRESSION"
]
},
{
"cell_type": "code",
"execution_count": 10,
"metadata": {},
"outputs": [
{
"name": "stdout",
"output_type": "stream",
"text": [
"Accuracy :  96.0\n"
]
}
],
"source": [
"from sklearn.linear_model import LogisticRegression\n",
"from sklearn.metrics import accuracy_score,r2_score,classification_report\n",
"logreg = LogisticRegression(solver='lbfgs',max_iter=1000)\n",
"logreg.fit(X_train, y_train)\n",
"y_pred = logreg.predict(X_test)\n",
"acc_logreg1 = round(accuracy_score(y_pred, y_test) , 2)*100\n",
"print(\"Accuracy : \",acc_logreg1)"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"### K NEIGHBOR CLASSIFIER "
]
},
{
"cell_type": "code",
"execution_count": 11,
"metadata": {},
"outputs": [
{
"name": "stdout",
"output_type": "stream",
"text": [
"Accuracy : 84.0\n"
]
}
],
"source": [
"from sklearn.neighbors import KNeighborsClassifier\n",
"\n",
"knn = KNeighborsClassifier(n_neighbors=7)\n",
"knn.fit(X_train, y_train)\n",
"y_pred = knn.predict(X_test)\n",
"acc_knn = round(accuracy_score(y_pred,y_test), 2) * 100\n",
"print(\"Accuracy :\" ,acc_knn)"
]
},
{
"cell_type": "code",
"execution_count": null,
"metadata": {},
"outputs": [],
"source": []
}
],
"metadata": {
"kernelspec": {
"display_name": "Python 3",
"language": "python",
"name": "python3"
},
"language_info": {
"codemirror_mode": {
"name": "ipython",
"version": 3
},
"file_extension": ".py",
"mimetype": "text/x-python",
"name": "python",
"nbconvert_exporter": "python",
"pygments_lexer": "ipython3",
"version": "3.7.3"
}
},
"nbformat": 4,
"nbformat_minor": 2
}