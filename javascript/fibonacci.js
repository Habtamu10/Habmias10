// Fibonacci using dynamic programming
function fibonacci(n) {
    const dp = [0, 1];
    for (let i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}
for (let i = 0; i < 10; i++) {
    process.stdout.write(fibonacci(i) + " ");
}
console.log();
