$(document).ready(function(){

    $('#updateUserPassForm').on('submit', function(e) {
        e.preventDefault();

        var formData = {
            updateCurrentPass: $('#updateCurrentPass').val(),
            updateNewPass: $('#updateNewPass').val(),
            updateNewPassConfirm: $('#updateNewPassConfirm').val()
        };

        $.ajax({
            type: 'POST',
            url: '/set_new_password',
            data: formData,
            success: function(response) {
                window.location.href = response.redirect_url;  // Redirecciona si es necesario
            },
            error: function(xhr) {
                if (xhr.status === 404) {
                    var errorMessage = xhr.responseJSON.message;
                    $('#currentPassError').text(errorMessage);
                } else {
                    $('#currentPassError').text('Error desconocido, por favor intente más tarde.');
                }
            }
        });
    });

    $('#updatePass').on('click', function(setpassform){
        var currentpass = $('#updateCurrentPass').val();
        var setpass = $('#updateNewPass').val();

        var error = [];

        if (setpass === currentpass){
            error.push("La nueva contraseña y la contraseña actual no pueden ser iguales");
            setpassform.preventDefault();
            $('#passwordError').html(error.join('<br>'));
        }

        if (!/[A-Z]/.test(setpass)){
            error.push("La contraseña debe contener al menos una letra mayúscula");
            setpassform.preventDefault();
            $('#passwordError').html(error.join('<br>'));
        } else{
            if(!/\d/.test(setpass)){
                error.push("La contraseña debe contener al menos un número");
                setpassform.preventDefault();
                $('#passwordError').html(error.join('<br>'));
            } else{
                if(!/[\W_]/.test(setpass)){
                    error.push("La contraseña debe contener al menos un caracter especial");
                    setpassform.preventDefault();
                    $('#passwordError').html(error.join('<br>'));
                } else{
                    if(setpass.length < 8){
                        error.push("La contraseña debe contener al menos 8 caracteres");
                        setpassform.preventDefault();
                        $('#passwordError').html(error.join('<br>'));
                    }
                }
            }
        }
    });

    $('#updateNewPass').on('input', function(){
        $('#passwordError').html('');
    });

    $('#updateCurrentPass').on('input', function(){
        $('#currentPassError').html('');
    })

    $('#setNewPass').on('hidden.bs.modal', function(){
        $('#updateUserPassForm')[0].reset();
        $('#passwordError').text('');
        $('#currentPassError').text('');
    });

    var closed_eye = document.createElement('i');
    closed_eye.className = 'icon-ojo-cruzado';
    var opened_eye = document.createElement('i');
    opened_eye.className = 'icon-ojo-abierto';


    $('.input-group-text').each(function(){
        $(this).append(closed_eye.cloneNode(true));
    });


    var showcurrentpass = $('#updateCurrentPass');
    $('#showCurrentPass').on('mousedown', function(){
        showcurrentpass.attr('type', 'text');
        $(this).find('i').replaceWith(opened_eye.cloneNode(true));
    });
    $('#showCurrentPass').on('mouseup mouseleave', function(){
        showcurrentpass.attr('type', 'password');
        $(this).find('i').replaceWith(closed_eye.cloneNode(true));
    });

    var shownewpass = $('#updateNewPass');
    $('#showNewPass').on('mousedown', function(){
        shownewpass.attr('type', 'text');
        $(this).find('i').replaceWith(opened_eye.cloneNode(true));
    });
    $('#showNewPass').on('mouseup mouseleave', function(){
        shownewpass.attr('type', 'password');
        $(this).find('i').replaceWith(closed_eye.cloneNode(true));
    });


    var shownewpassconfirm = $('#updateNewPassConfirm');
    $('#showNewPassConfirm').on('mousedown', function(){
        shownewpassconfirm.attr('type', 'text');
        $(this).find('i').replaceWith(opened_eye.cloneNode(true));
    });
    $('#showNewPassConfirm').on('mouseup mouseleave', function(){
        shownewpassconfirm.attr('type', 'password');
        $(this).find('i').replaceWith(closed_eye.cloneNode(true));
    });

});