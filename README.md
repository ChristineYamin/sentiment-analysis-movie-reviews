# Sentiment Analysis of Movie Review
This project builds an end-to-end Natural Language Processing (NLP) pipeline to classify movie reviews as **positive** or **negative**.

## Goal 
At the end of the project, we will predict the review whether it is positive or negative in the streamlit app.

##  Data Set
- IMDb Dataset of 50K Movie Reviews (Kaggle)
- Columns:
  - `review`: raw movie review text
  - `sentiment`: positive or negative label

## Workflow
    1. Create the environment for the project
    2. Download and load the raw data
    3. Clean the raw text (Remove HTML tags, Lower case, Punctuation, stopwords)
    4. Convert text to numbers ( TF-IDF)
    5. Splitting train and test data set
    6. Train model ( Logistic Regression )
    7. Evaluate the model accuracy ( Accuracy = 0.885 )
    8. Save the model
    9. Post-Model Exploratory data analysis (review length, sentiment distribution, class balance)
    10. In app.py, use streamlit


## Post-Model Exploratory Analysis
Exploratory analysis was performed to better understand review characteristics after model training.
This includes:
- Review length distribution
- Sentiment class balance
- Comparison of review length by sentiment
Note: This exploratory analysis was conducted to understand the dataset characteristics and does not influence model training.


## Library Used
- Python
- Pandas, NumPy
- Scikit-learn
- NLTK
- Streamlit

## Result
The trained model achieves 88.85 percentage on the test set.

## Live Demo ( Streamlit app)
https://sentiment-analysis-movie-reviews-swna7sktweepojrv6xm6uy.streamlit.app/
