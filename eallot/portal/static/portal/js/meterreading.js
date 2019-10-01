$(document).ready(function() {


    $("#meter-table-readings").DataTable({
        "ordering": false,
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

    $('select').formSelect();
    $('.modal').modal();
    $('.tabs').tabs();
    $(".tabs-content").css({ 'height': '100vh', 'width': '100%' })
    $(".dataTables_paginate").css({ "width": '400px','display': 'flex', 'justify-content': 'space-between', 'align-content': 'flex-end' })



});
