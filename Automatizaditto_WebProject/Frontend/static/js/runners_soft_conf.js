$(document).ready(function(){

    function clearErrors(tagId, tagName, tagError){
        $('#' + tagId).removeClass('border border-danger');
        $('#' + tagName).removeClass('border border-danger');
        $('#' + tagError).empty();
    }

    $('#insertScButton').on('click', function(e){
        e.preventDefault();

        var operative_system = $('#scOpSys').val();

        $.post('/verify_soft_conf', {
            scOpSys: operative_system
        }, function(response){
            if (response.exists === 1){
                console.log(response.exists);
                $('#testSoftConf').modal('hide');
                $('#testModal').modal('show');
                $('#runnerSoftConf').val(response.data.Nombre);
                $('#runnerSoftConfId').val(response.data.ID);
                clearErrors('runnerSoftConfId', 'runnerSoftConf', 'runnerSoftConfNull');
            }
            else if (response.exists === 0){
                $('#scName').prop('disabled', false);
                var name = $('#scName').val();
                $('#scDesc').prop('disabled', false);
                var desc = $('#scDesc').val();
                $.post('/insert_software_configuration', {
                    scName: name,
                    scDesc: desc,
                    scOpSys: operative_system,
                    redirect: 'false'
                })
                .done(function(addResponse){
                    if(addResponse.success){
                        $('#testSoftConf').modal('hide');
                        $('#testModal').modal('show');
                        $('#runnerSoftConf').val(addResponse.Name);
                        $('#runnerSoftConfId').val(addResponse.Id);
                        clearErrors('runnerSoftConfId', 'runnerSoftConf', 'runnerSoftConfNull');
                    }
                })
                .fail(function(jqXHR){
                    var validity_errors = jqXHR.responseJSON;
                    console.log(validity_errors);

                    if(validity_errors.nullName){
                        $('#scName').addClass('border border-danger');
                        $('#nullScName').text(validity_errors.nullName);
                    }
                });
            }
        });
    });
});