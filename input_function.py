import generator


def dialog(Recognizer):
    dialog = True

    while dialog:
        dialog = False
        print('Hello, how do your want to input lines (File or Console)')
        input_type = input().lower()
        if input_type == "file" or input_type == "f":
            print("Input filename:")
            filename = input()
            all_strings = generator.Generator(1000000, filename).get_file_content()
            recognizer = Recognizer
            recognizer.__strings = all_strings
            recognizer.check_strings_from_file()
            recognizer.analyze_overload()
            print("Data was saved to the file")
            print("Show statistic (y/n):")
            input_show = input().lower()
            if input_show == "yes" or input_type == "y":
                Over_A = recognizer.get_Over()
                for key in Over_A:
                    if Over_A.get(key) > 1:
                        print(str(key) + ' ' + str(Over_A.get(key)) + '\n')
                try:
                    f = open(recognizer.get_Time())
                    nf = f.read()
                    print("Time:", nf.split('\n')[1])

                    f.close()
                except IOError as e:
                    print("---- Error ----")

        elif input_type == "console" or input_type == "c":
            recognizer = Recognizer
            recognizer.__file = False
            recognizer.check_strings_from_console()
        else:
            print("You are wrong! Try again")
            dialog = True