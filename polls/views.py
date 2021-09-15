from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse

from django.http import HttpResponseRedirect

from django.template import loader

from .models import Choice, Question, Deepthought

from django.http import Http404

from django.urls import reverse

from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class ThoughtView(generic.ListView):
    model = Deepthought
    template_name = 'polls/thought.html'

class ListView(generic.ListView):
    model = Deepthought
    context_object_name = 'thoughts_list'
    template_name = 'polls/list.html'
    def get_queryset(self):
        return Deepthought.objects.all()

def add(request):

    t = Deepthought(title_text= request.POST["title"],thought_text=request.POST["thought"])
    t.save()
    return HttpResponseRedirect(reverse('polls:list'))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        
        
        
        
"""
        
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""