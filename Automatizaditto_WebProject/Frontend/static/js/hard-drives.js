$(document).ready(function(){
    $.ajax({
        url: '/select/hard-drives_brands',
        type: 'GET',
        success: function(data){
            var select = $('.hardDriveBrand');
            data.forEach(function(item){
                select.append(new Option(item['Marca'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Marcas: ", error);
        }
    });

    $.ajax({
        url: '/select/hard-drives_types',
        type: 'GET',
        success: function(data){
            var select = $('.hardDriveType');
            data.forEach(function(item){
                select.append(new Option(item['Nombre'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Tipos de Discos Duros: ", error);
        }
    });

    $.ajax({
        url: '/select/hard-drives_storage',
        type: 'GET',
        success: function(data){
            var select = $('.storageUnits');
            data.forEach(function(item){
                select.append(new Option(item['Nombre'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Unidades: ", error);
        }
    });
});