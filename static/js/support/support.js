
///////////////
setInterval(function() {
    // کدی برای بارگیری دیتای تازه و بروزرسانی صفحه
  }, 4000);

document.querySelector('#support_message').focus();
document.querySelector('#support_message').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#support_submit').click();
    }
};

document.querySelector('#support_submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#support_message');
    const message = messageInputDom.value;
    if(message){
        let token = $('input[name=csrfmiddlewaretoken]').val();
        let support_status = "active";
        let data = {
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
                let message_text = response.status;
                var currentText = $("#support_log").val();
                var newText = currentText + "\n" + message_text;
                $("#support_log").val(newText);
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