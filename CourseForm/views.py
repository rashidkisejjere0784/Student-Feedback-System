from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Coverage, QuatitativeFeedback, Assessment, Evaluation, Impact, Participation

# Create your views here.

def course(request):
    return render(request, 'pages/course.html')


def check_object_existence(Model, course_code):
    if(Model.objects.filter(course_code = course_code)).exists():
        obj = Model.objects.get(course_code = course_code)

        return (True, obj)
    
    return (False,)

def update_object(obj, value):
    if(value == "excellent_rating"):
        obj.excellent_rating += 1

    elif(value == "very_good_rating"):
        obj.very_good_rating += 1

    elif(value == "good_rating"):
        obj.good_rating += 1

    elif(value == "fair_rating"):
        obj.fair_rating += 1

    else:
        obj.poor_rating += 1

    obj.save()

def create_new_obj(Model,course_code,course_name, value):
    model = Model(
        course_code = course_code,
        excellent_rating = 1 if (value == "excellent_rating") else 0,
        very_good_rating = 1 if (value == "very_good_rating") else 0,
        good_rating = 1 if (value == "good_rating") else 0,
        fair_rating = 1 if (value == "fair_rating") else 0,
        poor_rating = 1 if (value == "poor_rating") else 0
    )

    model.save()
    

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
            likes = data['likes']
            suggestion = data['suggestions']

            qFeedback = QuatitativeFeedback(
                student_number = student_number,
                registration_number = registration_number,
                course_code = course_code,
                course_name = course_name,
                likes_field = likes,
                suggestion_field = suggestion,
                likes_sentiment = 0,
                suggestion_sentiment = 0
            )

            qFeedback.save()

            #Update data for the Class Table
            exists = check_object_existence(Evaluation, course_code)

            if exists[0]:
                #object already exisits so update its value
                obj = exists[1]
                update_object(obj, courseRating)

            else:
                #create a object
                create_new_obj(Evaluation, course_code, course_name, courseRating)

            #Update data for the assignmentsRating table
            exists = check_object_existence(Assessment, course_code)

            if exists[0]:
                obj = exists[1]
                update_object(obj, assignmentsRating)

            else:
                create_new_obj(Assessment, course_code, course_name, assignmentsRating)

             #Update data for the Class Size table
            exists = check_object_existence(Coverage, course_code)

            if exists[0]:
                obj = exists[1]
                update_object(obj, instructorRating)

            else:
                create_new_obj(Coverage, course_code, course_name, instructorRating)

            #Update data for the Class Size table
            exists = check_object_existence(Impact, course_code)

            if exists[0]:
                obj = exists[1]
                update_object(obj, teachingMethodsRating)

            else:
                create_new_obj(Impact, course_code, course_name, teachingMethodsRating)

            #Update data for the Class Size table
            exists = check_object_existence(Participation, course_code)

            if exists[0]:
                obj = exists[1]
                update_object(obj, communicationRating)

            else:
                create_new_obj(Participation, course_code, course_name, communicationRating)

            messages.success(request, "Feedback Recorded Successfully !, Thank you")
            return render(request, "pages/course.html")
        
        else:
            messages.success(request, "Invalid Request")
            return render(request, "pages/course.html")
    
    else:
        return redirect("login")