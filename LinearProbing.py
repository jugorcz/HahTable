
class HashTable:
    def __init__(self, length=4):
        self.table = [None] * length
        self.size = length
        self.prime = self.find_prime()

    def find_prime(self):
        val = self.size - 1
        while val >= 2:
            found_prime = True
            for i in range(2, val):
                if val % i == 0:
                    found_prime = False
                    break
            if found_prime:
                print("New prime: {} for size: {}".format(val, self.size))
                return val
            else:
                val -= 1
        return -1

    def hash2(self, key):
        return self.prime - (hash(key) % self.prime)

    def hash1(self, key):
        return hash(key) % self.size

    def is_full(self):
        count = 0
        for el in self.table:
            if el is not None:
                count += 1
        return count > self.size / 2

    def double(self):
        print("\n---NEW TABLE---")
        new_len = self.size * 2
        new_hash_table = HashTable(new_len)
        for el in self.table:
            if el is None or el == ("", -1):
                continue
            new_hash_table.add(el[0], el[1])

        self.table = new_hash_table.table
        self.size = new_hash_table.size
        self.prime = new_hash_table.prime
        print("------END------\n")

    def is_available(self, index):
        if self.table[index] is None or self.table[index] == ("", -1):
            return True
        return False

    def add(self, key, value):
        if value == -1:
            print("Value -1 is reserved for deleted items")
            return
        index1 = self.hash1(key)
        print("for {} index: {}, secondary: {}".format(key, index1, self.hash2(key)))
        if self.is_available(index1):
            self.table[index1] = (key, value)
        else:
            index2 = self.hash2(key)
            attempt = 1
            while True:
                new_index = (index1 + attempt * index2) % self.size
                print("Attempt: {}, new index: {}".format(attempt, new_index))
                if self.is_available(new_index):
                    self.table[new_index] = (key, value)
                    break
                attempt += 1

        self.display()
        if self.is_full():
            self.double()

    def get_index(self, key):
        index1 = self.hash1(key)
        index2 = self.hash2(key)
        attempt = 0
        while True:
            index = (index1 + attempt * index2) % self.size
            if self.table[index] is not None and self.table[index][0] == key:
                return index
            attempt += 1
            if attempt > self.size:
                raise KeyError()

    def get(self, key):
        index = self.get_index(key)
        return self.table[index][1]

    def delete(self, key):
        print("--DELETE {}-- ".format(key), end="")
        index = self.get_index(key)
        self.table[index] = ("", -1)
        self.display()

    def display(self):
        index = 0
        for el in self.table:
            if el is not None:
                print("{}:{} -> ".format(index, el), end="")
            else:
                print("{} -> ".format(index), end="")
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
    ht.add("cba", 99)


if __name__ == '__main__':
    main()
