
$(".slider2").owlCarousel({
loop: true,
autoplay: true,
autoplayTimeout: 1000, //2000ms = 2s;
autoplayHoverPause: true,
});

function closeOverLay(){
    document.getElementsByClassName("ppr")[0].style.display="none";
}
function rightScrolling(elem){
    document.getElementById("list").scrollBy(4,0);
}
function leftScrolling(elem){
    document.getElementById("list").scrollBy(-4,0);
}
function keepScrolling(elem, action) {
    var timer;
    var repeat = function () {
        action();
        timer = setTimeout(repeat, 1);
    }
    elem.onmousedown = function() {
        repeat();
    }
    elem.onmouseout = function(){
        clearTimeout(timer);
    }
    elem.onmouseup = function () {
        clearTimeout(timer);
    }
};
