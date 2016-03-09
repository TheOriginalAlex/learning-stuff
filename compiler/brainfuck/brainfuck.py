import sys
from interpreter import Interpreter

def main():
    while True:
        try:
            text = raw_input('fuck> ')
        except EOFError:
            break
        if not text:
            continue
        if text == "exit":
            print("Exiting...")
            sys.exit(0);
        interpreter = Interpreter(text)
        result = interpreter.run()
        print(result)


if __name__ == '__main__':
    main()
