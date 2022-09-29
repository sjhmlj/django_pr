from django.shortcuts import render

from config.settings import BASE_DIR
from .models import myTodo


def index(request):

    dbcontents = myTodo.objects.all().order_by("completed", "-priority")

    context = {
        "dbcontents": dbcontents,
    }

    return render(request, "todo/index.html", context)


def create(request):
    return render(request, "todo/create.html")


def create2(request):

    content = request.GET.get("content")
    # print(type(content))
    priority = request.GET.get("priority")
    priority_default = "Choose..."
    ## 페이지 새로고침할 때 똑같은 게 입력되는 거 막기
    contents = myTodo.objects.all()
    contents_content = []
    for i in contents:
        contents_content.append(i.content)
    print(contents_content[0], contents_content[1])
    if content in contents_content:
        return render(request, "todo/create2.html")
    else:

        if content != None and priority != priority_default:
            priority = int(priority)
            is_complete = request.GET.get("is_complete")
            completed = 1 if is_complete == "on" else 0
            deadline = request.GET.get("deadline")
            # print(type(deadline), deadline)
            # # on/off
            # print(type(priority), priority)
            # print(type(is_complete), is_complete)
            # print(content)
            if deadline == "":
                deadline = None
            todo = myTodo.objects.create(
                content=content,
                priority=priority,
                completed=completed,
                deadline=deadline,
            )
            todo.save()
        dbcontents = myTodo.objects.all().order_by("completed", "-priority")

        context = {
            "dbcontents": dbcontents,
        }
        return render(request, "todo/index.html", context)


def delete(request, pk):
    items = myTodo.objects.all()
    id_list = []
    for i in items:
        id_list.append(i.id)
    if pk in id_list:
        item = myTodo.objects.get(id=pk)
        item.delete()
    dbcontents = myTodo.objects.all().order_by("completed", "-priority")

    context = {
        "dbcontents": dbcontents,
    }
    return render(request, "todo/index.html", context)


def update(request, pk):
    item = myTodo.objects.get(id=pk)
    print(type(item.content), item.content)
    print(type(item.deadline), item.deadline)
    print(str(item.deadline), item.deadline)
    context = {
        "item": item,
        "pk": pk,
        "deadline": str(item.deadline),
    }
    return render(request, "todo/update.html", context)


def update2(request, pk):

    fields = [
        "id",
        "content",
        "priority",
        "completed",
        "created_At",
        "deadline",
    ]

    item = myTodo.objects.get(id=pk)
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    priority = int(priority)
    is_complete = request.GET.get("is_complete")
    completed = True if is_complete == "on" else False
    deadline = request.GET.get("deadline")
    if deadline == "":
        deadline = None

    item.content = content
    item.priority = priority
    item.completed = completed
    item.deadline = deadline
    item.save()
    dbcontents = myTodo.objects.all().order_by("completed", "-priority")

    context = {
        "dbcontents": dbcontents,
    }
    return render(request, "todo/index.html", context)


def test(request):
    items = myTodo.objects.all()

    dbcontents = myTodo.objects.all().order_by("completed", "-priority")

    context = {
        "dbcontents": dbcontents,
    }
    return render(request, "todo/test.html", context)


# dbcontents = dbcontents.order_by("completed")

# True 5
# True 5
# True 5
# True 4
# False 4
# False 4
# False 4
# False 3
# True 1
# True 1
# True 1

# --- 여기서 .order_by("-completed") 하면

# False 4
# False 3
# False 4
# False 4
# True 1
# True 1
# True 1
# True 5
# True 5
# True 4
# True 5

# dbcontents = myTodo.objects.all().order_by("-priority", "-completed")
# dbcontents = myTodo.objects.all().order_by("completed", "-priority")


# for i in dbcontents:
#     print(i.id, i.priority, i.completed, i.created_at)

# dbcontents = myTodo.objects.all().order_by("-completed", "-priority")
