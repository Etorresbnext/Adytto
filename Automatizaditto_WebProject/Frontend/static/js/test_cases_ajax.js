import  { ajaxRequest, cleanInputs, resetForm }  from './functions.js';

$(document).ready(function(){

    // INSERTAR
    ajaxRequest(
        'insertTestCaseForm',
        ['iTestCaseName', 'iAzureId', 'iProductId'],
        '/insert/test-case',
        'successOnInsert',
        'addRecordModal',
        ['iTestCaseName', 'iAzureId', 'iAzureId', 'iAzureId', 'iProductId'],
        ['nullTestCaseName', 'nullAzureId', 'nullAzureId', 'nullAzureId', 'nullProductId'],
        ['nullTestCaseName', 'nullAzureId', 'negativeAzureId', 'limitAzureId', 'nullProductId']
    );

    cleanInputs('iTestCaseName', 'nullTestCaseName');
    cleanInputs('iAzureId', 'nullAzureId');
    cleanInputs('iProductId', 'nullProductId');
    resetForm(
        'addRecordModal',
        'insertTestCaseForm',
        ['iTestCaseName', 'iAzureId', 'iProductId'],
        ['nullTestCaseName', 'nullAzureId', 'nullProductId']
    );


    // ACTUALIZAR
    ajaxRequest(
        'updateTestCaseForm',
        ['uHiddenId', 'uTestCaseName', 'uAzureId', 'uProductId'],
        '/update/test-case',
        'successOnUpdate',
        'updateRecordModal',
        ['uTestCaseName', 'uAzureId', 'uAzureId', 'uAzureId', 'uProductId'],
        ['uTestCaseNameError', 'uAzureIdError', 'uAzureIdError', 'uAzureIdError', 'uProductIdError'],
        ['nullTestCaseName', 'nullAzureId', 'negativeAzureId', 'limitAzureId', 'nullProductId']
    );

    cleanInputs('uTestCaseName', 'uTestCaseNameError');
    cleanInputs('uAzureId', 'uAzureIdError');
    cleanInputs('uProductId', 'uProductIdError');
    resetForm(
        'updateRecordModal',
        'updateTestCaseForm',
        ['uTestCaseName', 'uAzureId', 'uProductId'],
        ['uTestCaseNameError', 'uAzureIdError', 'uProductIdError']
    );

});