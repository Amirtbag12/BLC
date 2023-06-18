$(document).ready(function() {
  var cart = {}
  function pageData() {
    let user = $('input[name=user]').val();
    // set page content
    $(".cardtable").html('<tr>\
    <th>محصول</th>\
    <th>تصویر محصول</th>\
    <th>قیمت (تومان)</th>\
    <th>تعداد</th>\
    <th>جمع جزء</th>\
    <th>عملیات</th>\
  </tr>');
    $.get(`/api/cart/?ordering=${user}`, function(data) {
      let rest = data.results;
        for(let api = 0; api <= data.count; api++){
          cart = Object.assign(cart, {
            'id':rest[api].product_id,
            'user':user,
            'title':rest[api].product_title,
            'price':rest[api].price,
            'color':rest[api].color,
            'quantity':rest[api].quantity,
            'color_quantity':rest[api].color_quantity,
            'image':rest[api].image,
            'collection':rest[api].product_collection,
            'count':data.count,
          });
        // set dynimic site
        $("#cardtable").append('<tr>\
        <td>'+ cart['title'] +'</td>\
        <td>\
          <img id="image'+ cart['id'] +'" class="image'+ cart['id'] +'" src="'+ cart['image'] +'" width="80px" alt="'+ cart['title'] +'">\
        </td>\
        <td>'+ cart['price'] +'</td>\
        <td><input type="number" id="quantity" name="quantity'+cart['id']+'" class="quantity'+cart['id']+'" value="'+ cart['quantity'] +'" min="0"\
        <button id="update'+cart['id']+'" type="button" class="btn btn-outline-danger update'+cart['id']+'">به روز رسانی</button>\
        </td>\
        <td>'+ parseInt(cart['price']) * parseInt(cart['quantity']) +'</td>\
        <td>\
            <button id="remove'+ cart['id'] +'" type="button" class="btn btn-outline-danger remove'+ cart['id'] +'">حذف</button>\
        </td>\
      </tr>');
        }
    });
  }

  // update cart button 
  $('.update_quantity').click(function(e) {
    e.preventDefault();
    let token = $('input[name=csrfmiddlewaretoken]').val();
    let product_title = $('.product_title').val();
    let product_quantity = $('.quantity').val();
    let product_color_quantity = $('.product_color_quantity').val();
    let data = {
        'product_title': product_title,
        'quantity':product_quantity,
        'product_color_quantity': product_color_quantity,
        csrfmiddlewaretoken: token,
    };
    // Send request to server
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
  });
    // remove item
  $('.remove_from_cart').click(function(e) {
    e.preventDefault();
    let token = $('input[name=csrfmiddlewaretoken]').val();
    let product_title = $('.product_title').val();
    let data = {
        'product_title': product_title,
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
  });
    // apply discount
  $('.discount_code').click(function(e) {
    e.preventDefault();
    let token = $('input[name=csrfmiddlewaretoken]').val();
    let product_title = $('.product_title').val();
    let product_collection = $('.product_collection').val();
    let product_price = $('.product_price').val();
    let data = {
        'product_title': product_title,
        'product_price': product_price,
        'product_collection': product_collection,
        csrfmiddlewaretoken: token,
    };
    // Send request to server
    $.ajax({
      url: '/cart/discount',
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
  });
    // clear cart
  $('.clear_cart').click(function(e) {
    e.preventDefault();
    let token = $('input[name=csrfmiddlewaretoken]').val();
    let product_id = $('.product_id').val();
    let data = {
        'product_id': product_id,
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
  });
  pageData();
});