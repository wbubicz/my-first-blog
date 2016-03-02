from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def nazwa_metody_renderujacej_dany_widok(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def renderuj_widok_z_parametrem(request, pobrany_parametr):
	post = get_object_or_404(Post, id=pobrany_parametr)
	return render(request, 'blog/post_detail.html', {'post': post})