// Linked List in JavaScript
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}
class LinkedList {
    constructor() { this.head = null; }
    append(data) {
        const node = new Node(data);
        if (!this.head) { this.head = node; return; }
        let current = this.head;
        while (current.next) current = current.next;
        current.next = node;
    }
    display() {
        const elements = [];
        let current = this.head;
        while (current) { elements.push(current.data); current = current.next; }
        console.log(elements.join(" -> "));
    }
}
const ll = new LinkedList();
ll.append(1); ll.append(2); ll.append(3);
ll.display();
