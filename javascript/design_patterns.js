// JavaScript Design Patterns

// Singleton
class Database {
    constructor() {
        if (Database.instance) return Database.instance;
        this.connection = "Connected";
        Database.instance = this;
    }
}
const db1 = new Database();
const db2 = new Database();
console.log("Same instance:", db1 === db2); // true

// Observer
class Subject {
    constructor() { this.observers = []; }
    subscribe(fn) { this.observers.push(fn); }
    unsubscribe(fn) { this.observers = this.observers.filter(obs => obs !== fn); }
    notify(data) { this.observers.forEach(fn => fn(data)); }
}
const subject = new Subject();
const obs1 = data => console.log("Observer 1:", data);
const obs2 = data => console.log("Observer 2:", data);
subject.subscribe(obs1);
subject.subscribe(obs2);
subject.notify("Hello!");
subject.unsubscribe(obs1);
subject.notify("World!");
