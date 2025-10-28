$(document).foundation()


function draw_cards() {
    console.log("clicked");
    const number_select = document.getElementById("card_number_select");
    const cards_to_draw = number_select.value;
    console.log(cards_to_draw);
    const the_form = document.getElementById("draw_cards_form");
    the_form.submit();

}