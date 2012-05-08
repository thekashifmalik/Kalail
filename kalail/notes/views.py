# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from notes.models import Notepad
from django.contrib.auth.models import User

@login_required
def index(request):
	if request.method == 'POST':
		pass
	if request.user.notepad_set.all.count() == 0:
		new_notepad = Notepad(body = "", author = request.user)
		new_notepad.save()
	return render_to_response('notes/index.html', {"notepad" : }, context_instance=RequestContext(request))
	return render_to_response('blog/show_post.html', {'post': post, 'comments': comments}, context_instance=RequestContext(request))
