# LoL (League of Legends) Game Result Prediction
This is the final project of INFO6105 Data Science Tools and Methods in Spring 2019 semester at Northeastern University.

## Contributers
Zigeng Fu, Hao Cui, Yimu Jin, Ziyan Zhu

## Project Overview
In this project, our goal is to predict the LoL game result and its probability between two selected teams. We firstly scraped team and player data from a Chinese game platform (https://www.wanplus.com/lol/)  and did the data processing and feature engineering. Then, we built a prediction model using 3 machine learning models: Random Forest, Linear Regression, and MLP (Multi-Layer Perceptron). Evaluation criteria of the models was Confusion Matrix. We also developed a web application and deploy it on cloud for users.

## How to launch the prediction App 
You can either run the application online or clone the project and launch it on your machine.
1. Online App: https://flask-info6105-lol-predict-app.herokuapp.com/
2. Launch on local machine:
- Clone the project to local space;
- Open /codes folder in your IDE (pycharm recommended);
- Configure the python packages required in 'LoL.py';
- Run 'LoL.py'.

## Links
1. Project proposal:
https://codelabs-preview.appspot.com/?file_id=10prnfsaBoCaZXKREt6pIizqJujCCcLkeOaHM0BdjBGw#0
2. Project report:
https://codelabs-preview.appspot.com/?file_id=1t-AAXeMMHuEWYM5cMhXco-RmhpMWnF2Hmcx2U3FQftA#0
3. Online Web App:
https://flask-info6105-lol-predict-app.herokuapp.com/
4. Presentation slides:
https://docs.google.com/presentation/d/1HjdWhQDDwOfTSJ2D7eJt6Nur3FaEk4ChYVUsSlMpiXQ/edit?usp=sharing
