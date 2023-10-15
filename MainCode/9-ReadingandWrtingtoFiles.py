"All this code is about how to read and writ into files"

import os


print(os.getcwd())
print("\n\n\n test.txt")
ff = open(file="test.txt", mode='r')
print(ff.name)
print(ff.mode)

print(ff.readline(), end="")
print(ff.readlines(), end="")
print(ff.read(), end="")
ff.close()

print("\n\n\n README.md")
with open('readme.md', "r") as f:
    print(f.name)
    print(f.mode)
    f_contents = f.read()
    print(f_contents)

print(f.closed)
print(ff.closed)

print("\n\n\n text.txt loop")

with open("test.txt", 'r') as tx:
    count = 0
    for line in tx:
        count += 1
        print(f"Line {count}: {line}", end="")

print("\n\n\n text.txt loop2")

with open("test.txt", 'r') as tx:
    count = 0
    for line in tx.read(100):
        count += 1
        print(f"\nLine {count}: {line}", end="")


print("\n\n\n text.txt iteration with while")

with open("test.txt", 'r') as tx:
    count = 0
    size_to_read = 9
    tx_contents = tx.read(size_to_read)

    while len(tx_contents) > 0:
        count += 1
        print(f"\nLine {count}: {tx_contents}", end="")
        print(f"\nIndex: {tx.tell()}")
        tx_contents = tx.read(size_to_read)

print("\n Write text file")
with open("test.txt", 'r') as rf:
    with open("test_copy.txt", 'w') as wf:
        for line in rf:
            wf.write(line)

with open("test2.txt", 'w') as of:
    of.write("Test")
    of.write("Masoud")
    of.seek(0)
    of.write("R")

print("\n append")
with open("test2.txt", 'a') as of:
    of.write("Test2")

print("\n Write images file")
with open("signature.jpg", 'rb') as rf:
    with open("signature_copy.jpg", 'wb') as wf:
        for line in rf:
            wf.write(line)

print("\n Write images file chunk")
with open("signature.jpg", 'rb') as rf:
    with open("signature_copy_2.jpg", 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
