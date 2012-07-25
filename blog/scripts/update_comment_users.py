from blog.models import Comment
from django.contrib.auth.models import User
import pickle
import sys
import kalail.settings as settings
from boto.s3.connection import S3Connection
from boto.s3.key import Key

def run():
	print 'STARTING SCRIPT "update_comment_users.py"'

	all_comments = Comment.objects.all().order_by('created_on')
	number_of_comments = all_comments.count()

	print str(number_of_comments) + " COMMENTS DETECTED"

	print "DOWNLOADING USER IDS"
	s3_connection = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
	s3_bucket = s3_connection.create_bucket(settings.AWS_TEMP_STORAGE_BUCKET_NAME)
	users_file = Key(s3_bucket)
	users_file.key = "user_ids.pickle"
	user_ids_string = users_file.get_contents_as_string()
	user_ids = pickle.loads(user_ids_string)

	print "DONE"

	number_of_user_ids = len(user_ids)

	print "COMPARING OBJECT LENGTH"

	if number_of_comments == number_of_user_ids:
		print "DONE"
		print "UPDATING COMMENT RECORDS"
		index = 0
		for comment in all_comments:
			user_id = user_ids[index]
			if user_id == None:
				user = None
			else:
				user = User.objects.get(id=user_id)
			comment.user = user
			comment.save()
			index += 1
			sys.stdout.write(".")

		print "DONE"
	else:
		print "OBJECT MISMATCH. ABORTING"

	print "FIN"