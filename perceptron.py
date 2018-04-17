import random

learning_rate = 0.05
d = int(input())
m = int(input())
n = int(input())
training_set = []
test_set = []

for training_example in range(0, m):
    example = input()
    example = example.replace(' ', '')
    example = example.split(',')
    example = [float(i) for i in example]
    training_set.append(example)

for test_input in range(0, n):
    test = input()
    test = test.replace(' ', '')
    test = test.split(',')
    test = [float(i) for i in test]
    test_set.append(test)

# Initialize all the weights
# Weight for bias is the last one
weights = []
for element in range(0, d):
    weights.append(random.random())
weights.append(random.random())

errors = 100
iteration = 0
while errors != 0 and iteration < 1000:
    # print('Iteration {}: '.format(iteration))
    errors = 0
    for example in training_set:
        d = example[-1]
        example = example[:-1]
        example.append(1) # Appending the bias

        calculated_d = 0.0
        for element in range(0, len(example)):
            calculated_d += float(example[element]) * weights[element]

        if calculated_d >= 0:
            calculated_d = 1
        else:
            calculated_d = 0

        if d != calculated_d:
            errors += 1

        for element in range(0, len(weights)):
            weights[element] += learning_rate * (d - calculated_d) * example[element]

    iteration += 1

if iteration < 1000:
    for test in test_set:
            test.append(1) # Appending the bias

            calculated_d = 0.0
            for element in range(0, len(test)):
                calculated_d += float(test[element]) * weights[element]

            if calculated_d >= 0:
                calculated_d = 1
            else:
                calculated_d = 0

            print(calculated_d)
else:
    print('no solution found')


