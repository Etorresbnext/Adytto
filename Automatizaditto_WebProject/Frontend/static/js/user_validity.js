$(document).ready(function(){
    $('#insert_user').on('click', function(sendform){
        var insertusername = $('#name').val();
        var insertuserlastname = $('#lastname').val();
        var insertuseremail = $('#email').val();
        var insertuserpass = $('#password').val();

        var errorname = [];
        var errorlastname = [];
        var erroremail = [];
        var errorpass = [];

        if(!/^(?!\s*$).+/.test(insertusername)){
            errorname.push("Debe capturar un Nombre para el usuario")
            sendform.preventDefault();
            $('#userNameNull').html(errorname.join('<br>'));
        }

        if(!/^(?!\s*$).+/.test(insertuserlastname)){
            errorlastname.push("Debe capturar un Apellido para el usuario")
            sendform.preventDefault();
            $('#userLastNameNull').html(errorlastname.join('<br>'));
        }

        if(!/^(?!\s*$).+/.test(insertuseremail)){
            erroremail.push("Debe capturar un Correo Electrónico para el usuario")
            sendform.preventDefault();
            $('#userEmailNull').html(erroremail.join('<br>'));
        }

        if (insertuserpass.length < 8){
            errorpass.push("La contraseña debe contener al menos 8 caracteres");
            sendform.preventDefault();
            $('#userPasswordNull').html(errorpass.join('<br>'));
        } else{
            if(!/[A-Z]/.test(insertuserpass)){
                errorpass.push("La contraseña debe contener al menos una letra mayúscula");
                sendform.preventDefault();
                $('#userPasswordNull').html(errorpass.join('<br>'));
            } else{
                if(!/\d/.test(insertuserpass)){
                    errorpass.push("La contraseña debe contener al menos un número");
                    sendform.preventDefault();
                    $('#userPasswordNull').html(errorpass.join('<br>'));
                } else{
                    if(!/[\W_]/.test(insertuserpass)){
                        errorpass.push("La contraseña debe contener al menos un caracter especial");
                        sendform.preventDefault();
                        $('#userPasswordNull').html(errorpass.join('<br>'));
                    }
                }
            }
        }
    });

    $('#name').on('input', function(){
        $('#userNameNull').html('');
    });
    $('#lastname').on('input', function(){
        $('#userLastNameNull').html('');
    });
    $('#email').on('input', function(){
        $('#userEmailNull').html('');
    });
    $('#password').on('input', function(){
        $('#userPasswordNull').html('');
    });


    $('#insert_new_user_modal').on('hidden.bs.modal', function(){
        $('#insert_new_user_form')[0].reset();
        $('#userNameNull').text('');
        $('#userLastNameNull').text('');
        $('#userEmailNull').text('');
        $('#userPasswordNull').text('');
    });


    /*var closed_eye = document.createElement('i');
    closed_eye.className = 'icon-ojo-cruzado';
    var opened_eye = document.createElement('i');
    opened_eye.className = 'icon-ojo-abierto';

    $('.input-group-text').each(function(){
        $(this).append(closed_eye.cloneNode(true));
    });


    var showpass = $('#password');
    $('#showPass').on('mousedown', function(){
        showpass.attr('type', 'text');
        $(this).find('i').replaceWith(opened_eye.cloneNode(true));
    });
    $('#showPass').on('mouseup mouseleave', function(){
        showpass.attr('type', 'password');
        $(this).find('i').replaceWith(closed_eye.cloneNode(true));
    });*/

});