from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs"
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Save method for Blog."""
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blogapp:details", kwargs={"slug": self.slug})


class Comment(models.Model):
    """Model definition for Comment."""

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()

    class Meta:
        """Meta definition for Comment."""

        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        """Unicode representation of Comment."""
        return f"Comment by {self.user.username} - {self.blog.title}"
