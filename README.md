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
