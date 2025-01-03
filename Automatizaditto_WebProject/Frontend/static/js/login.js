$(document).ready(function(){

    $('#loginForm').on('submit', function(form){
        form.preventDefault();

        var formData = {
            user_email: $('#user_email').val(),
            user_password: $('#user_password').val()
        };

        $.ajax({
            type: 'POST',
            url: '/login',
            data: formData,
            success: function(response){
                window.location.href = response.redirect_url;
            },
            error: function(xhr){
                if(xhr.status === 404){
                    var inputErrors = xhr.responseJSON;
                    console.log(inputErrors);

                    if(inputErrors.message){
                        $('#userAuthFail').text(inputErrors.message)
                    }
                }
            }
        });

    });
});