$(document).ready(function() {

    $('select').material_select();
    $('.modal').modal();
    $('.tabs').tabs();
    $(".tabs-content").css({ 'height': '100vh' })
    $("#summary-table").DataTable({
         dom: 'Bfrtip',
         buttons: [
        'copyHtml5',
        'excelHtml5'

    ]
    });


});
