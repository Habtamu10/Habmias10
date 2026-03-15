// Async/Await in JavaScript
async function fetchUser(id) {
    return new Promise(resolve =>
        setTimeout(() => resolve({ id, name: "Habtamu", role: "Engineer" }), 100)
    );
}
async function main() {
    const user = await fetchUser(42);
    console.log("User:", user);
}
main();
