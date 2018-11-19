from django.conf.urls import include, url
from django.contrib import admin
from jira_app import views, exceptions
from django.conf import settings



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/', views.ProjectListView.as_view()),
    url(r'^issues/', views.CreatingIssue.as_view()),
    url(r'^subtask/', views.CreatingSubtask.as_view()),
    url(r'^subtask123/', views.CreatingSubtask123.as_view()),
    url(r'^sprint/', views.CreatingSprint.as_view()),
    url(r'^component/', views.CreatingComponent.as_view()),
    url(r'^comment/', views.AddingComment.as_view()),
    url(r'^s_issue/', views.GettingSprintIssues.as_view()),
    url(r'^raise/', views.CreatingRaise),
    url(r'^responsecheck/', views.ResponseCheck),

]


