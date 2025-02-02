# 📄 Documentation: Instructions for Participants

## 📌 Task Description:

### 🔹 You need to write a function that takes an array as input and returns the largest number in that array.
### 🔹 Above your function, write a comment with your name and GitHub link.
### 🔹 Name your function after your name, considering case sensitivity in the programming language.
### 🔹 Call your function inside the pre-existing `main()` function (which is already written in the file).

---
## 📝 Instructions for Participants:
### ✅ Do not modify anything outside your function. The `main()` function is already written for you.
### ✅ Write a comment above your function with your name and GitHub link.
### ✅ Name your function exactly as your name (avoid spaces or special characters, use underscores `_` if needed).
### ✅ Ensure your function correctly finds and returns the largest number in the given array.
### ✅ Call your function inside `main()` (the `main()` function is already there, just use your function inside it).
---

##🔹 Example of a Correct Submission (Python)
### ✅ Participant's Contribution (Only This Part is Required)
```python
# John Doe
# GitHub: https://github.com/johndoe

def JohnDoe(arr):
    max_value = arr[0]  # Assume the first element is the largest
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value
```
## 📌 Pre-existing Code (Call your function only) 
```python
def main():
    arr = [10, 45, 3, 67, 23]
    print(JohnDoe(arr))  # Call your function here

# John Doe
# GitHub: https://github.com/johndoe

def JohnDoe(arr):
    max_value = arr[0]  # Assume the first element is the largest
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

if __name__ == "__main__":
    main()
```

---
## 💡 Additional Notes:
### 🚨 DO NOT modify main()—just call your function inside it.
### ✅ Make sure your function correctly finds the largest number in the array.
### 🔹 Ensure your function name is exactly the same as your name (case-sensitive).
### 🔥 Once done, commit your changes and submit a pull request.

## 📢 Good luck and happy coding! 🚀
