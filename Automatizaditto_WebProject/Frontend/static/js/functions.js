// FUNCIONES COMPARTIDAS EN CATÁLOGOS


// Cargar información de los registros del catálogo en tabla generada con DataTables
export function displayTableData(tableName, dataArray){

    var columns = [
        {
            "data": null,
            "defaultContent": '<button id="selectrow" type="button" data-bs-toggle="modal" data-bs-target="#updateRecordModal" style="border: none; background-color: transparent;"><img src="../static/images/editar.png" width="24" height="24"></button>'
        },
        {
            "data": null,
            "defaultContent": '<button id="deleterow" type="button" data-bs-toggle="modal" data-bs-target="#deleteRecordModal" style="border: none; background-color: transparent;"><img src="../static/images/trash.png" width="24" height="24"></button>'
        }
    ];

    dataArray.forEach(columnName => {
        columns.push({ "data": columnName });
    });

    var table = $('#dataTableGrid').DataTable({

        /*language: {
            url: '//cdn.datatables.net/plug-ins/2.0.8/i18n/es-MX.json',
        },*/

        "ajax":{
            "url": "/select/" + tableName,
            "dataSrc": ""
        },

        layout: {
            topStart: [{
                buttons: [
                    {
                        extend: 'colvis',
                        columnText: function (dt, idx, title) {
                            return idx + 1 + ': ' + title;
                        }
                    }
                ]
            }, 'pageLength'],
            bottomEnd: [{
                buttons: [
                    {
                        text: '<i class="lni lni-circle-plus" style="background-color:blue;"></i> Nuevo',
                        className: 'btn btn-success',
                        action: function(e, dt, node, config){
                            $('#addRecordModal').modal('show');
                        }
                    }
                ]
            }, 'paging'],
        },

        "columns": columns
    });

    return table;
}


// Visualizar opciones de los 'Dropdown' en caso de que los catálogos posean este tipo de campo
export function getDropdownOptions(endpoint, dropdownClass, dropdownOption, dropdownValue){
    $.ajax({
        url: '/select/' + endpoint,
        type: 'GET',
        success: function(data){
            var select = $('.' + dropdownClass);
            data.forEach(function(item){
                select.append(new Option(item[dropdownOption], item[dropdownValue]));
            });
        },
        error: function(error){
            console.log("Error al obtener información", error);
        }
    });
}


// Llenar automáticamente los campos del formulario (update y delete) con la información del registro seleccionado
export function getRecordData(buttonId, tableId, inputIdArray, valueArray){
    $('#dataTableGrid tbody').on('click', buttonId, function(){
        var data = tableId.row($(this).parents('tr')).data();
        inputIdArray.forEach((inputId, i) => {
            var value = valueArray[i];
            $('#' + inputId).val(data[value]);
        });
    });
}


// Crear Input oculto en el formulario (update y delete) para almacenar el ID del registro seleccionado
export function hiddenInputId(inputId, inputName, formId){
    var hiddenId = document.createElement('input');
    hiddenId.type = 'text';
    hiddenId.id = inputId;
    hiddenId.name = inputName;
    document.querySelector('#' + formId).appendChild(hiddenId)
}


// Construir solicitud AJAX para agregar o actualizar registros.
export function ajaxRequest(formId, inputData, endpoint, succesAction, modalId, inputIdArray, messageIdArray, keyIdArray){

    $('#' + formId).on('submit', function(form){
        form.preventDefault();

        var formData = getFormData(inputData)

        $.ajax({
            type: 'POST',
            url: endpoint,
            data: formData,
            success: function(response){
                successResponse(response, succesAction, modalId);
            },
            error: function(xhr){
                if(xhr.status === 404){
                    var inputErrors = xhr.responseJSON;
                    console.log(inputErrors);
                    
                    keyIdArray.forEach((keyId, i) => {
                        var inputId = inputIdArray[i];
                        var messageId = messageIdArray[i];
                        if(inputErrors[keyId]){
                            showErrors(inputId, messageId, inputErrors[keyId]);
                        }
                    });
                }
            }
        });
    });
}


// Borrar mensajes de error de un campo
export function cleanInputs(inputId, messageId){
    $('#' + inputId).on('input', function(){
        removeErrors(inputId, messageId);
    });
}


// Resetear formulario a sus valores default y borrar mensajes de error de sus campos
export function resetForm(modalId, formId, inputIdArray, messageIdArray){
    $('#' + modalId).on('hidden.bs.modal', function(){
        $('#' + formId)[0].reset();
        inputIdArray.forEach((inputId, i) => {
            var messageId = messageIdArray[i];
            removeErrors(inputId, messageId);
        });
    });
}


// Mostrar mensajes de error para validaciones
function showErrors(inputId, messageId, messageContent){
    $('#' + inputId).addClass('border border-danger');
    $('#' + messageId).text(messageContent)
}


// Borrar mensajes de error de un campo
function removeErrors(inputId, messageId){
    $('#' + inputId).removeClass('border border-danger');
    $('#' + messageId).empty();
}

// Recopilar datos de los formularios
function getFormData(inputData){
    let formData = {};
    inputData.forEach(id => {
        formData[id] = $('#' + id).val();
    });
    return formData;
}


// Solicitud AJAX exitosa
function successResponse(response, succesAction, modalId){
    $('#showSuccessMessage').html(response[succesAction]);
    $('#' + modalId).modal('hide');
    $('#successInsert').modal('show');

    $('#refreshPage').on('click', function(){
        window.location.href = response.redirect_url;
    });
}