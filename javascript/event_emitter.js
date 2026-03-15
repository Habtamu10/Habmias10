// Event Emitter implementation
class EventEmitter {
    constructor() {
        this._events = {};
    }
    on(event, listener) {
        if (!this._events[event]) this._events[event] = [];
        this._events[event].push(listener);
        return this;
    }
    off(event, listener) {
        if (!this._events[event]) return this;
        this._events[event] = this._events[event].filter(l => l !== listener);
        return this;
    }
    emit(event, ...args) {
        if (!this._events[event]) return false;
        this._events[event].forEach(listener => listener(...args));
        return true;
    }
    once(event, listener) {
        const wrapper = (...args) => {
            listener(...args);
            this.off(event, wrapper);
        };
        return this.on(event, wrapper);
    }
}
const emitter = new EventEmitter();
emitter.on("greet", name => console.log(`Hello, ${name}!`));
emitter.emit("greet", "Habtamu");
