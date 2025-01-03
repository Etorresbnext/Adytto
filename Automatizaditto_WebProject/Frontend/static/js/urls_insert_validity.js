$(document).ready(function(){
    $('#insertURLForm').on('submit', function(form){
        form.preventDefault();

        var formData = {
            urlName: $('#urlName').val(),
            urlEnv: $('#urlEnv').val(),
            urlProduct: $('#urlProduct').val(),
            urlProtocol: $('#urlProtocol').val(),
            urlDomain: $('#urlDomain').val(),
            urlPort: $('#urlPort').val(),
            urlPath: $('#urlPath').val()
        };

        $.ajax({
            type: 'POST',
            url: '/insert_url',
            data: formData,
            success: function(response){
                window.location.href = response.redirect_url;
            },
            error: function(xhr){
                if (xhr.status === 404){
                    var validity_errors = xhr.responseJSON;

                    if (validity_errors.nullName){
                        $('#urlName').addClass('border border-danger');
                        $('#urlNameNull').text(validity_errors.nullName);
                    }
                    if (validity_errors.nullProtocol){
                        $('#urlProtocol').addClass('border border-danger');
                        $('#protocolNull').text(validity_errors.nullProtocol);
                    }
                    if (validity_errors.nullDomain){
                        $('#urlDomain').addClass('border border-danger');
                        $('#urlDomainNull').text(validity_errors.nullDomain);
                    }
                    else{
                        $('#urlDomain').addClass('border border-danger');
                        $('#urlDomainNull').text(validity_errors.invalidIp);
                    }
                    if (validity_errors.nullPort){
                        $('#urlPort').addClass('border border-danger');
                        $('#urlPortNull').text(validity_errors.nullPort);
                    }
                    if (validity_errors.nullPath){
                        $('#urlPath').addClass('border border-danger');
                        $('#urlPathNull').text(validity_errors.nullPath);
                    }
                    if (validity_errors.nullProduct){
                        $('#urlProduct').addClass('border border-danger');
                        $('#productNull').text(validity_errors.nullProduct);
                    }
                    if (validity_errors.nullEnv){
                        $('#urlEnv').addClass('border border-danger');
                        $('#envNull').text(validity_errors.nullEnv);
                    }
                }
            }
        });
    });

    $('#urlName').on('input', function(){
        $('#urlName').removeClass('border border-danger');
        $('#urlNameNull').html('');
    });

    $('#urlEnv').on('change', function(){
        $('#urlEnv').removeClass('border border-danger');
        $('#envNull').html('');
    });

    $('#urlProduct').on('change', function(){
        $('#urlProduct').removeClass('border border-danger');
        $('#productNull').html('');
    });

    $('#urlProtocol').on('change', function(){
        $('#urlProtocol').removeClass('border border-danger');
        $('#protocolNull').html('');
    });

    $('#urlDomain').on('input', function(){
        $('#urlDomain').removeClass('border border-danger');
        $('#urlDomainNull').html('');
    });

    $('#urlPort').on('input', function(){
        $('#urlPort').removeClass('border border-danger');
        $('#urlPortNull').html('');
    });

    $('#urlPath').on('input', function(){
        $('#urlPath').removeClass('border border-danger');
        $('#urlPathNull').html('');
    });

    $('#addRecordModal').on('hidden.bs.modal', function(){
        console.log("Modal cerrado, reseteando formulario");
        $('#insertURLForm')[0].reset();
        $('#urlName').removeClass('border border-danger');
        $('#urlNameNull').text('');
        $('#urlEnv').removeClass('border border-danger');
        $('#envNull').text('');
        $('#urlProduct').removeClass('border border-danger');
        $('#productNull').text('');
        $('#urlProtocol').removeClass('border border-danger');
        $('#protocolNull').text('');
        $('#urlDomain').removeClass('border border-danger');
        $('#urlDomainNull').text('');
        $('#urlPort').removeClass('border border-danger');
        $('#urlPortNull').text('');
        $('#urlPath').removeClass('border border-danger');
        $('#urlPathNull').text('');
    });




    /*$('#insertURLButton').on('click', function(sendform){
        var insertUrlName = $('#urlName').val()
        var insertUrlDomain = $('#urlDomain').val()
        var insertUrlPort = $('#urlPort').val()
        var insertUrlPath = $('#urlPath').val()

        var errorname = []
        var errordomain = []
        var errorport = []
        var errorpath = []

        if(!/^(?!\s*$).+/.test(insertUrlName)){
            errorname.push("Debe capturar un Nombre para la URL")
            sendform.preventDefault();
            $('#urlNameNull').html(errorname.join('<br>'));
        }
        if(!/^(?!\s*$).+/.test(insertUrlDomain)){
            errordomain.push("Debe capturar el Dominio de la URL")
            sendform.preventDefault();
            $('#urlDomainNull').html(errordomain.join('<br>'));
        }
        if(!/^(?!\s*$).+/.test(insertUrlPort)){
            errorport.push("Debe capturar el Puerto de la URL")
            sendform.preventDefault();
            $('#urlPortNull').html(errorport.join('<br>'));
        }
        if(!/^(?!\s*$).+/.test(insertUrlPath)){
            errorpath.push("Debe capturar la Ruta de la URL")
            sendform.preventDefault();
            $('#urlPathNull').html(errorpath.join('<br>'));
        }
    });


    $('#urlDomain').on('input', function(){
        $('#urlDomainNull').html('');
    });

    $('#urlPort').on('input', function(){
        $('#urlPortNull').html('');
    });

    $('#urlPath').on('input', function(){
        $('#urlPathNull').html('');
    });

    $('#addRecordModal').on('hidden.bs.modal', function(){
        $('#insertURLForm')[0].reset();
        $('#urlNameNull').text('');
        $('#urlDomainNull').text('');
        $('#urlPortNull').text('');
        $('#urlPathNull').text('');
    });*/
});