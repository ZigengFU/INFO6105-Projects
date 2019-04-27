# NEU INFO6105 Spring2019 Team6 Projects
This repository contains the total 5 projects of Team6 in this semester, including 4 assignments and 1 final project. Please view the summary below and look through the details in sub-folders.

## Team Members
Zigeng Fu, Hao Cui, Yimu Jin, Ziyan Zhu

## Assignment1: Fintech Hiring Trends Analysis (Part 1)
### Summary
We analyzed 4 fintech reports of World Economic Forum (WEF), and totally 3,584 posted jobs on the careers site of 2 of the top U.S. banks, which are BNY Mellon and Capital One, and then figured out the insight on:
- Key fintech areas
- Job demands distributions
- Key fintech hiring trends
- Core competitiveness in fintech

### Tools and Methods
- Web scraping: Beautiful Soup
- Text extraction: pdfminer
- Keywords extraction: Word Count, TF-IDF, TextRank

### Links
- Online Report: https://codelabs-preview.appspot.com/?file_id=1-Tb8qcxYM2QH2U6BrbRFy_HdPpH1WVHb7nkiC8gkwTc#0


## Assignment2: Fintech Hiring Trends Analysis (Part 2)
### Summary
This project continue to analyze fintech hiring trends in banking industry with data from top 24 U.S. banks to come out scientific findings and predictions. The insight we gained on included:
- Fintech job contribution in 24 banks
- Fintech related job hiring trends
- Number and proportion of fintech related jobs in each of 24 banks
- Fitech categories with most jobs and least jobs
- Recommendations for job seekers in fintech area

### Tools and Methods
- Exploratory Data Analysis (EDA)
- Feature Engineering: clustering
- Docker
- Pipelining: Luigi, Airflow, Dask

### Links
- Online Report: https://codelabs-preview.appspot.com/?file_id=1mI2ATyKHXyLkZwq-8-KVx3s24uA8C9gKtrzXx98cZUk#0
- Video Presentation: https://www.youtube.com/watch?v=dpe_9bZGBM4


## Assignment3: Lending Club Loan Interest Rate Prediction
### Summary
Lending Club is a peer to peer lending company based in the United States, in which investors provide funds for potential borrowers and investors earn a profit depending on the risk they take (the borrowers credit score).
And arbitragers are people on Lending Club platform who can take advantage of their credit, borrow money at low interest rate, and then lend it out at high interest rate to make profit.
In this project, we decided to build machine learning models and select one with best performances to predict loan interst rate for arbitragers.

### Tools and Methods
- Machine Learning Models: NN, LR
- Manual vs Automated Feature Engineering
- AutoML: H2O, TPOT, Auto-SKLearn

### Links
- Online Report: https://codelabs-preview.appspot.com/?file_id=1mwss-8xq9ji4nPS8sN9bZD1rjvXWkbm59-eMQyppT7w#0
- Video Presentation: https://www.youtube.com/watch?v=39uDsF4bOiY&t=0s


## Assignment4: Music Mood Classification (Happy/Sad)
### Summary
In this project, we designed and developed a Chinese music mood classification App. Using this App, people can input Chinese lyrics and then predict the mood of the song (which is happy or sad) and the probability of the prediction.

### Tools and Methods
- Segment Analysis: Text Classification
- Neural Network: MLP
- Google Translate Api
- Web App DevOps: FLASK framework, heroku platform

### Links
- Online Report: https://codelabs-preview.appspot.com/?file_id=1UQlHwWT_0uEmYVj_D7ulWvFiVdK0-y1GbDgq1oufzsM#0
- Web App Demo: https://flask-info6105-music-app.herokuapp.com/
- Video Presentation: https://www.youtube.com/watch?v=oMeLmwlSaxA&t=0s


## Final Project: LoL Game Result Prediction
### Summary
In this project, our goal is to predict the LoL game result and its probability between two selected teams. We firstly scraped team and player data from a Chinese game platform (https://www.wanplus.com/lol/)  and did the data processing and feature engineering. Then, we built a prediction model using 3 machine learning models: Random Forest, Linear Regression, and MLP (Multi-Layer Perceptron). Evaluation criteria of the models was Confusion Matrix. We also developed a web application and deploy it on cloud for users.

### Tools and Methods
- Web scraping: Beautiful Soup
- Data processing and EDA
- Model building: Neural Network (MLP)
- Model evaluation: Confusion Matrix
- Hyper-parameter tuning
- Model comparison and selection
- Web App DevOps: FLASK framework, heroku platform

### Links
1. Project proposal:
https://codelabs-preview.appspot.com/?file_id=10prnfsaBoCaZXKREt6pIizqJujCCcLkeOaHM0BdjBGw#0
2. Project report:
https://codelabs-preview.appspot.com/?file_id=1t-AAXeMMHuEWYM5cMhXco-RmhpMWnF2Hmcx2U3FQftA#0
3. Online Web App:
https://flask-info6105-lol-predict-app.herokuapp.com/
4. Presentation slides:
https://docs.google.com/presentation/d/1HjdWhQDDwOfTSJ2D7eJt6Nur3FaEk4ChYVUsSlMpiXQ/edit?usp=sharing
