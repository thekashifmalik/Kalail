from blog.models import Comment
from django.contrib.auth.models import User
import pickle
import sys
import kalail.settings as settings
from boto.s3.connection import S3Connection
from boto.s3.key import Key

def run():
	print 'STARTING SCRIPT "save_comment_user_ids.py"'

	all_comments = Comment.objects.all().order_by('created_on')
	user_ids = []
	number_of_comments = all_comments.count()

	print str(number_of_comments) + " COMMENTS DETECTED"

	print "COLLECTING USER IDS"
	for comment in all_comments:
		user_name = comment.author
		if user_name == "Anonymous":
			user = None
		else:
			try:
				user = User.objects.get(first_name=user_name)
				user = user.id
			except User.DoesNotExist:
				user = None
			except User.MultipleObjectsReturned:
				user = User.objects.filter(first_name=user_name)[0].id

		user_ids.append(user)
		sys.stdout.write(".")

	print "DONE"

	print "UPLOADING"

	s3_connection = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
	s3_bucket = s3_connection.create_bucket(settings.AWS_TEMP_STORAGE_BUCKET_NAME)
	users_file = Key(s3_bucket)
	users_file.key = "user_ids.pickle"
	user_ids_string = pickle.dumps(user_ids)
	users_file.set_contents_from_string(user_ids_string)

	print "DONE"

	print "FIN"