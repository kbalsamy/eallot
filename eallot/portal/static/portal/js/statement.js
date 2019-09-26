$(document).ready(function() {

    $('select').material_select();
    $('.modal').modal();
    $('.tabs').tabs();
    $(".tabs-content").css({ 'height': '100vh', 'width': '100%' })
    $("#summary-table").DataTable({


    });

    $(".dataTables_filter").css({'display': 'flex', 'justify-content':'flex-end', 'align-content':'flex-end'})

});
