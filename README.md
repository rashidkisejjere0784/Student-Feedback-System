# Student Feedback System - Project README

Welcome to the Student Feedback System project repository. This repository contains the source code and documentation for our web application that facilitates the collection, analysis, and reporting of student feedback regarding courses, instructors, and campus facilities.

## About the Project

Our team of five embarked on developing a robust and user-friendly Student Feedback System using Django, a powerful web development framework. The system incorporates sentiment analysis to gain valuable insights from the feedback data, contributing to data-driven decision-making and improvements.

## Key Features

- Streamlined feedback collection process for students.
- Integration of sentiment analysis model for automatic feedback sentiment evaluation.
- Comprehensive reporting system to identify strengths and areas for improvement.
- User authentication and security measures for data privacy.

## System Diagrams

### Class Diagram - Evaluation, Coverage, Impact, and Participation Classes

```mermaid
classDiagram
    class Evaluation {
        + created_at: DateTime
        + course_code: CharField(max_length=50)
        + excellent_rating: IntegerField
        + very_good_rating: IntegerField
        + good_rating: IntegerField
        + fair_rating: IntegerField
        + poor_rating: IntegerField
    }
    
    class Coverage {
        + created_at: DateTime
        + course_code: CharField(max_length=50)
        + excellent_rating: IntegerField
        + very_good_rating: IntegerField
        + good_rating: IntegerField
        + fair_rating: IntegerField
        + poor_rating: IntegerField
    }
    
    class Impact {
        + created_at: DateTime
        + course_code: CharField(max_length=50)
        + excellent_rating: IntegerField
        + very_good_rating: IntegerField
        + good_rating: IntegerField
        + fair_rating: IntegerField
        + poor_rating: IntegerField
    }
    
    class Participation {
        + created_at: DateTime
        + course_code: CharField(max_length=50)
        + excellent_rating: IntegerField
        + very_good_rating: IntegerField
        + good_rating: IntegerField
        + fair_rating: IntegerField
        + poor_rating: IntegerField
    }
```
---

## Use Case Diagram - Student Feedback Process
```mermaid
graph TD

    subgraph Student Feedback System
        Admin[Administrator]
        Student[Student]
        WebApp[Student Feedback Web App]

        Admin --> |Manages| WebApp
        Student --> |Provides Feedback| WebApp
        WebApp --> |Collects Feedback| FeedbackSystem
        WebApp --> |Generates Reports| ReportingSystem
        WebApp --> |Performs Sentiment Analysis| SentimentAnalysis
    end

    subgraph External Systems
        ReportingSystem[Reporting System]
        SentimentAnalysis[Sentiment Analysis System]
        FeedbackSystem[Feedback Collection System]
    end
```

### Activity Diagram - Feedback Submission and Report Generation

```mermaid
graph TD

    subgraph Student Feedback Process
        Start(Start)
        SubmitFeedback[Submit Feedback]
        PerformAnalysis[Perform Sentiment Analysis]
        GenerateReport[Generate Reports]
        End(End)
    end

    Start --> SubmitFeedback --> PerformAnalysis --> GenerateReport --> End

    style Start, End fill:#77DD77,stroke:#4CAF50,stroke-width:2px
```
## Download Project Report
For a detailed understanding of the project, including its development process, system architecture, and features, you can download the project report from the following link:
[Download Project Report]()

## How to Run the Project
To run the Student Feedback System locally, follow these steps:

- Clone this repository.
- create the virtual Environment `python venv -m env `
- Activate the Environment `env \Script\activate.bat`
- Install the required dependencies by running `pip install -r requirements.txt`.
- Run the migrations `python manage.py makemigrations`
- Migrate the models `python manage.py migrate`
- Run the Django development server using `python manage.py runserver`.
