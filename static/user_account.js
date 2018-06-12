"use strict";

// get all poop images by class name
let poopImages = document.querySelectorAll(".poop_img");
let poopImagesh1 = document.querySelectorAll(".poop_img_h1");
let mouseFunction = function(){
    console.log(this.children[0]);
    this.style.display = "none";
    $(this).siblings().css("display", "none");
    // $(this).parent().siblings().css("display", "inline-block")
    $(this).parent().siblings().each(function(index, val){
        console.log(val);
        $(val).children().css("display", "inline-block");
    });
    // img.children[2].style.display = "inline-block";
    // img.children[3].style.display = "inline-block";
}
// loop through class of poopimages
// for (let img of poopImages) {
    // console.log(img);
    // on page load display h1 tag (children[0]) but
    // on mouseover hide h1 and display the
    // children[1] and children[2] input/img tag
$(".poop_img_h1").mouseenter(mouseFunction);
    // img.addEventListener("mouseover", function(){
    //     console.log("children!!!!");
    //     console.log(this.children);
    //     this.children[0].style.display = "none";
    //     this.children[1].style.display = "none";
    //     this.children[2].style.display = "inline-block";
    //     this.children[3].style.display = "inline-block";
    // });

    // mouseout hides input/img and 
    // displays h1 tag
$(".radio_img").mouseleave(mouseFunction);



    // ("display", "inline-block");    
    // img.children[2].style.display = "none";
    // img.children[3].style.display = "none";   
// }



