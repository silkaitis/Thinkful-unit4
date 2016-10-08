# Thinkful Unit 4 Exercises

**Purpose**

Explore and learn various tools available in Pandas, Sklearn, Statsmodels and Scipy

**Exercise Descriptions**

1. RandomForest_limited.ipynb
  * Purpose
    * Predict movement type from a limited feature set of accelerometer and gyroscopic data
    * Identify the top 10 features of a Random Forest Classifier
  * Learning Objectives
    * Use RandomForestClassifier from Sklearn
  * Output
```
    The Random Forest Classifier model accuracy score is 0.914 using 66 features
    The Random Forest Classifier model precision score is 0.916 using 66 features
    The Random Forest Classifier model recall score is 0.914 using 66 features

    Top Ten Features in the Model

    1. tGravityAcc_Mean_X (0.130)
    2. tGravityAcc_Mean_Y (0.065)
    3. fAccJerk_kurtosis_Z (0.040)
    4. tAcc_Mean_Z (0.039)
    5. fAcc_STD_Z (0.039)
    6. fAcc_Mean_Z (0.034)
    7. fAcc_kurtosis_Z (0.029)
    8. fAccJerk_STD_Z (0.027)
    9. tAcc_STD_Z (0.027)
    10. tAccJerk_STD_Z (0.027)
```
![text](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Feature_Importance.png?raw=true)

2. RandomForest.ipynb
  * Purpose
    * Predict movement type from all features of accelerometer and gyroscopic data
    * Identify the top 10 features of a Random Forest Classifier
  * Learning Objectives
    * Use RandomForestClassifier from Sklearn
  * Output
```
    The Random Forest Classifier model accuracy score is 0.925 using 561 features
    The Random Forest Classifier model precision score is 0.926 using 561 features
    The Random Forest Classifier model recall score is 0.925 using 561 features

    Top Ten Features in the Model

    1. tGravityAcc_energy_X (0.031)
    2. tGravityAcc_min_X (0.030)
    3. tGravityAcc_Mean_X (0.030)
    4. angle_X_gravityMean (0.029)
    5. tGravityAcc_min_Y (0.026)
    6. angle_Y_gravityMean (0.025)
    7. tGravityAcc_Mean_Y (0.024)
    8. tGravityAcc_max_Y (0.024)
    9. tGravityAcc_max_X (0.022)
    10. tGravityAcc_energy_Y (0.017)
```
![img](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Feature_Importance_Full.png?raw=true)

3. kNN.ipynb
  * Purpose
    * Classify flower type using feature lengths
  * Learning Objectives
    * Implement a Nearest Neighbor function
  * Output
  ![img](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/kNN_sepal_wid_vs_len.png?raw=true)
  ```
      Iteration 0
    Majority class is Iris-virginica
    Data point 130 was selected
    Data point class is Iris-virginica

    Iteration 1
    Majority class is Iris-virginica
    Data point 118 was selected
    Data point class is Iris-virginica

    Iteration 2
    Majority class is Iris-setosa
    Data point 38 was selected
    Data point class is Iris-setosa

    Iteration 3
    Majority class is Iris-versicolor
    Data point 77 was selected
    Data point class is Iris-versicolor

    Iteration 4
    Majority class is Iris-virginica
    Data point 54 was selected
    Data point class is Iris-versicolor

    Iteration 5
    Majority class is Iris-setosa
    Data point 33 was selected
    Data point class is Iris-setosa

    Iteration 6
    Majority class is Iris-setosa
    Data point 106 was selected
    Data point class is Iris-virginica

    Iteration 7
    Majority class is Iris-setosa
    Data point 6 was selected
    Data point class is Iris-setosa

    Iteration 8
    Majority class is Iris-virginica
    Data point 105 was selected
    Data point class is Iris-virginica

    Iteration 9
    Majority class is Iris-setosa
    Data point 31 was selected
    Data point class is Iris-setosa
  ```

4. kMeans.ipynb
  * Purpose
    * Cluster individuals based on age, infant mortality and GDP
  * Learning Objectives
    * Implement kMeans from SciPy
  * Output

    ![i1](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/GDPperCapita.png?raw=true)

    ![i2](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Average%20within-cluster%20sum%20of%20squares.png?raw=true)

5. cross_validation.ipynb
  * Purpose
    * Cross validate a linear regression model of loan data
  * Learning Objectives
    * Apply KFold from Sklearn to loan data
  * Output
    ```
    Average mean squared error for entire cross validation : 17.51

    Average mean absolute error for entire cross validation : 3.38

    Average R squared for entire cross validation : -0.00
    ```
6. LDA_iris.ipynb
  * Purpose
    * Inspect the data transformation of a Linear Discriminant Analysis
    * Visual comparison of kMean and Linear Discriminant Analysis
  * Learning Objectives
    * Implement a Linear Discriminant Analysis from Sklearn
  * Output

    ![img](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Iris%20dataset%20-%20raw.png?raw=true)

    ![img](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Iris%20dataset%20-%20LDA.png?raw=true)

    ![img](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Iris%20dataset%20-%20LDA%20kMeans.png?raw=true)

7. PCA_iris.ipynb
  * Purpose
    * Visual comparison of kNN and Principal Component Analysis (PCA) classification of iris data
  * Learning Objectives
    * Implement PCA from Sklearn
  * Output

  ![graph](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Iris%20dataset%20-%20PCA.png?raw=true)

    ![graph](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Iris%20dataset%20-%20kNN.png?raw=true)

8. SVM_iris.ipynb
  * Purpose
    * Classify flower type using feature lengths
  * Learning Objectives
    * Implement Support Vector Machine from Sklearn
  * Output
    ![graph](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Iris%20-%20SVM.png?raw=true)

9. NaiveBayes.ipynb
  * Purpose
    * Predict gender from actual and ideal weight
  * Learning Objectives
    * Use Gaussian Navie Bayes from Sklearn
  * Output
  ![graph](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Acutal%20&%20Ideal%20Weight.png?raw=true)

    ![graph](https://github.com/silkaitis/Thinkful-unit4/blob/master/images/Difference%20in%20Actual%20&%20Ideal%20Weight.png?raw=true)

    ```
    An individual with an actual weight of 145, an ideal weight of 160 and weight different of -15 is most likely Male

    An individual with an actual weight of 160, an ideal weight of 145 and weight different of 15 is most likely Female
    ```
