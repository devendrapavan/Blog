from usermanagement.models import  *

class Article(CustomModel):
    STATUS = (('CREATED','CREATED'),('APPROVED','APPROVED'),('REJECTED','REJECTED'))
    body = models.TextField()
    header = models.CharField(max_length=200)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='User')
    status = models.CharField(choices=STATUS, default='CREATED', max_length=20)

    def __str__(self):
        return self.header

class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, article_instance=None):
        qs = super(CommentManager, self).filter(article=article_instance)
        return qs

class Comments(CustomModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    comment_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_by')
    objects = CommentManager()

    class Meta:
        # sort comments in chronological order by default
        ordering = ('-createdAt',)
        verbose_name = 'comments'
        verbose_name_plural = 'comments'

    def __str__(self):
        return 'Comment by {}'.format(self.comment_by.username)

    def children(self):
        return Comments.objects.filter(parent=self)

    def timesince(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        from django.utils.timesince import timesince as timesince_
        return timesince_(self.createdAt, now)




