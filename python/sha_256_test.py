import sha_256_preprocessing

def main():
    input_message = input("enter the message you want to hash: \n")
    message = sha_256_preprocessing.padding(input_message)
    print(message)

if __name__ == "__main__":
    main()