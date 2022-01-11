// function toggle(x) {
//     x.classList.toggle("change");
// 	$('#nav').slideToggle(200);
//     // var menuBox = document.getElementById('nav'); 
//     // if(menuBox.style.display == "block") { // if is menuBox displayed, hide it
//     //     menuBox.style.display = "none";
//     //   }
//     //   else { // if is menuBox hidden, display it
//     //     menuBox.style.display = "block";
//     //   }
//     }


	$(window).on('load', function () {
		setTimeout(removeLoader,1000);
  	}); 
	  function removeLoader(){
		$('#loading').hide();
	}
	
	$(document).ready(function(){
		$(".menu-btn").click(function(){
		$(this).toggleClass("change");
		$('.navbar-collapse').slideToggle(-1);
		});
	});
    $(document).ready(function(){
		$('.menu-1').click(function(){
			$('#drop-1').slideToggle(200);
		});
	});
    $(document).ready(function(){
		$('.menu-2').click(function(){
			$('.drop-2').slideToggle();
		});
	});
    $(document).ready(function(){
		$('.menu-3').click(function(){
			$('.drop-3').slideToggle();
		});
	});
    $(document).ready(function(){
		$('.menu-4').click(function(){
			$('.drop-4').slideToggle();
		});
	});
	
	$(document).ready(function(){
		$('#overview-btn').click(function(){
			$('.overview').fadeIn();
			$('.course-cover').hide();
			$('.career-opportunity').hide();
		});
	});
	$(document).ready(function(){
		$('#course-cover-btn').click(function(){
			$('.course-cover').fadeIn();
			$('.overview').hide();
			$('.career-opportunity').hide();
		});
	});
	$(document).ready(function(){
		$('#career-opportunity-btn').click(function(){
			$('.career-opportunity').fadeIn();
			$('.overview').hide();
			$('.course-cover').hide();
		});
	});
	
	$(document).ready(function(){
		$('.course-cover-main-title').click(function(){
			$(this).siblings().slideToggle();
		});
	});

	$(document).ready(function(){
		$('#enrollment').click(function(){
			$('.enroll-form-outer').fadeIn();
			$('.enroll-frm').fadeIn();
		});
		$('#about-us-enroll').click(function(){
			$('.enroll-form-outer').fadeIn();
			$('.enroll-frm').fadeIn();
		});
	});
	
	$(document).ready(function(){
		$('.enroll-form-close').click(function(){
			$('.enroll-form-outer').fadeOut();
			$('.enroll-frm').fadeOut();
		});
	});
	
	$(document).ready(function(){
		$('#banner-close').click(function(){
			$('.new-batch-banner').fadeOut();
		});
	});
	$('.post-form').on('submit',async function(event){
		event.preventDefault();
		$('.form-check').hide();
		$('.form-submit-loader').fadeIn();
		$('.form-loader').addClass('active');
		console.log("form submitted!")  // sanity check
		await mail_ajax();
		$('.form-check').show();
		$('.form-check').addClass('active');
		$('.form-thank').fadeIn();
		console.log("end")
	});
	
		
	  
	


