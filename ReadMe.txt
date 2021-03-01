======================================================================================
This is the ReadMe file for Activity Challenge given by Full Throttle Labs.
======================================================================================
Author: kummari naresh
Place: hyderabad , India
Date:   March 01, 2021
Version: v1.0
======================================================================================
Software Requirements:
1. Python3
2. Django 3.0
Testing Software:
1. Postman 7.13.0
Database:
1. SQLite (pre-installed with Django)
======================================================================================
Folder Structure: 
Project name: Activity
Folder name:  activitylog
App name:     1. log(contains models for the activity period details) 
              2. user(contains models for the user details)
App structure:
	      1. log-
                 1. models.py: contains model for the activity logs details
                 2. serializers.py: conatins serializers for the validation 
                     of data
                 3. views.py: contains business logic for the execution of 
		     program
                 4. urls.py: contains urls for APIViews 
	      2. user-
                 1. models.py: contains model for the logs details
                 2. serializers.py: conatins serializers for the validation 
                     of data
                 3. views.py: contains business logic for the execution of 
		     program
                 4. urls.py: contains urls for APIViews 
=====================================================================================
Description:
A. Models:
1. UserMan(The name has been changed from User to avoid contradictory issues 
   with the already present User Model)
   Fields:
         1. s_no: Primary Key
	 2. user_id: Alphanumeric Key
	 3. name: The real name of the person
	 4. time_zone: The time_zone that person belongs to.
2. Log(This contains details for the start_time, end_time pertaining to a 
   particular user login period.)
   Fields: 
         1. s_num: Primary Key
	 2. s_no: Foreign Key to UserMan Table
	 3. start_time: the start-time of the login session
	 4. end_time: the end_time of the login session.
B. Serializers:
1. user.serializer:
	 1. UserSerializer: a ModelSerializer on model UserMan and fields 
		s_no, user_id, name, time_zone
2. log.serializer:
         1. LogSerializer: a ModelSerializer on model Log and fields s_num,
		s_no, start_time, end_time
	 2. LogTimeSerializer: a ModelSerializer on model Log and fields 
		start_time, end_time
3. user.serializer:
	 2. UserLogSerializer: a ModelSerializer on model UserMan and fields 
		nested over on LogTimeSerializer which includes user_id, name,
		time_zone, activity_periods(start_time, end_time)
C.Views:
1. user.views:
	 1. UsersView: an APIView on UserSerializer with post and get methods
		to post data about a user and get details of all users
2. log.views:
         1. LogView: an ApiView on LogSerializer with post and get method to 
		post data about the activity_periods of a particluar user
	 2. LogUpdateView: an ApiView on LogSerializer with post method to 
		update the end_time for a particluar session marked by the 
		s_num through the slug-url.
3. user.views:
	 2. MembersActivity: an ApiView on UserLogSerializer with get method 
		to retrieve all the details as desired in JSON.
D. Urls:
1. user.urls:
	 1. 'all_users/': on UsersView to post and get the user details
2. log.urls:
	 1.'all_logs/': on LogView to post and get the records for the 
		activity_periods on users.
	 2. 'log_end_time/<slug:s_num>/: on LogUpdateView to post the end_time
		pertaining to a particual login session. 
3. user.urls:
	 2. 'members_record/': on MembersActivity to get the final JSON structure 
		details  
====================================================================================
Changes in the settings file before testing on Postman:
1. Comment out 'django.middleware.csrf.CsrfViewMiddleware' in the MiddleWare Section
2. Put False on USE_L10N and USE_TZ settings
3. Give the following settings on DATETIME_FORMAT = '%b %d %Y %H:%M'
====================================================================================
Changes in the app.urls before testing on Postman:
1. Comment out path('admin/', admin.site.urls),
2. Add the following in url_patterns:
    path('user/', include('user.urls')),
    path('log/', include('log.urls')),
====================================================================================
Steps to be followed:
1. Enter the details for the Users first.
2. Enter the details of the login session.
3. Update the details for the end_time of the login session.
4. View the Members Activity at the end.
====================================================================================
************************************************************************************
====================================================================================
