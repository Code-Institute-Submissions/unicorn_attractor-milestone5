from django.conf.urls import url
from .views import all_bugs, create_or_edit_bug, bug_detail

urlpatterns = [
    url(r'^$', all_bugs, name='all_bugs'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug')
]