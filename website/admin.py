from django.contrib import admin
from .models import BatchBanner
from .models import Courses,CoursesCategory,CourseOverview,CourseCoverMainTopic,CourseCoverSubTopic,CareerOpportunities,TrendingCourses,Event,Blogs,Review
# Register your models here.


class Coursetable(admin.ModelAdmin):
     list_display = ('course_name','course_cat','course_image','course_duration','lecture_duration','job_opportunity','footer')
admin.site.register(Courses,Coursetable)


class Coursecattable(admin.ModelAdmin):
     list_display = ('category_name',)
admin.site.register(CoursesCategory,Coursecattable)


class Coverview(admin.ModelAdmin):
     list_display = ('course_name','overview_title','overview_content')
admin.site.register(CourseOverview,Coverview)

class Coursecovertopic(admin.ModelAdmin):
     list_display = ('topic_title','course')
admin.site.register(CourseCoverMainTopic,Coursecovertopic)  

class Coursecoversubtopic(admin.ModelAdmin):
     list_display = ('sub_topic_title','main_topic_title','course')
admin.site.register(CourseCoverSubTopic,Coursecoversubtopic)

class Careeropportunity(admin.ModelAdmin):
     list_display = ('career_opportunity','course')
admin.site.register(CareerOpportunities,Careeropportunity)

class trendcourse(admin.ModelAdmin):
     list_display = ('course_name',)
admin.site.register(TrendingCourses,trendcourse)

class events(admin.ModelAdmin):
     list_display = ('event_name','event_description','event_start_time','event_end_time','event_venue','event_date')
admin.site.register(Event,events)


class blogtable(admin.ModelAdmin):
     list_display = ('blog_title','blog_description','blog_content','blog_author','blog_date')
admin.site.register(Blogs,blogtable)

class reviewtable(admin.ModelAdmin):
     list_display = ('name','position','link','review')
admin.site.register(Review,reviewtable)

class batch(admin.ModelAdmin):
     list_display = ('batch_image',)
admin.site.register(BatchBanner,batch)