$(document).ready(function(){
    var tableName = 'operative-systems'
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
                "defaultContent": '<button id="selectrow" type="button" data-bs-toggle="modal" data-bs-target="#updateOsModal" style="border: none; background-color: transparent;"><img src="../static/images/editar.png" width="24" height="24"></button>'
            },
            {
                "data": null,
                "defaultContent": '<button id="deleterow" type="button" data-bs-toggle="modal" data-bs-target="#deleteRecordModal" style="border: none; background-color: transparent;"><img src="../static/images/trash.png" width="24" height="24"></button>'
            },
            { "data": "ID" },
            { "data": "Familia" },
            { "data": "Nombre" },
            { "data": "Edición" },
            { "data": "Versión" },
            { "data": "Arquitectura" },
        ]
    });

    $.ajax({
        url: '/select/os_families',
        type: 'GET',
        success: function(data){
            var select = $('.osFamily');
            data.forEach(function(item){
                select.append(new Option(item['Operative_Systems'], item['Operative_Systems']));
            });
        },
        error: function(error){
            console.log("Error al obtener Unidades: ", error);
        }
    });


    $.ajax({
        url: '/select/os_architectures',
        type: 'GET',
        success: function(data){
            var select = $('.osArch');
            data.forEach(function(item){
                select.append(new Option(item['Architecture'], item['Architecture']));
            });
        },
        error: function(error){
            console.log("Error al obtener Arquitecturas: ", error);
        }
    });


    var hidden_id_input = document.createElement('input');
    hidden_id_input.type = 'hidden';
    hidden_id_input.id = 'updateID_hidden';
    hidden_id_input.name = 'updateID_hidden';
    document.querySelector('#updateOsForm').appendChild(hidden_id_input)

    $('#dataTableGrid tbody').on('click', 'button#selectrow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#updateID_hidden').val(data.ID)
        $('#updateOsId').val(data.ID)
        $('#updateOsFamily').val(data.Familia)
        $('#updateOsName').val(data.Nombre)
        $('#updateOsEdition').val(data["Edición"])
        $('#updateOsVersion').val(data["Versión"])
        $('#updateOsArch').val(data.Arquitectura)
    });

    var hidden_delete_row = document.createElement('input');
    hidden_delete_row.type = 'hidden';
    hidden_delete_row.id = 'idHidden';
    hidden_delete_row.name = 'idHidden';
    document.querySelector('#deleteOsForm').appendChild(hidden_delete_row)

    $('#dataTableGrid tbody').on('click', 'button#deleterow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#idHidden').val(data.ID)
    });

});