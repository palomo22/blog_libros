from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Page
from .forms import CommentForm, PageForm
from django.db.models import Q

# Vista de lista de publicaciones (ordenadas por fecha descendente)
class PageListView(ListView):
    model = Page
    template_name = 'pages/home.html'
    context_object_name = 'pages'
    paginate_by = 5
    ordering = ['-published_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset

# Vista de detalle con comentarios
class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            messages.error(request, "Debés iniciar sesión para comentar.")
            return redirect('login')

        if form.is_valid():
            comment = form.save(commit=False)
            comment.page = self.object
            comment.author = request.user
            comment.save()
            messages.success(request, "Comentario publicado con éxito.")
            return redirect('page_detail', pk=self.object.pk)

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

# Vista para "Acerca de mí"
def about_view(request):
    return render(request, 'pages/about.html')

# Vista para crear publicaciones (solo logueados)
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "La publicación fue creada con éxito.")
        return response

# Vista para editar publicaciones (solo logueados)
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "La publicación fue actualizada con éxito.")
        return response
#
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from .models import Comment

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # Verificar que el usuario sea el autor del comentario
    if comment.author != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")

    if request.method == "POST":
        page_pk = comment.page.pk
        comment.delete()
        messages.success(request, "Comentario eliminado con éxito.")
        return redirect('page_detail', pk=page_pk)

    # Opcional: Confirmación antes de borrar (puedes usar un template)
    return render(request, 'pages/confirm_delete_comment.html', {'comment': comment})
#
@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    # Solo el autor puede editar su comentario
    if comment.author != request.user:
        messages.error(request, "No tenés permiso para editar este comentario.")
        return redirect('page_detail', pk=comment.page.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentario editado con éxito.")
            return redirect('page_detail', pk=comment.page.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'pages/edit_comment.html', {
        'form': form,
        'comment': comment
    })
