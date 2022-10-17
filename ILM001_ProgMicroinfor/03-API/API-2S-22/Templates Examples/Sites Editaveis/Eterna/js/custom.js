/*global jQuery:false */
jQuery(document).ready(function ($) {
  "use strict";

  (function () {

    var $menu = $('.navigation nav'),
      optionsList = '<option value="" selected>Go to..</option>';

    $menu.find('li').each(function () {
        var $this = $(this),
          $anchor = $this.children('a'),
          depth = $this.parents('ul').length - 1,
          indent = '';

        if (depth) {
          while (depth > 0) {
            indent += ' - ';
            depth--;
          }
        }

        $(".nav li").parent().addClass("bold");
        optionsList += '<option value="' + $anchor.attr('href') + '">' + indent + ' ' + $anchor.text() + '</option>';
      }).end()
      .after('<select class="selectmenu">' + optionsList + '</select>');

    $('select.selectmenu').on('change', function () {
      window.location = $(this).val();
    });

  })();

  //Navi hover
  $('ul.nav li.dropdown').hover(function () {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn();
  }, function () {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut();
  });

  //add some elements with animate effect

  var iOS = false,
    p = navigator.platform;

  if (p === 'iPad' || p === 'iPhone' || p === 'iPod') {
    iOS = true;
  }

  if (iOS === false) {

    $('.flyIn').bind('inview', function (event, visible) {
      if (visible === true) {
        $(this).addClass('animated fadeInUp');
      }
    });

    $('.flyLeft').bind('inview', function (event, visible) {
      if (visible === true) {
        $(this).addClass('animated fadeInLeftBig');
      }
    });

    $('.flyRight').bind('inview', function (event, visible) {
      if (visible === true) {
        $(this).addClass('animated fadeInRightBig');
      }
    });

  }

  $(".box").hover(
    function () {
      $(this).find('.ico').addClass("animated rotateIn");
      $(this).find('h4').addClass("animated fadeInUp");
    },
    function () {
      $(this).find('.ico').removeClass("animated rotateIn");
      $(this).find('h4').removeClass("animated fadeInUp");
    }
  );

  $('.accordion').on('show', function (e) {

    $(e.target).prev('.accordion-heading').find('.accordion-toggle').addClass('active');
    $(e.target).prev('.accordion-heading').find('.accordion-toggle i').removeClass('icon-plus');
    $(e.target).prev('.accordion-heading').find('.accordion-toggle i').addClass('icon-minus');
  });

  $('.accordion').on('hide', function (e) {
    $(this).find('.accordion-toggle').not($(e.target)).removeClass('active');
    $(this).find('.accordion-toggle i').not($(e.target)).removeClass('icon-minus');
    $(this).find('.accordion-toggle i').not($(e.target)).addClass('icon-plus');
  });

  // testimonial
  var TestiSlide = $('.bxslider');
  TestiSlide.bxSlider({
    auto: true,
    pager: false,
    controls: false,
    useCSS: false,
    speed: 2000,
    easing: 'easeOutElastic',
    mode: 'horizontal',
    controlDirections: true
  });

  //prettyphoto
  $("a[data-pretty^='prettyPhoto']").prettyPhoto({
    social_tools: ''
  });

  // tooltip
  $('.social-network li a, .options_box .color a').tooltip();

  //scroll to top
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('.scrollup').fadeIn();

    } else {
      $('.scrollup').fadeOut();

    }
  });

  $('.scrollup').click(function () {
    $("html, body").animate({
      scrollTop: 0
    }, 1000);
    return false;
  });

  //flexslider
  $('.flexslider').flexslider({
    animation: "fade",
    directionNav: true,
    controlNav: false,
    pauseOnAction: true,
    pauseOnHover: true,
    slideshowSpeed: 5500
  });

});
