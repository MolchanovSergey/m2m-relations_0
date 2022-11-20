from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Topic, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_form_exist = False
        for form in self.forms:
            if form.cleaned_data.get('is_main_topic'):
                if not main_form_exist:
                    main_form_exist = True
                else:
                    raise ValidationError('Может быть только одна главная тема')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass



