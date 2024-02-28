from django.conf import settings
from django.db.models.fields import related
from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.mail import send_mail
from website.admin import batch, events
from .models import Courses
from .models import CoursesCategory
from website import models
from .forms import EnrollForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import random
from django.core.mail import EmailMultiAlternatives

# Create your views here.

data = {}
def index(request):
    global data
    get_data()
    offered_course1 = []
    offered_course2=[]
    
    length = len(data['courses'].values_list())
    if length:
        templst1= data['courses'].values_list()[0:length/2:1]
        templst2 = data['courses'].values_list()[length/2::1]
        review = models.Review.objects.all()
        events = models.Event.objects.all().order_by('event_date').reverse().values()
        if(len(templst1)<6):
             offered_course1 = random.sample(templst1,len(templst1))
             offered_course2 = random.sample(templst2,len(templst2))
        else:
            offered_course1 = random.sample(templst1,6)
            offered_course2 = random.sample(templst2,6)

        data['reviews']= review
        data['offered_course1'] = offered_course1
        data['offered_course2'] = offered_course2
        
        blog  = models.Blogs.objects.all().order_by('blog_date')[:3]
        data['blogs'] = blog
        data['events'] = events

        batch_banner = models.BatchBanner.objects.all().reverse().values_list()[0]
        #print(batch_banner)
        data['banner'] = batch_banner
    return render(request, 'index.html', data)  

def sorting(e):
    return e.date

def courses(request,course_name):
    global data
    if(len(data)==0):
        get_data()
        
    try : 
        course = Courses.objects.filter(course_name=course_name).values()
        course_overview = models.CourseOverview.objects.filter(course_name = course_name).values()
        course_cover_main_title = models.CourseCoverMainTopic.objects.filter(course = course_name).order_by('time').values_list('topic_title',flat = True)
        course_cover_sub_title = models.CourseCoverSubTopic.objects.filter(course = course_name).values()
        career_opportunities = models.CareerOpportunities.objects.filter(course=course_name).values_list()
        trending_courses = models.TrendingCourses.objects.all()
        # events = models.Event.objects.all().values_list()[0:2]

        related_courses = []
        related_course2=[]
        for values in data['courses'].values():
            if(values['course_cat_id']==course[0]['course_cat_id']):
                if(values['course_name']!=course_name):
                    related_courses.append(values)
                
        for i in range(2):
            related_course2.append(random.choice(related_courses))

        
        # temp_event=[]
        # for event in events:
        #     if(event['active_status']):
        #         temp_event.append(event)
            
        if course_overview.first() and course.first():

            data1 = data.copy()
            data1['course_name'] = course[0]['course_name']
            data1['course_headline'] = course[0]['course_headline']
            data1['course_duration'] = course[0]['course_duration']
            data1['lecture_duration'] = course[0]['lecture_duration']
            data1['job_opportunity'] = course[0]['job_opportunity']
            data1['course_img'] =  Courses.objects.get(course_name = course_name)
            data1['course_overview_title']= course_overview[0]['overview_title']
            data1['course_overview_content']= course_overview[0]['overview_content']
            data1['course_cover_main_topic']= course_cover_main_title  
            data1['course_cover_sub_topic'] = course_cover_sub_title
            data1['carrer_opportunities'] = career_opportunities
            data1['related_courses'] = related_course2
            data1['trending_courses'] = trending_courses

           # print(data['courses'].values()[0]['course_cat_id'])
           #print(Courses.objects.get(course_name = course_name))        
                        
        else:
             raise Http404("Course does not exist")

    except ObjectDoesNotExist as DoesNotExist:
        raise Http404("Course does not exist")
    
    # for i in  course_overview:
    #     print(i)
    #print(data['course_overview_content'])
    # print(course_overview_title[0]['overview_title'])
    
    return render(request, 'courses.html', data1)


def blogs(request,blog_title):
    return render(request, 'blogs.html', data)

def get_data():
    global data
    c = Courses.objects.all()
    cat = CoursesCategory.objects.all()
    cat_lst = (list(cat.values_list('category_name', flat=True)))

    data = {'courses': c,'loop_times': range(0,len(cat_lst),2),'cat_lst' : cat_lst}
    data['enroll_form'] = EnrollForm()

    return data

def allcourses(request):
    global data
    data1 = data.copy()
    courses = Courses.objects.all()
    p= Paginator(courses,6)
    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page_number is out of range then assign the last page
        page_obj = p.page(p.num_pages) 
        
    data1['page_obj'] = page_obj
    data1['row_loop'] = range(3)

    return render(request, 'allcourses.html',data1)


def allevents(request):
    global data
    data1 = data.copy()
    events= models.Event.objects.all().order_by('event_date').reverse()
    p= Paginator(events,12)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page_number is out of range then assign the last page
        page_obj = p.page(p.num_pages) 

    data1['page_obj'] = page_obj
    data1['row_loop'] = range(3)
    return render(request, 'allevents.html',data1)

    
def contactus(request):
    global data
    data1 = data.copy()
    return render(request, 'contactus.html', data1)

def mailsent(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        suject=request.POST.get('subject')
        message=request.POST.get('message')

        subject, from_email = 'Admission Inquiry on GI site ', settings.EMAIL_HOST_USER
        text_content = 'plain text body message.'
        html_content = '<p>Name : <h2>'+name+'</h2>Email :<h2>'+email+'</h2>Number :<h2>'+number+'</h2> Subject:<h3>'+suject+'</h3>Mesaage : <h3>'+message+'</h3></p>'
        msg = EmailMultiAlternatives(subject,html_content, from_email, ['kevalvavaliya@gmail.com'])

        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        #send_mail( "Admission inquiry on GI institue Site",subject+"<br/>"+message,"<br>My email is :<h1>"+email+"</h1><br>My number is:<h1>"+number+"</h1>", ['kevalvavaliya@gmail.com'])
    return HttpResponse(json.dumps("Mail Sent"),content_type="application/json")
