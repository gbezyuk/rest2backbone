from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from sample_app.resources import AuthorView, BookView, PublisherView
from rest2backbone.resources import IndexedRouter

admin.autodiscover()

router = IndexedRouter(trailing_slash=False)
router.register('author', AuthorView)
router.register('book', BookView)
router.register('publisher', PublisherView)

from rest2backbone.views import restApi
from rest2backbone.forms import FormFactory

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'rest2backbone.views.home', name='home'),
    # url(r'^rest2backbone/', include('rest2backbone.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^/?$', TemplateView.as_view(template_name='sample/app.html'), {'forms': FormFactory(router)}),
    url(r'^js-locale/(?P<packages>\S+?)/?$', 'django.views.i18n.javascript_catalog'),
    url(r'^js-restAPI/?$', restApi.as_view(), {'router': router, 'url_prefix': '/api'}, name='rest-api'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
