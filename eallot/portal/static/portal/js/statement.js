$(document).ready(function() {

    $("#summary-table").DataTable({
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

    $('select').formSelect();
    $('.modal').modal();
    $('.tabs').tabs();
    $(".tabs-content").css({ 'height': '100vh', 'width': '100%' })
    $(".dataTables_filter").css({ 'display': 'flex', 'justify-content': 'flex-end', 'align-content': 'flex-end' })

});





