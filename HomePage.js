const slides = document.querySelectorAll(".slide");
const dots = document.querySelectorAll(".dot");

let currentSlide = 0;

function showSlide(index){

    slides.forEach(slide =>
        slide.classList.remove("active")
    );

    dots.forEach(dot =>
        dot.classList.remove("active-dot")
    );
