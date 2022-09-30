from todo.todo.models import myTodo_bt


Tdeadlineo.objects.create(content="실습 제출", priority=5, deadline="2022-09-27")

Todo.objects.order_by("id")

Todo.objects.order_by("-deadline")

Todo.objects.order_by("-priority")

a = Todo.objects.filter(priority=5)
a = a.order_by("id")

a = Todo.objects.filter(completed=True)
a = a.order_by("id")

a = len(Todo.objects.filter(priority=5))

Todo.objects.get(id=1)

Todo.objects.get(id=1).delete()


all = myTodo.objects.all()

for i in all:
    new = myTodo_bt()
    new.content = i.content
    new.priority = i.priority
    new.deadline = i.deadline
    new.created_at = i.created_at
    # completed 빼먹었다.
    new.save()
