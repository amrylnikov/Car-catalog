from django.shortcuts import render
from .models import Mark, Model
from car_app.scripts.update_catalog import update_autoru_catalog

def index(request):
    if request.method == 'POST':
        mark_id = request.POST.get('mark')
        print(f'type(mark_id): {type(int(mark_id))}')
        selected_mark = Mark.objects.get(pk=mark_id)
        models = Model.objects.filter(mark=selected_mark)
        marks = Mark.objects.all()
        return render(request, 'index.html', {'marks': marks, 'mark_id': int(mark_id), 'models': models})

    marks = Mark.objects.all()
    return render(request, 'index.html', {'marks': marks})

def update(request):
    if request.method == 'POST':
        update_autoru_catalog()

    marks = Mark.objects.all()
    return render(request, 'index.html', {'marks': marks})
