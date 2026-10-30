# 🐍 Python Contribution Guide

Welcome to the Python section of **First Code Collaboration!** 🎉

This is your opportunity to make your first open-source contribution using Python. Whether you're a beginner or an experienced developer, you're welcome to participate!

## 📌 Your Task

Write a Python function that takes a list of numbers as input and returns the largest number in that list.

### Requirements

1. Write a function that accepts a list of numbers (`list`) as an argument.
2. Return the largest number in the list.
3. Add a comment above your function containing your name and GitHub profile link.
4. Name your function after your GitHub username. Use underscores (`_`) instead of spaces or special characters if necessary.
5. Do not modify any existing code outside your contribution.
6. Do not modify the existing `main()` function.
7. Do not add function calls outside your own function.

## 📝 Example Contribution

```python
# Name: John Doe
# GitHub: https://github.com/johndoe

def johndoe(arr):
    if not arr:
        return None

    return max(arr)
```

## ⚠️ Important Rules

- Only add your own function to the designated contribution section in `python.py`.
- Do not change or delete other contributors' code.
- Do not modify `main()` or the execution block.
- Your function must receive the list as an argument, not ask the user to enter numbers.
- Your function must return the result instead of only printing it.
- Make sure your code works correctly before submitting your Pull Request.

## 🧪 Testing Your Function

You can test your function locally using:

```python
print(johndoe([10, 45, 3, 67, 23]))
# Expected output: 67
```

Additional test cases:

```python
print(johndoe([-5, -2, -10]))
# Expected output: -2

print(johndoe([42]))
# Expected output: 42

print(johndoe([]))
# Expected output: None
```

## 🚀 Submitting Your Contribution

1. Fork the repository.
2. Clone your fork.
3. Add your name to `CONTRIBUTING.md`.
4. Open `languages/python/python.py`.
5. Add your function to the designated contribution section.
6. Commit and push your changes.
7. Open a Pull Request to the original repository.

## 🎉 Thank You!

Thank you for contributing to First Code Collaboration!

Every contribution matters, and we're happy to help you take your first step into the open-source community.

Happy coding! 💻
