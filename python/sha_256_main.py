import sha_256_preprocessing
import sha_256_hash

def main():
    input_message = input("enter the message you want to hash: \n")
    message = sha_256_preprocessing.padding(input_message)
    print(message)
    print(len(message)) # should be multiple of 64 bytes (512 bits)
    
    M = sha_256_preprocessing.chunk_divider(message)
    print(M)
    print(len(M))

    ret = sha_256_hash.sha_256_secure_hash(M)
    print(ret)
    



if __name__ == "__main__":
    main()