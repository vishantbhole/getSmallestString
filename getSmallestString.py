def getSmallestString(s: str) -> str:
    chars = list(s)

    for i in range(len(chars)):
        if chars[i] > 'a':
            chars[i] = chr(ord(chars[i]) - 1)  # Decrease character by one

            # Modify the first contiguous substring
            j = i + 1
            while j < len(chars) and chars[j] > 'a':
                chars[j] = chr(ord(chars[j]) - 1)
                j += 1

            return "".join(chars)  # Return modified string immediately

    # If all characters are 'a', change the last one to 'z'
    chars[-1] = 'z'
    return "".join(chars)

# Example usage:
if __name__ == "__main__":
    print(getSmallestString("aaaaa"))  # Output: "gackerrank"
