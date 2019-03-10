from django.conf.urls import url,include
from HotelApp import views
from HotelApp.views import hotelSearch
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

csrf_exempt(views.HotelsViewSet.as_view)
csrf_exempt(views.HotelList.as_view())
router = routers.DefaultRouter()
router.register(r'hotelView' , views.HotelsViewSet)


app_name = 'HotelApp'
urlpatterns = [
     url(r'^$', views.hotelindex, name='hotelindex'),
     url(r'^dashboard/$', views.userDash, name='userDash'),
     url(r'^hotels/(?P<pk>[0-9]+)/$', views.hoteldetails, name='hoteldetails'),
     url(r'^search$', hotelSearch.as_view(), name='hotelsearch'),
     url(r'^(?P<id>[0-9]+)/reviews/create$', views.reviewCreateView.as_view(), name='createreview'),
     url(r'^(?P<pk>[0-9]+)/reviews/edit$', views.reviewUpdateView.as_view(), name='editreview'),
     url(r'^(?P<pk>[0-9]+)/reviews/delete$', views.reviewDeleteView.as_view(), name='deletereview'),
     url(r'^partner/apply$', views.partnerCreateView.as_view(), name='newproposal'),
     url(r'^api/', include(router.urls)),
     url(r'^rest-auth/', include('rest_auth.urls')),
     url(r'^getHotel/', views.HotelList.as_view()),

]
