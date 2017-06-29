from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question, Photo



def index(request):
    photo_list = Photo.objects.order_by('-regression_error')[:50]
    context = {'photo_list': photo_list}
    return render(request, 'index.html', context)


def detail(request, photo_uid):
    try:
        photo = Photo.objects.get(uid=photo_uid)
    except Question.DoesNotExist:
        raise Http404("Photo does not exist")
    return render(request, 'detail.html', {'photo': photo})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('webapps:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


