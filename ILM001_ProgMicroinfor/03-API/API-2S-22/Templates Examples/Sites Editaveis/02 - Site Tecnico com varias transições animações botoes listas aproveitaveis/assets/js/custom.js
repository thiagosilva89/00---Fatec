jQuery(document).ready(function($) {

  // Append a close trigger for each block
  $('.box-tile .content').append('<span class="close">x</span>');
  // Show window
  function showContent(elem) {
    hideContent();
    elem.find('.content').addClass('expanded');
    elem.addClass('cover');
  }
  // Reset all
  function hideContent() {
    $('.box-tile  .content').removeClass('expanded');
    $('.box-tile  li').removeClass('cover');
  }

  // When a li is clicked, show its content window and position it above all
  $('.box-tile  li').click(function() {
    showContent($(this));
  });
  // When tabbing, show its content window using ENTER key
  $('.box-tile  li').keypress(function(e) {
    if (e.keyCode == 13) {
      showContent($(this));
    }
  });

  // When right upper close element is clicked  - reset all
  $('.box-tile  .close').click(function(e) {
    e.stopPropagation();
    hideContent();
  });
  // Also, when ESC key is pressed - reset all
  $(document).keyup(function(e) {
    if (e.keyCode == 27) {
      hideContent();
    }
  });

  // Create the dropdown base
  $("<select />").appendTo("nav");

  // Create default option "Go to..."
  $("<option />", {
    "selected": "selected",
    "value": "",
    "text": "Go to..."
  }).appendTo("nav select");

  // Populate dropdown with menu items
  $("nav a").each(function() {
    var el = $(this);
    $("<option />", {
      "value": el.attr("href"),
      "text": el.text()
    }).appendTo("nav select");
  });

  // To make dropdown actually work
  // To make more unobtrusive: http://css-tricks.com/4064-unobtrusive-page-changer/
  $("nav select").change(function() {
    window.location = $(this).find("option:selected").val();
  });

  $("a[data-pretty^='prettyPhoto']").prettyPhoto();

  $(".gallery:first a[data-pretty^='prettyPhoto']").prettyPhoto({
    animation_speed: 'normal',
    theme: 'pp_default',
    slideshow: 3000,
    autoplay_slideshow: false
  });
  $(".gallery:gt(0) a[data-pretty^='prettyPhoto']").prettyPhoto({
    animation_speed: 'fast',
    slideshow: 10000,
    hideflash: true
  });

  $("#custom_content a[data-pretty^='prettyPhoto']:first").prettyPhoto({
    custom_markup: '<div id="map_canvas" style="width:260px; height:265px"></div>',
    changepicturecallback: function() {
      initialize();
    }
  });

  $("#custom_content a[data-pretty^='prettyPhoto']:last").prettyPhoto({
    custom_markup: '<div id="bsap_1259344" class="bsarocks bsap_d49a0984d0f377271ccbf01a33f2b6d6"></div><div id="bsap_1237859" class="bsarocks bsap_d49a0984d0f377271ccbf01a33f2b6d6" style="height:260px"></div><div id="bsap_1251710" class="bsarocks bsap_d49a0984d0f377271ccbf01a33f2b6d6"></div>',
    changepicturecallback: function() {
      _bsap.exec();
    }
  });



  $('iframe').each(function() { /*fix youtube z-index*/
    var url = $(this).attr("src");
    if (url.indexOf("youtube.com") >= 0) {
      if (url.indexOf("?") >= 0) {
        $(this).attr("src", url + "&wmode=transparent");
      } else {
        $(this).attr("src", url + "?wmode=transparent");
      }
    }
  });

  $('ul.nav li.dropdown').hover(function() {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn();
  }, function() {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut();
  });

  // tooltip
  $("a[data-rel^='tooltip']").tooltip();
  $('.tooltip').tooltip();

  if ($("#mainslider").length) {
    $('#mainslider').flexslider({
      animation: "slide",
      controlNav: "thumbnails"
    });
  }

  if ($(".flexslider").length) {
    $('.flexslider').flexslider({
      animation: "slide",
      controlNav: false
    });
  }

});
