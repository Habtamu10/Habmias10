// Promises in JavaScript
function fetchData(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (id > 0) resolve({ id, name: "Habtamu" });
            else reject(new Error("Invalid ID"));
        }, 100);
    });
}
fetchData(1)
    .then(data => console.log("Data:", data))
    .catch(err => console.error("Error:", err.message));
