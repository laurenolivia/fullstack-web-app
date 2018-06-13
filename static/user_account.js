"use strict";

// get all poop images by class name
// let poopImages = document.querySelectorAll(".poop_img");
// let poopImagesh1 = document.querySelectorAll(".poop_img_h1");

let mouseFunction = function(){
    this.style.display = "none";
    $(this).siblings().css("display", "inline-block");
    
    // $(this).siblings().each(function(index, val){
    //     console.log(val);
    //     $(val).children().css("display", "inline-block");
    // });
};

$(".descriptor").mouseenter(mouseFunction);

$(".descriptorSibling").mouseleave(mouseFunction);




