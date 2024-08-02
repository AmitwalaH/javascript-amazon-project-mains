export const cart = []

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