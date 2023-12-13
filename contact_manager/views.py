from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from .models import Contact
from .forms import ContactForm


class ContactListView(ListView):
    model = Contact
    template_name = 'contact_manager/contact_list.html'
    context_object_name = 'contacts'


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact_manager/contact_detail.html'
    context_object_name = 'contact'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        

        if not self.object.pk:
            return redirect('contact_manager:contact_list')

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_manager/contact_form.html'
    success_url = reverse_lazy('contact_manager:contact_list')
    
    def get_success_url(self):
        return reverse_lazy('contact_manager:contact_list')


class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_manager/contact_update.html'
    success_url = reverse_lazy('contact_manager:contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact_manager/contact_delete.html'
    success_url = reverse_lazy('contact_manager:contact_list')


