from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from checker.forms import FileAddAndUpdateForm
from checker.models import File, Logs, FileStatus


class FilesListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'checker/files_list.html'

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)


class AddFileView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = FileAddAndUpdateForm
    template_name = 'checker/add_file.html'
    success_url = reverse_lazy('files_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = self.request.user
            file.save()

        return redirect(self.success_url)


class DetailFileView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    template_name = 'checker/detail_file.html'

    def get_object(self, *args, **kwargs):
        try:
            return Logs.objects.get(file_id=self.kwargs['pk'])
        except:
            return None


class UpdateFileView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = File
    form_class = FileAddAndUpdateForm
    template_name = 'checker/update_file.html'
    success_url = reverse_lazy('files_list')

    def post(self, request, *args, **kwargs):
        file = File.objects.get(id=self.kwargs['pk'])
        file.file.delete()
        super().post(request, *args, **kwargs)

        if self.form_valid:
            self.object.status = FileStatus.UPDATED
            self.object.save()

        return redirect(self.success_url)


class DeleteFileView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = File
    template_name = 'checker/delete_file.html'
    success_url = reverse_lazy('files_list')
