// Stack implementation in Java
import java.util.ArrayList;
public class Stack<T> {
    private ArrayList<T> items = new ArrayList<>();
    public void push(T item) { items.add(item); }
    public T pop() {
        if (isEmpty()) throw new RuntimeException("Stack is empty");
        return items.remove(items.size() - 1);
    }
    public T peek() {
        if (isEmpty()) throw new RuntimeException("Stack is empty");
        return items.get(items.size() - 1);
    }
    public boolean isEmpty() { return items.isEmpty(); }
    public int size() { return items.size(); }
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        s.push(1); s.push(2); s.push(3);
        System.out.println("Peek: " + s.peek());
        System.out.println("Pop: " + s.pop());
        System.out.println("Size: " + s.size());
    }
}
