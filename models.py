from django.db import models


class Subject(models.Model):
    """A subject or course, e.g. 'Maths' or 'History'."""

    name = models.CharField(max_length=100)

    def __str__(self):
        # This is what shows up in the admin site and in dropdowns.
        return self.name


class Task(models.Model):
    """A single study task, like a homework or a chapter to revise."""

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,   # if a subject is deleted, delete its tasks too
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # set once, when created

    class Meta:
        ordering = ["due_date"]  # show the soonest deadline first

    def __str__(self):
        return self.title
