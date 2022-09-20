let SlideIndex=0;
showSlides();

function showSlides() {
	let slides=document.getElementsByClassName("mySlide");
	for (var i = 0; i < slides.length; i++) {
			slides[i].style.display="none";
		}
		SlideIndex++;
		if (SlideIndex>slides.length) {SlideIndex=1;}
		slides[SlideIndex-1].style.display="block";
		setTimeout(showSlides,2000);	
}