function updateCart(productTitle, productId, productColorQuantity){
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let quantity = document.getElementById(productId).value;
  let data = {
    'product_title': productTitle,
    'quantity':quantity,
    'product_color_quantity': productColorQuantity,
    csrfmiddlewaretoken: token,
  }
  $.ajax({
    url: '/cart/update',
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
        Swal.fire({
          icon: "success",
          title: response.status,
          showConfirmButton: false,
          timer: 2000,
        });
        location.reload(true)
      }
    },
    error: function(xhr, status, error) {
      console.log(status);
      Swal.fire({
        icon: "error",
        title: status,
        showConfirmButton: false,
        timer: 3000,
      });
    }
  });
}
// remove cart item
function removeItem(productTitle){
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let data = {
      'product_title': productTitle,
      csrfmiddlewaretoken: token,
  };
  // Send request to server
  $.ajax({
    url: '/cart/remove',
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
        Swal.fire({
          icon: "success",
          title: response.status,
          showConfirmButton: false,
          timer: 2000,
        });
        location.reload(true)
      }
    },
    error: function(xhr, status, error) {
      console.log(status);
      Swal.fire({
        icon: "error",
        title: status,
        showConfirmButton: false,
        timer: 3000,
      });
    }
  });
}
function clearCart(){
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let productID = $('.quantity').val();
  let data = {
      'product_id': productID,
      csrfmiddlewaretoken: token,
  };
  // Send request to server
  $.ajax({
    url: '/cart/clear',
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
        Swal.fire({
          icon: "success",
          title: response.status,
          showConfirmButton: false,
          timer: 2000,
        });
        location.reload(true)
      }
    },
    error: function(xhr, status, error) {
      console.log(status);
      Swal.fire({
        icon: "error",
        title: status,
        showConfirmButton: false,
        timer: 3000,
      });
    }
  });
}
