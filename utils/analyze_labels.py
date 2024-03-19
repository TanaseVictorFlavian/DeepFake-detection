import csv

csvs = ["./data/train_labels.csv", "./data/test_labels.csv"]
column_index = 1


# Reading the CSV file
for p in csvs:
    count_0 = 0
    count_1 = 0
    with open(p, newline='') as file:
        reader = csv.reader(file)
        next(reader)  

        # Iterate through each row in the CSV
        for row in reader:
            if row[column_index] == '0':
                count_0 += 1
            elif row[column_index] == '1':
                count_1 += 1

    # Print the counts
    print(f"Count of 0s: {count_0}")
    print(f"Count of 1s: {count_1}")
