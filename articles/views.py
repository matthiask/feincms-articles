from __future__ import absolute_import

from django.views.generic import ListView

from feincms.module.mixins import ContentView

from .models import Article


class AppContentMixin(object):
    def render_to_response(self, context, **response_kwargs):
        """
        Returns the template tuple needed for FeinCMS App Content.
        """
        if hasattr(self.request, '_feincms_extra_context') and 'app_config' in self.request._feincms_extra_context:
            return (self.get_template_names(), context)

        return super(AppContentMixin, self).render_to_response(context, **response_kwargs)


class ArticleDetail(AppContentMixin, ContentView):
    model = Article

    def get_queryset(self):
        return Article.objects.active()


class ArticleList(AppContentMixin, ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.active()
