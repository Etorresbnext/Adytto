$(document).ready(function(){
    var tableName = 'runners'
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
                        text: '<i class="lni lni-circle-plus" style="background-color:blue;"></i> Agregar',
                        className: 'btn btn-success',
                        action: function(e, dt, node, config){
                            $('#testModal').modal('show');
                        }
                    }
                ]
            }, 'paging'],
        },

        "columns": [
            {
                "data": null,
                "defaultContent": '<button id="selectrow" type="button" data-bs-toggle="modal" data-bs-target="#updateRunnerModal" style="border: none; background-color: transparent;"><img src="../static/images/editar.png" width="24" height="24"></button>'
            },
            {
                "data": null,
                "defaultContent": '<button id="deleterow" type="button" data-bs-toggle="modal" data-bs-target="#deleteRecordModal" style="border: none; background-color: transparent;"><img src="../static/images/trash.png" width="24" height="24"></button>'
            },
            { "data": "id" },
            { "data": "name" },
            { "data": "description" },
            { "data": "ip" },
            { "data": "name_hc" },
            { "data": "name_sc" }
        ]
    });

    $.ajax({
        url: '/select/hardware-configurations',
        type: 'GET',
        success: function(data){
            var select = $('.runnerHardConf');
            data.forEach(function(item){
                select.append(new Option(item['Nombre'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener las Configuraciones de Hardware: ", error);
        }
    });

    $.ajax({
        url: '/select/software-configurations',
        type: 'GET',
        success: function(data){
            var select = $('.runnerSoftConf');
            data.forEach(function(item){
                select.append(new Option(item['Nombre'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener las Configuraciones de Software: ", error);
        }
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
                select.append(new Option(item['Marca'] + ' ' + item['Tipo'] + ' ' + item['Almacenamiento'], item['ID']));
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

    $.ajax({
        url: '/select/operative-systems',
        type: 'GET',
        success: function(data){
            var select = $('.scOpSys');
            data.forEach(function(item){
                select.append(new Option(item['Nombre'] + ' ' + item['Edición'] + ' ' + item['Versión'] + ' ' + item['Arquitectura'], item['ID']));
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
    document.querySelector('#updateRunnerForm').appendChild(hidden_id_input)

    $('#dataTableGrid tbody').on('click', 'button#selectrow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#updateID_hidden').val(data.id)
        $('#updateRunnerId').val(data.id)
        $('#updateRunnerName').val(data.name)
        $('#updateRunnerDesc').val(data.description)
        $('#updateRunnerIp').val(data.ip)
        $('#updateRunnerHardConf').val(data["id_hc"])
        $('#updateRunnerSoftConf').val(data["id_sc"])
    });



    /* BORRAR */
    var hidden_delete_row = document.createElement('input');
    hidden_delete_row.type = 'hidden';
    hidden_delete_row.id = 'idHidden';
    hidden_delete_row.name = 'idHidden';
    document.querySelector('#deleteRunnerForm').appendChild(hidden_delete_row)

    $('#dataTableGrid tbody').on('click', 'button#deleterow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#idHidden').val(data.id)
    });

});