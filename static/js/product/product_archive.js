$(document).ready(function() {
    var perPage = 8;
    var page = 1;

    function loadProducts() {
      var startIndex = (page - 1) * perPage;
      var endIndex = startIndex + perPage;
  
      $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem`, function(data) {
        var product_item = data.items;
        if (product_item.length > 0) {
          totalPages = Math.ceil(product_item.length / perPage);
          for (var i = startIndex; i < endIndex; i++) {
            if (i >= product_item.length) {
              break;
            }
            var productPage = product_item[i];
            var productPageId = productPage.id;
            var productPageSlug = productPage.meta.slug;
            var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
            $.getJSON(productPostsAPIURL, function(productsData) {
              var product = productsData;
              if (product.PRODUCT_OFFER.length > 0) {
                var postHTML = `
                  <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                    <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                    <div class="card-body">
                      <h3 class="card-title h4">
                        <a href="" class="black-color">${product.title}</a>
                      </h3>
                      <span class="text-decoration-line-through icon2">${product.price}</span>
                      <span class="red-color">${product.PRODUCT_OFFER[0].value}<span>تومان</span></span>
                      <hr />
                      <div id="TOOLS" class="tolspro">
                      <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','${product.PRODUCT_OFFER[0].value}')"></span>
                        <span class="price"></span></a>
                        <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                        <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','${product.PRODUCT_OFFER[0].value}')"></span>
                      </div>
                    </div>
                  </div>
                `;
                $('#PRODUCT').append(postHTML);
              } else {
                var postHTML = `
                  <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                    <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                    <div class="card-body">
                      <h3 class="card-title h4">
                        <a href="" class="black-color">${product.title}</a>
                      </h3>
                      <span class="red-color">${product.price}<span>تومان</span></span>
                      <hr />
                      <div id="TOOLS" class="tolspro">
                      <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', '${productPageSlug}', '${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                      <span class="price"></span>
                        <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                        <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                        </div>
                    </div>
                  </div>
                `;
                $('#PRODUCT').append(postHTML);
              }
  
            });
          }
          if (page >= totalPages) {
            $('#load-more').hide();
          } else {
            $('#load-more').show();
          }
  
          page++;
        }
      });
    }
    $('#load-more').click(function() {
        loadBlogPages();
      });
    loadProducts();
  });
// Start filters :
function defaultProduct() {
  var perPage = 8;
  var page = 1;
  var startIndex = (page - 1) * perPage;
  var endIndex = startIndex + perPage;

  $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem`, function(data) {
    var product_item = data.items;
    if (product_item.length > 0) {
      totalPages = Math.ceil(product_item.length / perPage);
      $('#PRODUCT').html("");

      for (var i = startIndex; i < endIndex; i++) {
        if (i >= product_item.length) {
          break;
        }
        var productPage = product_item[i];
        var productPageId = productPage.id;
        var productPageSlug = productPage.meta.slug;
        var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
        $.getJSON(productPostsAPIURL, function(productsData) {
          var product = productsData;
          if (product.PRODUCT_OFFER.length > 0) {
            var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="text-decoration-line-through icon2">${product.price}</span>
                  <span class="red-color">${product.PRODUCT_OFFER[0].value}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','${product.PRODUCT_OFFER[0].value}')"></span>
                    <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','${product.PRODUCT_OFFER[0].value}')"></span>
                    </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          } else {
            var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="red-color">${product.price}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', '${productPageSlug}', '${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                  <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                    </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          }

        });
      }
      if (page >= totalPages) {
        $('#load-more').hide();
      } else {
        $('#load-more').show();
      }

      page++;
    }
  });
}
function oldProduct() {
  var perPage = 8;
  var page = 1;
  var startIndex = (page - 1) * perPage;
  var endIndex = startIndex + perPage;

  $.getJSON(`/UNIQUEAPI174/pages/?type=-product.InventoryItem`, function(data) {
    var product_item = data.items;
    if (product_item.length > 0) {
      totalPages = Math.ceil(product_item.length / perPage);
      $('#PRODUCT').html("");

      for (var i = startIndex; i < endIndex; i++) {
        if (i >= product_item.length) {
          break;
        }
        var productPage = product_item[i];
        var productPageId = productPage.id;
        var productPageSlug = productPage.meta.slug;
        var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
        $.getJSON(productPostsAPIURL, function(productsData) {
          var product = productsData;
          if (product.PRODUCT_OFFER.length > 0) {
            var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>{
                  <span class="text-decoration-line-through icon2">${product.price}</span>
                  <span class="red-color">${product.PRODUCT_OFFER[0].value}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','${product.PRODUCT_OFFER[0].value}')"></span>
                    <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','${product.PRODUCT_OFFER[0].value}')"></span>
                    </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          } else {
            var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="red-color">${product.price}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', '${productPageSlug}', '${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                  <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                    </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          }

        });
      }
      if (page >= totalPages) {
        $('#load-more').hide();
      } else {
        $('#load-more').show();
      }

      page++;
    }
  });
}
function lowPrice() {
  var perPage = 8;
  var page = 1;
  var startIndex = (page - 1) * perPage;
  var endIndex = startIndex + perPage;
  $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem&order=price`, function(data) {
    var product_item = data.items;
    if (product_item.length > 0) {
      totalPages = Math.ceil(product_item.length / perPage);
      $('#PRODUCT').html("");
      for (var i = startIndex; i < endIndex; i++) {
        if (i >= product_item.length) {
          break;
        }
        var productPage = product_item[i];
        var productPageId = productPage.id;
        var productPageSlug = productPage.meta.slug;
        var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
        $.getJSON(productPostsAPIURL, function(productsData) {
          var product = productsData;
          if (product.PRODUCT_OFFER.length > 0) {
            var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="text-decoration-line-through icon2">${product.price}</span>
                  <span class="red-color">${product.PRODUCT_OFFER[0].value}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','${product.PRODUCT_OFFER[0].value}')"></span>
                    <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','${product.PRODUCT_OFFER[0].value}')"></span>
                    </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          } else {
            var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="red-color">${product.price}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', '${productPageSlug}', '${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                  <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                    </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          }

        });
      }
      if (page >= totalPages) {
        $('#load-more').hide();
      } else {
        $('#load-more').show();
      }

      page++;
    }
  });
}
function highPrice() {
  var perPage = 8;
  var page = 1;
  var startIndex = (page - 1) * perPage;
  var endIndex = startIndex + perPage;
  $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem&order=-price`, function(data) {
    var product_item = data.items;
    if (product_item.length > 0) {
      totalPages = Math.ceil(product_item.length / perPage);
      $('#PRODUCT').html("");
      for (var i = startIndex; i < endIndex; i++) {
        if (i >= product_item.length) {
          break;
        }
        var productPage = product_item[i];
        var productPageId = productPage.id;
        var productPageSlug = productPage.meta.slug;
        var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
        $.getJSON(productPostsAPIURL, function(productsData) {
          var product = productsData;
          if (product.PRODUCT_OFFER.length > 0) {
            var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="text-decoration-line-through icon2">${product.price}</span>
                  <span class="red-color">${product.PRODUCT_OFFER[0].value}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','${product.PRODUCT_OFFER[0].value}')"></span>
                    <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','${product.PRODUCT_OFFER[0].value}')"></span>
                    </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          } else {
            var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="red-color">${product.price}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', '${productPageSlug}', '${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                  <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                    </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          }

        });
      }
      if (page >= totalPages) {
        $('#load-more').hide();
      } else {
        $('#load-more').show();
      }

      page++;
    }
  });
}
function rangePrice() {
var perPage = 10;
var page = 1;
var minPrice = document.getElementById("min-price").value;
var maxPrice = document.getElementById("max-price").value;
var startIndex = (page - 1) * perPage;
var endIndex = startIndex + perPage;
$('#PRODUCT').html("");
for(var i = minPrice; i <= maxPrice; i++){
  $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem&price=${i}`, function(data) {
    console.log(data);
    rangeItem = data.items[0];
    if(data.meta.total_count > 0){
      var rangeId = rangeItem.id;
      var productSlug = rangeItem.meta.slug;
      var APIUrl = `/UNIQUEAPI174/pages/${rangeId}`;
      $.getJSON(APIUrl, function(productsData) {
        var product = productsData;
        if (product.PRODUCT_OFFER.length > 0) {
          var postHTML = `
            <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
              <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
              <div class="card-body">
                <h3 class="card-title h4">
                  <a href="" class="black-color">${product.title}</a>
                </h3>
                <span class="text-decoration-line-through icon2">${product.price}</span>
                <span class="red-color">${product.PRODUCT_OFFER[0].value}<span>تومان</span></span>
                <hr />
                <div id="TOOLS" class="tolspro">
                <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','${product.PRODUCT_OFFER[0].value}')"></span>
                  <span class="price"></span>
                  <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                  <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','${product.PRODUCT_OFFER[0].value}')"></span>
                  </div>
              </div>
            </div>
          `;
          $('#PRODUCT').append(postHTML);
        } else {
          var postHTML = `
            <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
              <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
              <div class="card-body">
                <h3 class="card-title h4">
                  <a href="" class="black-color">${product.title}</a>
                </h3>
                <span class="red-color">${product.price}<span>تومان</span></span>
                <hr />
                <div id="TOOLS" class="tolspro">
                <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', '${productPageSlug}', '${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                <span class="price"></span>
                  <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                  <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                  </div>
              </div>
            </div>
          `;
          $('#PRODUCT').append(postHTML);
        }

      });

    }
  });
  }
}
export function add_favourite(product_id, product_slug, product_title, product_image, product_quantity, product_color, product_add_cart_date){
  // Data to be sent with the POST request
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let data = {
    'product_id': product_id,
    'product_slug':product_slug,
    'product_title': product_title,
    'product_image': product_image,
    'quantity':product_quantity,
    'selected_color_text':product_color,
    'add_cart_date':product_add_cart_date,
    csrfmiddlewaretoken: token,
  };
  // Send request to server
  $.ajax({
    url: '/cart/favourite/add',
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
// add comparison
export function add_comparison(product_id, product_slug, product_title, product_image, product_quantity, product_color, product_color_quantity, product_add_cart_date){
  let token = $('input[name=csrfmiddlewaretoken]').val();
  // Data to be sent with the POST request
  let data = {
    'product_id':product_id,
    'product_slug':product_slug,
    'product_title': product_title,
    'product_image': product_image,
    'quantity':product_quantity,
    'selected_color_text':product_color,
    'product_color_quantity':product_color_quantity,
    'add_cart_date':product_add_cart_date,
    csrfmiddlewaretoken: token,
  };
  // Send request to server
  $.ajax({
    url: '/cart/comparison/add',
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


document.getElementById("defaultFilter").addEventListener("click", function(event) {
  event.preventDefault();
  defaultProduct();
});
document.getElementById("lowPriceFilter").addEventListener("click", function(event) {
  event.preventDefault();
  lowPrice();
});
document.getElementById("highPriceFilter").addEventListener("click", function(event) {
  event.preventDefault();
  highPrice();
});
document.getElementById("newFilter").addEventListener("click", function(event) {
  event.preventDefault();
  defaultProduct();
});
document.getElementById("oldFilter").addEventListener("click", function(event) {
  event.preventDefault();
  oldProduct();
});
document.getElementById("rangePriceFilter").addEventListener("click", function(event) {
  event.preventDefault();
  rangePrice();
});
// فیلتر - چک باکس
var inventoryCheckbox = document.getElementById("inventory");
var specialDiscountCheckbox = document.getElementById("specialdiscount");

inventoryCheckbox.addEventListener("change", function() {
  if (inventoryCheckbox.checked) {
    var perPage = 8;
    var page = 1;
    var startIndex = (page - 1) * perPage;
    var endIndex = startIndex + perPage;
    $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem&is_available=true`, function(data) {
      var product_item = data.items;
      if (product_item.length > 0) {
        totalPages = Math.ceil(product_item.length / perPage);
        $('#PRODUCT').html("");
        for (var i = startIndex; i < endIndex; i++) {
          if (i >= product_item.length) {
            break;
          }
          var productPage = product_item[i];
          var productPageId = productPage.id;
          var productPageSlug = productPage.meta.slug;
          var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
          $.getJSON(productPostsAPIURL, function(productsData) {
            var product = productsData;
            if (product.PRODUCT_OFFER.length > 0) {
              var postHTML = `
                <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                  <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                  <div class="card-body">
                    <h3 class="card-title h4">
                      <a href="" class="black-color">${product.title}</a>
                    </h3>
                    <span class="text-decoration-line-through icon2">${product.price}</span>
                    <span class="red-color">${product.PRODUCT_OFFER[0].value}<span>تومان</span></span>
                    <hr />
                    <div id="TOOLS" class="tolspro">
                    <span class="bi bi-heart" onclick="add_favourite(${product.id}, ${productPageSlug}, ${product.product_title},${product.image.url},'FV','SV',${product.PRODUCT_OFFER[0].value})"></span>
                      <span class="price"></span>
                      <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                      <span class="bi bi-arrow-left-right" onclick="add_comparison(${product.id},${productPageSlug},${product.product_title},${product.image.url},'FV','SV','1',${product.PRODUCT_OFFER[0].value})"></span>
                    </div>
                  </div>
                </div>
              `;
              $('#PRODUCT').append(postHTML);
            } else {
              var postHTML = `
                <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                  <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                  <div class="card-body">
                    <h3 class="card-title h4">
                      <a href="" class="black-color">${product.title}</a>
                    </h3>
                    <span class="red-color">${product.price}<span>تومان</span></span>
                    <hr />
                    <div id="TOOLS" class="tolspro">
                    <span class="bi bi-heart" onclick="add_favourite(${product.id}, ${productPageSlug}, ${product.product_title},${product.image.url},'FV','SV',${product.PRODUCT_OFFER[0].value})"></span>
                      <span class="price"></span>
                      <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                      <span class="bi bi-arrow-left-right" onclick="add_comparison(${product.id},${productPageSlug},${product.product_title},${product.image.url},'FV','SV','1',${product.PRODUCT_OFFER[0].value})"></span>
                    </div>
                  </div>
                </div>
              `;
              $('#PRODUCT').append(postHTML);
            }
  
          });
        }
        if (page >= totalPages) {
          $('#load-more').hide();
        } else {
          $('#load-more').show();
        }
  
        page++;
      }
    });
  } else {
    loadProducts();
  }
});

specialDiscountCheckbox.addEventListener("change", function() {
  if (specialDiscountCheckbox.checked) {
    var perPage = 8;
    var page = 1;
    var startIndex = (page - 1) * perPage;
    var endIndex = startIndex + perPage;
    $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem`, function(data) {
      var product_item = data.items;
      if (product_item.length > 0) {
        totalPages = Math.ceil(product_item.length / perPage);
        $('#PRODUCT').html("");
        for (var i = startIndex; i < endIndex; i++) {
          if (i >= product_item.length) {
            break;
          }
          var productPage = product_item[i];
          var productPageId = productPage.id;
          var productPageSlug = productPage.meta.slug;
          var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}/?PRODUCT_OFFER`;
          $.getJSON(productPostsAPIURL, function(productsData) {
            var product = productsData;
            if (product.PRODUCT_OFFER.id > 0) {
              var postHTML = `
                <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                  <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                  <div class="card-body">
                    <h3 class="card-title h4">
                      <a href="" class="black-color">${product.title}</a>
                    </h3>
                    <span class="text-decoration-line-through icon2">${product.price}</span>
                    <span class="red-color">${product.PRODUCT_OFFER[0].value}<span>تومان</span></span>
                    <hr />
                    <div id="TOOLS" class="tolspro">
                    <span class="bi bi-heart" onclick="add_favourite(${product.id}, ${productPageSlug}, ${product.product_title},${product.image.url},'FV','SV',${product.PRODUCT_OFFER[0].value})"></span>
                      <span class="price"></span>
                      <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                      <span class="bi bi-arrow-left-right" onclick="add_comparison(${product.id},${productPageSlug},${product.product_title},${product.image.url},'FV','SV','1',${product.PRODUCT_OFFER[0].value})"></span>
                    </div>
                  </div>
                </div>
              `;
              $('#PRODUCT').append(postHTML);
            }
          });
        }
        if (page >= totalPages) {
          $('#load-more').hide();
        } else {
          $('#load-more').show();
        }
  
        page++;
      }
    });
  } else {
    loadProducts();
  }
});
function loadProductCategory() {
    $.getJSON(`/UNIQUEAPI174/pages/?type=category.CategoryProduct&order=-first_published_at`, function(data) {
      var totalChild = data.meta.total_count;
      var categoryData = data.items;

      for (var i = 0; i < totalChild; i++) {
        if (i >= totalChild) {
          break;
        }
        var pageCategory = categoryData[i];

        var category_to_pages = `<ul class="navliststyle asidecat">
        <li class="bbs1px">
          <a href="${pageCategory.meta.html_url}" class="black-color ahover">${pageCategory.title}</a>
          <span>${pageCategory.id}</span>
        </li>
      </ul>`;
        $('#setCat').append(category_to_pages);
      }
    });
  }
loadProductCategory();