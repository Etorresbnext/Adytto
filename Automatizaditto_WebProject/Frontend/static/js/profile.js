$(document).ready(function(){
    var tableName = 'profile_name';
    $.ajax({
        url: '/select/' + tableName,
        type: 'GET',
        contentType: 'application/json',
        success: function(data){
            if(data){
                $('#getUserName').val(data["Nombre"]);
                $('#getUserLastName').val(data.Apellido);
            }
        },
        error: function(){
            console.log("Error al obtener los datos del usuario.");
        }
    });

    $('#profileImage').on('change', function(){
        const file = this.files[0];
        if(file){
            const reader = new FileReader();
            reader.onload = function(e){
                $('img#showProfilePicture').attr('src', e.target.result);
                $('img#showProfilePicture').css('opacity', '0.5')
            }
            reader.readAsDataURL(file);
        }
        $('#updateUserFullName').prop('disabled', false)
    });

    $('#loadPicture').on('click', function(){
        $('#profileImage').click();
    });

});