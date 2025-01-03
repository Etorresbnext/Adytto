//SELECCIONAR REGISTROS DE UNA TABLA

$('#productsTable tbody').on('click', 'tr', function(){
    if($(this).hasClass('selected')){
        $(this).removeClass('selected');
    }
    else{
        table.$('tr.selected').removeClass('selected');
        $(this).addClass('selected');
    }
});


//MOSTRAR INFORMACIÓN DEL REGISTRO SELECCIONADO EN UN FORMULARIO
$('#selectrow').on('click', function() {
var data = table.row('.selected').data();
if (data) {
    // Llena el formulario del modal con los datos de la fila seleccionada
    $('#editID').val(data.ID);
    $('#editName').val(data.Nombre);
    $('#editCode').val(data.Código);
    $('#editDescription').val(data.Descripción);
    $('#editActive').prop('checked', data.Activo);

    // Muestra el modal
    $('#updateRecordModal').modal('show');
} else {
    alert('No hay fila seleccionada');
}
});


//CHECK ACTIVO E INACTIVO
if(data.Activo === true || data.Activo === 'true'){
    $('#updateActive').prop('checked', true);
}
else{
    $('#updateActive').prop('checked', false);
}