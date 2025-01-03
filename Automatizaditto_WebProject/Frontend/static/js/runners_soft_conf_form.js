$(document).ready(function(){

    function buttonState(verify, insert){
        $('#verifyScButton').prop('disabled', verify);
        $('#insertScButton').prop('disabled', insert);
    };

    function softConfData(){
        $('#dynamicOsName').empty();
        $('#dynamicOsDesc').empty();
    };

    var softConfLabels = {
        nameLabel:  '<label for="scName" class="form-label required">Nombre:</label>',
        descLabel:  '<label for="scDesc" class="form-label required">Descripción:</label>'
    };


    $('#softConfModal').on('click', function(){
        /*resetSoftForm = true;
        console.log(resetSoftForm);*/
        $('#runnerSoftConfId').prop('disabled', false);
        var runnerSoftConfId = $('#runnerSoftConfId').val();
        $('#runnerSoftConfId').prop('disabled', true);
        $('#runnerSoftConf').prop('disabled', false);
        var runnerSoftConf = $('#runnerSoftConf').val();
        $('#runnerSoftConf').prop('disabled', true);

        if (runnerSoftConfId.trim() === '' || runnerSoftConf.trim() === '') {
            $('#insertScForm')[0].reset();
            softConfData();
            $('#testSoftConf').modal('show');
            buttonState(false, true);
        }
        else {
            $('#testSoftConf').modal('show');
            buttonState(true, true);
            $('#scName, #scDesc').prop('disabled', true);
        }
    });

    $('#verifyScButton').on('click', function(e){
        e.preventDefault();

        var formData = {
            scOpSys: $('#scOpSys').val()
        };

        $.ajax({
            type: 'POST',
            url: '/verify_soft_conf',
            data: formData,
            success: function(response){
                softConfData();
                if (response.exists === 1){
                    $('#dynamicOsName').append(
                        softConfLabels.nameLabel +
                        '<input id="scName" name="scName" class="form-control" type="text" value="' + response.data.Nombre + '" disabled>'
                    );
                    $('#dynamicOsDesc').append(
                        softConfLabels.descLabel +
                        '<input id="scDesc" name="scDesc" class="form-control" type="text" value="' + response.data.Descripción + '" disabled>'
                    );
                    buttonState(true, false);
                }
                else if (response.exists === 0){
                    $('#dynamicOsName').append(
                        softConfLabels.nameLabel +
                        '<input id="scName" name="scName" class="form-control" type="text" placeholder="Ejemplo">' +
                        '<small id="nullScName" style="color: red;"></small>'
                    );
                    $('#dynamicOsDesc').append(
                        softConfLabels.descLabel +
                        '<input id="scDesc" name="scDesc" class="form-control" type="text" placeholder="Ejemplo">'
                    );
                    buttonState(true, false);
                }
            },
            error: function(xhr){
                if(xhr.status === 404){
                    var validity_errors = xhr.responseJSON;
                    var erasedRecord = xhr.responseJSON.erased;
                    if (erasedRecord){
                        $('#scErased').text(erasedRecord);
                    }
                    if (validity_errors.nullOs){
                        $('#scOpSys').addClass('border border-danger');
                        $('#nullOs').text(validity_errors.nullOs);
                    }
                }
            }
        });
    });

    $('#scOpSys').on('change', function(){
        buttonState(false, true);
        $('#scOpSys').removeClass('border border-danger');
        $('#nullOs').empty();
        $('#scErased').empty();
        softConfData();
    });
});