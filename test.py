class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
