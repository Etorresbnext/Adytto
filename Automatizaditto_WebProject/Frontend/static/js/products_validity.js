import  { showErrors, cleanInputs, resetForm, getFormData, successResponse }  from './functions.js';

$(document).ready(function(){

    $('#insertProductForm').on('submit', function(form){
        form.preventDefault();

        var formData = getFormData(['productName', 'productDesc']);

        $.ajax({
            type: 'POST',
            url: '/insert/product',
            data: formData,
            success: function(response){   
                successResponse(response, 'successOnInsert', 'addRecordModal');
            },
            error: function(xhr){
                if(xhr.status === 404){
                    var validity_errors = xhr.responseJSON;
                    console.log(validity_errors);

                    if(validity_errors.nullProductName){
                        showErrors('productName', 'productNameNull', validity_errors.nullProductName);
                    }
                    if(validity_errors.duplicateProductName){
                        showErrors('productName', 'productNameNull', validity_errors.duplicateProductName);
                    }
                    if(validity_errors.nullProductDesc){
                        showErrors('productDesc', 'productDescNull', validity_errors.nullProductDesc);
                    }
                }
            }
        });
    });


    cleanInputs('productName', 'productNameNull');
    cleanInputs('productDesc', 'productDescNull');
    resetForm('addRecordModal', 'insertProductForm', ['productName', 'productDesc'], ['productNameNull', 'productDescNull']);


    $('#updateProductForm').on('submit', function(updForm){
        updForm.preventDefault();
        
        var updFormData = getFormData(['uHiddenId', 'uProductName', 'uProductDesc']);

        $.ajax({
            type: 'POST',
            url: '/update/product',
            data: updFormData,
            success: function(response){
                successResponse(response, 'successOnUpdate', 'updateRecordModal');
            },
            error: function(xhr){
                if(xhr.status === 404){
                    var update_errors = xhr.responseJSON;
                    console.log(update_errors)

                    if(update_errors.nullProductName){
                        showErrors('uProductName', 'uProductNameNull', update_errors.nullProductName);
                    }
                    if(update_errors.duplicateProductName){
                        showErrors('uProductName', 'uProductNameNull', update_errors.duplicateProductName);
                    }
                    if(update_errors.nullProductDesc){
                        showErrors('uProductDesc', 'uProductDescNull', update_errors.nullProductDesc);
                    }
                }
            }
        });
    });


    cleanInputs('uProductName', 'uProductNameNull');
    cleanInputs('uProductDesc', 'uProductDescNull');
    resetForm('updateRecordModal', 'updateProductForm', ['uProductName', 'uProductDesc'], ['uProductNameNull', 'uProductDescNull'])


    /* SE USARÁ DESPUÉS */
    /*$('#deleteProductForm').on('submit', function(delForm){
        delForm.preventDefault();

        var delFormData = {
            idHidden: $('#idHidden').val()
        };

        $.ajax({
            type: 'POST',
            url: '/delete/delete_product',
            data: delFormData,
            success: function(response){
                successResponse(response, 'successOnDelete', 'deleteRecordModal');
            }
        });
    });*/
});