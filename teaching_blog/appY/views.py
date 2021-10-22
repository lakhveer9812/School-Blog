from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (FormView, TemplateView, DetailView, ListView, CreateView,UpdateView,DeleteView)

from .models import Standard, Subject, Lesson
from .forms import LessonForm
from django.urls import reverse_lazy

class StandardListView(ListView):
    model = Standard
    context_object_name = 'standards'
    template_name = 'standard_list_view.html'

class SubjectListView(DetailView):
    model = Standard
    context_object_name = 'standards'
    template_name = 'subject_list_view.html'

class LessonListView(DetailView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'lesson_list_view.html'

class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'lesson_detail_view.html'

class LessonCreateView(CreateView):
    form_class = LessonForm
    context_object_name = 'subject'
    model = Subject
    template_name = 'lesson_create.html'


    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('appY:lesson_list', kwargs={'standard': standard.slug,
                                                        'slug':self.object.slug})
    
    def form_valid(self,form,*args, **kwargs):
        self.object = self.get_object()
        fm = form.svae(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.objects.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())                                                    