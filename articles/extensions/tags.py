from django.conf.urls.defaults import patterns, url
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from feincms import extensions


try:
    from taggit.managers import TaggableManager
except ImportError:
   raise ImproperlyConfigured(
        'You need to install django-taggit to use the tags extension')


def get_urlpatterns(cls):
    return cls.get_urlpatterns_orig() + patterns('taggit.views',
        url(r'^tags/(?P<slug>[^/]+)/$', 'tagged_object_list', {
            'queryset': cls.objects.active,
            }, name="article_tagged_list"),
        )


class Extension(extensions.Extension):
    def handle_model(self):
        self.model.add_to_class('tags',
            TaggableManager(verbose_name=_('tags'), blank=True))

        self.model.get_urlpatterns_orig = self.model.get_urlpatterns
        self.model.get_urlpatterns = classmethod(get_urlpatterns)

    def handle_modeladmin(self, modeladmin):
        modeladmin.add_extension_options('tags')
