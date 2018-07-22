$(function() {
    $("#about").hide();
    $("#about-button").click(function () {
        $("#about").toggle(1000);
    });
});

$(function () {
    $("#inp1").hide();
    $("#inp1-button").click(function () {
        if (($("#inp1").css('display') == 'none' && $("#inp2").css('display') == 'none' || $("#inp1").css('display') == 'none')) {
            $(".initial").hide(1000);
        }
        else {
            $(".initial").show(1000);
        }
        $("#inp2").hide(1000);
        $("#inp1").toggle(1000);

    });
});

$(function () {
    $("#inp2").hide();
    $("#inp2-button").click(function () {
        if (($("#inp1").css('display') == 'none' && $("#inp2").css('display') == 'none') || $("#inp2").css('display') == 'none') {
            $(".initial").hide(1000);
        }
        else {
            $(".initial").show(1000);
        }
        $("#inp1").hide(1000);
        $("#inp2").toggle(1000);

    });
});