$(document).ready(function(){
    var tableName = 'hardware-configurations'
    var table = $('#dataTableGrid').DataTable({

        scrollX: true,

        /*language: {
            url: '//cdn.datatables.net/plug-ins/2.0.8/i18n/es-MX.json',
        },*/

        "ajax": {
            "url": "/select/" + tableName,  // Ruta en Flask para obtener los casos de prueba
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

        "columns": [
            {
                "data": null,
                "defaultContent": '<button id="selectrow" type="button" data-bs-toggle="modal" data-bs-target="#updateRecordModal" style="border: none; background-color: transparent;"><img src="../static/images/editar.png" width="24" height="24"></button>'
            },
            {
                "data": null,
                "defaultContent": '<button id="deleterow" type="button" data-bs-toggle="modal" data-bs-target="#deleteRecordModal" style="border: none; background-color: transparent;"><img src="../static/images/trash.png" width="24" height="24"></button>'
            },
            { "data": "ID" },
            { "data": "Nombre" },
            { "data": "Descripción" },
            { "data": "Procesador" },
            { "data": "Almacenamiento" },
            { "data": "Memoria RAM" }
        ]
    });

    $.ajax({
        url: '/select/processors',
        type: 'GET',
        success: function(data){
            var select = $('.hcProcessor');
            data.forEach(function(item){
                select.append(new Option(item['Nombre'] + ' ' + item['Modelo'] + ' ' + item['Frecuencia'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Unidades: ", error);
        }
    });

    $.ajax({
        url: '/select/hard-drives',
        type: 'GET',
        success: function(data){
            var select = $('.hcHardDrive');
            data.forEach(function(item){
                select.append(new Option(item['Tipo'] + ' ' + item['Almacenamiento'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Unidades: ", error);
        }
    });

    $.ajax({
        url: '/select/rams',
        type: 'GET',
        success: function(data){
            var select = $('.hcRam');
            data.forEach(function(item){
                select.append(new Option(item['Capacidad'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Unidades: ", error);
        }
    });

    /* MODIFICAR */
    var hidden_id_input = document.createElement('input');
    hidden_id_input.type = 'hidden';
    hidden_id_input.id = 'updateID_hidden';
    hidden_id_input.name = 'updateID_hidden';
    document.querySelector('#updateHcForm').appendChild(hidden_id_input)

    $('#dataTableGrid tbody').on('click', 'button#selectrow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#updateID_hidden').val(data.ID)
        $('#updateHcId').val(data.ID)
        $('#updateHcName').val(data.Nombre)
        $('#updateHcDesc').val(data["Descripción"])
        $('#updateHcProcessor').val(data["ID Procesador"])
        $('#updateHcHardDrive').val(data["ID Almacenamiento"])
        $('#updateHcRam').val(data["ID Memoria RAM"])
    });


    var hidden_delete_row = document.createElement('input');
    hidden_delete_row.type = 'hidden';
    hidden_delete_row.id = 'idHidden';
    hidden_delete_row.name = 'idHidden';
    document.querySelector('#deleteHcForm').appendChild(hidden_delete_row)

    $('#dataTableGrid tbody').on('click', 'button#deleterow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#idHidden').val(data.ID)
    });

});