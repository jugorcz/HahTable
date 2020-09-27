
class HashTable:
    def __init__(self, length=4):
        self.table = [None] * length

    def hash(self, key):
        length = len(self.table)
        return hash(key) % length

    def is_full(self):
        count = 0
        for el in self.table:
            if el is not None:
                count += 1
        return count > len(self.table) / 2

    def double(self):
        print("\n---NEW TABLE---")
        new_len = len(self.table) * 2
        new_hash_table = HashTable(new_len)
        for el in self.table:
            if el is None or el == ("", -1):
                continue
            new_hash_table.add(el[0], el[1])
        print("------END------\n")

        self.table = new_hash_table.table

    def add(self, key, value):
        if value == -1:
            print("Value -1 is reserved for deleted items")
            return
        index = self.hash(key)
        print("for {} index: {}".format(key, index))
        if self.table[index] is None or self.table[index] == ("", -1):
            self.table[index] = (key, value)
        else:
            found = False
            i = index - 1
            while not found and i != index:
                if i < 0:
                    i = len(self.table) - 1
                if self.table[i] is None or self.table[i] == ("", -1):
                    self.table[i] = (key, value)
                    found = True
                else:
                    i -= 1
        self.display()
        if self.is_full():
            self.double()

    def get(self, key):
        index = self.hash(key)
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1]
        else:
            i = index - 1
            for k in range(len(self.table)):
                if i < 0:
                    i = len(self.table) - 1
                if self.table[i] is not None and self.table[i][0] == key:
                    return self.table[i][1]
                else:
                    i -= 1
        raise KeyError()

    def delete(self, key):
        index = self.hash(key)
        if self.table[index] is not None and self.table[index][0] == key:
            self.table[index] = ("", -1)
        else:
            i = index - 1
            for k in range(len(self.table)):
                if i < 0:
                    i = len(self.table) - 1
                if self.table[i] is not None and self.table[i][0] == key:
                    self.table[i] = ("", -1)
                else:
                    i -= 1
        self.display()

    def display(self):
        index = 0
        for el in self.table:
            if el is not None:
                print("{}:{} -> ".format(index, el), end="")
            index += 1
        print("None")


def main():
    ht = HashTable(4)
    ht.add("abc", 88)
    ht.add("abb", 35)
    ht.add("abd", 34)
    ht.add("abe", 30)
    ht.delete("abc")
    ht.add("aba", 99)


if __name__ == '__main__':
    main()
