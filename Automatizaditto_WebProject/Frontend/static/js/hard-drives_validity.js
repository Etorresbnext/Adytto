$(document).ready(function(){

    function showErrors(inputId, messageId, messageContent){
        $('#' + inputId).addClass('border border-danger');
        $('#' + messageId).text(messageContent);
    }

    function removeErrors(inputId, messageId){
        $('#' + inputId).removeClass('border border-danger');
        $('#' + messageId).empty();
    }

    $('#insertHardDriveForm').on('submit', function(form){
        form.preventDefault();

        var formData = {
            hardDriveBrand: $('#hardDriveBrand').val(),
            hardDriveType: $('#hardDriveType').val(),
            hardDriveStorage: $('#hardDriveStorage').val(),
            storageUnits: $('#storageUnits').val()
        };

        $.ajax({
            type: 'POST',
            url: '/insert_hard-drive',
            data: formData,
            success: function(response){
                window.location.href = response.redirect_url;
            },
            error: function(xhr){
                if(xhr.status === 404){
                    var validity_errors = xhr.responseJSON;

                    if(validity_errors.nullBrand){
                        showErrors('hardDriveBrand', 'hardDriveBrandNull', validity_errors.nullBrand);
                    }
                    if(validity_errors.nullType){
                        showErrors('hardDriveType', 'hardDriveTypeNull', validity_errors.nullType);
                    }
                    if(validity_errors.nullStorage){
                        if ($('#hardDriveStorage').val().trim() !== '' && $('#storageUnits').val() === null){
                            showErrors('storageUnits', 'hardDriveStorageNull', validity_errors.nullStorage);
                        }
                        if ($('#hardDriveStorage').val().trim() === '' && $('#storageUnits').val() !== null){
                            showErrors('hardDriveStorage', 'hardDriveStorageNull', validity_errors.nullStorage);
                        }
                        if ($('#hardDriveStorage').val().trim() === '' && $('#storageUnits').val() === null){
                            showErrors('hardDriveStorage, #storageUnits', 'hardDriveStorageNull', validity_errors.nullStorage);
                        }
                    }
                }
            }
        });
    });

    $('#hardDriveBrand').on('change', function(){
        removeErrors('hardDriveBrand', 'hardDriveBrandNull');
    });

    $('#hardDriveType').on('change', function(){
        removeErrors('hardDriveType', 'hardDriveTypeNull');
    });

    $('#hardDriveStorage').on('input', function(){
        removeErrors('hardDriveStorage', 'hardDriveStorageNull');
    });

    $('#storageUnits').on('change', function(){
        removeErrors('storageUnits', 'hardDriveStorageNull');
    });

    $('#addRecordModal').on('hidden.bs.modal', function(){
        $('#insertHardDriveForm')[0].reset();
        removeErrors('hardDriveBrand', 'hardDriveBrandNull');
        removeErrors('hardDriveType', 'hardDriveTypeNull');
        removeErrors('hardDriveStorage', 'hardDriveStorageNull');
        removeErrors('storageUnits', 'hardDriveStorageNull');
    });
});