import { displayTableData, hiddenInputId, getRecordData, getDropdownOptions } from './functions.js';

$(document).ready(function(){
  
    var table = displayTableData(
        'test-cases',
        ['ID', 'Nombre', 'ID Azure', 'Producto']
    );


    getDropdownOptions('products', 'dropDownProducts', 'Nombre', 'ID');


    hiddenInputId('uHiddenId', 'uHiddenId', 'updateTestCaseForm');
    hiddenInputId('dHiddenId', 'dHiddenId', 'deleteTestCaseForm');

    
    getRecordData('button#selectrow', table, 
        ['uHiddenId', 'uTestCaseId', 'uTestCaseName', 'uAzureId', 'uProductId'],
        ['ID', 'ID', 'Nombre', 'ID Azure', 'ID Producto']
    );
    getRecordData('button#deleterow', table, ['dHiddenId'], ['ID']);

});