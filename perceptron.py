d = int(input())
m = int(input())
n = int(input())
training_set = []
test_set = []

for training_example in range(0, m):
    example = input()
    example = example.split(', ')
    training_set.append(example)

for test_input in range(0, n):
    test = input()
    test = test.split(', ')
    test_set.append(test)

print(training_set)
print(test_set)