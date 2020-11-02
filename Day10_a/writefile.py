def writeFunc():
    msg = input("Enter a string:")
    try:
        f = open("data.txt", "a")
        print("\n", file=f)
        print(msg, file=f)
        print("Data inserted Successfully")

    except Exception as e:
        print(f'Warning: {e}')

    finally:
        f.close()


def readfun():
    try:
        f = open("data.txt", "r")
        for line in f.readlines():
            print(line)

    except Exception as e:
        print(f'Warning: {e}')

    finally:
        f.close()


if __name__ == "__main__":
    writeFunc()
