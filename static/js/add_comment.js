function add_comment_script(comment)
{
	// var new_comment = "<li>
	// <p><em>{{comment.text}}</em></p>
	// <p><strong>-{{comment.author}}</strong> - <em>({{comment.created_on|date:"SHORT_DATETIME_FORMAT"}})</em></p>
	// </li>";
	var new_comment = "<li><p><em>" + comment.text + "</em></p><p><strong>-" + comment.author + "</strong> - <em>(" + comment.created_on + ".)</em></p></li>";
	$('#comments').append(new_comment);
	$('#new_comment_text').val("");
}