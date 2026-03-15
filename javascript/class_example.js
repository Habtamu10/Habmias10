// JavaScript ES6 Classes
class Animal {
    constructor(name, sound) {
        this.name = name;
        this.sound = sound;
    }
    speak() {
        console.log(`${this.name} says ${this.sound}`);
    }
}
class Dog extends Animal {
    constructor(name) {
        super(name, "Woof");
    }
    fetch(item) {
        console.log(`${this.name} fetches the ${item}`);
    }
}
const dog = new Dog("Rex");
dog.speak();
dog.fetch("ball");
