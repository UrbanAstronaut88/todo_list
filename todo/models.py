from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks", blank=True)

    class Meta:
        ordering = ["is_done", "created"]
        #verbose_name = "Task"
        #verbose_name_plural = "Tasks"

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
