$(document).ready(function() {
    var message = "Hello Python. How are you?"; // Just for the example

    $("#message").val(message);

    $("#but1").click(function() {
        $.ajax({
            type: "POST",
            //url: "/aza",
            url: "/a",
            data: {"jsText": message},
            cache: false,
            success: function(data, textStatus, jqXHR) {
                $('#wrap').append(data.paragraph);
                $('#' + data.paragraph_id).append(data.letter)
                //$('.cloundcontainer').append('<div class="cloud"><p>'+$('#cloudName').val()+'</p><p>'+$('#cloudFamily').val()+'</p></div>');
                //alert(data);    //Object
                //alert(jqXHR);   //Object
            },
            error: function(jqXHR, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });

    });
});