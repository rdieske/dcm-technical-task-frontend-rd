$(document).ready(function () {
    $('#detailModal').on('show.bs.modal', function(e) {
        var testId = $(e.relatedTarget).data().testid;
        var dataUrl = "/api/v1/test-run/" + testId;
        $.ajax({
            type: "GET",
            url: dataUrl,
            dataType: 'json',
            success:function(dataResponse) {
                $('#idField').html(dataResponse.id);
                $('#reqField').html(dataResponse.requested_by);
                $('#envField').html(dataResponse.env_name);
                
                
                var path_names = $.map(dataResponse.path_names, function(item){
                    return item.path + '\n';
                })

                $('#pathField').html(path_names);
                $('#stateColumn').removeClass();
                $('#stateColumn').addClass(dataResponse.status);
                $('#stateField').html(dataResponse.status);

                $('#logsField').html(dataResponse.logs);
            }
        });
    });
});