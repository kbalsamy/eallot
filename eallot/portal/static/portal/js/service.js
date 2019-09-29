    $(document).ready(function() {



    var sgForm = $("#add-sg-form");
    var sgForm_delete = $("#delete-sg-form");
    var serviceMapping = $("#service-mapping");
    var displayService = $("#display-service");
    var serviceUpdate = $("#service-update");
    var serviceDelete = $("#serviceDelete");
    $('#servicelist-table').DataTable({
        "searching": false,
        "ordering": false,
        "pagingType": "full_numbers"

    });
    $('select').formSelect();
    $('.modal').modal();

    $(".dataTables_info").css("font-size", "12px");


    // handle post request for adding the service group into db
    sgForm.submit(function(e) {
        e.preventDefault();

        $.ajax({
            type: sgForm.attr('method'),
            url: sgForm.attr('action'),
            data: sgForm.serialize(),
            success: function(data) {
                M.toast({html:data})
                $('.modal').modal('close');
                setTimeout(function(){ location.reload(); }, 1000);

            },
            error: function(data) {
                M.toast({html:'Connection timeout!!'})
            },

        })

    });

    //delete service group

    sgForm_delete.submit(function(e) {
        e.preventDefault();

        $.ajax({
            type: sgForm_delete.attr('method'),
            url: sgForm_delete.attr('action'),
            data: { 'name': $("#del-name").val() },
            success: function(data) {
                M.toast({html:data})
                $('.modal').modal('close');
                setTimeout(function(){ location.reload(); }, 1000);
            },
            error: function(data) {
                M.toast({html:"Error, Try again!"});
                $('.modal').modal('close');
            },

        })

    });

    // service mapping post requests handling

    serviceMapping.submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: serviceMapping.attr('method'),
            url: serviceMapping.attr('action'),
            data: serviceMapping.serialize(),
            success: function(data) {
                M.toast({html:data})
                $('.modal').modal('close');
                setTimeout(function(){ location.reload(); }, 1000);
            },
            error: function(data) {
                M.toast({html:data})
            },

        });

    });


    // service update requests handler

    serviceUpdate.submit(function(e){
        e.preventDefault();
        $.ajax({

            type: serviceUpdate.attr('method'),
            url: serviceUpdate.attr('action'),
            data: serviceUpdate.serialize(),
            success: function(data) {
                M.toast({html:data})
                $('.modal').modal('close');
                setTimeout(function(){ location.reload(); }, 1000);


            },
            error: function(data) {
                M.toast({html:'error! Fill all options and try again'})
               ;
            },
        });

    });

    // service delete Handler


    serviceDelete.submit(function(e){
        e.preventDefault();
        $.ajax({

            type: serviceDelete.attr('method'),
            url: serviceDelete.attr('action'),
            data: {'number': $("#serviceDelete input[name='serviceNumber']").val()},
            success: function(data) {
                M.toast({html:data})
                $('.modal').modal('close');
                setTimeout(function(){ location.reload(); }, 1000);

            },
            error: function(data) {
                M.toast({html:"Error, Try again!"})
               ;
            },
        });

    });


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
    //to be worked out
    // $('#zonal option').filter(function() {
    //     return this.value == values[3];
    // }).prop("selected", true);


    M.updateTextFields();


}
