
// function toggleImage(){
//     let poopImages = document.querySelector(".poop_img");
    
// }


// get all poop images by class name
let poopImages = document.querySelectorAll(".poop_img");

// loop through poopimages
for (let img of poopImages) {
    // console.log(img);
    img.addEventListener("mouseover", function(){
        this.children[0].style.display = "none";
        this.children[1].style.display = "inline-block";
        this.children[2].style.display = "inline-block";
    });

    img.addEventListener("mouseout", function(){
        this.children[0].style.display = "inline-block";
        this.children[1].style.display = "none";
        this.children[2].style.display = "none";
    });    
}
