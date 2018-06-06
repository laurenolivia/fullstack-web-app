"use strict";

// get all poop images by class name
let poopImages = document.querySelectorAll(".poop_img");

let message = document.getElementById("messageDisplay").innerHTML;
let headlines = ["cancer is on the rise", "healthy food means healthy poop",
                "more young people are dying of colon cancer"]


// loop through class of poopimages
for (let img of poopImages) {
    // console.log(img);
    // on page load display h1 tag (children[0]) but
    // on mouseover hide h1 and display the
    // children[1] and children[2] input/img tag
    img.addEventListener("mouseover", function(){
        this.children[0].style.display = "none";
        this.children[1].style.display = "inline-block";
        this.children[2].style.display = "inline-block";
    });

    // mouseout hides input/img and 
    // displays h1 tag
    img.addEventListener("mouseout", function(){
        this.children[0].style.display = "inline-block";
        this.children[1].style.display = "none";
        this.children[2].style.display = "none";
    });    
}

// SCROLL THROUGH ARRAY OF NEWS HEADLINES ON HOMEPAGE

function getHeadline(){
    for (let i of headlines){
        message.text = i;
        console.log(i);
    }

};







