"Try Exception"

print("1")
try:
    f = open('teste.txt')
except Exception:
    print("1-Sorry. This file does not exist.")
# else:
#     pass
# finally:
#     pass

print("\n2")
try:
    f = open('test.txt')
    var = bad_var
except FileNotFoundError:
    print("2-Sorry. This file does not exist.")
except Exception:
    print("Sorry. Something went wrong!")
# else:
#     pass
# finally:
#     pass

print("\n3")
try:
    f = open('test.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)


print("\n4")
try:
    f = open('test.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()


print("\n5")
try:
    f = open('test.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")


print("\n6")
try:
    f = open('teste.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")


print("\n7")
try:
    f = open('test.txt')
    if f.name == 'test.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Erro!")
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
