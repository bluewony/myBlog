from django.conf.urls import patterns, include, url
from blog.views import PostView, Main, ArchiveMonth

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/'                          , include(admin.site.urls)),
    url(r'^post/(?P<dpk>\d+)/$'             , PostView.as_view(), {}, 'post'),
    url(r'^archive_month/(\d+)/(\d+)/$'    , ArchiveMonth.as_view(), {}, 'archive_month'),
    url(r'^$'                               , Main.as_view(), {}, 'main'),
    # (r"^delete_comment/(\d+)/$"       , "delete_comment", {}, "delete_comment"),
)
