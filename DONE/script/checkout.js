import { cart, removeCartItem, calculateCartQuantity, updateQuantity } from '../data/cart.js';
import { products } from '../data/products.js';
import { formatCurrency } from './utility/money.js';

let matchingProduct = '';

// Iterate through each item in the cart and find the corresponding product in the products list
cart.forEach((item) => {
  let prodId = item.prodId;
  let matchingProd;

  // Find the matching product
  products.forEach((product) => {
    if (product.id === prodId) {
      matchingProd = product;
    }
  });

  // Build the HTML structure for the cart items
  matchingProduct += ` <div class="cart-item-container js-cart-container-${matchingProd.id}">
            <div class="delivery-date">
              Delivery date: Tuesday, June 21
            </div>

            <div class="cart-item-details-grid">
              <img class="product-image" src="${matchingProd.image}">

              <div class="cart-item-details">
                <div class="product-name">${matchingProd.name}</div>
                <div class="product-price">${formatCurrency(matchingProd.priceCents)}</div>
                <div class="product-quantity">
                  <span>
                    Quantity: <span class="quantity-label js-quantity-label-${matchingProd.id}">${item.q}</span>
                  </span>
                  <span class="update-quantity-link link-primary js-update-link" data-product-id="${matchingProd.id}">
                    Update
                  </span>
                  <input class="quantity-input js-quantity-input-${matchingProd.id}">
                  <span class="save-quantity-link link-primary js-save-link" data-product-id="${matchingProd.id}">
                     Save
                  </span>                  
                  <span class="delete-quantity-link link-primary js-delete-link" data-product-id="${matchingProd.id}">
                    Delete
                  </span>
                </div>
              </div>

              <div class="delivery-options">
                <div class="delivery-options-title">
                  Choose a delivery option:
                </div>
                <div class="delivery-option">
                  <input type="radio" checked class="delivery-option-input" name="delivery-option-${matchingProd.id}">
                  <div>
                    <div class="delivery-option-date">
                      Tuesday, June 21
                    </div>
                    <div class="delivery-option-price">
                      FREE Shipping
                    </div>
                  </div>
                </div>
                <div class="delivery-option">
                  <input type="radio" class="delivery-option-input" name="delivery-option-${matchingProd.id}">
                  <div>
                    <div class="delivery-option-date">
                      Wednesday, June 15
                    </div>
                    <div class="delivery-option-price">
                      $4.99 - Shipping
                    </div>
                  </div>
                </div>
                <div class="delivery-option">
                  <input type="radio" class="delivery-option-input" name="delivery-option-${matchingProd.id}">
                  <div>
                    <div class="delivery-option-date">
                      Monday, June 13
                    </div>
                    <div class="delivery-option-price">
                      $9.99 - Shipping
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>`;
});

// Insert the generated HTML into the cart summary section
document.querySelector('.js-cart-summary').innerHTML = matchingProduct;

// Handle delete button clicks
document.querySelectorAll('.js-delete-link').forEach((link) => {
  link.addEventListener('click', () => {
    const prodId = link.dataset.productId;
    removeCartItem(prodId);

    // Remove the corresponding cart item container
    let container = document.querySelector(`.js-cart-container-${prodId}`);
    container.remove();

    // Update the cart quantity
    updateCartQuantity();
  });
});

// Function to update the cart quantity displayed
export function updateCartQuantity() {
  let cartQuantity = calculateCartQuantity(); // Assuming this function exists and works as intended

  // Update the return-to-home-link with the current cart quantity
  document.querySelector('.js-return-to-home-link').innerHTML = `${cartQuantity} items`;
}

// Initialize the cart quantity on page load
updateCartQuantity();

// Handle the 'Update' button click, which allows editing the quantity
document.querySelectorAll('.js-update-link').forEach((link) => {
  link.addEventListener('click', () => {
    const productId = link.dataset.productId;
    const container = document.querySelector(`.js-cart-container-${productId}`);
    container.classList.add('is-editing-quantity'); // Show the input field for editing
  });
});

// Handle the 'Save' button click to save the updated quantity
document.querySelectorAll('.js-save-link').forEach((link) => {
  link.addEventListener('click', () => {
    const productId = link.dataset.productId;

    // Retrieve the container and quantity input elements
    const container = document.querySelector(`.js-cart-container-${productId}`);
    const quantityInput = document.querySelector(`.js-quantity-input-${productId}`);
    const newQuantity = Number(quantityInput.value);

    // Validate the new quantity
    if (newQuantity < 0 || newQuantity >= 1000) {
      alert('Quantity must be at least 0 and less than 1000');
      return; // Early return if validation fails
    }

    // Update the quantity and remove the editing state
    updateQuantity(productId, newQuantity);
    container.classList.remove('is-editing-quantity');

    // Update the quantity label with the new value
    const quantityLabel = document.querySelector(`.js-quantity-label-${productId}`);
    quantityLabel.innerHTML = newQuantity;

    // Update the cart quantity after modification
    updateCartQuantity();
  });
});
