from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
   (r'^i18n/', include('django.conf.urls.i18n')),
   # url(r'^blog/$', 'landing_page.views.blog', name='blog'),
   # url(r'^blog/articles$', 'landing_page.views.articles', name='articles'),
   (r'^blog/', include('blog.urls')),
   (r'^ckeditor/', include('ckeditor.urls')),

   url(r'^admin/', include(admin.site.urls)),
   (r'^grappelli/', include('grappelli.urls')),

)

urlpatterns += i18n_patterns('',
    # Examples:
    url(r'^$', 'landing_page.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)