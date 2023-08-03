from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import QuatitativeFeedback, TeachingRate, InteractionRate

# Create your views here.

def instructor(request):
    return render(request, 'pages/instructor.html')


def check_object_existence(Model, instructor_name):
    if(Model.objects.filter(instructor_name = instructor_name)).exists():
        obj = Model.objects.get(instructor_name = instructor_name)

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

def create_new_obj(Model,instructor_name,course_code, value):
    model = Model(
        instructor_name = instructor_name,
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
            instructor_name = data['instructor_name']
            course_code = data['course_code']
            courseContentRating = data['courseContentRating']
            instructorTeachingRating = data['instructorTeachingRating']
            likes = data['likes']
            suggestion = data['suggestions']

            qFeedback = QuatitativeFeedback(
                student_number = student_number,
                registration_number = registration_number,
                instructor_name = instructor_name,
                course_code = course_code,
                likes_field = likes,
                suggestion_field = suggestion,
                likes_sentiment = 0,
                suggestion_sentiment = 0
            )

            qFeedback.save()

            #Update data for the Class Table
            exists = check_object_existence(TeachingRate, instructor_name)

            if exists[0]:
                #object already exisits so update its value
                obj = exists[1]
                update_object(obj, courseContentRating)

            else:
                #create a object
                create_new_obj(TeachingRate, instructor_name, course_code, courseContentRating)

            #Update data for the instructorTeachingRating table
            exists = check_object_existence(InteractionRate, instructor_name)

            if exists[0]:
                obj = exists[1]
                update_object(obj, instructorTeachingRating)

            else:
                create_new_obj(InteractionRate, instructor_name, course_code, instructorTeachingRating)

            messages.success(request, "Feedback Recorded Successfully !, Thank you")
            return render(request, "pages/instructor.html")
        
        else:
            messages.success(request, "Invalid Request")
            return render(request, "pages/instructor.html")
    
    else:
        return redirect("login")