from calculator import perform_operation,takeinputs
def main():
    test_takeinputs();


def test_takeinputs():
    try:
        assert takeinputs();
    except AssertionError:
         print("test failed !")
    else:
        assert perform_operation(takeinputs()) != 4;


if __name__ == "__main__":
    main();