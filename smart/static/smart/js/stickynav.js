window.onscroll = function() {myFunction()};

let navbar = document.getElementById("nav-bar");

let sticky = navbar.offsetTop;
console.log(sticky);

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

$(document).ready(function() {
    $('.nav li a').click(function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            let $target = $(this.hash);
            $target = $target.length && $target || $('[name=' + this.hash.slice(1) + ']');
            if ($target.length) {
                let targetOffset = $target.offset().top;
                $('html, body').animate({
                    scrollTop: targetOffset
                }, 2000);
                return false;
            }
        }
    });
});