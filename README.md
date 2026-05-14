# Sum-and-Average-of-elements-in-a-list
# Sum and Average of Elements in a List Using Python

## Introduction
This Python program calculates the **sum** and **average** of elements entered by the user in a list.

The program:
- Takes input from the user
- Stores elements in a list
- Calculates the total sum
- Finds the average of all elements
- Displays the results

---

# Python Program

```python
print("SUM and AVERAGE of elements in a list\n")

lst = []
sum = 0

n = int(input("Enter number of elements: "))

for i in range(0, n):
    elements = float(input(f"Enter element {i+1}: "))
    lst.append(elements)

    sum += lst[i]

average = sum / n

print("Your list is", lst)
print("Sum of elements in", lst, "is", sum)
print("Average of elements in", lst, "is", average)
```

---

# Sample Output

```python
SUM and AVERAGE of elements in a list

Enter number of elements: 5
Enter element 1: 10
Enter element 2: 20
Enter element 3: 30
Enter element 4: 40
Enter element 5: 50

Your list is [10.0, 20.0, 30.0, 40.0, 50.0]
Sum of elements in [10.0, 20.0, 30.0, 40.0, 50.0] is 150.0
Average of elements in [10.0, 20.0, 30.0, 40.0, 50.0] is 30.0
```

---

# Explanation

## Step 1: Create an Empty List

```python
lst = []
```

- An empty list is created to store user inputs.

---

## Step 2: Initialize Sum Variable

```python
sum = 0
```

- Stores the total sum of elements.

---

## Step 3: Take Number of Elements

```python
n = int(input("Enter number of elements: "))
```

- User enters how many elements they want in the list.

---

## Step 4: Input Elements Using Loop

```python
for i in range(0, n):
```

- Loop runs `n` times to take inputs.

---

## Step 5: Store Elements in List

```python
lst.append(elements)
```

- Adds each entered element into the list.

---

## Step 6: Calculate Sum

```python
sum += lst[i]
```

- Adds each list element to the total sum.

---

## Step 7: Calculate Average

```python
average = sum / n
```

- Average is calculated using:

\[
\text{Average} = \frac{\text{Sum of Elements}}{\text{Number of Elements}}
\]

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Traversing list | O(n) |

Where `n` is the number of elements in the list.

---

# Concepts Used
- Lists
- Loops
- User Input
- Arithmetic Operations
- Traversing Lists

---

# Conclusion
This program demonstrates how to:
- Store data in a list
- Traverse list elements
- Calculate sum and average efficiently using loops in Python.
