from background_task.models import Task, CompletedTask
from django.utils import timezone

def get_process_status(count):
    now = timezone.now()

    if count == 10:
        pending_tasks = Task.objects.filter(run_at__gt=now)
        count = count + 1
    elif count == 11:
        running_tasks = Task.objects.filter(locked_at__gte=now) 
        count = count + 1
    else:
        completed_tasks = CompletedTask.objects.all()

    print(completed_tasks, running_tasks, pending_tasks)
    return process_status

