$(document).ready(function() {
    var search_text = $('.searchnox').val();
    var perPage = 8;
    var page = 1;
    function search() {
      var startIndex = (page - 1) * perPage;
      var endIndex = startIndex + perPage;
      $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem&search=${search_text}`, function(data) {
        var product_item = data.items;
        if (product_item.length > 0) {
          document.title = search_text;
          var pagebody = `
          <header class="headerblog">
          <div class="h1divhead">
            <h1 class="blogh1 white-color">
              ${search_text}
            </h1>
          </div>
        </header>
        <div class="container-fluid">
          <div id="PRODUCT" class="row">
          </div>
          <div class="plusbutton">
          <button type="button" class="btn btn-outline-danger" id="load-more">
        بارگیری بیشتر محصولات
          </button>
          </div>
          </div>
          <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.min.js"
          integrity="sha384-Y4oOpwW3duJdCWv5ly8SCFYWqFDsfob/3GkgExXKV4idmbt98QcxXYs9UoXAB7BZ"
          crossorigin="anonymous"
        ></script>
          `;
          $('#BODY').html(pagebody);
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
                        <span class="bi bi-heart"></span>
                        <span class="price"></span>
                        <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                        <span class="bi bi-arrow-left-right"></span>
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
                        <span class="bi bi-heart"></span>
                        <span class="price"></span>
                        <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                        <span class="bi bi-arrow-left-right"></span>
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
        }else{
          document.title = "چیزی پیدا نشد";
          var pagebody = `
          <header class="headerblog">
          <div class="h1divhead">
            <h1 class="blogh1 white-color">
              محتوایی مطابق با جستجوی درخواستی پیدا نشد
            </h1>
          </div>
        </header>
        <div class="container-fluid">
          <div id="PRODUCT" class="row">
          <p>متاسفانه محتوایی مطابق با جستجوی شما یافت نشد</p>
          </div>
          <div class="plusbutton">
          <a href="/"><button type="button" class="btn btn-outline-danger" id="load-more">بازگشت به خانه</button></a>
          </div>
          </div>
          <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.min.js"
          integrity="sha384-Y4oOpwW3duJdCWv5ly8SCFYWqFDsfob/3GkgExXKV4idmbt98QcxXYs9UoXAB7BZ"
          crossorigin="anonymous"
        ></script>
          `;
          $('#BODY').html(pagebody);
        }
      });
    }
    $('#load-more').click(function() {
        search();
      });
      $('#search_product').click(function() {
        search();
      });
  });