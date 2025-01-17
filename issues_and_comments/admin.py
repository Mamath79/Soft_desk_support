from django.contrib import admin
from issues_and_comments.models import Issue, Comment

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'author_user', 'assigned_contributor', 'priority', 'status', 'date_created')
    search_fields = ('title', 'author_user__username', 'assigned_contributor__username')
    list_filter = ('priority', 'tag', 'status', 'date_created')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'issue', 'author_user')
    search_fields = ('content', 'issue', 'author_user')