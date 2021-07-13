from blog.models import Post
from django import template
from django.db.models import Count
register = template.Library()

@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_post.html')
def show_latest_post():
    latest_post = Post.objects.order_by('-publish')[:3]
    return {'latest_post':latest_post}

@register.simple_tag
def get_most_commented_post():
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:3]
