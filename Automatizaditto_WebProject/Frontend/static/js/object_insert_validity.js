$(document).ready(function(){
    $('#insertObjectForm').on('submit', function(form){
        form.preventDefault();

        var formData = {
            objectName: $('#objectName').val(),
            objectType: $('#objectType').val(),
            objectProduct: $('#objectProduct').val(),
            objectDescription: $('#objectDescription').val(),
            objectIdGrouper: $('#objectIdGrouper').val(),
            objectNameGrouper: $('#objectNameGrouper').val(),
            objectClassGrouper: $('#objectClassGrouper').val(),
            objectXpathGrouper: $('#objectXpathGrouper').val()
        };

        $.ajax({
            type: 'POST',
            url: '/insert_object',
            data: formData,
            success: function(response){
                window.location.href = response.redirect_url;
            },
            error: function(xhr){
                if (xhr.status === 404){
                    var validity_errors = xhr.responseJSON;

                    if (validity_errors.nullName){
                        $('#objectName').addClass('border border-danger');
                        $('#objectNameNull').text(validity_errors.nullName);
                    }
                    if (validity_errors.nullType){
                        $('#objectType').addClass('border border-danger');
                        $('#objectTypeNull').text(validity_errors.nullType);
                    }
                    if (validity_errors.nullProduct){
                        $('#objectProduct').addClass('border border-danger');
                        $('#objectProductNull').text(validity_errors.nullProduct);
                    }
                }
            }
        });
    });

    $('#objectName').on('input', function(){
        $('#objectName').removeClass('border border-danger');
        $('#objectNameNull').html('');
    });

    $('#objectType').on('change', function(){
        $('#objectType').removeClass('border border-danger');
        $('#objectTypeNull').html('');
    });

    $('#objectProduct').on('change', function(){
        $('#objectProduct').removeClass('border border-danger');
        $('#objectProductNull').html('');
    });

    $('#addRecordModal').on('hidden.bs.modal', function(){
        console.log("Modal cerrado, reseteando formulario");
        $('#insertObjectForm')[0].reset();
        $('#objectName').removeClass('border border-danger');
        $('#objectNameNull').text('');
        $('#objectType').removeClass('border border-danger');
        $('#objectTypeNull').text('');
        $('#objectProduct').removeClass('border border-danger');
        $('#objectProductNull').text('');
    });



    /*$('#insertObjectButton').on('click', function(sendform){
        var insertObjectName = $('#objectName').val();
        var errorname = [];

        if(!/^(?!\s*$).+/.test(insertObjectName)){
            errorname.push("Debe capturar un Nombre para el Objeto")
            sendform.preventDefault();
            $('#objectNameNull').html(errorname.join('<br>'));
        }
    });



    $('#addRecordModal').on('hidden.bs.modal', function(){
        $('#insertObjectForm')[0].reset();
        $('#objectNameNull').text('');
    });*/
});