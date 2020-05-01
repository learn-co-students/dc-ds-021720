# Module 4 Final Project


## Introduction

In this lesson, we'll review all of the guidelines and specifications for the final project for Module 4.

## Objectives

* Understand all required aspects of the Final Project for Module 4
* Understand all required deliverables
* Understand what constitutes a successful project

## Final Project Summary

Final module down -- you're absolutely crushing it! You've made it all the way through one of the toughest modules of this course. You must have an amazing brain in your head!

<img src='https://raw.githubusercontent.com/learn-co-students/dsc-mod-4-project-seattle-ds-102819/master/images/brain.gif'>

## The Datasets

For this module's final project, you have the choice of three different types of problems: 

- Time Series Modeling 
- Recommendation System 
- Image Classification with Deep Learning 


For each problem, we have provided a dataset.  You are highly encouraged to use the provided dataset, but you may use an alternative dataset of your own choosing, pending instructor approval.

Like Project \#3, the focus here is on *prediction*. It will be up to you to determine how best to evaluate your model, but for any of these projects you should imagine that your goal is to build something that **works**.  If you invest in poorly chosen ZIP codes, this will hurt the business. If you make poor movie recommendations, people will stop trusting your judgments.  And the seriousness of the consequences of mis-classifying pneumonic or non-pneumonic lungs goes without saying! 

When choosing a problem, consider:

1. **Portfolio Depth:** One option is to choose the same type of problem you plan to tackle in Module 5 (capstone).  This will allow you to practice the necessary skills in a group setting, before diving into your individual project.  You will likely produce a capstone project that is more polished and sophisticated, but your portfolio will demonstrate less breadth.
2. **Portfolio Breadth:** Another option is to choose a type of problem that interests you, but that you don't plan to use in your capstone project.  Each of your individual projects will end up less polished and sophisticated, but you will end up with a portfolio that demonstrates a wider range of skills.


### Problem 1: Time Series Modeling

