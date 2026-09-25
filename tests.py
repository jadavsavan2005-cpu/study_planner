"""
A few basic tests. Run them with:  python manage.py test
"""
from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Subject, Task


class ModelTests(TestCase):
    def test_task_string_is_its_title(self):
        subject = Subject.objects.create(name="Maths")
        task = Task.objects.create(subject=subject, title="Finish worksheet", due_date=date.today())
        self.assertEqual(str(task), "Finish worksheet")


class ViewTests(TestCase):
    def setUp(self):
        self.subject = Subject.objects.create(name="Maths")
        self.task = Task.objects.create(subject=self.subject, title="Finish worksheet", due_date=date.today())

    def test_task_list_page_loads(self):
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Finish worksheet")

    def test_toggle_marks_task_done(self):
        self.client.get(reverse("toggle_task", args=[self.task.id]))
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)

    def test_delete_subject_also_deletes_its_tasks(self):
        self.client.post(reverse("delete_subject", args=[self.subject.id]))
        self.assertEqual(Task.objects.count(), 0)
