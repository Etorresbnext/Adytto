$(document).ready(function(){

    function showErrors(inputId, messageId, messageContent){
        $('#' + inputId).addClass('border border-danger');
        $('#' + messageId).text(messageContent)
    }

    function removeErrors(inputId, messageId){
        $('#' + inputId).removeClass('border border-danger');
        $('#' + messageId).empty();
    }

    $('#insertProcessorForm').on('submit', function(form){
        form.preventDefault();

        var formData = {
            processorName: $('#processorName').val(),
            processorBrand: $('#processorBrand').val(),
            processorModel: $('#processorModel').val(),
            processorFreq: $('#processorFreq').val(),
            freqUnits: $('#freqUnits').val(),
            processorArch: $('#processorArch').val()
        };

        $.ajax({
            type: 'POST',
            url: '/insert_processor',
            data: formData,
            success: function(response){
                window.location.href = response.redirect_url;
            },
            error: function(xhr){
                if(xhr.status === 404){
                    var validity_errors = xhr.responseJSON;

                    if(validity_errors.nullName){
                        showErrors('processorName', 'processorNameNull', validity_errors.nullName);
                    }
                    if(validity_errors.nullBrand){
                        showErrors('processorBrand', 'processorBrandNull', validity_errors.nullBrand);
                    }
                    if(validity_errors.nullModel){
                        showErrors('processorModel', 'processorModelNull', validity_errors.nullModel);
                    }
                    if(validity_errors.nullArch){
                        showErrors('processorArch', 'processorArchNull', validity_errors.nullArch);
                    }
                    if(validity_errors.nullFreq){
                        if ($('#processorFreq').val().trim() !== '' && $('#freqUnits').val() === null){
                            console.log('Unidades vacías');
                            showErrors('freqUnits', 'processorFreqNull', validity_errors.nullFreq);
                        }
                        if ($('#processorFreq').val().trim() === '' && $('#freqUnits').val() !== null){
                            console.log('Cantidad vacía');
                            showErrors('processorFreq', 'processorFreqNull', validity_errors.nullFreq);
                        }
                        if ($('#processorFreq').val().trim() === '' && $('#freqUnits').val() === null){
                            console.log('Ambos vacías');
                            showErrors('processorFreq, #freqUnits', 'processorFreqNull', validity_errors.nullFreq);
                        }
                    }
                }
            }
        });
    });

    $('#processorName').on('input', function(){
        removeErrors('processorName', 'processorNameNull');
    });

    $('#processorBrand').on('change', function(){
        removeErrors('processorBrand', 'processorBrandNull');
    });

    $('#processorModel').on('input', function(){
        removeErrors('processorModel', 'processorModelNull');
    });

    $('#processorArch').on('change', function(){
        removeErrors('processorArch', 'processorArchNull');
    });

    $('#addRecordModal').on('hidden.bs.modal', function(){
        $('#insertProcessorForm')[0].reset();
        removeErrors('processorName', 'processorNameNull');
        removeErrors('processorBrand', 'processorBrandNull');
        removeErrors('processorModel', 'processorModelNull');
        removeErrors('processorArch', 'processorArchNull');
        $('#processorFreq').removeClass('border border-danger');
        $('#processorFreqNull').empty();
        $('#freqUnits').removeClass('border border-danger');
    });





    $('#updateProcessorForm').on('submit', function(updForm){
        updForm.preventDefault();

        var updFormData = {
            updateID_hidden: $('#updateID_hidden').val(),
            updateProcessorName: $('#updateProcessorName').val(),
            updateProcessorBrand: $('#updateProcessorBrand').val(),
            updateProcessorModel: $('#updateProcessorModel').val(),
            updateProcessorFreq: $('#updateProcessorFreq').val(),
            updateFreqUnits: $('#updateFreqUnits').val(),
            updateProcessorArch: $('#updateProcessorArch').val()
        };

        $.ajax({
            type: 'POST',
            url: '/update_processor',
            data: updFormData,
            success: function(response){
                window.location.href = response.redirect_url;
            },
            error: function(xhr){
                if(xhr.status === 404){
                    var update_errors = xhr.responseJSON;

                    if(update_errors.nullName){
                        showErrors('updateProcessorName', 'updateProcessorNameNull', update_errors.nullName);
                    }
                    if(update_errors.nullModel){
                        showErrors('updateProcessorModel', 'updateProcessorModelNull', update_errors.nullModel);
                    }
                    if(update_errors.nullFreq){
                        showErrors('updateProcessorFreq', 'updateProcessorFreqNull', update_errors.nullFreq);
                    }
                }
            }
        });
    });

    $('#updateProcessorName').on('input', function(){
        removeErrors('updateProcessorName', 'updateProcessorNameNull');
    });

    $('#updateProcessorModel').on('input', function(){
        removeErrors('updateProcessorModel', 'updateProcessorModelNull');
    });

    $('#updateProcessorFreq').on('input', function(){
        removeErrors('updateProcessorFreq', 'updateProcessorFreqNull');
    });

    $('#updateRecordModal').on('hidden.bs.modal', function(){
        $('#updateProcessorForm')[0].reset();
        removeErrors('updateProcessorName', 'updateProcessorNameNull');
        removeErrors('updateProcessorModel', 'updateProcessorModelNull');
        removeErrors('updateProcessorFreq', 'updateProcessorFreqNull');
    });

});