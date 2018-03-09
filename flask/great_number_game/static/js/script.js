$(document).ready(function(){
    $('#add_guess_box').click(function(){
        var guess_box_text = session['guess_string'];
        var div_data = "";

        console.log("Is this working?:", guess_box_text)

        if ( guess_box_text === "Too low!" || guess_box_text === "Too high!"){
            div_data = '<div class="guess-box" id="red"><p>' + guess_box_text + '</p></div>';
        } else {
            div_data = '<div class="guess-box" id="green"><p>' + guess_box_text + '</p></div>';
        }

        // Add the proper <div></div> to the body of the html file.
        $('#guess_box').append(div_data);
    })

});