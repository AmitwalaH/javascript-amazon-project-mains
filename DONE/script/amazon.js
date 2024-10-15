import { cart, addtoCart, calculateCartQuantity } from '../data/cart.js';
import { products } from '../data/products.js';
import { formatCurrency } from './utility/money.js';

let productDocs = '';

// Loop through the products and build the HTML structure for the product grid
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
            ${formatCurrency(product.priceCents)}
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

          <button class="add-to-cart-button button-primary js-add-cart" data-prod-id="${product.id}">
            Add to Cart
          </button>
        </div>`;
});

// Insert the generated product HTML into the product grid
document.querySelector('.js-prod-grid').innerHTML = productDocs;

// Function to update the cart quantity displayed in the cart icon
export function updateCartQuantity() {
  let cartQuantity = 0;

  // Calculate the total quantity from the cart
  cart.forEach((item) => {
    cartQuantity += Number(item.q);
  });

  // Use `calculateCartQuantity` if it's meant to calculate from a different source
  const calculatedCartQuantity = calculateCartQuantity();
  cartQuantity = calculatedCartQuantity ? calculatedCartQuantity : cartQuantity;

  // Update the cart quantity only if it's not zero
  if (cartQuantity !== 0) {
    document.querySelector('.js-cart-quantity').innerHTML = cartQuantity;
  }
}

// Initial update to display the cart quantity on page load
updateCartQuantity();

// Add event listeners to all 'Add to Cart' buttons
document.querySelectorAll('.js-add-cart').forEach((button) => {
  button.addEventListener('click', () => {
    const prodId = button.dataset.prodId;

    // Call the function to add the product to the cart
    addtoCart(prodId);

    // Update the cart quantity after adding a product
    updateCartQuantity();
  });
});
