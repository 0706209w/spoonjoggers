jQuery(document).ready(function($) {
	jQuery('#wrapper3').hide();
	jQuery('.picture-pop').click( function(event) {
		window.open("http://127.0.0.1:8000" + $(this).attr('href1'),'_blank','height=600,width=650');
		
	});


});