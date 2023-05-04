$(document).ready(function() {
	$("#staff_order_details").load('/staff_order_details/')
    profile_detail_display()
	product_detail_display()
	
	function profile_detail_display() {
		$("#profile_details").load('/profile_details/')
	}
	function product_detail_display() {
		$("#product_details").load('/product_details/')
	}

	$('#register-form').submit(function(event) {
		event.preventDefault();

		$('#register-btn').attr('disabled', true).text('Registering...');

		var formData = {
			'username': $('#username').val(),
			'email': $('#email').val(),
			'password1': $('#password1').val(),
			'password2': $('#password2').val(),
			'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
		};

		$.ajax({
			url: '/register/',
			type: 'POST',
			data: formData,
			success: function(response) {
				
				errorMessage = ''
				if (response.message == 'success') {
					errorMessage = response.status
					
					// window.location = response.url_To;
				}
				else {
					var errors = response.message;
                    for (var key in errors) {
						errorMessage = errors[key][0]
                        console.log(errors[key][0]); // display first error message for each field
                    }
					$('#register-btn').attr('disabled', false).html('Register');
				}
				$('#error-message').text(errorMessage);
			}
		});
	});

	$('.form').submit(function(event) {
		event.preventDefault();
		let $form = $(this)
		let $url = $form.attr('action')
		let $btn = $form.find('.submit_btn')
		let $warning = $form.find('.error-message')
		// $btn.attr('disabled', true).text('Processing...');
		$.ajax({
			url: $url,
			type: 'POST',
			data: new FormData(this),
			processData: false,
         	contentType: false,
			success: function(response) {
				setTimeout($("#profile_update_modal").modal("hide"),100)
				// profile_detail_display()
				console.log(response.message)
				errorMessage = ''
				if (response.message == 'success') {
					errorMessage = response.message
					window.location = response.url_to;
				}
				else {
					errorMessage = response.message;
                    // for (var key in errors) {
					// 	errorMessage = errors[key][0]
                    //     console.log(errors[key][0]); // display first error message for each field
                    // }
					// $btn.attr('disabled', false).html('Register');
				}
				$warning.text(errorMessage);
			}
		});
	});
});

$('.form-profile-update').submit(function(event) {
	event.preventDefault();
	let $form = $(this)
	let $url = $form.attr('action')
	let $btn = $form.find('.submit_btn')
	$btn.attr('disabled', true).text('Processing...');
	$.ajax({
		url: $url,
		type: 'POST',
		data: new FormData(this),
		processData: false,
		contentType: false,
		success: function(response) {
			$btn.attr('disabled', false).text('Update');
			if (response.message == 'success') {
				setTimeout($("#profile_update_modal").modal("hide"),100)
				$("#profile_details").load('/profile_details/')
			}
		}
	});
});
$('.product_form').submit(function(event) {
	event.preventDefault();
	let $form = $(this)
	let $url = $form.attr('action')
	let $btn = $form.find('.submit_btn')
	$btn.attr('disabled', true).text('Processing...');
	$.ajax({
		url: $url,
		type: 'POST',
		data: new FormData(this),
		processData: false,
		contentType: false,
		success: function(response) {
			console.log(response)
			$btn.attr('disabled', false).text('Add product');
			if (response.message == 'success') {

				// setTimeout($("#profile_update_modal").modal("hide"),100)
				$("#product_details").load('/product_details/')
			}
		}
	});
});


function get_product_data(id,name,category,quantity) {
	$('#product_edit_modal').modal('show')
	$('#pr_id').val(id)
	$('#pr_name').val(name)
	$('#pr_category').val(category)
	$('#pr_quantity').val(quantity)
}

function get_staff_data(id,username,email,phone,address) {
	$('#staff_details_modal').modal('show')
	$('#staff_username').html(username)
	$('#staff_email').html(email)
	$('#staff_phone').html(phone)
	$('#staff_address').html(address)
}

$('.product_update_form').submit(function(event) {
	event.preventDefault();
	let $form = $(this)
	let $url = $form.attr('action')
	let $btn = $form.find('.submit_btn')
	// $btn.attr('disabled', true).text('Processing...');
	$.ajax({
		url: $url,
		type: 'POST',
		data: new FormData(this),
		processData: false,
		contentType: false,
		success: function(response) {
			console.log(response)
			// $btn.attr('disabled', false).text('Update');
			if (response.message == 'success') {
				setTimeout($("#product_edit_modal").modal("hide"),100)
				$("#product_details").load('/product_details/')
			}
		}
	});
});

function get_product_id(id) {
	$('#product_delete_modal').modal('show')
	$('#delete_modal_btn').attr('data-id',id)
}
$('#delete_modal_btn').click(function() {
	
	$(this).attr('disabled', true).text('Processing...');
	
	$.ajax({
		url: `/product/${$(this).attr('data-id')}`,
		type: 'GET',
		processData: false,
		contentType: false,
		success: function(response) {
			console.log(response)
			
			if (response.message == 'success') {
				$('#delete_modal_btn').attr('disabled', false).html('Yes');
				setTimeout($("#product_delete_modal").modal("hide"),100)
				$("#product_details").load('/product_details/')
			}
		}
	});
});

$('.order_request_form').submit(function(event) {
	// alert('opo')
	// return
	event.preventDefault();
	let $form = $(this)
	let $url = $form.attr('action')
	let $btn = $form.find('.submit_btn')
	// $btn.attr('disabled', true).text('Processing...');
	$.ajax({
		url: $url,
		type: 'POST',
		data: new FormData(this),
		processData: false,
		contentType: false,
		success: function(response) {
			console.log(response)
			// $btn.attr('disabled', false).text('Update');
			if (response.message == 'success') {
				// setTimeout($("#product_edit_modal").modal("hide"),100)
				$("#staff_order_details").load('/staff_order_details/')
			}
		}
	});
});