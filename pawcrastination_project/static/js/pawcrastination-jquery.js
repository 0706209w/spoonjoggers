jQuery(document).ready(function($) {
	jQuery('#wrapper3').hide();
	jQuery('.picture-pop').click( function(event) {
        window.open($(this).attr('href1'),'_blank','height=600,width=650');	
	});


});