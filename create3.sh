 
#!/bin/bash

# Output file
output_file="large4.txt"

# Desired file size in KB
desired_size=130

# Fetch Lorem Ipsum text and append to the output file until the desired size is reached
while [ $(stat -c%s "$output_file") -lt $((desired_size * 1024)) ]; do
    curl -sL "https://www.lipsum.com/feed/json?amount=1000" | jq -r '.feed.lipsum' >> "$output_file"
done
