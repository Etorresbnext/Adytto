import  { ajaxRequest, cleanInputs, resetForm }  from './functions.js';

$(document).ready(function(){

    // INSERTAR
    ajaxRequest(
        'insertObjectTypeForm',
        ['iObjTypeName'],
        '/insert/object-type',
        'successOnInsert',
        'addRecordModal',
        ['iObjTypeName', 'iObjTypeName'],
        ['iObjTypeNameError', 'iObjTypeNameError'],
        ['nullObjTypeName', 'duplicateObjTypeName'],
    );


    cleanInputs('iObjTypeName', 'iObjTypeNameError');
    resetForm('addRecordModal', 'insertObjectTypeForm', ['iObjTypeName'], ['iObjTypeNameError']);
});