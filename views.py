"""
Views for the study planner.

These are plain function-based views: each one takes a request and returns
a response. This is the simplest style Django offers, which is why this
beginner project uses it instead of class-based views.
"""
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import SubjectForm, TaskForm
from .models import Subject, Task


def task_list(request):
    """Home page: show every task, soonest due date first."""
    tasks = Task.objects.all()  # Meta.ordering in models.py sorts these
    context = {"tasks": tasks, "today": timezone.localdate()}
    return render(request, "studyplanner/task_list.html", context)


def add_task(request):
    if not Subject.objects.exists():
        messages.info(request, "Add a subject first, then you can add tasks to it.")
        return redirect("add_subject")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added.")
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "studyplanner/task_form.html", {"form": form, "title": "Add task"})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated.")
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(request, "studyplanner/task_form.html", {"form": form, "title": "Edit task"})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted.")
        return redirect("task_list")

    # GET: show a confirmation page first
    return render(request, "studyplanner/confirm_delete.html", {"object": task})


def toggle_task(request, task_id):
    """Flip a task between done and not done."""
    task = get_object_or_404(Task, id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect("task_list")


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, "studyplanner/subject_list.html", {"subjects": subjects})


def add_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject added.")
            return redirect("subject_list")
    else:
        form = SubjectForm()

    return render(request, "studyplanner/subject_form.html", {"form": form})


def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)

    if request.method == "POST":
        subject.delete()
        messages.success(request, "Subject deleted (its tasks were deleted too).")
        return redirect("subject_list")

    return render(request, "studyplanner/confirm_delete.html", {"object": subject})
