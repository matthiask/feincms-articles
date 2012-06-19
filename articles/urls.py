from __future__ import absolute_import

from .models import Article

urlpatterns = Article.get_urls()
