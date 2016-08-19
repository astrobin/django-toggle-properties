from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns("",
    url(r'^add$', ajax_add_toggleproperty, name="toggleproperty_ajax_add"),
    url(r'^remove$', ajax_remove_toggleproperty, name="toggleproperty_ajax_remove"),
)
