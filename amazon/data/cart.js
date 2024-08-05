export let cart = [{
    prodId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
    q: 2
},{
    prodId: "15b6fc6f-327a-4ec4-896f-486349e85a3d",
    q: 1
}]

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
}
 
 export function removeCartItem(prodId) {
    const newCart = []

    cart.forEach((item) => {
        if (item.prodId !== prodId) {
            newCart.push(item);
        }
    })

    cart = newCart;
}