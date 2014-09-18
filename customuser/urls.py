from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplebbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'customuser.views.index'),
    )

