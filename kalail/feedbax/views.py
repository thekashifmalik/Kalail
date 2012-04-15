# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from feedbax.models import TestSystem, Feedback
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.core.mail import EmailMessage

@login_required
def index(request):
	systems = request.user.testsystem_set.all()
	return render_to_response('feedbax/index.html', {'systems': systems}, context_instance=RequestContext(request))

@login_required
def setup_feedback_system(request):
	if request.method == 'POST':
		new_name = request.POST['new_feedbax_name']
		new_site = "http://" + request.POST['new_comment_site']
		new_report_email = request.POST['new_feedbax_report_email']
		new_user = request.user
		new_feedbax_site = slugify(new_name)
		
		new_system = TestSystem(name=new_name, site=new_site, feedbax_site=new_feedbax_site, report_email=new_report_email)
		new_system.save()
		new_system.users.add(new_user)

		email_message = "Thank you for setting up your " + new_name + " Feedbax.\n\
		\n\
		Send in feedback to " + request.build_absolute_uri(reverse('feedbax.views.send_feedback', args=[new_feedbax_site])) + "\n\
		Feedback will automatically forwarded to " + new_report_email

		# Send email
		setup_email = EmailMessage('Setup Complete', email_message, to=[new_report_email, request.user.email])
		setup_email.send()
		
		return HttpResponseRedirect(reverse('feedbax.views.index'))
	return render_to_response('feedbax/setup_feedback_system.html', {}, context_instance=RequestContext(request))

@login_required
def show_system_feedback(request, feedbax_site):
	system = get_object_or_404(TestSystem, feedbax_site=feedbax_site)
	all_feedback = system.feedback_set.all().order_by('created_on')
	return render_to_response('feedbax/show_system_feedback.html', {'system': system, 'all_feedback': all_feedback}, context_instance=RequestContext(request))

@login_required
def send_feedback(request, feedbax_site):
	system = get_object_or_404(TestSystem, feedbax_site=feedbax_site)
	if request.method == 'POST':
		new_content = request.POST['new_feedback_content']
		new_user = request.user

		new_feedback = Feedback(content=new_content, system=system, user=new_user)
		new_feedback.save()
		
		# Send email
		email_message = "Feedbax report: Feedback recieved for " + system.name + "\n\
		\n\
		\"" + new_content + "\"\n\
		By: " + new_user.email + "\n\
		\n\
		Send in feedback to " + request.build_absolute_uri(reverse('feedbax.views.send_feedback', args=[system.feedbax_site])) + "\n\
		Feedback will automatically forwarded to " + system.report_email

		# Send email
		feedback_email = EmailMessage('Feedbax report: ' + system.name, email_message, to=[system.report_email])
		feedback_email.send()

		# Add user to feedback system
		if not new_user in system.users.all():
			system.users.add(new_user)

		return HttpResponseRedirect(reverse('feedbax.views.index'))
	return render_to_response('feedbax/send_feedback.html', {'system': system}, context_instance=RequestContext(request))