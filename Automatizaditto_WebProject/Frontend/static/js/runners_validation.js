$(document).ready(function(){
    $('#insertRunnerForm').on('submit', function(e) {
        e.preventDefault();

        var formData = {
            runnerName: $('#runnerName').val(),
            runnerDesc: $('#runnerDesc').val(),
            runnerIp: $('#runnerIp').val(),
            runnerHardConf: $('#runnerHardConf').val(),
            runnerSoftConf: $('#runnerSoftConf').val()
        };

        $.ajax({
            type: 'POST',
            url: '/insert_runner',
            data: formData,
            success: function(response) {
                window.location.href = response.redirect_url;  // Redirecciona si es necesario
            },
            error: function(xhr) {
                if (xhr.status === 404) {
                    var errorMessage = xhr.responseJSON.message;
                    $('#runnerNameNull').text(errorMessage);
                }
            }
        });
    });
});