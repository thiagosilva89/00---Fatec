var SliderStatus = true;

// Navigation
(function($){

	"use strict"

	$(window).on("scroll", function(){
		var navBar = $(".navbar-fixed-top"),
			windowHeight = $(this).innerHeight()-navBar.innerHeight();

		if($(this).scrollTop() > windowHeight)
		{
			SliderStatus = false;
			navBar.removeClass("bottom");
		}
		else
		{
			SliderStatus = true;
			navBar.addClass("bottom");
		}
	});
})(jQuery);

// Header Slider
(function($){

	"use strict"

	var aPrev = $(".nav-slide a.prev"),
		aNext = $(".nav-slide a.next"),
		NextTitle = $(".nav-slide a.next h3"),
		NextAuthor = $(".nav-slide a.next p"),
		NextImg = $(".nav-slide a.next img"),
		PrevTitle = $(".nav-slide a.prev h3"),
		PrevAuthor = $(".nav-slide a.prev p"),
		PrevImg = $(".nav-slide a.prev img"),
		activeSlide = $(".image-slide"),
		activeTitle = $(".slider-content h1"),
		activeIndex, nextIndex, prevIndex,
		objHeaderLength = dataHeader.length - 1,
		SliderTimeout = false;

	aPrev.on("click", function(){
		loader(false);
	});

	aNext.on("click", function(){
		loader(true);
	});

	function SliderInterval(){
		SliderTimeout = setInterval(function(){
			if(SliderStatus) loader(true);
		}, 8000);
	}

	function startImageHeader(){
		if(typeof activeIndex === "undefined")
		{
			activeIndex = 0;
			nextIndex = 1;
			prevIndex = objHeaderLength;
		}

		dataHeader.forEach(function(a){
			a.show = false;
		});

		dataHeader[activeIndex].show = true;

		new preLoader([dataHeader[activeIndex].bigImage, dataHeader[prevIndex].bigImage, dataHeader[nextIndex].bigImage], {
			onComplete: function(loaded, errors){

				var brokenImage = "images/broken-image.jpg",
					activeImg = dataHeader[activeIndex].bigImage,
					prevImg = dataHeader[prevIndex].bigImage,
					nextImg = dataHeader[nextIndex].bigImage;

				if (errors){
		            for(var i=0; i<errors.length; i++)
		            {
		            	activeImg = (errors[i] === activeImg) ? brokenImage : activeImg;
		            	prevImg = (errors[i] === prevImg) ? brokenImage : prevImg;
		            	nextImg = (errors[i] === nextImg) ? brokenImage : nextImg;
		            }
		        }
		        
		        setTimeout(function(){
		        	loaderSVG.hide();
		        	SliderInterval();
		        }, 2000);

		        activeSlide.css("background-image", "url('" + activeImg + "')");
			
				PrevImg.attr("src", prevImg);
				
				NextImg.attr("src", nextImg);
		    }
		});

		activeTitle.text(dataHeader[activeIndex].title);

		PrevAuthor.text("by " + dataHeader[prevIndex].author);
		PrevTitle.text(dataHeader[prevIndex].title);
		NextAuthor.text("by " + dataHeader[nextIndex].author);
		NextTitle.text(dataHeader[nextIndex].title);
	}

	function loader(n){
		clearInterval(SliderTimeout);
		loaderSVG.show();

		for (var i = 0; i<=objHeaderLength; i++) {
			if(dataHeader[i].show && n)
			{
				activeIndex = (i+1 > objHeaderLength) ? 0 : i+1;
				nextIndex = (activeIndex+1 > objHeaderLength) ? 0 : activeIndex+1;
				prevIndex = i;

				break;
			}
			else if(dataHeader[i].show && !n)
			{
				activeIndex = (i-1 < 0) ? objHeaderLength : i-1;
				prevIndex = (activeIndex-1 < 0) ? objHeaderLength : activeIndex-1;
				nextIndex = i;
				break;
			}
		}

		setTimeout(function(){
			startImageHeader();
		}, 800);	
	}

	startImageHeader();

})(jQuery);


