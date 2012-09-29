
var saved_notepad_text = '';

function determine_submit_state()
{
	var text = document.getElementById('notepad_text').value;
	if (text != saved_notepad_text)
	{
		enable_save();
	}
	else
	{
		disable_save();
	}
}

function disable_save()
{
	var button = document.getElementById("notepad_submit");
	button.disabled = true;
	button.value = 'Saved';
}

function enable_save()
{
	var button = document.getElementById("notepad_submit");
	button.disabled = false;
	button.value = 'Save';

}

function update_notepad()
{
	var text = document.getElementById('notepad_text').value;
	var update_notepad_url = document.URL;

	prepare_ajax();

	request_data = {
		notepad_text: text,
	};
	
	$.post(update_notepad_url, request_data, update_notepad_callback);

	return false;
}

function update_notepad_callback(data)
{
	if (data == 'OK')
	{
		save_current_notepad();
	}
	else
	{
		alert('The server did not respond. Try again.');
	}
}

function save_current_notepad()
{
	saved_notepad_text = document.getElementById('notepad_text').value;
	determine_submit_state();
}

window.onload = save_current_notepad;