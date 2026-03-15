# Algorithm Complexity (Big O) Reference

## Common Complexities (best to worst)
| Notation | Name        | Example                 |
|----------|-------------|-------------------------|
| O(1)     | Constant    | Array access            |
| O(log n) | Logarithmic | Binary search           |
| O(n)     | Linear      | Linear search           |
| O(n log n) | Linearithmic | Merge sort, Heap sort |
| O(n^2)   | Quadratic   | Bubble sort, Selection  |
| O(2^n)   | Exponential | Recursive Fibonacci     |
| O(n!)    | Factorial   | Brute-force permutation |

## Sorting Algorithms
| Algorithm    | Best     | Average  | Worst    | Space  |
|-------------|----------|----------|----------|--------|
| Bubble Sort | O(n)     | O(n^2)   | O(n^2)   | O(1)   |
| Merge Sort  | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort  | O(n log n) | O(n log n) | O(n^2) | O(log n) |
| Heap Sort   | O(n log n) | O(n log n) | O(n log n) | O(1) |
