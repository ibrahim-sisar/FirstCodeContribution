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

## 🔹 Example of a Correct Submission (C)
### ✅ Participant's Contribution (Only This Part is Required)
```c
// John Doe
// GitHub: https://github.com/johndoe

int JohnDoe(int arr[], int size) {
    int max_value = arr[0]; // Assume the first element is the largest
    for (int i = 1; i < size; i++) {
        if (arr[i] > max_value) {
            max_value = arr[i];
        }
    }
    return max_value;
}
```
## 📌 Pre-existing Code (Call your function only) 
```c
#include <stdio.h>
int JohnDoe(int arr[], int size);
int main() {
    int arr[] = {10, 45, 3, 67, 23};
    printf("%d\n", JohnDoe(arr, 5));  
}
// john doe
// https://github.com/JohnDoe

int JohnDoe(int arr[], int size) {
    int max_value = arr[0];
    for (int i = 0; i < size; i++) {
        if (arr[i] > max_value) {
            max_value = arr[i];
        }
    }
    return max_value;
}

```

---
## 💡 Additional Notes:
### 🚨 DO NOT modify main()—just call your function inside it.
### ✅ Make sure your function correctly finds the largest number in the array.
### 🔹 Ensure your function name is exactly the same as your name (case-sensitive).
### 🔥 Once done, commit your changes and submit a pull request.

## 📢 Good luck and happy coding! 🚀
