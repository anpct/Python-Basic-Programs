# Write a Python class to reverse a string word by word

class rev:
    def calc(self):
        return (" ".join(reversed(input("Enter the string: ").split())))
if __name__=="__main__":
    print(rev().calc())
