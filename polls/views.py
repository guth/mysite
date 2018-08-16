from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question

def indexOld(request):
    latest_question_list = Question.objects.order_by('-date_published')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ', '.join([q.text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detailsOld(request, question_id):
    # try:
    #     # Alternatively: id=question_id
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")
    # return HttpResponse("You're looking at question %s." % question_id)

    # There’s also a get_list_or_404() function, which works just
    # as get_object_or_404() – except using filter() instead of get().
    # It raises Http404 if the list is empty.
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/details.html', {'question': question})

def resultsOld(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions (not including
        those set to be published in the future)."""
        # return Question.objects.order_by('-date_published')[:5]
        return Question.objects.filter(
            date_published__lte=timezone.now()
            ).order_by('-date_published')[:5]

class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(date_published__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choice_id = request.POST['choice']
    try:
        selected_choice = question.choice_set.get(id=choice_id)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.vote_count += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))