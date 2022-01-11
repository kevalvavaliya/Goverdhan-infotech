# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import fields
from django.db.models.fields import CharField




class CourseOverview(models.Model):
    overview_title = models.CharField(max_length=200,primary_key=True)
    overview_content = models.TextField()
    course_name = models.OneToOneField('Courses', models.DO_NOTHING, db_column='course_name')

    class Meta:
        managed = False
        db_table = 'course-overview'

    def __str__(self) -> str:
        return self.overview_title  

class Courses(models.Model):
    course_name = models.CharField(primary_key=True, max_length=255)
    course_cat = models.ForeignKey('CoursesCategory', models.DO_NOTHING, db_column='course_cat')
    course_headline = models.CharField(max_length=225)
    course_image = models.ImageField(upload_to='images/')
    course_duration = models.CharField(max_length=255)
    lecture_duration = models.CharField(max_length=255)
    job_opportunity = models.CharField(max_length=255)
    popular = models.BooleanField()
    footer = models.BooleanField()


    class Meta:
        managed = False
        db_table = 'courses'
    
    def __str__(self) -> str:
        return self.course_name


class CoursesCategory(models.Model):
    category_name = models.CharField(primary_key=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'courses_category'

    def __str__(self) -> str:
        return self.category_name



class CourseCoverMainTopic(models.Model):
    topic_title = models.CharField(primary_key=True, max_length=200)
    course = models.ForeignKey('Courses', models.DO_NOTHING, db_column='course')
    time = models.DateTimeField()
    
    class Meta:
        managed = False
        db_table = 'course-cover-main-topic'

    
    def __str__(self) -> str:
        return self.topic_title

class CourseCoverSubTopic(models.Model):
    sub_topic_title = models.CharField(primary_key=True, max_length=300)
    main_topic_title = models.ForeignKey(CourseCoverMainTopic, models.DO_NOTHING, db_column='main_topic_title')
    course = models.ForeignKey('Courses', models.DO_NOTHING, db_column='course')

    class Meta:
        managed = False
        db_table = 'course-cover-sub-topic'
    def __str__(self) -> str:
        return self.sub_topic_title


class CareerOpportunities(models.Model):
    career_opportunity = models.CharField(db_column='career-opportunity', primary_key=True, max_length=255)  # Field renamed to remove unsuitable characters.
    course = models.ForeignKey('Courses', models.DO_NOTHING, db_column='course')

    class Meta:
        managed = False
        db_table = 'career-opportunities'
    
    def __str__(self) -> str:
        return self.career_opportunity

class TrendingCourses(models.Model):
    course_name = models.OneToOneField(Courses, models.DO_NOTHING, db_column='course_name', primary_key=True)

    class Meta:
        managed = False
        db_table = 'trending_courses'
    

class Event(models.Model):
    event_name = models.CharField(primary_key=True, max_length=255)
    event_description = models.CharField(max_length=300)
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    event_venue = models.CharField(max_length=255)
    event_link = models.TextField() 
    event_date = models.DateField()



    class Meta:
        managed = False
        db_table = 'event'
    
    def __str__(self) -> str:
        return self.event_name


class Blogs(models.Model):
    blog_title = models.CharField(primary_key=True,max_length=255)
    blog_description = models.CharField(max_length=255)
    blog_content = models.TextField()
    blog_author = models.CharField(max_length=255)
    blog_date = models.DateField()
    blog_image = models.ImageField(upload_to='images/')


    class Meta:
        managed = False
        db_table = 'blogs'
    
    def __str__(self) -> str:
        return self.blog_title

class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    position = models.CharField(max_length=100, blank=True, null=True)
    link = models.TextField()

    class Meta:
        managed = False
        db_table = 'review'

    def __str__(self) -> str:
        return self.name

class BatchBanner(models.Model):
    batch_image = models.ImageField(upload_to='images/',db_column='batch-image')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'batch-banner'
    def __str__(self) -> str:
        return self.batch_image