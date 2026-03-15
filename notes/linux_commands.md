# Essential Linux Commands

## File and Directory Operations
```bash
ls -la                    # List with details
pwd                       # Print working directory
cd /path/to/dir           # Change directory
mkdir -p dir/sub/dir      # Create nested dirs
cp -r src/ dest/          # Copy recursively
mv old_name new_name      # Move/rename
rm -rf directory/         # Remove recursively
find . -name "*.py"       # Find files
```

## File Content
```bash
cat file.txt              # Print file
head -20 file.txt         # First 20 lines
tail -f log.txt           # Follow log
grep -r "pattern" .       # Search recursively
wc -l file.txt            # Count lines
sort file.txt             # Sort lines
```

## Process Management
```bash
ps aux                    # All processes
top                       # Interactive process view
jobs                      # Background jobs
nohup ./script.sh &       # Run in background
```

## Network
```bash
curl -X GET http://api.example.com
ping google.com
netstat -tlnp             # Open ports
```
