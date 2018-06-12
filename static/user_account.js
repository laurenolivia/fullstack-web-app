"use strict";

// get all poop images by class name
let poopImages = document.querySelectorAll(".poop_img");
let poopImagesh1 = document.querySelectorAll(".poop_img_h1");
let mouseFunction = function(){
    this.style.display = "none";
    $(this).siblings().css("display", "none");
    $(this).parent().siblings().each(function(index, val){
        console.log(val);
        $(val).children().css("display", "inline-block");
    });
}

$(".poop_img_h1").mouseenter(mouseFunction);

$(".radio_img").mouseleave(mouseFunction);




