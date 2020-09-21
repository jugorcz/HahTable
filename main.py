
class HashTable:
    def __init__(self, length=4):
        self.array = [list()] * length

    # hash_table["abc"] = 9
    def __setitem__(self, key, value):
        self.add(key, value)

    # value = hash_table["abc"]
    def __getitem__(self, key):
        return self.get(key)

    # if "abc" in table
    def __contains__(self, key):
        try:
            self.get(key)
        except KeyError:
            return False
        return True

    # for el in hash_table:
    def __iter__(self):
        for node in self.array:
            for el in node:
                yield el

    def is_full(self):
        count = 0
        for el in self.array:
            if len(el) != 0:
                count += 1
        return count > len(self.array) / 2

    def double(self):
        new_hash_table = HashTable(len(self.array) * 2)
        for i in range(len(self.array)):
            if not self.array[i]:
                continue
            for key_value_pair in self.array[i]:
                new_hash_table.add(key_value_pair[0], key_value_pair[1])
        self.array = new_hash_table.array

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index]:
            found = False
            for key_value_pair in self.array[index]:
                if key_value_pair[0] == key:
                    key_value_pair[1] = value
                    found = True
                    break

            if not found:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])

        if self.is_full():
            self.double()

    def get(self, key):
        index = self.hash(key)
        if not self.array[index]:
            raise KeyError()
        else:
            for key_value_pair in self.array[index]:
                if key_value_pair[0] == key:
                    return key_value_pair[1]
            raise KeyError()

    def display(self):
        index = 0
        for node in self.array:
            print(" [{}] -> ".format(index), end="")
            for pair in node:
                print("{} -> ".format(pair), end="")
            index += 1
            print("None")


def main():
    hash_table = HashTable(2)
    hash_table.add("abc", 99)
    hash_table.add("abd", 98)
    hash_table.add("abd", 66)
    hash_table.add("a", 66)
    hash_table.add("b", 66)
    hash_table.add("c", 66)
    hash_table.add("d", 66)
    hash_table.add("f", 66)
    hash_table.add("g", 66)
    hash_table.add("h", 66)
    hash_table.display()

    k = "i" in hash_table
    if k:
        print("Jest!")
        print(hash_table["i"])
    else:
        print("nie ma")

    for el in hash_table:
        print(el)


if __name__ == '__main__':
    main()
