from django.shortcuts import render, get_object_or_404, redirect
from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


# T a s k   C R U D
def task_list(request):
    tasks = Task.objects.all().order_by("is_done", "-created")
    return render(request, "todo/task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:task_list")
    else:
        form = TaskForm()
    return render(request, "todo/task_form.html", {"form": form, "title": "Add Task"})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("todo:task-list")
    else:
        form = TaskForm(instance=task)
    return render(request, "todo/task_form.html", {"form": form, "title": "Edit"})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("todo:task-list")
    return render(request, "todo/task_confirm_delete.html", {"task": task})


def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:task-list")


# T A G  C R U D
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "todo/tag_list.html", {"tags": tags})


def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:tag-list")
    else:
        form = TagForm()
    return render(request, "todo/tag_form.html", {"form": form})


def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("todo:tag-list")
    else:
        form = TagForm(instance=tag)
    return render(request, "todo/tag_form.html", {"form": form})


def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        return redirect("todo:tag-list")
    return render(request, "todo/tag_confirm_delete.html", {"tag": tag})
