$(document).ready(function(){

    function clearErrors(tagId, tagName, tagError){
        $('#' + tagId).removeClass('border border-danger');
        $('#' + tagName).removeClass('border border-danger');
        $('#' + tagError).empty();
    }

    $('#testInsertHcButton').on('click', function(e){
        e.preventDefault();

        var processor = $('#verifyHcProcessor').val();
        var hard_drive = $('#verifyHcHardDrive').val();
        var ram = $('#verifyHcRam').val();

        $.post('/verify_hard_conf', {
            verifyHcProcessor: processor,
            verifyHcHardDrive: hard_drive,
            verifyHcRam: ram
        }, function(response){
            if (response.exists === 1){
                console.log(response.exists);
                $('#testHardConf').modal('hide');
                $('#testModal').modal('show');
                $('#runnerHardConf').val(response.data.Nombre);
                $('#runnerHardConfId').val(response.data.ID);
                clearErrors('runnerHardConfId', 'runnerHardConf', 'runnerHardConfNull');
            }
            else if (response.exists === 0) {
                $('#hcName').prop('disabled', false);
                var name = $('#hcName').val();
                $('#hcDesc').prop('disabled', false);
                var description = $('#hcDesc').val();
                $.post('/insert_hardware_configuration', {
                    hcName: name,
                    hcDesc: description,
                    hcProcessor: processor,
                    hcHardDrive: hard_drive,
                    hcRam: ram,
                    redirect: 'false'
                })
                .done(function(addResponse){
                    if(addResponse.success){
                        $('#testHardConf').modal('hide');
                        $('#testModal').modal('show');
                        $('#runnerHardConf').val(addResponse.Name);
                        $('#runnerHardConfId').val(addResponse.Id);
                        clearErrors('runnerHardConfId', 'runnerHardConf', 'runnerHardConfNull');
                    }
                })
                .fail(function(jqXHR){
                    var validity_errors = jqXHR.responseJSON;
                    console.log(validity_errors);

                    if(validity_errors.nullName){
                        $('#hcName').addClass('border border-danger');
                        $('#nullHcName').text(validity_errors.nullName);
                    }
                });
            }
        });
    });
});