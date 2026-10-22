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

    slides[index].classList.add("active");
    dots[index].classList.add("active-dot");

    currentSlide = index;
}

function nextSlide(){

    currentSlide++;

    if(currentSlide >= slides.length){
        currentSlide = 0;
    }

    showSlide(currentSlide);
}

function prevSlide(){

    currentSlide--;

    if(currentSlide < 0){
        currentSlide = slides.length - 1;
    }

    showSlide(currentSlide);
}

document.querySelector(".next").addEventListener("click", nextSlide);

document.querySelector(".prev").addEventListener("click", prevSlide);

setInterval(nextSlide,6000);