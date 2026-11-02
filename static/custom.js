(function() {
	'use strict';

	/*----------------------------------------
		Detect Mobile
	----------------------------------------*/
	var isMobile = {
		Android: function() {
			return navigator.userAgent.match(/Android/i);
		},
		BlackBerry: function() {
			return navigator.userAgent.match(/BlackBerry/i);
		},
		iOS: function() {
			return navigator.userAgent.match(/iPhone|iPad|iPod/i);
		},
		Opera: function() {
			return navigator.userAgent.match(/Opera Mini/i);
		},
		Windows: function() {
			return navigator.userAgent.match(/IEMobile/i);
		},
		any: function() {
			return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
		}
	};

	/*----------------------------------------
		Navigation & Smooth Scrolling
	----------------------------------------*/
	var OnePageNav = function() {
		var navToggler = $('.navbar-toggler');
		var navCollapse = $('#navbarsExample09');

		$("a.smoothscroll[href^='#'], #pb-navbar ul li a[href^='#']").on('click', function(e) {
			var hash = this.hash;
			if (!hash || !$(hash).length) return;

			e.preventDefault();
			var targetOffset = Math.max(0, $(hash).offset().top - 70);

			$('html, body').animate({
				scrollTop: targetOffset
			}, 700, 'easeInOutExpo', function(){
				if (history.pushState) {
					history.pushState(null, null, hash);
				} else {
					window.location.hash = hash;
				}
			});

			if (navCollapse.hasClass('show')) {
				navToggler.click();
			}
		});
	};

	/*----------------------------------------
		Navbar Scroll State
	----------------------------------------*/
	var navbarState = function() {
		var navbar = $('.site-navbar');
		$(window).on('scroll', function(){
			var st = $(this).scrollTop();
			if (st > 100) {
				navbar.addClass('scrolled');
			} else {
				navbar.removeClass('scrolled');
			}
		});
	};

	/*----------------------------------------
		Waypoints Animation
	----------------------------------------*/
	var contentWayPoint = function() {
		if (typeof $.fn.waypoint === 'undefined') return;

		$('.site-animate').waypoint(function(direction) {
			if (direction === 'down' && !$(this.element).hasClass('site-animated')) {
				var el = $(this.element);
				el.addClass('item-animate');
				setTimeout(function(){
					var effect = el.data('animate-effect');
					if (effect === 'fadeIn') {
						el.addClass('fadeIn site-animated');
					} else if (effect === 'fadeInLeft') {
						el.addClass('fadeInLeft site-animated');
					} else if (effect === 'fadeInRight') {
						el.addClass('fadeInRight site-animated');
					} else {
						el.addClass('fadeInUp site-animated');
					}
					el.removeClass('item-animate');
				}, 100);
			}
		}, { offset: '90%' });
	};

	/*----------------------------------------
		Dynamic Typewriter Effect
	----------------------------------------*/
	var initTypewriter = function() {
		var $el = $('#typed-text');
		if (!$el.length) return;

		var phrases = [
			"Aspiring Data Scientist",
			"Python & Flask Developer",
			"Machine Learning Learner",
			"Graphic Design Enthusiast"
		];

		var phraseIdx = 0;
		var charIdx = 0;
		var isDeleting = false;
		var typingSpeed = 90;

		function step() {
			var currentPhrase = phrases[phraseIdx];

			if (isDeleting) {
				$el.text(currentPhrase.substring(0, charIdx - 1));
				charIdx--;
				typingSpeed = 45;
			} else {
				$el.text(currentPhrase.substring(0, charIdx + 1));
				charIdx++;
				typingSpeed = 95;
			}

			if (!isDeleting && charIdx === currentPhrase.length) {
				typingSpeed = 2200; // Pause after completing phrase
				isDeleting = true;
			} else if (isDeleting && charIdx === 0) {
				isDeleting = false;
				phraseIdx = (phraseIdx + 1) % phrases.length;
				typingSpeed = 400; // Pause before starting next phrase
			}

			setTimeout(step, typingSpeed);
		}

		step();
	};

	/*----------------------------------------
		Portfolio Filtering & Masonry
	----------------------------------------*/
	var portfolioMasonry = function() {
		var $grid = $('.grid');
		if (!$grid.length || typeof $.fn.isotope === 'undefined') return;

		var initIsotope = function() {
			$grid.isotope({
				itemSelector: '.single-portfolio',
				layoutMode: 'fitRows',
				transitionDuration: '0.4s'
			});
		};

		if (typeof $.fn.imagesLoaded !== 'undefined') {
			$grid.imagesLoaded(function() {
				initIsotope();
			});
		} else {
			$(window).on('load', function() {
				initIsotope();
			});
			initIsotope();
		}

		$('.filters ul li').on('click', function() {
			$('.filters ul li').removeClass('active');
			$(this).addClass('active');

			var filterValue = $(this).attr('data-filter') || '*';
			$grid.isotope({ filter: filterValue });
		});
	};

	/*----------------------------------------
		Contact Form AJAX Handler
	----------------------------------------*/
	var initContactForm = function() {
		var $form = $('.site-form');
		var $alertContainer = $('#form-alert-container');
		if (!$form.length) return;

		$form.on('submit', function(e) {
			e.preventDefault();
			var $submitBtn = $form.find('input[type="submit"], button[type="submit"]');
			var originalBtnVal = $submitBtn.val() || $submitBtn.text();

			$submitBtn.prop('disabled', true).val('Sending message...');
			$alertContainer.empty();

			$.ajax({
				url: $form.attr('action'),
				type: 'POST',
				data: $form.serialize(),
				dataType: 'json',
				headers: {
					'X-Requested-With': 'XMLHttpRequest'
				}
			}).done(function(data) {
				var messageText = data.message || "Thank you! Your message has been sent successfully.";
				$alertContainer.html(
					'<div class="alert alert-success alert-dismissible fade show mt-3" role="alert">' +
					'<strong>Success!</strong> ' + messageText +
					'<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
					'<span aria-hidden="true">&times;</span>' +
					'</button></div>'
				);
				$form[0].reset();
			}).fail(function(xhr) {
				var errorMsg = "Something went wrong while submitting the message. Please try again or reach out via email.";
				if (xhr.responseJSON && xhr.responseJSON.message) {
					errorMsg = xhr.responseJSON.message;
				}
				$alertContainer.html(
					'<div class="alert alert-danger alert-dismissible fade show mt-3" role="alert">' +
					'<strong>Error:</strong> ' + errorMsg +
					'<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
					'<span aria-hidden="true">&times;</span>' +
					'</button></div>'
				);
			}).always(function() {
				$submitBtn.prop('disabled', false).val(originalBtnVal);
			});
		});
	};

	/*----------------------------------------
		DOM Ready Initialization
	----------------------------------------*/
	$(function() {
		OnePageNav();
		navbarState();
		contentWayPoint();
		initTypewriter();
		portfolioMasonry();
		initContactForm();
	});

})();
