$(document).ready(function() {

             var sgForm = $("#add-sg-form");
             var sgForm_delete = $("#delete-sg-form");
             var serviceMapping = $("#service-mapping");
             var displayService = $("#display-service");
             var serviceUpdate = $("#service-update");
             $('select').material_select();
             $('.modal').modal();
             $('#servicelist-table').DataTable(
                {
                     "searching": false,
                     "ordering": false,
                });
             $(".dataTables_info").css("font-size", "12px");
             $(".dataTables_paginate").css("font-size", "12px");



             // handle post request for adding the service group into db
             sgForm.submit(function(e){
                e.preventDefault();

                $.ajax({
                    type:sgForm.attr('method'),
                    url:sgForm.attr('action'),
                    data:sgForm.serialize(),
                    success:function(data){
                         Materialize.toast(data, 2000)
                          $('.modal').modal('close');
                          location.reload();

                    },
                    error: function(data) {
                        Materialize.toast('connection timeout')
            },

                })

             });

             //delete service group

             sgForm_delete.submit(function(e){
                e.preventDefault();

                $.ajax({
                    type:sgForm_delete.attr('method'),
                    url:sgForm_delete.attr('action'),
                    data:{'name':$("#del-name").val()},
                    success:function(data){
                         Materialize.toast(data, 2000)
                          $('.modal').modal('close');
                          location.reload();
                    },
                    error: function(data) {
                        Materialize.toast('connection timeout')
            },

                })

             });

             // service mapping post requests handling

             serviceMapping.submit(function(e){
                e.preventDefault();
                $.ajax({
                    type:serviceMapping.attr('method'),
                    url:serviceMapping.attr('action'),
                    data:serviceMapping.serialize(),
                    success:function(data){
                         Materialize.toast(data, 2000)
                          $('.modal').modal('close');
                          location.reload();
                    },
                    error: function(data) {
                        Materialize.toast('connection timeout')
            },

                });

             });


             // service update requests handler




             // display selected service in the table



             // function for checkbox selects all
             $("#all").change(function() {

                 if (this.checked) {
                     $("[name='cell']").each(function() {
                         $(this).prop('checked', true)
                     })
                 } else {
                     $("[name='cell']").each(function() {
                         $(this).prop('checked', false)
                     })

                 }

             });

             // deactivate / activate

             $('input[name=cell]').change(function() {
                 if ($(this).is(':checked')) {

                     $("#edit-btn").removeClass('disabled')
             $("#delete-btn").removeClass('disabled')

                 } else {
                     // Checkbox is not checked..
                     $("#edit-btn").addClass('disabled')
             $("#delete-btn").addClass('disabled')
                 }
             });


             //function for checkbox - grab its siblings val

             $("[name='cell']").click(getValues);


         });

         function getValues() {

             var values = []

             $.each($("input[name='cell']:checked").closest("td").siblings("td"),
                 function() {

                     values.push($(this).text());
                 });

             $("[name='id']").each(function() {
                 $(this).val(values[0])
             });

             $("[name='serviceNumber']").each(function() {
                 $(this).val(values[2])
             });

             $("#zonal").val(values[3]);


             Materialize.updateTextFields();


        }
