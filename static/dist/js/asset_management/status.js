//////////////////// MISSING

$("#missingForm").on("submit", function(e){

    var current = $(current_status).val()
    console.log(current)

    var replace_status = ""

    if (current == "Sold"){
        replace_status = "sell_asset"
    }
    console.log(replace_status)
    
    e.preventDefault();
    form =  { 
        created_by : $(created_by_id).val(),
        asset_id : $(missing_asset_id).val(),
        remarks: $(missing_remarks).val(),
        missing_date: new Date($(missing_date).val()),
        };

        $.ajax({
            url:'/asset_management/api/missing_asset/',
            type: "POST",
            data: JSON.stringify(form),
            dataType: "JSON",
            contentType: "application/json",

            success: function(data){

                if (replace_status != ""){
                    $.ajax({
                        url:'/asset_management/api/'+ replace_status +'/'+ $(missing_asset_id).val(),
                        type: "DELETE",
                        dataType: "JSON",
                        contentType: "application/json"
                    })
                }

                events = {
                    asset_id : $(missing_asset_id).val(),
                    event_title : "Lost/Missing",
                    event_message: $(missing_remarks).val() +". Asset lost or missing on "+ moment($(missing_date).val()).format('LL') + ". Updated by " + sessionStorage.getItem("name")
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

//////////////////// SELL

$("#sellForm").on("submit", function(e){

    var current = $(current_status).val()
    console.log(current)

    var replace_status = ""

    if (current == "Missing"){
        replace_status = "missing_asset"
    }

    e.preventDefault();
    form =  { 
        created_by : $(created_by_id).val(),
        asset_id : $(sell_asset_id).val(),
        sell_to : $(sell_to).val(),
        sell_to_contact : $(sell_to_contact).val(),
        sell_to_email : $(sell_to_email).val(),
        sell_date : new Date($(sell_date).val()),
        sell_price : $(sell_price).val(),
        remarks: $(sell_remarks).val(),
        };
        
        $.ajax({
            url:'/asset_management/api/sell_asset/',
            type: "POST",
            data: JSON.stringify(form),
            dataType: "JSON",
            contentType: "application/json",

            success: function(data){

                if (replace_status != ""){
                    $.ajax({
                        url:'/asset_management/api/'+ replace_status +'/'+ $(sell_asset_id).val(),
                        type: "DELETE",
                        dataType: "JSON",
                        contentType: "application/json"
                    })
                }

                events = {
                    asset_id : $(missing_asset_id).val(),
                    event_title : "Sold",
                    event_message: $(sell_remarks).val() +". Asset sold on "+ moment($(sell_date).val()).format('LL') +
                                                             " at ₱"+ $(sell_price).val() + " to " +$(sell_to).val() +
                                                             ". Contact: "+ $(sell_to_contact).val() + ". Email: " + $(sell_to_email).val() +
                                                             ". Updated by " + sessionStorage.getItem("name")
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
                    $('#sellModal').modal('hide');
                    toastr.success('Asset edited successfully')
                    }
                })
                
            }
        })
    
    });
    
