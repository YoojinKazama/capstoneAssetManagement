$("#missingForm").on("submit", function(e){

    e.preventDefault();
    form =  { 
        asset_id : $(missing_asset_id).val(),
        remarks: $(missing_remarks).val(),
        missing_date: new Date($(missing_date).val()),
        };

    console.log(sessionStorage.getItem("name"))

        $.ajax({
            url:'/asset_management/api/missing_asset/',
            type: "POST",
            data: JSON.stringify(form),
            dataType: "JSON",
            contentType: "application/json",

            success: function(data){

                events = {
                    asset_id : $(missing_asset_id).val(),
                    event_title : "Lost/Missing",
                    event_message: $(missing_remarks).val() +". Asset lost or missing at "+ moment($(missing_date).val()).format('LL') + ". Updated by " + sessionStorage.getItem("name")
                }

                    $.ajax({
                    url:'/asset_management/api/Event/',
                    type: "POST",
                    data: JSON.stringify(events),
                    dataType: "JSON",
                    contentType: "application/json",

                    success: function(data){
                    console.log("EVENT CREATED")

                    assetDetails()
                    load_event($(missing_asset_id).val())
                    $('#missingModal').modal('hide');
                    toastr.success('Asset edited successfully')
                    }
                })
            }
        })
    
    });

