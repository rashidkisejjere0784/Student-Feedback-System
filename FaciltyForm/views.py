from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import QuatitativeFeedback, ClassroomFacilty, ClassSizeFacilty, TechnologyFacilty
import os
from wordcloud import WordCloud


# Create your views here.

def generate_wordCloud(text, file_name):
    word_cloud = WordCloud(width=900,
                            height=400,
                            background_color="white",
                            min_font_size=10, colormap="viridis").generate(text)
    
    word_cloud.to_file(f"static/img/{file_name}.png")

def facility(request):
    classroom = ClassroomFacilty.objects.all()
    classsize = ClassSizeFacilty.objects.all()
    technology = TechnologyFacilty.objects.all()
    qFeedback = QuatitativeFeedback.objects.all()

    isAdmin = True if request.user.username == os.environ.get("ADMIN_USER_NAME") else False

    #generate word cloud
    data = QuatitativeFeedback.objects.values_list("likes_field", flat=True)
    text = " ".join(data)
    if text != "":
        generate_wordCloud(text, "word_cloud")
    else:
        if os.path.exists("static/img/word_cloud.png"):
            os.remove("static/img/word_cloud.png")

    data = QuatitativeFeedback.objects.values_list("suggestion_field", flat=True)
    text = " ".join(data)
    if text != "":
        generate_wordCloud(text, "word_cloud2")

    else:
        if os.path.exists("static/img/word_cloud2.png"):
            os.remove("static/img/word_cloud2.png")

    return render(request, 'pages/facility.html', {
        "classroom" : classroom,
        "classsize" : classsize,
        "technology" : technology,
        "qFeedback" : qFeedback,
        "isAdmin" : isAdmin
    })


def check_object_existence(Model, facilty_name):
    if(Model.objects.filter(facilty_name = facilty_name)).exists():
        obj = Model.objects.get(facilty_name = facilty_name)

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

def create_new_obj(Model,facility_name, value):
    model = Model(
        facilty_name = facility_name,
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
            facility_name = data['facility_name']
            classroom = data['classroom']
            technology = data['technology']
            class_size = data['class_size']
            likes = data['likes']
            suggestion = data['suggestions']

            qFeedback = QuatitativeFeedback(
                student_number = student_number,
                registration_number = registration_number,
                facilty_name = facility_name,
                likes_field = likes,
                suggestion_field = suggestion,
                likes_sentiment = 0,
                suggestion_sentiment = 0
            )

            qFeedback.save()

            #Update data for the Class Table
            exists = check_object_existence(ClassroomFacilty, facility_name)

            if exists[0]:
                #object already exisits so update its value
                obj = exists[1]
                update_object(obj, classroom)

            else:
                #create a object
                create_new_obj(ClassroomFacilty, facility_name, classroom)

            #Update data for the Technology table
            exists = check_object_existence(ClassSizeFacilty, facility_name)

            if exists[0]:
                obj = exists[1]
                update_object(obj, class_size)

            else:
                create_new_obj(ClassSizeFacilty, facility_name, class_size)

             #Update data for the Class Size table
            exists = check_object_existence(TechnologyFacilty, facility_name)

            if exists[0]:
                obj = exists[1]
                update_object(obj, technology)

            else:
                create_new_obj(TechnologyFacilty, facility_name, technology)

            messages.success(request, "Feedback Recorded Successfully !, Thank you")
            return redirect("facility")
        
        else:
            messages.success(request, "Invalid Request")
            return redirect("facility")
    
    else:
        return redirect("login")