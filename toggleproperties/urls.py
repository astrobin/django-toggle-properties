from django.conf.urls import url
from views import *

urlpatterns = (
    url(r'^add$', ajax_add_toggleproperty, name="toggleproperty_ajax_add"),
    url(r'^remove$', ajax_remove_toggleproperty, name="toggleproperty_ajax_remove"),
)
