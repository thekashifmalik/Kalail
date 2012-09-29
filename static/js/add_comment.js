
function append_new_comment(data)
{
	if ('user' in data)
	{
		var username = data.user;
	}
	else
	{
		var username = 'Anonymous';
	}
	var new_comment = "<li><p><em>\"" + data.comment + "\"</em></p><p>-" + username + "</p><br></li>";
	$('#comments').append(new_comment);
	$('#new_comment_text').val("");
}

function submit_new_comment()
{
	// Validate comment
	var comment = document.forms['new_comment_form']['new_comment_text'].value;
	if (comment==null || comment=='')
	{
		alert('The text field is empty!');
		return false;
	}

	var captcha = document.forms['new_comment_form']['new_comment_captcha'].value;
	if (captcha!='red')
	{
		alert('The captcha is incorrect! Use the value "red"');
		return false;
	}

	// Submit new comment
	var add_comment_url = document.URL + 'add_comment/';

	$.ajaxSetup({
		crossDomain: false, // obviates need for sameOrigin test
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type)) {
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		}
	});

	request_data = {
		comment: comment,
	};
	
	$.post(add_comment_url, request_data, append_new_comment);

	return false
}