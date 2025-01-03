$(document).ready(function(){
    var tableName = 'users';
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
                            $('#insert_new_user_modal').modal('show');
                        }
                    }
                ]
            }, 'paging'],
        },


        "columns": [
            {
                "data": null,
                "defaultContent": '<button id="selectrow" type="button" data-bs-toggle="modal" data-bs-target="#update_user_modal" style="border: none; background-color: transparent;"><img src="../static/images/editar.png" width="24" height="24"></button>'
            },
            {
                "data": null,
                "defaultContent": '<button id="deleterow" type="button" data-bs-toggle="modal" data-bs-target="#delete_user_modal" style="border: none; background-color: transparent;"><img src="../static/images/trash.png" width="24" height="24"></button>'
            },
            { "data": "ID" },
            { "data": "Nombre(s)" },
            { "data": "Apellido(s)" },
            { "data": "Correo Electrónico" },
            { "data": "Perfil" }
        ]
    });

    var hidden_id_input = document.createElement('input');
    hidden_id_input.type = 'hidden';
    hidden_id_input.id = 'updateID_hidden';
    hidden_id_input.name = 'updateID_hidden';
    document.querySelector('#updateUserForm').appendChild(hidden_id_input)

    $('#dataTableGrid tbody').on('click', 'button#selectrow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#updateID_hidden').val(data.ID)
        $('#updateUserID').val(data.ID)
        $('#updateUserName').val(data["Nombre(s)"])
        $('#updateUserLastName').val(data["Apellido(s)"])
        $('#updateUserEmail').val(data["Correo Electrónico"])
        $('#updateUserProfile').val(data["ID Perfil"])
    });




    /* Actualizar Contraseña de Usuario */
    var hidden_id_pass_input = document.createElement('input');
    hidden_id_pass_input.type = 'hidden';
    hidden_id_pass_input.id = 'updateUserPassID';
    hidden_id_pass_input.name = 'updateUserPassID';
    document.querySelector('#updateUserPassForm').appendChild(hidden_id_pass_input)

    $('#update_user_modal form').on('click', 'button#updateUserPass', function(){
        var userID = $('#updateID_hidden').val();
        $('input#updateUserPassID').val(userID)
    });

    
    /* Borrar Usuario */
    var hidden_delete_row = document.createElement('input');
    hidden_delete_row.type = 'hidden';
    hidden_delete_row.id = 'idHidden';
    hidden_delete_row.name = 'idHidden';
    document.querySelector('#deleteUserForm').appendChild(hidden_delete_row)


    $('#dataTableGrid tbody').on('click', 'button#deleterow', function(){
        var data = table.row($(this).parents('tr')).data();
        $('input#idHidden').val(data.ID)
    });

});