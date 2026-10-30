# 🐍 Python Contribution Guide

Welcome to the Python section of **First Code Collaboration!** 🎉

This is your opportunity to make your first open-source contribution using Python. Whether you're a beginner or an experienced developer, you're welcome to participate!

## 📌 Task Description

Your task is to write a Python function that takes a list of numbers as input and returns the largest number in that list.

### Requirements

1. Write a function that accepts a list of numbers (`list`) as an argument.
2. Return the largest number in the list.
3. Add a comment above your function containing your name and GitHub profile link.
4. Name your function after your GitHub username. Use underscores (`_`) instead of spaces or special characters if necessary.
5. Call your function inside the existing `main()` function.

## 📝 Instructions for Contributors

- Do not modify or delete other contributors' functions.
- Do not change the existing list inside `main()`.
- You are allowed to add a single function call inside `main()` to execute your function.
- Add your function in the designated contribution section, following the existing code structure.
- Your function must accept the predefined list as an argument. Do not request input from the user.
- Your function must return the largest number rather than only printing it.
- Make sure your function name matches the name used in the function call.

## 💡 Example Contribution

Suppose your GitHub username is `JohnDoe`.

**1. Add your function:**

```python
# Name: John Doe
# GitHub: https://github.com/johndoe

def JohnDoe(arr):
    max_value = arr[0]

    for num in arr:
        if num > max_value:
            max_value = num

    return max_value
```

**2. Add your function call inside `main()`:**

```python
def main():
    arr = [10, 45, 3, 67, 23]

    print(JohnDoe(arr))
```

**Important:** Only add your own function and its corresponding function call. Do not modify the existing code or other contributors' work.

## 🧪 Testing Your Function

For the list:

```python
[10, 45, 3, 67, 23]
```

Expected output:

```text
67
```

## 🚀 Submitting Your Contribution

1. Fork this repository.
2. Clone your fork to your local machine.
3. Add your name and GitHub profile link to `CONTRIBUTING.md`.
4. Navigate to `languages/python/python.py`.
5. Add your function and its corresponding function call inside `main()`.
6. Test your code.
7. Commit and push your changes.
8. Submit a Pull Request to the original repository.

## 🎉 Thank You!

Thank you for contributing to **First Code Collaboration!**

Your contribution helps make open source more welcoming to beginners around the world.

Happy coding! 💻🚀
