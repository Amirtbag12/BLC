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
    const message = messageInputDom.value + "<br>";

    messageInputDom.value = '';
};