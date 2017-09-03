from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "index.html"

    # def get_context_data(self, kwargs):
    #     context = super(DisplayTaskView, self).get_context_data(kwargs)
    #     context['task'] = Task.objects.get(pk=self.kwargs.get('task_id', None))
    #     return context


class ContactTemplateView(TemplateView):
    template_name = "contact.html"