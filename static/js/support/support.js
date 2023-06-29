document.querySelector('#support_message').focus();
document.querySelector('#support_message').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#support_submit').click();
    }
};
function load_message(){
  
}
document.querySelector('#support_submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#support_message');
    const message = messageInputDom.value;
    if(message){
        let token = $('input[name=csrfmiddlewaretoken]').val();
        let search_user = $('input[name=Supported_user]').val();
        let support_status = "active";
        $.ajax({
          url: `/api/support/?search=${search_user}`,
          type: 'GET',
          dataType: 'json',
          success: function(response) {
            // Handle the response data here
            var results = response.results;
            for (var i = 0; i < results.length; i++) {
              var supporter = results[i].supporter;
              var supportUser = results[i].support_user;
              let data = {
                'supporter': supporter,
                'supported_user' : supportUser,
                'support_message': message,
                'support_status':support_status,
                csrfmiddlewaretoken: token,
              }
              $.ajax({
                url: '/support/message',
                type: 'POST',
                data: data,
                success: function(response) {
                  if (response.success === false) {
                    Swal.fire({
                      icon: "error",
                      title: response.status,
                      showConfirmButton: false,
                      timer: 3000,
                    });
                  } else {
                      var message_recive = response.status;
                      $("#support_log").prepend(`<h2> ${message_recive} </h2>`);
                  }
                },
                error: function(xhr, status, error) {
                  Swal.fire({
                    icon: "error",
                    title: status,
                    showConfirmButton: false,
                    timer: 3000,
                  });
                }
              });
            }
          },
        });
    }else{
        Swal.fire({
            icon: "error",
            title: "پیام پشتیبانی نمیتواند خالی باشد",
            showConfirmButton: false,
            timer: 2000,
          });
    }
    messageInputDom.value = '';
};