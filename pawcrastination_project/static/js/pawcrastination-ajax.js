$('#likes').click(function(){
    var picid;
    picid = $(this).attr("data-profileid");
    $.get('/pawcrastination/goto3/', {animalprofile_id: profileid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});