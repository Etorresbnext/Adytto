$(document).ready(function(){
    var tableName = 'runners-status'
    var table = $('#dataTableGrid').DataTable({

        scrollX: true,

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
            }, 'pageLength']
        },

        "columns": [
            { "data": "id" },
            { "data": "name" },
            { "data": "ip" },
            {
                "data": "connected_led",
                "render": function(data, type, row){
                    if(data){
                        return '<img src="data:image/png;base64,' + data + '" alt="Estado de conexión" style="width: 20px; height: 20px;">';
                    }
                    else{
                        return 'Sin imagen';
                    }
                }
            },
            {
                "data": "last_ping",
                render: function(data){
                    const date = new Date(data);

                    return date.toLocaleString('es-MS', {
                        timezone: 'America/Mexico_City',
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                        hour: '2-digit',
                        minute: '2-digit',
                        second: '2-digit'
                    });
                }
            }
        ]
    });
})