If you choose the Time Series option, you will be forecasting real estate prices of various zip codes using data from [Zillow](https://www.zillow.com/research/data/). However, this won't be as straightforward as just running a time-series analysis -- you're going to have to make some data-driven decisions and think critically along the way!

For this project, you will be acting as a consultant for a fictional real-estate investment firm. The firm has asked you what seems like a simple question:

> What are the top 5 best zip codes for us to invest in?

This may seem like a simple question at first glance, but there's more than a little ambiguity here that you'll have to think through in order to provide a solid recommendation. Should your recommendation be focused on profit margins only? What about risk? What sort of time horizon are you predicting against?  Your recommendation will need to detail your rationale and answer any sort of lingering questions like these in order to demonstrate how you define "best".

As mentioned previously, the data you'll be working with comes from the [Zillow Research Page](https://www.zillow.com/research/data/). However, there are many options on that page, and making sure you have exactly what you need can be a bit confusing. For simplicity's sake, we have already provided the dataset for you in this repo -- you will find it in the file `time-series/zillow_data.csv`.

The goal of this project is to have you complete a very common real-world task in regard to time series modeling. However, real world problems often come with a significant degree of ambiguity, which requires you to use your knowledge of statistics and data science to think critically about and answer. While the main task in this project is time series modeling, that isn't the overall goal -- it is important to understand that time series modeling is a tool in your toolbox, and the forecasts it provides you are what you'll use to answer important questions.

In short, to pass this project, demonstrating the quality and thoughtfulness of your overall recommendation is at least as important as successfully building a time series model!

#### Starter Jupyter Notebook

For this project, you will be provided with a Jupyter notebook, `time-series/starter_notebook.ipynb`, containing some starter code. If you inspect the Zillow dataset file, you'll notice that the datetimes for each sale are the actual column names -- this is a format you probably haven't seen before. To ensure that you're not blocked by preprocessing, we've provided some helper functions to help simplify getting the data into the correct format. You're not required to use this notebook or keep it in its current format, but we strongly recommend you consider making use of the helper functions so you can spend your time working on the parts of the project that matter.

#### Evaluation

In addition to deciding which quantitative metric(s) you want to target (e.g. minimizing mean squared error), you need to start with a definition of "best investment".  Consider additional metrics like risk vs. profitability, or ROI yield.

### Problem 2: Recommendation System

If you choose the Recommendation System option, you will be making movie recommendations based on the [MovieLens](https://grouplens.org/datasets/movielens/latest/) dataset from the GroupLens research lab at the University of Minnesota.  Unless you are planning to run your analysis on a paid cloud platform, we recommend that you use the "small" dataset containing 100,000 user ratings (and potentially, only a particular subset of that dataset).

Your task is to:

> Build a model that provides top 5 movie recommendations to a user, based on their ratings of other movies. 

The MovieLens dataset is a "classic" recommendation system dataset, that is used in numerous academic papers and machine learning proofs-of-concept.  You will need to create the specific details about how the user will provide their ratings of other movies, in addition to formulating a more specific business problem within the general context of "recommending movies".

#### Collaborative Filtering

At minimum, your recommendation system must use collaborative filtering.  If you have time, consider implementing a hybrid approach, e.g. using collaborative filtering as the primary mechanism, but using content-based filtering to address the [cold start problem](https://en.wikipedia.org/wiki/Cold_start_(computing)).

#### Evaluation

The MovieLens dataset has explicit ratings, so achieving some sort of evaluation of your model is simple enough.  But you should give some thought to the question of metrics.  Since the rankings are ordinal, we know we can treat this like a regression problem.  But when it comes to regression metrics there are several choices: RMSE, MAE, etc.  [Here](http://fastml.com/evaluating-recommender-systems/) are some further ideas.

### Problem 3: Image Classification with Deep Learning

If you choose this option, you'll put everything you've learned together to build a deep neural network that trains on a large dataset for classification on a non-trivial task.  In this case, using x-ray images of pediatric patients to identify whether or not they have pneumonia.  The dataset comes from Kermany et al. on [Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/3), although there is also a version on [Kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) that may be easier to use.

Your task is to:

> Build a model that can classify whether a given patient has pneumonia, given a chest x-ray image. 

#### Aim for a Proof of Concept

With Deep Learning, data is king -- the more of it, the better. However, the goal of this project isn't to build the best model possible -- it's to demonstrate your understanding by building a model that works. You should try to avoid datasets and model architectures that won't run in reasonable time on your own machine. For many problems, this means downsampling your dataset and only training on a portion of it. Once you're absolutely sure that you've found the best possible architecture and other hyperparameters for your model, then consider training your model on your entire dataset overnight (or, as larger portion of the dataset that will still run in a feasible amount of time).

At the end of the day, we want to see your thought process as you iterate and improve on a model. A project that achieves a lower level of accuracy but has clearly iterated on the model and the problem until it found the best possible approach is more impressive than a model with high accuracy that did no iteration. We're not just interested in seeing you finish a model -- we want to see that you understand it, and can use this knowledge to try and make it even better!

#### Evaluation

Evaluation is fairly straightforward for this project.  But you'll still need to think about which metric to use and about how best to cross-validate your results.



## The Deliverables

For online students, your completed project should contain the following four deliverables:

1. A **_Jupyter Notebook_** containing any code you've written for this project. This work will need to be pushed to a public GitHub repository dedicated for this project.

2. An organized **README.md** file in the GitHub repository that describes the contents of the repository. This file should be the source of information for navigating through the repository. 

3. An **_"Executive Summary" PowerPoint Presentation_** that gives a brief overview of your problem/dataset, and each step of the CRISP-DM process.


### Jupyter Notebook Must-Haves

For this project, your Jupyter Notebook should meet the following specifications:

**_Organization/Code Cleanliness_**

* The notebook should be well organized, easy to follow, and code is commented where appropriate.  
    * Level Up: The notebook contains well-formatted, professional looking markdown cells explaining any substantial code. All functions have docstrings that act as professional-quality documentation.  
* The notebook is written to technical audiences with a way to both understand your approach and reproduce your results. The target audience for this deliverable is other data scientists looking to validate your findings.  

**_Process, Methodology, and Findings_**

* Your notebook should contain a clear record of your process and methodology for exploring and preprocessing your data, building and tuning a model, and interpreting your results.
* We recommend you use the CRISP-DM process to help organize your thoughts and stay on track.

## The Process

These steps are informed by the CRISP-DM process.

### 1. Getting Started

Please start by reviewing this document. If you have any questions, please ask them in Slack ASAP so (a) we can answer the questions and (b) so we can update this repository to make it clearer.

### 2. CRISP-DM Check-In pt.1 - Monday
You will meet with your coaches on Monday to “pitch” your project idea.  Be prepared to answer the following questions:

- What questions will you be addressing?
- What ways might you visualize this data to address the question?

You will meet with the coaches to discuss your progress on the project and your plan for the rest of the week to make sure you are on the right track.  We will be focusing on the steps of the CRISP-DM model.  Be prepared to answer the following questions.

- Business Understanding
   - Have you clearly defined your goal for your analysis?
   - Have your thought about who your audience is and how they would use this information?
   - How does this help the goals of the business/organization?
- Data Understanding
   - What data are you using?
   - How does your data help you answer the business question?
   - How many observations does your dataset contain?
   - What is the distribution of your data?
   - What data types do you have?   
- Data Preparation
   - Have you looked/dealt with missing values?
   - Have you done any data-type conversion?
      - ex: numerical data incorrectly ‘typed’ as strings.
    - Does your data contain any outliers or non-sensical values?
    
### 3. CRISP-DM Check-In pt.2 - Tuesday
- EDA/Visualization
   - What visualizations have you already made/planning to make?
   - What messages are these visualizations trying to convey?
   - What visualizations have you already made/planning to assess if your data meets the assumtions of linear regression?
   
- Modeling:
    - Is this a classification task? A regression task? Something else?
    - What models will we try?
    - How do we deal with overfitting?
    - Do we need to use regularization or not?
    - What sort of validation strategy will we be using to check that our model  - works well on unseen data?
    - What loss functions will we use?
    - What threshold of performance do we consider as successful?

- Evaluation:
    - How are you determining which variables are important.
    - What overall metric of success are you using.
    - What additional steps might you need to take to improve the model? (ex: transforming data, scaling data, getting more features) 
   
### 4. MVP Checkin - Wednesday
You will meet with an  instructor who will check if the minimum requirements of the project are completed. At this point you should have your visualizations done and they should answer the business questions.  Following this meeting you should be ready to polish your notebook and work on your slidedeck.

### 5. Practice Presentations- Thursday
You will meet with the coaches and do a practice presentation with them.  At this point the coaches will provide verbal feedback which can be incorportated in your final presentation.

### 6. Project Presentations- Friday
You will present your project to the class using your slidedeck.  This presentation should not take more than 5 minutes and should be directed towards a non-technical audience.  Both partners should participate in the presentation of the project.


## Submitting your Project

You’re almost done! In order to submit your project for review, please complete the Mod 4 Project Submission form in Canvas.

## Grading Rubric

The grading rubric for the project can be found in the same folder as this description.

## Summary

The end of module projects and project reviews are a critical part of the program. They give you a chance to both bring together all the skills you've learned into realistic projects and to practice key "business judgement" and communication skills that you otherwise might not get as much practice with.


