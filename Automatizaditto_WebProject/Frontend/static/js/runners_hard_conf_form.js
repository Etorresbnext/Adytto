$(document).ready(function(){

    function buttonsState(verify, insert){
        $('#verifyHcButton').prop('disabled', verify);
        $('#testInsertHcButton').prop('disabled', insert);
    };

    function hideFields(){
        $('#dynamicName').empty();
        $('#dynamicDescription').empty();
    };

    var hardConfLabels = {
        nameLabel:  '<label for="hcName" class="form-label required">Nombre:</label>',
        descLabel:  '<label for="hcDesc" class="form-label required">Descripción:</label>'
    };


    $('#hardConfModal').on('click', function(){
        /*resetHardForm = true;
        console.log(resetHardForm);*/
        $('#runnerHardConfId').prop('disabled', false);
        var runnerHardConfId = $('#runnerHardConfId').val();
        $('#runnerHardConfId').prop('disabled', true);
        $('#runnerHardConf').prop('disabled', false);
        var runnerHardConf = $('#runnerHardConf').val();
        $('#runnerHardConf').prop('disabled', true);

        if (runnerHardConfId.trim() === '' || runnerHardConf.trim() === ''){
            $('#verifyHcForm')[0].reset();
            hideFields();
            $('#testHardConf').modal('show');
            buttonsState(false, true)
        }
        else{
            $('#testHardConf').modal('show');
            buttonsState(true, true);
            $('#hcName, #hcDesc').prop('disabled', true)
        }
    });

    $('#verifyHcButton').on('click', function(e){
        e.preventDefault();

        var formData = {
            verifyHcProcessor: $('#verifyHcProcessor').val(),
            verifyHcHardDrive: $('#verifyHcHardDrive').val(),
            verifyHcRam: $('#verifyHcRam').val()
        };

        $.ajax({
            type: 'POST',
            url: '/verify_hard_conf',
            data: formData,
            success: function(response){
                hideFields();
                if (response.exists === 1){
                    $('#dynamicName').append(
                        hardConfLabels.nameLabel +
                        '<input id="hcName" name="hcName" class="form-control" type="text" value="' + response.data.Nombre + '" disabled>'
                    );
                    $('#dynamicDescription').append(
                        hardConfLabels.descLabel +
                        '<input id="hcDesc" name="hcDesc" class="form-control" type="text" value="' + response.data.Descripción + '" disabled>'
                    );
                    buttonsState(true, false);
                }
                else if (response.exists === 0){
                    $('#dynamicName').append(
                        hardConfLabels.nameLabel +
                        '<input id="hcName" name="hcName" class="form-control" type="text" placeholder="Ejemplo">' +
                        '<small id="nullHcName" style="color: red;"></small>'
                    );
                    $('#dynamicDescription').append(
                        hardConfLabels.descLabel +
                        '<input id="hcDesc" name="hcDesc" class="form-control" type="text" placeholder="Ejemplo">'
                    );
                    buttonsState(true, false);
                }
            },
            error: function(xhr){
                if(xhr.status === 404){
                    var validity_errors = xhr.responseJSON;
                    var erasedRecord = xhr.responseJSON.erased;
                    if (erasedRecord){
                        $('#erasedRecord').text(erasedRecord);
                    }
                    if (validity_errors.processorNull){
                        $('#verifyHcProcessor').addClass('border border-danger');
                        $('#nullProcessor').text(validity_errors.processorNull);
                    }
                    if (validity_errors.hardDriveNull){
                        $('#verifyHcHardDrive').addClass('border border-danger');
                        $('#nullHardDrive').text(validity_errors.hardDriveNull);
                    }
                    if (validity_errors.ramNull){
                        $('#verifyHcRam').addClass('border border-danger');
                        $('#nullRam').text(validity_errors.ramNull);
                    }
                }
            }
        });
    });

    $('#verifyHcProcessor').on('change', function(){
        buttonsState(false, true);
        $('#verifyHcProcessor').removeClass('border border-danger');
        $('#nullProcessor').empty();
        $('#erasedRecord').empty();
        hideFields();
    });

    $('#verifyHcHardDrive').on('change', function(){
        buttonsState(false, true);
        $('#verifyHcHardDrive').removeClass('border border-danger');
        $('#nullHardDrive').empty();
        $('#erasedRecord').empty();
        hideFields();
    });

    $('#verifyHcRam').on('change', function(){
        buttonsState(false, true);
        $('#verifyHcRam').removeClass('border border-danger');
        $('#nullRam').empty();
        $('#erasedRecord').empty();
        hideFields();
    });

    /*$('#testHardConf').on('hidden.bs.modal', function(){
        $('#verifyHcForm')[0].reset();
        $('#verifyHcProcessor').removeClass('border border-danger');
        $('#nullProcessor').empty();
        $('#verifyHcHardDrive').removeClass('border border-danger');
        $('#nullHardDrive').empty();
        $('#verifyHcRam').removeClass('border border-danger');
        $('#nullRam').empty();
        $('#erasedRecord').empty();
        hideFields();
    });*/

    /*$('#testModal').on('hidden.bs.modal', function(){
        $('#testForm')[0].reset();
        $('#verifyHcForm')[0].reset();
    });*/
});