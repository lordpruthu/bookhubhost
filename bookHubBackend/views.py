from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import os
from services.models import Form

from youtubesearchpython import VideosSearch
from django.http import Http404

from django.shortcuts import render
from django.http import FileResponse, Http404


import pytube

def pdf(request):
    filename = request.GET.get('subject')
    try:
        return FileResponse(open(f'media/pdfs/{filename}pfd', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')
def main(request):
    return render(request,'bookDeatils.html')
    


def pdf_view(request):
    subject = request.GET.get('subject')
    Sem = request.GET.get('Sem')
    if not subject:
        return HttpResponse('No filename provided')

    filepath = os.path.join('media', 'pdfs', f'{subject}.pdf')
    if not os.path.isfile(filepath):
        return HttpResponse('File not found')

    with open(filepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'filename={subject}.pdf'
        return response




def index(request):
    return render(request,"index.html")

def productDetails(request):
    return render(request,"product-details.html")

def engineering(request):
    return render(request,"engineering.html")

def engineeringDetails(request):
    #context = {'string_value': string_value}
    data = {
        "streamName": "Engineering",
        "Sem1": "Semester 1",
        "Sem2": "Semester 2",
        "Sem3": "Semester 3",
        "Sem4": "Semester 4",
        "Sem5": "Semester 5",
        "Sem6": "Semester 6",
        "Sem7": "Semester 7",
        "Sem8": "Semester 8"
    }
        
    return render(request,"engineeringDetails.html",data)

def streams(request):

    return render(request,"streams.html")

def streamDetails(request):
    sem = request.GET.get('sem')
    subject = request.GET.get('subject')
   
    subject = subject.replace(' ', '+')
    


    

    # construct the search URL and send a GET request
    url = f'https://www.youtube.com/results?search_query={subject}'
    
    query = subject

    videos_search = VideosSearch(query, limit=6)
    results = videos_search.result()["result"]

    # create a dictionary to store the top 5 YouTube embedded links
    youtube_dict = {}
    try:
        for i in range(len(results)):
            video_id = results[i]["id"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            yt = pytube.YouTube(video_url)
            embedded_link = yt.streams.filter(file_extension="mp4", res="720p").first().url
            youtube_dict[f"linkYT{i+1}"] = embedded_link
            return render(request, "streamDetails.html", {'youtube_dict': youtube_dict})
    except:
        return render(request, "streamDetails.html", {'youtube_dict': 'No_video_found'})

    return render(request,"streamDetails.html")


def semester1(request):
    data = {

        "semName": "semester1",
       
        "subject1": "Engineering Mathematics - I",
        "subject2": "Engineering Physics",
        "subject3": "Engineering Chemistry",                          
        "subject4": "Engineering Drawing",
        "subject5": "Engineering Graphics",
        "subject6": "Engineering Mechanics" 
    }
    return render(request,"engineeringSUB.html",data)

def semester2(request):
    data = {
        "semName": "semester2",
        "subject1": "Engineering Mathematics - II",
        "subject2": "Engineering Physics - II",
        "subject3": "Engineering Chemistry - II",
        "subject4": "Engineering Graphics",
        "subject5": "Engineering Mechanics - II",
        "subject6": "C Programming"
    }
    return render(request,"engineeringSUB.html",data)

def semester3(request):
    data = {
        "semName": "semester3",
        "subject1": "Engineering Mathematics - III",
        "subject2": "Discrete Mathematics and Graph Theory",
        "subject3": "Data Structures",
        "subject4": "Digital logic Computer Organization and Architecture",
        "subject5": "Object Oriented Programming with Java",
        "subject6": "Computer Graphics"
    }
    return render(request,"engineeringSUB.html",data)

def semester4(request):
    data = {
        "semName": "semester4",
        "subject1": "Engineering Mathematics - IV",
        "subject2": "Database Management Systems",
        "subject3": "Operating Systems",
        "subject4": "Microprocessor",
        "subject5": "Python Programming",
        "subject6": "Analysis of Algorithms"
    }
    return render(request,"engineeringSUB.html",data)

def semester5(request):
    data = {
        "semName": "semester5",
        "subject1": "Theoretical Computer Science",
        "subject2": "Computer Networks",
        "subject3": "Software Engineering",
        "subject4": "Computer Organization and Architecture",
        "subject5": "Data Warehousing and Data Mining",
        "subject6": "Professional Ethics and Communication Skills"
    }
    return render(request,"engineeringSUB.html",data)

def semester6(request):
    data = {
        "semName": "semester6",
        "subject1": "Artificial Intelligence",
        "subject2": "Internet of Things",
        "subject3": "Cryptography & System Security",
        "subject4": "Computer Vision",
        "subject5": "Mobile Computing",
        "subject6": "System Programming and Compiler Construction"
    }
    return render(request,"engineeringSUB.html",data)

def semester7(request):
    data = {
        "semName": "semester7",
        "subject1": "Machine Learning",
        "subject2": "Cloud Computing",
        "subject3": "Big Data Analytics",
        "subject4": "Data Science",
        "subject5": "Information Retrieval",
        "subject6": "Natural Language Processing"
    }
    return render(request,"engineeringSUB.html",data)

def semester8(request):
    data = {
        "semName": "semester8",
        "subject1": "Deep Learning",
        "subject2": "Blockchain",
        "subject3": "Cyber Security",
        "subject4": "Data Structures and Algorithms",
        "subject5": "Data Science",
        "subject6": "Information Retrieval"
    }
    return render(request,"engineeringSUB.html",data)




def science(request):
    data = {               
        "stream": "Science",
       
        "subject1": "Biology",
        "subject2": "Chemistry",
        "subject3": "Physics",
        "subject4": "Mathematics",              
        "subject5": "English",
        "subject6": "Computer Science"        
    }
    return render(request,"streams.html",data)

def commerce(request):
    data = {

        "stream": "Commerce",
       
        "subject1": "Economics",
        "subject2": "Organisation of Commerce",
        "subject3": "Book Keeping & Accountancy",                          
        "subject4": "Mathematics / Secretarial Practice",
        "subject5": "EVS",
        "subject6": "Physical Education" 
    }

    return render(request,"streams.html", data)

def arts(request):
    data = {

        "stream": "arts",
       
        "subject1": "Economics",
        "subject2": "History",
        "subject3": "Political Science",
        "subject4": "Geography",                  
        "subject5": "Sociology",
        "subject6": "Philosophy" 
    }

    return render(request,"streams.html", data) 

def medical(request):
    data = {

        "stream": "Medical",
       
        "subject1": "Economics",
        "subject2": "Organisation of Commerce",
        "subject3": "Book Keeping & Accountancy",                          
        "subject4": "Mathematics / Secretarial Practice",
        "subject5": "EVS",
        "subject6": "Physical Education"
    }
    
    return render(request,"streams.html", data)

def law(request):
    data = {

        "stream": "Law",
        
        "subject1": "Labor Law",
        "subject2": "Company Law",
        "subject3": "Jurisprudence",                          
        "subject4": "Legal Writing",     
        "subject5": "Family Law",
        "subject6": "Administrative Law"
    }

    return render(request,"streams.html", data)

def php(request):
    data = {

        "stream": "php",
        "book1": "Head first PHP & MySQL",
        "book2": "PHP : for Dynamic Web Sites: Visual QuickPro Guide",
        "book3": "PHP : Novice to Ninja",
        "book4": "PHP : The Missing Manual",                 
        "book5": "PHP : Web Development",
        "book6": "PHP : A bigineer's guide" 
    }

    return render(request,"books.html", data) 

def javascript(request):
    data = {

        "stream": "javascript",
        
        "book1": "Learning JavaScript Design Patterns",
        "book2": "PHP : Effective JavaScript",
        "book3": "PHP : JavaScript: The Good Part",
        "book4": "PHP : You Don't Know JS",                 
        "book5": "PHP : Web Development",
        "book6": "PHP : A bigineer's guide" 
    }

    return render(request,"books.html", data) 

def python(request):
    data = {

        "stream": "Python",
        
        "book1": "Python Cookbook",
        
        "book2": "Automate the Boring Stuff with Python",
        "book3": "Python for Data Analysis",
        "book4": "Fluent Python",                 
        "book5": "Python Crash Course",
        "book6": "Learning Python"
    }

    return render(request,"books.html", data) 

def flutter(request):
    data = {

        "stream": "flutter",
        "book1": "Flutter in Action",
        "book2": "flutter cookbook",
        "book3": "Flutter for Beginners",
        "book4": "Flutter for Dummies",                 
        "book5": "Flutter for Web Developers",
        "book6": "Flutter UI Design Handbook" 
    }

    return render(request,"books.html", data) 

def react(request):
    data = {

        "stream": "React",
        "book1": "Learning React",
        "book2": "React: Up & Running",
        "book3": "React Native: Building Mobile Apps with JavaScript",
        "book4": "Pro React",                 
        "book5": "React Design Patterns and Best Practices",
        "book6": "React Cookbook" 
    }

    return render(request,"books.html", data) 



def bookDetails(request):
    sem = request.GET.get('sem')
    subject = request.GET.get('subject')
   
    subject = subject.replace(' ', '+')
    


    

    # construct the search URL and send a GET request
    url = f'https://www.youtube.com/results?search_query={subject}'
    
    query = subject

    videos_search = VideosSearch(query, limit=6)
    results = videos_search.result()["result"]

    # create a dictionary to store the top 5 YouTube embedded links
    youtube_dict = {}
    try:
        for i in range(len(results)):
            video_id = results[i]["id"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            yt = pytube.YouTube(video_url)
            embedded_link = yt.streams.filter(file_extension="mp4", res="720p").first().url
            youtube_dict[f"linkYT{i+1}"] = embedded_link
            return render(request, "bookDetails.html", {'youtube_dict': youtube_dict})
    except:
        return render(request, "bookDetails.html", {'youtube_dict': 'No_video_found'})
        
def contact(request):
    return render(request, "contact.html")

def contactForm(request):
    if request.method=="POST":
        if "submitted" is True:
            return render(request, 'index.html',{"submitted":False})
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        subject=request.POST.get('subject')
        send_mail(
            subject,
            'Name: '+name+'\nMessage: '+message,
            'thane_nigga@outlook.com',
            [email],
            fail_silently=False,
        )
        print (name, email, message, subject)

        contact = Form(Name=name, Email=email,Message=message)
        contact.save()
        return render(request, 'index.html',{"submitted":True})
    else:
        return render(request, 'index.html')
    

    