$(document).ready(function(){
    $('#update').on('click', function(sendformupdate){
        var updusername = $('#updateUserName').val();
        var upduserlastname = $('#updateUserLastName').val();
        var upduseremail = $('#updateUserEmail').val();

        var errorname = [];
        var errorlastname = [];
        var erroremail = [];

        if(!/^(?!\s*$).+/.test(updusername)){
            errorname.push("Debe capturar un Nombre para el usuario")
            sendformupdate.preventDefault();
            $('#updateNameNull').html(errorname.join('<br>'));
        }

        if(!/^(?!\s*$).+/.test(upduserlastname)){
            errorlastname.push("Debe capturar un Apellido para el usuario")
            sendformupdate.preventDefault();
            $('#updateLastNameNull').html(errorlastname.join('<br>'));
        }

        if(!/^(?!\s*$).+/.test(upduseremail)){
            erroremail.push("Debe capturar un Correo Electrónico para el usuario")
            sendformupdate.preventDefault();
            $('#updateEmailNull').html(erroremail.join('<br>'));
        }
    });

    $('#updateUserName').on('input', function(){
        $('#updateNameNull').html('');
    });
    $('#updateUserLastName').on('input', function(){
        $('#updateLastNameNull').html('');
    });
    $('#updateUserEmail').on('input', function(){
        $('#updateEmailNull').html('');
    });


    $('#update_user_modal').on('hidden.bs.modal', function(){
        $('#updateUserForm')[0].reset();
        $('#updateNameNull').text('');
        $('#updateLastNameNull').text('');
        $('#updateEmailNull').text('');
    });
});