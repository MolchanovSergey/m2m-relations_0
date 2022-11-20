from django.views.generic import ListView

from articles.models import Article, Scope


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        articles = []
        for element in context['object_list']:
            scopes = []
            for scope in Scope.objects.filter(article=element):
                scopes.append(scope)

            scopes.sort(key=lambda scope: str(scope.topic))
            scopes.sort(key=lambda scope: not scope.is_main_topic)

            articles.append({
                'title': element.title,
                'text': element.text,
                'image': element.image,
                'scopes': scopes
            })
        context['articles'] = articles
        return context

# def articles_list(request):
#     template = 'articles/news.html'
#     context = {}
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     ordering = '-published_at'
#
#     return render(request, template, context)
