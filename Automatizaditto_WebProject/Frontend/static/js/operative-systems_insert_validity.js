$(document).ready(function(){

    function showErrors(inputId, messageId, messageContent){
        $('#' + inputId).addClass('border border-danger');
        $('#' + messageId).text(messageContent);
    };

    function dropErrors(inputId, messageId){
        $('#' + inputId).removeClass('border border-danger');
        $('#' + messageId).empty();
    };

    $('#addOsRecordForm').on('submit', function(form){
        form.preventDefault();

        var formData = {
            osFamily: $('#osFamily').val(),
            osName: $('#osName').val(),
            osEdition: $('#osEdition').val(),
            osVersion: $('#osVersion').val(),
            osArch: $('#osArch').val()
        };

        $.ajax({
            type: 'POST',
            url: '/insert_operative_system',
            data: formData,
            success: function(response){
                window.location.href = response.redirect_url;
            },
            error: function(xhr){
                if (xhr.status === 404){
                    var validity_errors = xhr.responseJSON;

                    if (validity_errors.nullFamily){
                        showErrors('osFamily', 'osFamilyNull', validity_errors.nullFamily);
                    }
                    if (validity_errors.nullName){
                        showErrors('osName', 'osNameNull', validity_errors.nullName);
                    }
                    if (validity_errors.nullEdition){
                        showErrors('osEdition', 'osEditionNull', validity_errors.nullEdition);
                    }
                    if (validity_errors.nullVersion){
                        showErrors('osVersion', 'osVersionNull', validity_errors.nullVersion);
                    }
                    if (validity_errors.nullArch){
                        showErrors('osArch', 'osArchNull', validity_errors.nullArch);
                    }
                }
            }
        });
    });

    $('#osFamily').on('change', function(){
        dropErrors('osFamily', 'osFamilyNull');
    });

    $('#osName').on('input', function(){
        dropErrors('osName', 'osNameNull');
    });

    $('#osEdition').on('input', function(){
        dropErrors('osEdition', 'osEditionNull');
    });

    $('#osVersion').on('input', function(){
        dropErrors('osVersion', 'osVersionNull');
    });

    $('#osArch').on('change', function(){
        dropErrors('osArch', 'osArchNull');
    });

    $('#addRecordModal').on('hidden.bs.modal', function(){
        $('#addOsRecordForm')[0].reset();
        dropErrors('osFamily', 'osFamilyNull');
        dropErrors('osName', 'osNameNull');
        dropErrors('osEdition', 'osEditionNull');
        dropErrors('osVersion', 'osVersionNull');
        dropErrors('osArch', 'osArchNull');
    });
});