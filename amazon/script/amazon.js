
import {cart} from '../data/cart.js';
import {products} from '../data/products.js';

let productDocs = '';

products.forEach((product) => {
  productDocs += `<div class="product-container">
          <div class="product-image-container">
            <img class="product-image"
              src="${product.image}">
          </div>

          <div class="product-name limit-text-to-2-lines">
            ${product.name}
          </div>

          <div class="product-rating-container">
            <img class="product-rating-stars"
              src="images/ratings/rating-${product.rating.stars * 10}.png">
            <div class="product-rating-count link-primary">
              ${product.rating.count}
            </div>
          </div>

          <div class="product-price">
            ${product.priceCents / 100}
          </div>

          <div class="product-quantity-container">
            <select>
              <option selected value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              <option value="6">6</option>
              <option value="7">7</option>
              <option value="8">8</option>
              <option value="9">9</option>
              <option value="10">10</option>
            </select>
          </div>

          <div class="product-spacer"></div>

          <div class="added-to-cart">
            <img src="images/icons/checkmark.png">
            Added
          </div>

          <button class="add-to-cart-button button-primary js-add-cart" data-prod-id = "${product.id}">
            Add to Cart
          </button>
        </div>`
});


// console.log(productDocs)

document.querySelector('.js-prod-grid').innerHTML = productDocs;

document.querySelectorAll('.js-add-cart').forEach((button) => {
  button.addEventListener('click', () => {
    const prodId = button.dataset.prodId;

    let matchingItem;

    cart.forEach((item) => {
      if (prodId === item.prodId) {
        matchingItem = item;
      }
    });

    if (matchingItem) {
      matchingItem.q = Number(matchingItem.q) + 1;
    } 
    else {
      cart.push({
        prodId: prodId,
        q: 1
      });
    }

    let cartCount = 0;
    
    cart.forEach((item) => {
      cartCount += Number(item.q);
    });

    document.querySelector('.js-cart-quat').innerHTML = cartCount;

    console.log(cartCount);
    console.log(cart);
  });
});


