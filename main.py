def helloworld(a):
    msg = f"Hello World! {a}!"
    print(msg)  # black test
    return msg


if __name__ == "__main__": # pragma: no cover
    helloworld("test")
