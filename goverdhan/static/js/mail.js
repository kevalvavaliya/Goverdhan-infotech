
async function mail_ajax() {
    console.log("Mail is working!") // sanity check
    await $.ajax({
        url : "mailsent/", // the endpoint
        type : "POST", // http method
        data : { 
                name : $('#nm').val(),
                email : $('#em').val(),
                message : $('#msg').val(),
                number :$('#num').val(),
                subject : $('#sub').val(),
                csrfmiddlewaretoken: $('#tk').val()
            }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#nm').val('success'); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            return true;
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            return false;
        }
    });
};