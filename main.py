from Cipher.Cipher import Cipher

if __name__ == '__main__':
    cipher_obj = Cipher()

    while True:
        try:

            print("Enter your option: ")
            print("1. Encrypt your files: ")
            print("2. Decrypt your files: ")
            print("-1. quit ")
            option = int(input("Enter the option : "))

            print("-----------------------------------------------------------------------------------")

            if option == 1:
                input_file_path = input("Enter the input file path:  ")
                output_file_path = input("Enter the output file path: ")
                key1 = input("input enter your key")

                key = 0
                for i in key1:
                    key += ord(i)

                key = key % 256

                cipher_obj.encrypt_file(input_file_path, output_file_path, key)

                print("-----------------------------------------------------------------------------------")

            elif option == 2:
                input_file_path = input("Enter the input file path:  ")
                output_file_path = input("Enter the output file path: ")
                key1 = input("input enter your key")

                key = 0
                for i in key1:
                    key += ord(i)

                key = key % 256

                cipher_obj.decrypt_file(input_file_path, output_file_path, key)

                print("-----------------------------------------------------------------------------------")


            elif option == -1:
                break

            else:
                print("option entered is wrong. ")

        except Exception as e:
            print(str(e))
            print("option entered is invalid. Provide valid input.")
