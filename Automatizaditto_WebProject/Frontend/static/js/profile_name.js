$(document).ready(function(){
    $('#updateUserFullName').prop('disabled', true);

    $('#getUserName, #getUserLastName').on('input', function(){
        $('#updateUserFullName').prop('disabled', false)
    });


    $('#updateUserFullName').on('click', function(setnameform){
        var name = $('#getUserName').val();
        var lastname = $('#getUserLastName').val();

        var namenull = [];
        var lastnamenull = [];


        if(!/^(?!\s*$).+/.test(name)){
            namenull.push("El nuevo nombre de Usuario no puede ser nulo");
            setnameform.preventDefault();
            $('#nameError').html(namenull.join('<br>'));
        }

        if(!/^(?!\s*$).+/.test(lastname)){
            lastnamenull.push("El apellido del Usuario no puede ser nulo");
            setnameform.preventDefault();
            $('#lastnameError').html(lastnamenull.join('<br>'));
        }
    });

    $('#getUserName').on('input', function(){
        $('#nameError').html('');
    });
    $('#getUserLastName').on('input', function(){
        $('#lastnameError').html('');
    });


});