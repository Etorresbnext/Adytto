$(document).ready(function(){
    $('#insertRunnerForm').on('submit', function(form){
        form.preventDefault();

        $('#runnerHardConfId').prop('disabled', false);
        $('#runnerSoftConfId').prop('disabled', false);

        var formData = {
            runnerName: $('#runnerName').val(),
            runnerIp: $('#runnerIp').val(),
            runnerDesc: $('#runnerDesc').val(),
            runnerHardConfId: $('#runnerHardConfId').val(),
            runnerSoftConfId: $('#runnerSoftConfId').val()
        };

        $('#runnerHardConfId').prop('disabled', true);
        $('#runnerSoftConfId').prop('disabled', true);

        $.ajax({
            type: 'POST',
            url: '/insert_runner',
            data: formData,
            success: function(response){
                window.location.href = response.redirect_url;
            },
            error: function(xhr){
                if (xhr.status === 404){
                    var validity_errors = xhr.responseJSON;

                    if (validity_errors.nullName){
                        $('#runnerName').addClass('border border-danger');
                        $('#runnerNameNull').text(validity_errors.nullName);
                    }
                    if (validity_errors.nullIp){
                        $('#runnerIp').addClass('border border-danger');
                        $('#runnerIpNull').text(validity_errors.nullIp);
                    }
                    else{
                        $('#runnerIp').addClass('border border-danger');
                        $('#runnerIpNull').text(validity_errors.invalidIp);
                    }
                    if (validity_errors.nullHardConf){
                        $('#runnerHardConfId').addClass('border border-danger');
                        $('#runnerHardConf').addClass('border border-danger');
                        $('#runnerHardConfNull').text(validity_errors.nullHardConf);
                    }
                    if (validity_errors.nullSoftConf){
                        $('#runnerSoftConfId').addClass('border border-danger');
                        $('#runnerSoftConf').addClass('border border-danger');
                        $('#runnerSoftConfNull').text(validity_errors.nullSoftConf);
                    }
                }
                else if (xhr.status === 500){
                    var validity_errors = xhr.responseJSON;

                    if (validity_errors.dbError){
                        $('#runnerIpNull').text(validity_errors.dbError);
                    }
                }
            }
        });
    });

    $('#runnerName').on('input', function(){
        $('#runnerName').removeClass('border border-danger');
        $('#runnerNameNull').empty();
    });

    $('#runnerIp').on('input', function(){
        $('#runnerIp').removeClass('border border-danger');
        $('#runnerIpNull').empty();
    });

    var preventReset = false;

    $('#testModal').on('hidden.bs.modal', function(){
        if (!preventReset){
            console.log("Reseteando formulario");
            $('#insertRunnerForm')[0].reset();
            $('#runnerNameNull').empty();
            $('#runnerName').removeClass('border border-danger');
            $('#runnerIpNull').empty();
            $('#runnerIp').removeClass('border border-danger');
            $('#runnerHardConfNull').empty();
            $('#runnerHardConfId').removeClass('border border-danger');
            $('#runnerHardConf').removeClass('border border-danger');
            $('#runnerSoftConfNull').empty();
            $('#runnerSoftConfId').removeClass('border border-danger');
            $('#runnerSoftConf').removeClass('border border-danger');
        }
        else {
            console.log("El formulario no se resetea");
            preventReset = false;
        }
    });

    $('#softConfModal').on('click', function(){
        preventReset = true;
    });

    $('#hardConfModal').on('click', function(){
        preventReset = true;
    });
});