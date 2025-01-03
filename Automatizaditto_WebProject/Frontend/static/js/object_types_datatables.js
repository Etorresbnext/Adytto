import { displayTableData, hiddenInputId, getRecordData } from './functions.js';

$(document).ready(function(){

    var table = displayTableData(
        'object-types',
        ['ID', 'Nombre']
    );

    hiddenInputId('uHiddenId', 'uHiddenId', 'updateObjectTypeForm');
    hiddenInputId('dHiddenId', 'dHiddenId', 'deleteObjectTypeForm');


    getRecordData('button#selectrow', table, 
        ['uHiddenId', 'uObjectTypeId', 'uObjectTypeName'],
        ['ID', 'ID', 'Nombre']
    );
    getRecordData('button#deleterow', table, ['dHiddenId'], ['ID']);

});