// TEMPLATE
(function($){
	$(document).on("ready", function(){
		"use strict"
		

		//Header fit screen

	    $(function() {
	        "use strict";
	        $("#header").css({
	            "height": ($(window).height()) + "px"
	        });
	        $(window).resize(function() {
	            $("#header").css({
	                "height": ($(window).height()) + "px"
	            });
	        });
	    });

		// anchor handler
		$(document).on("click", "a", function(e){
			var full_url = this.href,
				windowWidth = window.innerWidth,
				navBar = (windowWidth >= 768) ? $(".navbar-fixed-top") : $(".navbar-header"),
				windowLocation = window.location.href.split("#")[0],
				parts = full_url.split("#");

			if(windowLocation !== parts[0])
				return

			if(parts[1].length > 0 && $("#" + parts[1]).length > 0)
			{
				$.smoothScroll({
					offset : -navBar.innerHeight(),
					scrollTarget: "#" + parts[1],
					speed : 500
				});
			}

		    return false;
		});


		// animated element
		$(".animated").appear(function() {
	        var element = $(this),
	        	animation = element.data("animate"),
	        	animationDelay = element.data("delay");

	        if (animationDelay) {
	            setTimeout(function() {
	                element.addClass(animation + " visible");
	                if (element.hasClass("counter")) {
	                    element.find('.value').countTo();
	                }
	            }, animationDelay);
	        } else {
	            element.addClass(animation + " visible");
	            if (element.hasClass("counter")) {
	                element.find(".value").countTo();
	            }
	        }
	    }, {
	        accY: -150
	    });

	    $(".skill-bar .percentage").appear(function() {
	        var element = $(this),
	        	animation = element.data("value");
	        element.animate({
	        	"width" : animation
	        }, 2000);
	    });
	});


    // PORTFOLIO

    $(document).on("ready", function(){
    	"use strict"

    	function columnsSplit(){
	    	if($(window).innerWidth() >= 1200)
	    		return 4
	    	else if($(window).innerWidth() >= 992)
	    		return 3
	    	else if($(window).innerWidth() >= 768)
	    		return 2
	    	else return 1
	    }

	    var portWidth = $(window).innerWidth() / columnsSplit(),
	    	containerPortfolio = $(".container-portfolio"),
	    	portImage = [];

	    $(window).on("resize", function(){
	    	$(".container-portfolio .portfolio-view").each(function(a, b){
	    		$(b).css({
	    			"width" : $(window).innerWidth()/columnsSplit(),
	    			"height" : ($(window).innerWidth()/columnsSplit() - 113)
	    		});
	    	});
	    });

	    $.each(portfolio, function(a, b){
	    	portImage.push(b.image);
	    });

	    new preLoader(portImage, {
	    	onComplete : function(load, errors){
	    		$.each(portfolio, function(a, b){
			    	var image = (typeof b.image === "undefined") ? "images/broken-image.jpg" : b.image;

			    	if (errors){
			            for(var i=0; i<errors.length; i++)
			            {
			            	image = (errors[i] === image) ? "images/broken-image.jpg" : image;
			            }
			        }

			        var portList = $('<figure class="portfolio-view ' + b.category + '" style="width:' + portWidth + 'px;height:' + (portWidth-113) + 'px"><img src="' + image + '"><figcaption><h2>' + b.title + '</span></h2><p>' + b.text + '</p><a href="' + b.link + '">View more</a></figcaption></figure>');

			    	portList.appendTo(containerPortfolio);
			    });
			    
			    $(".container-portfolio").mixItUp({
			    	selectors : {
			    		target : ".portfolio-view"
			    	},
			    	animation: {
			    		effects: "fade stagger scale rotateX(-360deg)",
						easing: "cubic-bezier(0.215, 0.61, 0.355, 1)"
					}
			    });
	    	}
	    });
    });


    //Google map

	$(document).on("ready", function() {

		var map;

		$(".btn-map").click(function() {
			if($("#google_map").children() > 0)
				$("#google_map").slideToggle(300, function(){
					map.getCenter();
				});
			else
				$("#google_map").slideToggle(300, initialize);
        });

		function initialize() {
		    var mapOptions = {
		        zoom: 17,
		        center: new google.maps.LatLng(-6.86041, 107.590006),
		        disableDefaultUI: true,
		        scrollwheel: false,
		        styles: [{
		            "featureType": "water",
		            "elementType": "geometry",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 17
		            }]
		        }, {
		            "featureType": "landscape",
		            "elementType": "geometry",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 20
		            }]
		        }, {
		            "featureType": "road.highway",
		            "elementType": "geometry.fill",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 17
		            }]
		        }, {
		            "featureType": "road.highway",
		            "elementType": "geometry.stroke",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 29
		            }, {
		                "weight": 0.2
		            }]
		        }, {
		            "featureType": "road.arterial",
		            "elementType": "geometry",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 18
		            }]
		        }, {
		            "featureType": "road.local",
		            "elementType": "geometry",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 16
		            }]
		        }, {
		            "featureType": "poi",
		            "elementType": "geometry",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 21
		            }]
		        }, {
		            "elementType": "labels.text.stroke",
		            "stylers": [{
		                "visibility": "on"
		            }, {
		                "color": "#000000"
		            }, {
		                "lightness": 16
		            }]
		        }, {
		            "elementType": "labels.text.fill",
		            "stylers": [{
		                "saturation": 36
		            }, {
		                "color": "#000000"
		            }, {
		                "lightness": 40
		            }]
		        }, {
		            "elementType": "labels.icon",
		            "stylers": [{
		                "visibility": "off"
		            }]
		        }, {
		            "featureType": "transit",
		            "elementType": "geometry",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 19
		            }]
		        }, {
		            "featureType": "administrative",
		            "elementType": "geometry.fill",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 20
		            }]
		        }, {
		            "featureType": "administrative",
		            "elementType": "geometry.stroke",
		            "stylers": [{
		                "color": "#000000"
		            }, {
		                "lightness": 17
		            }, {
		                "weight": 1.2
		            }]
		        }]
		    };

		    map = new google.maps.Map(document.getElementById('google_map'), mapOptions);

		    var contentString = "<div class='map-tooltip'><h2>Manja<span>real</span></h2></div>";

		    var infowindow = new google.maps.InfoWindow({
		    	content: contentString
		    });

			var marker = new google.maps.Marker({
				position: new google.maps.LatLng(-6.86041, 107.590006),
				map: map,
				icon : "images/map-pin.png"
			});

			google.maps.event.addListener(marker, 'click', function() {
				infowindow.open(map,marker);
			});
		}
	});

})(jQuery);