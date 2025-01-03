import { displayTableData, hiddenInputId, getRecordData } from './functions.js';

$(document).ready(function() {

    var table = displayTableData(
        'products',
        ['ID', 'Nombre', 'Descripción', 'Código']
    );

    hiddenInputId('uHiddenId', 'uHiddenId', 'updateProductForm');
    hiddenInputId('dHiddenId', 'dHiddenId', 'deleteProductForm');


    getRecordData('button#selectrow', table, 
        ['uHiddenId', 'uProductId', 'uProductName', 'uProductDesc'],
        ['ID', 'ID', 'Nombre', 'Descripción']
    );
    getRecordData('button#deleterow', table, ['dHiddenId'], ['ID']);
});