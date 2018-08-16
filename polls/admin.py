from django.contrib import admin

from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['date_published', 'text']
    fieldsets = [
        (None, {'fields': ['text']}),
        # ('Date Information', {'fields': ['date_published']}),
        ('Date Information', {'fields': ['date_published'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # Admin page uses str() by default.
    # A tuple of field names to display, as columns,
    # on the change list page for the object:
    list_display = ('text', 'date_published', 'was_published_recently')

    # Add a filter by date_published menu to the admin page.
    list_filter = ['date_published']

    # Adds a search box to the admin page
    search_fields = ['text']

# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)