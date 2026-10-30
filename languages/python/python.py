def main():
  arr = [2,7,9,23,8,6,1,0,-1,5,4,3]
  # Call your function
  print(AdarshPatil07(arr))

#name : Raghavendra31 and link : https://github.com/Raghavendra31

def Raghavendra31():
  arr = input("Enter numbers separated by spaces: ").split()
  sortarr = sorted(arr, reverse=True)
  print(f"The largest number in the array is: {sortarr[0]}")
  return sortarr[0]
  

"""
 You need to write a function that takes an array as input and returns the largest number in that array.
 Above your function, write a comment with your name and GitHub link.
 Name your function after your name, considering case sensitivity in the programming language.
Call your function inside the pre-existing main() function (which is already written in the file).
"""


# Name: Adarsh Patil
# GitHub: https://github.com/adarshpatil-07
def AdarshPatil07(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value


if __name__ == "__main__":
  main()
  raghavendra31 = Raghavendra31()
# 📢 Good luck and happy coding! 🚀

