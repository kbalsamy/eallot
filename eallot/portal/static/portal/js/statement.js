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


    $("#form-update-db").on('submit', function(e){

        e.preventDefault()

        var d = new Date()

        var year = d.getFullYear().toString();
        var month = "0"+ d.getMonth().toString()
        var csrf = $("input[name='csrfmiddlewaretoken']").val()

        $.ajax({

            type:'get',
            url:"statement/database",
            data: {'month':month, 'year':year, 'csrfmiddlewaretoken':csrf},
            success:function(data){

                console.log(data)
            },


        });
    });

});





