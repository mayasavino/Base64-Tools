import base64
import binascii


def base64_encode(initial_string):
    initial_bytes = initial_string.encode('utf-8') # convert string to bytes
    encoded_bytes = base64.b64encode(initial_bytes) # encode bytes to base64
    encoded_string = encoded_bytes.decode('utf-8') # convert encoded bytes to a string
    return encoded_string

def base64_decode(encoded_string):
    try:
        decoded_bytes = base64.b64decode(encoded_string) # convert string to bytes
        decoded_string = decoded_bytes.decode('utf-8') # decode bytes to plain text
        return decoded_string
    except binascii.Error as e:
        print(f'Error: {e}')
        print('Possible issues:')
        print(' - Invalid Base64 data')
        print(' - Binary data instead of text data')
        exit()
        
    except UnicodeDecodeError as e:
        print(f'Error: {e}')
        print('Possible issues:')
        print(' - Invalid UTF-8 data')
        print(' - Unsupported characters')
        print(' - Incorrect encoding specified')
        exit()

def output(results):
    choice = input('Print results or output to text file?(P/F): ').lower()
    while 1: # loop until input is valid
        if choice == 'p': # Print
            print(results)
            break
        elif choice == 'f': # Output to text file
            with open('results.txt', 'w') as f: # write results to results.txt
                f.write(results)
            print('Results can be found in \"results.txt\"')
            break
        else:
            print('Invalid input. Valid inputs: P, F')

def main():
    while 1: # loop until input is valid
        choice = input('Encode or Decode?(E/D): ').lower()
        if choice == 'e': # Encode
            initial_string = input('Enter text to encode: ')
            encoded_string = base64_encode(initial_string)
            output(encoded_string) # choose output type
            break
        elif choice == 'd': # Decode
            encoded_string = input('Enter text to decode: ')
            decoded_string = base64_decode(encoded_string)
            output(decoded_string) # choose output type
            break
        else:
            print('Invalid input. Valid inputs: E, D')


if __name__ == "__main__":
    main()
