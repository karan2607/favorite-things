a = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 119, 101, 102, 102, 107, 102, 112, 102, 108, 101, 109, 115, 105, 115, 111, 100, 100 ]


b=[]
for i in a:
    b.append("".join(chr(i)))
c = "".join(b)
print(c)



from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABc-tUsOQKQhFzV8Ey3vYo8DU7YXqX0olF1C9zS2QwOpBarpsfEZyYkRRIvE88FAdqDjB0oqyBAo4oTgj6aBpxD2IaWNItjh3OZe7ZpI0o8QZqTJA1YRNT9IOr3uVUSNgSz3UYHCdLolds428zIw4r0FsCWw80rWeNbsGPlk4Vm989BTp0='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()