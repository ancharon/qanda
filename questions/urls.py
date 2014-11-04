from django.conf.urls import patterns, url, include
from questions import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)