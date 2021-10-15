#String Compression 

https://leetcode.com/problems/string-compression/

```python3
def compress(chars):
    length = len(chars)
    if length == 1:
        return 1
    sample = chars[0]
    chars.append(" ")
    count = 0
    for i in range(length + 1):
        char = chars[0]
        chars.pop(0)
        if char == sample:
            count += 1
        else:
            if count == 1:
                chars.append(sample)
            else:
                chars.append(sample)
                chars += list(str(count))
            sample = char
            count = 1
    return len(chars)
```
