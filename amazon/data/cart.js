export let cart = JSON.parse(localStorage.getItem('cart'));

if(!cart){
    [{
        prodId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
        q: 2
    },{
        prodId: "15b6fc6f-327a-4ec4-896f-486349e85a3d",
        q: 1
    }]
}

function saveToStorage(){
    localStorage.setItem('cart',JSON.stringify(cart));
}

export function addtoCart(prodId) {
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
    saveToStorage();
}

export function removeCartItem(prodId) {
    const newCart = []
    
    cart.forEach((item) => {
        if (item.prodId !== prodId) {
            newCart.push(item);
        }
    })
    
    cart = newCart;

    saveToStorage();
}

export function calculateCartQuantity() {
    let cartQuantity = 0;
  
    cart.forEach((cartItem) => {
      cartQuantity += cartItem.quantity;
    });
  
    return cartQuantity;
  }