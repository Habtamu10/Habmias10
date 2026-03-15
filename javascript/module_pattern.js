// JavaScript Module Pattern (IIFE)
const ShoppingCart = (() => {
    const _items = [];
    function _findIndex(id) {
        return _items.findIndex(item => item.id === id);
    }
    return {
        add(item) {
            const idx = _findIndex(item.id);
            if (idx >= 0) _items[idx].quantity++;
            else _items.push({ ...item, quantity: 1 });
        },
        remove(id) {
            const idx = _findIndex(id);
            if (idx >= 0) _items.splice(idx, 1);
        },
        total() {
            return _items.reduce((sum, item) => sum + item.price * item.quantity, 0);
        },
        items() { return [..._items]; }
    };
})();

ShoppingCart.add({ id: 1, name: "Book", price: 15 });
ShoppingCart.add({ id: 2, name: "Pen", price: 2 });
ShoppingCart.add({ id: 1, name: "Book", price: 15 });
console.log("Items:", ShoppingCart.items());
console.log("Total: $" + ShoppingCart.total());
