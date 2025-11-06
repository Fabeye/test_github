with open('C:\\Users\\Student\\Desktop\\test_github\\config\\config.txt', 'r') as file:
    lines = file.readlines()
    interval_value = int(lines[0].split('=')[-1])
    print(interval_value)