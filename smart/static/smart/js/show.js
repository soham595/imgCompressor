$(function () {
    $("#inp1").hide();
    $("#trainpLiver").slideDown(1000);
    $(".inp1-button").click(function () {
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
    $(".inp2-button").click(function () {
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

$(function() {
    $("#trainpLiver").hide();
    $("#trainpBC").hide();
    let particlest = new Particles('#trainLiver');
    let particlesbc = new Particles('#trainBC');
    let particlest2 = new Particles('#trainhLiver');
    let particlesbc2 = new Particles('#trainhBC');
    $("#trainLiver").click(function () {
        $("#trainhLiver").hide(1000);
        particlest2.disintegrate();
        particlesbc2.disintegrate();
        particlest.disintegrate();
        particlesbc.disintegrate();
        $("#trainpLiver").slideDown(1000);
    });
    $("#trainBC").click(function () {
        $("#trainhBC").hide(1000);
        particlest2.disintegrate();
        particlesbc2.disintegrate();
        particlest.disintegrate();
        particlesbc.disintegrate();
        $("#trainpLiver").slideDown(1000);
    });
});