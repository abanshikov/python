# --------------- forms.py -------------------------
from django import forms

# здесь объявляйте класс формы
class CommentForm:
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    agree froms.BooleanField()
    content = forms.CharField(widget=forms.Textarea)

# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import CommentForm

# здесь объявляйте функцию представления
def comment_add(request):
    if request.method = "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            return form
    else:
        form = CommentForm()

    return render(request, 'user/comment_add.html', {'form': form})
