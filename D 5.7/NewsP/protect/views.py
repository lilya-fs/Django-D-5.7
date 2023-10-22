from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin # D5.6
from django.views.generic.edit import CreateView

# D5.4 class IndexView(LoginRequiredMixin, TemplateView):
# D5.4     template_name = 'protect/index.html'

# D5.5
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context




#class MyView(PermissionRequiredMixin, View):
        #  permission_required = ('<app>.<action>_<model>', '<app>.<action>_<model>')

class ForAuthor(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',
                           'news.edit_post', 'news.delete_post',)