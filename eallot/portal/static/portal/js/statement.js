$(document).ready(function() {

            var bulkDownload = $("#bulk-query")
             $('select').material_select();
             $('.modal').modal();
             $('.tabs').tabs({
                 swipeable: true
             });
             $(".tabs-content").css({'height':'100vh', 'width':'100%'})
             // $("#summary-table").DataTable()

             bulkDownload.submit(function(e){

                e.preventDefault();
                $.ajax({
                type: bulkDownload.attr('method'),
                url: bulkDownload.attr('action'),
                data:bulkDownload.serialize(),
                dataType:'json',
                success: function(data) {


            },
                error: function(data) {
                    Materialize.toast('error Try again!', 2000 )
                },
                })

             });




         });


