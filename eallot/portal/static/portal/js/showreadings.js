
$(document).ready(function(){

    $('select').formSelect();
    $('.modal').modal();
    $('.tabs').tabs();
    $('.tabs').tabs('select', 'customized-download');
    $(".tabs-content").css({ 'height': '100vh', 'width': '100%' })
    $("#monthly-readings").DataTable({
        "ordering": false,
        "scrollX": true,
        dom: 'Bfrtip',
        "buttons": {
            "dom": {
                "button": {
                    "tag": "button",
                    "className": "waves-effect waves-light btn"
                }
            },
            "buttons": ['print','excelHtml5', 'pdfHtml5']
        }
    });


    $(".dataTables_paginate").css({'width':'350px', 'display': 'flex', 'justify-content': 'space-between', 'align-content': 'flex-end' })


});
