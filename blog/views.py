from django.shortcuts import render
from django.utils import timezone
from .models import Post


def nazwa_metody_renderujacej_dany_widok(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})