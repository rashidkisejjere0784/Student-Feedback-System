import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Coverage, QuatitativeFeedback, Assessment, Evaluation, Impact, Participation
import os
from wordcloud import WordCloud
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import matplotlib

matplotlib.use('Agg')

# import the model
model_path = "sentiment"

model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Create your views here.


def generate_wordCloud(text, file_name):
    word_cloud = WordCloud(width=600,
                           height=500,
                           background_color="white",
                           min_font_size=10, colormap="viridis").generate(text)

    word_cloud.to_file(f"static/img/{file_name}.png")


def PieChart(p_feedback, n_feedback, file_name):
    total = QuatitativeFeedback.objects.count()

    if os.path.exists(f"static/img/{file_name}.png"):
        os.remove(f"static/img/{file_name}.png")

    # calculate the percentage for each of the feedbacks

    if total != 0:

        p_feedback = (p_feedback / total) * 100
        n_feedback = (n_feedback / total) * 100

        arr = np.array([p_feedback, n_feedback])
        labels = ["positive", "negative"]

        plt.pie(arr, labels=labels)
        plt.legend()
        plt.savefig(f"static/img/{file_name}.png")

        plt.close()


def course(request):
    # read the data from database
    evaluation = Evaluation.objects.all()
    assessments = Assessment.objects.all()
    coverage = Coverage.objects.all()
    impact = Impact.objects.all()
    participation = Participation.objects.all()

    isAdmin = True if request.user.username == os.environ.get(
        "ADMIN_USER_NAME") else False

    # generate word cloud
    data = QuatitativeFeedback.objects.values_list("feedback_field", flat=True)
    text = " ".join(data)
    if text != "":
        generate_wordCloud(text, "word_cloud")

    else:
        if os.path.exists("static/img/word_cloud.png"):
            os.remove("static/img/word_cloud.png")

    data = QuatitativeFeedback.objects.values_list(
        "suggestion_field", flat=True)
    text = " ".join(data)
    if text != "":
        generate_wordCloud(text, "word_cloud2")

    else:
        if os.path.exists("static/img/word_cloud2.png"):
            os.remove("static/img/word_cloud2.png")

    # count the number of positive and negative sentiments
    feedback_positive = QuatitativeFeedback.objects.filter(
        feedback_sentiment=1).count()
    feedback_negative = QuatitativeFeedback.objects.filter(
        feedback_sentiment=0).count()

    # plt the piechart
    PieChart(feedback_positive, feedback_negative, "piechart")

    suggestion_positive = QuatitativeFeedback.objects.filter(
        suggestion_sentiment=1).count()
    suggestion_negative = QuatitativeFeedback.objects.filter(
        suggestion_sentiment=0).count()

    # plt the piechart
    PieChart(suggestion_positive, suggestion_negative, "piechart2")

    return render(request, 'pages/course.html', {"evaluation": evaluation,
                                                 "assessments": assessments,
                                                 "coverage": coverage,
                                                 "impact": impact,
                                                 "participation": participation,
                                                 "isAdmin": isAdmin,
                                                 "f_postive": feedback_positive,
                                                 "f_negative": feedback_negative,
                                                 "s_positive": suggestion_positive,
                                                 "s_negative": suggestion_negative
                                                 })


def check_object_existence(Model, course_code):
    if (Model.objects.filter(course_code=course_code)).exists():
        obj = Model.objects.get(course_code=course_code)

        return (True, obj)

    return (False,)


def update_object(obj, value):
    if (value == "excellent_rating"):
        obj.excellent_rating += 1

    elif (value == "very_good_rating"):
        obj.very_good_rating += 1

    elif (value == "good_rating"):
        obj.good_rating += 1

    elif (value == "fair_rating"):
        obj.fair_rating += 1

    else:
        obj.poor_rating += 1

    obj.save()


def create_new_obj(Model, course_code, course_name, value):
    model = Model(
        course_code=course_code,
        excellent_rating=1 if (value == "excellent_rating") else 0,
        very_good_rating=1 if (value == "very_good_rating") else 0,
        good_rating=1 if (value == "good_rating") else 0,
        fair_rating=1 if (value == "fair_rating") else 0,
        poor_rating=1 if (value == "poor_rating") else 0
    )

    model.save()


def view_feedback(request, feedback_type):
    if request.user.is_authenticated:
        data = QuatitativeFeedback.objects.all()
        return render(request, "pages/view-feedback.html", {"data": data, "feedback": feedback_type})

    else:
        return redirect("login")


def add_feedback(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST

            student_number = data["student_number"]
            registration_number = data['reg_number']
            course_code = data['course_code']
            course_name = data['course_name']
            courseRating = data['courseRating']
            assignmentsRating = data['assignmentsRating']
            instructorRating = data['instructorRating']
            teachingMethodsRating = data['teachingMethodsRating']
            communicationRating = data['communicationRating']
            feedback = data['feedback']
            suggestion = data['suggestions']

            # check the sentiment of the two fields
            input_1 = tokenizer(str(feedback).lower(), return_tensors="pt")[
                "input_ids"]  # tokenize the text
            input_2 = tokenizer(str(suggestion).lower(), return_tensors="pt")[
                "input_ids"]  # tokenize the text

            print("output", input_1)
            print(model(input_1))
            # predict the sentiment
            output_1 = model(input_1).logits.argmax().item()
            output_2 = model(input_2).logits.argmax().item()

            qFeedback = QuatitativeFeedback(
                student_number=student_number,
                registration_number=registration_number,
                course_name=course_name,
                course_code=course_code,
                feedback_field=feedback,
                suggestion_field=suggestion,
                feedback_sentiment=output_1,
                suggestion_sentiment=output_2
            )

            qFeedback.save()

            # Update data for the Class Table
            exists = check_object_existence(Evaluation, course_code)

            if exists[0]:
                # object already exisits so update its value
                obj = exists[1]
                update_object(obj, courseRating)

            else:
                # create a object
                create_new_obj(Evaluation, course_code,
                               course_name, courseRating)

            # Update data for the assignmentsRating table
            exists = check_object_existence(Assessment, course_code)

            if exists[0]:
                obj = exists[1]
                update_object(obj, assignmentsRating)

            else:
                create_new_obj(Assessment, course_code,
                               course_name, assignmentsRating)

             # Update data for the Class Size table
            exists = check_object_existence(Coverage, course_code)

            if exists[0]:
                obj = exists[1]
                update_object(obj, instructorRating)

            else:
                create_new_obj(Coverage, course_code,
                               course_name, instructorRating)

            # Update data for the Class Size table
            exists = check_object_existence(Impact, course_code)

            if exists[0]:
                obj = exists[1]
                update_object(obj, teachingMethodsRating)

            else:
                create_new_obj(Impact, course_code, course_name,
                               teachingMethodsRating)

            # Update data for the Class Size table
            exists = check_object_existence(Participation, course_code)

            if exists[0]:
                obj = exists[1]
                update_object(obj, communicationRating)

            else:
                create_new_obj(Participation, course_code,
                               course_name, communicationRating)

            messages.success(
                request, "Feedback Recorded Successfully !, Thank you")
            return redirect("course")

        else:
            messages.success(request, "Invalid Request")
            return redirect("course")

    else:
        return redirect("login")
