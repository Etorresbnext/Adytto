$(document).ready(function(){
    $.ajax({
        url: '/select/processor_brands',
        type: 'GET',
        success: function(data){
            var select = $('.processorBrand');
            data.forEach(function(item){
                select.append(new Option(item['Marca'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Tipos de Objetos: ", error);
        }
    });

    $.ajax({
        url: '/select/processor-frequencies',
        type: 'GET',
        success: function(data){
            var select = $('.freqUnits');
            data.forEach(function(item){
                select.append(new Option(item['Nombre'], item['Nombre']));
            });
        },
        error: function(error){
            console.log("Error al obtener Unidades: ", error);
        }
    });

    $.ajax({
        url: '/select/processor-architectures',
        type: 'GET',
        success: function(data){
            var select = $('.processorArch');
            data.forEach(function(item){
                select.append(new Option(item['Nombre'], item['ID']));
            });
        },
        error: function(error){
            console.log("Error al obtener Unidades: ", error);
        }
    });
});