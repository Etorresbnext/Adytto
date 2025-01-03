$(document).ready(function(){
    var tableName = 'urls';
    var table = $('#dataTableGrid').DataTable({

        /*language: {
            url: '//cdn.datatables.net/plug-ins/2.0.8/i18n/es-MX.json',
        },*/

        "ajax": {
            "url": "/select/" + tableName,  // Ruta en Flask para obtener los usuarios
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
            { "data": "URL" },
            { "data": "Ambiente" },
            { "data": "Producto" }
        ]
    });

    $.ajax({
        url: '/select/protocols',
        type: 'GET',
        success: function(data){
            var select = $('.urlProtocol');
            data.forEach(function(item){
                select.append(new Option(item['Protocolo'], item['Protocolo']));
            });
        },
        error: function(error){
            console.log("Error al obtener Protocolos: ", error);
        }
    });

    $.ajax({
        url: '/select/products',
        type: 'GET',
        success: function(data){
            var select = $('.urlProduct');
            data.forEach(function(item){
                select.append(new Option(item['Nombre'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Productos: ", error);
        }
    });


    $.ajax({
        url: '/select/environment_types',
        type: 'GET',
        success: function(data){
            var select = $('.urlEnv');
            data.forEach(function(item){
                select.append(new Option(item['Ambiente'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Productos: ", error);
        }
    });


    /* MODIFICAR */
    var hidden_id_input = document.createElement('input');
    hidden_id_input.type = 'hidden';
    hidden_id_input.id = 'updateID_hidden';
    hidden_id_input.name = 'updateID_hidden';
    document.querySelector('#updateURLForm').appendChild(hidden_id_input)

    $('#dataTableGrid tbody').on('click', 'button#selectrow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#updateID_hidden').val(data.ID)
        $('#updateURLId').val(data.ID)
        $('#updateURLName').val(data.Nombre)
        $('#updateUrlDomain').val(data.Dominio)
        $('#updateUrlPort').val(data.Puerto)
        $('#updateUrlPath').val(data.Ruta)
        $('#updateUrlProtocol').val(data.Protocolo)
        $('#updateUrlEnv').val(data["ID Ambiente"])
        $('#updateUrlProduct').val(data["ID Producto"])
    });


    /* BORRAR */
    var hidden_delete_row = document.createElement('input');
    hidden_delete_row.type = 'hidden';
    hidden_delete_row.id = 'idHidden';
    hidden_delete_row.name = 'idHidden';
    document.querySelector('#deleteURLForm').appendChild(hidden_delete_row)

    $('#dataTableGrid tbody').on('click', 'button#deleterow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#idHidden').val(data.ID)
    });

});