// Linked List in Java
public class LinkedList {
    static class Node {
        int data;
        Node next;
        Node(int data) { this.data = data; }
    }
    Node head;
    public void append(int data) {
        Node node = new Node(data);
        if (head == null) { head = node; return; }
        Node current = head;
        while (current.next != null) current = current.next;
        current.next = node;
    }
    public void display() {
        Node current = head;
        StringBuilder sb = new StringBuilder();
        while (current != null) {
            sb.append(current.data);
            if (current.next != null) sb.append(" -> ");
            current = current.next;
        }
        System.out.println(sb);
    }
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.append(1); ll.append(2); ll.append(3);
        ll.display();
    }
}
