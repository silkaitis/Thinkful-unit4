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
![text](https://github.com/silkaitis/Thinkful-unit4/blob/master/Feature_Importance.png?raw=true)

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
![img](https://github.com/silkaitis/Thinkful-unit4/blob/master/Feature_Importance_Full.png?raw=true)
