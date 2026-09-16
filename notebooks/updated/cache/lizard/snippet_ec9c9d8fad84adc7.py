def blog_categories(*args):
    posts = BlogPost.objects.published()
    categories = BlogCategory.objects.filter(blogposts__in=posts)
    return list(categories.annotate(post_count=Count('blogposts')))