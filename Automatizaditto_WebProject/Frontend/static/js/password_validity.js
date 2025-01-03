$(document).ready(function(){
    $('#updatePass').on('click', function(sendform){
        var newpass = $('#updateNewPass').val();

        var error = [];

        if (!/[A-Z]/.test(newpass)){
            error.push("La contraseña debe contener al menos una letra mayúscula");
            sendform.preventDefault();
            $('#passwordError').html(error.join('<br>'));
        } else{
            if(!/\d/.test(newpass)){
                error.push("La contraseña debe contener al menos un número");
                sendform.preventDefault();
                $('#passwordError').html(error.join('<br>'));
            } else{
                if(!/[\W_]/.test(newpass)){
                    error.push("La contraseña debe contener al menos un caracter especial");
                    sendform.preventDefault();
                    $('#passwordError').html(error.join('<br>'));
                } else{
                    if(newpass.length < 8){
                        error.push("La contraseña debe contener al menos 8 caracteres");
                        sendform.preventDefault();
                        $('#passwordError').html(error.join('<br>'));
                    }
                }
            }
        }
    });

    $('#update_user_password').on('hidden.bs.modal', function(){
        $('#updateUserPassForm')[0].reset();
        $('#passwordError').text('');
    });

    var closed_eye = document.createElement('i');
    closed_eye.className = 'icon-ojo-cruzado';
    var opened_eye = document.createElement('i');
    opened_eye.className = 'icon-ojo-abierto';


    $('.input-group-text').each(function(){
        $(this).append(closed_eye.cloneNode(true));
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