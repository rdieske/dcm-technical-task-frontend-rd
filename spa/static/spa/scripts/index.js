//inspired from: https://docs.djangoproject.com/en/3.2/ref/csrf/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function () {
    renderTable();
    setInterval(function () {
        renderTable();
    }, 5000);

    $('#testRunRequestForm').submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: '/api/v1/test-run',
            dataType: 'json',
            data:$('#testRunRequestForm').serialize(),
            success:function(){
                renderTable()
            }
        });
    });
});

function renderTable()
{
    $.ajax({
        type: "GET",
        url: "",
        dataType: 'json',
    }).done(function(data) {
        $('#testRunRequestsContainer').html(data.html_table);
    });

}