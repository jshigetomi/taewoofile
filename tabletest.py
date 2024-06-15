data = [('Name', 'Age', 'Country'),
        ('John', 25, 'USA'),
        ('Maria', 28, 'Spain'),
        ('Tom', 30, 'Canada')]

# Determine the max width for each column
col_widths = [max(len(str(word)) + 10 for word in col) for col in zip(*data)]

# Create a row format based on column widths
row_format = '|'.join("{:<" + str(width) + "}" for width in col_widths)

# Print each row using the row format
for row in data:
    print(row_format.format(*row), end="\n\n")