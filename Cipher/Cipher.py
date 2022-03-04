from logger.logger import Logger


class Cipher:
    __log_obj = Logger("Logs//log.log")

    @staticmethod
    def encrypt_file(input_file_path, output_file_path, key):
        try:
            """method to encrypt the file""""
            file = open(input_file_path, 'rb')  # reading the file in binary mode
            data = file.read()
            file.close()





            Cipher.__log_obj.add_log(f"read data from file: {input_file_path} ")  # logging

            byte_array_data = bytearray(data)  # for each element in the data, getting its ASCII value.

            for index, item in enumerate(byte_array_data):
                byte_array_data[index] = byte_array_data[index] ^ key   # doing XOR so that we can encrypt each bit

            Cipher.__log_obj.add_log("Encrypted the file.")

            file = open(output_file_path, 'wb')  # writing the encrypted file
            file.write(byte_array_data)
            file.close()

            Cipher.__log_obj.add_log(f"The encrypted file has been stored at: {output_file_path}")

        except Exception as e:
            Cipher.__log_obj.add_log("Error occurred at file: ", input_file_path)
            Cipher.__log_obj.add_log(str(e))

    @staticmethod
    def decrypt_file(input_file_path, output_file_path, key):
        try:
            file = open(input_file_path, 'rb')
            data = file.read()
            file.close()
            Cipher.__log_obj.add_log(f"Encrypted file read : {input_file_path}")

            byte_array_data = bytearray(data)

            for index, item in enumerate(byte_array_data):
                byte_array_data[index] = byte_array_data[index] ^ key

            Cipher.__log_obj.add_log("Decryption done for file")

            file = open(output_file_path, 'wb')
            file.write(byte_array_data)
            file.close()
            Cipher.__log_obj.add_log(f"The decrypted file is stored at :{output_file_path}")

        except Exception as e:
            Cipher.__log_obj.add_log("Error occurred at file ", input_file_path)
            Cipher.__log_obj.add_log(str(e))


