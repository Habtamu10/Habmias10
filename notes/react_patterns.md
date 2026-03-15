# React Patterns and Best Practices

## Functional Component
```jsx
const Button = ({ label, onClick, disabled = false }) => (
    <button onClick={onClick} disabled={disabled}>
        {label}
    </button>
);
```

## useState Hook
```jsx
const [count, setCount] = useState(0);
setCount(prev => prev + 1);
```

## useEffect Hook
```jsx
useEffect(() => {
    fetchData();
    return () => cleanup();
}, [dependency]);
```

## useCallback and useMemo
```jsx
const handleClick = useCallback(() => doSomething(id), [id]);
const expensiveValue = useMemo(() => compute(data), [data]);
```

## Custom Hook
```jsx
function useLocalStorage(key, initial) {
    const [value, setValue] = useState(initial);
    const setStored = (val) => {
        setValue(val);
        localStorage.setItem(key, JSON.stringify(val));
    };
    return [value, setStored];
}
```
