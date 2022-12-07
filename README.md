# VHGshop
Bài này là của Vi Hoàng Gia

Thời gian : 11:34pm
Ngày : 6/12/2022
tgian video : 4:05:31


code carousel trong myscript.js

$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 2,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 4,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})