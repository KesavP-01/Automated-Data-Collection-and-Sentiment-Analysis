

# Opinion Mining

## Overview

This repository contains an end-to-end pipeline for opinion mining using Natural Language Processing (NLP) techniques. The project involves scraping movie reviews, pre-processing text data, training machine learning models, and performing sentiment analysis. The goal is to extract opinions from reviews and classify them based on sentiment, providing insights into public perception of movies.

## Features
**Web Scraping:** Collects movie reviews and metadata from IMDb using automated web scraping.

**Data Preprocessing:** Cleans and processes raw text data to prepare it for modeling.

**Sentiment Analysis:** Uses machine learning models to classify reviews as positive, negative, or neutral.

**Model Training & Evaluation:** Trains machine learning models and evaluates their performance.

## Installation
To set up the project locally, follow these steps:

**Clone the Repository:**

```bash
git clone https://github.com/KesavP-01/Opinion_Mining.git
cd Opinion_Mining
```
**Create and Activate a Virtual Environment (Optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
**Install the Dependencies:**
```bash
pip install -r requirements.txt
```
**Install the Package:**
```
python setup.py install
```

## Usage
**Prepare Data:**

Before starting, make sure the data/movieNames.csv is populated with the names of the movies you wish to scrape reviews for.

**Run the movieReviews.py script to collect reviews:**
```
python script/movieReviews.py
```
**Train the Model:**

Preprocess the data and train the sentiment analysis model using:
```
python models/modelTrain.py
```
**Evaluate the Model:**

Once the model is trained, evaluate its performance using:
```
python models/modelEvaluate.py
```
**Make Predictions:**

Use the trained model to make sentiment predictions on new data.

## Results

**Achieved an accuracy of 54% on the test Dataset.**
