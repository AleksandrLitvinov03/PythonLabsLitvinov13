import re

def clean_data(data):
    if isinstance(data, str):
        data = data.split(',')
    cleaned = [item.strip().lower() for item in data]
    print("Task 1:", cleaned)
    return cleaned

def filter_emails(emails_string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    valid_emails = re.findall(pattern, emails_string)
    valid_emails_list = [email for email in valid_emails if email.count('@') == 1]
    print("Task 2:", valid_emails_list)
    return valid_emails_list

def extract_keywords(words, length):
    filtered_words = [word for word in words.split() if len(word) > length]
    print("Task 3:", filtered_words)
    return filtered_words

def process_text(text):
    processed = [item.strip().lower().strip('.?!') for item in text.split(',')]
    processed = [item for item in processed if item]
    print("Task 4:", processed)
    return processed

def normalize_data(numbers):
    numbers_list = [float(num) for num in numbers.split(',')]
    max_value = max(numbers_list)
    normalized = [round(num / max_value, 3) for num in numbers_list]
    print("Task 5:", normalized)
    return normalized

def concatenate_strings(data, separator):
    concatenated = ''.join(data.split(separator))
    print("Task 6:", concatenated)
    return concatenated

def sum_numeric_strings(numbers):
    total_sum = sum(map(int, re.findall(r'\d+', numbers)))
    print("Task 7:", total_sum)
    return total_sum

def filter_numbers(input_string, threshold):
    numbers_list = [int(num) for num in re.findall(r'\d+', input_string)]
    filtered_numbers = [num for num in numbers_list if num > threshold]
    print("Task 8:", filtered_numbers)
    return filtered_numbers

def map_to_squares(numbers):
    squared_numbers = [int(num) ** 2 for num in numbers.split(',')]
    print("Task 9:", squared_numbers)
    return squared_numbers

def reverse_strings(words):
    reversed_words = [word[::-1] for word in words.split(',')]
    print("Task 10:", reversed_words)
    return reversed_words

# Test the functions
data = " Apple,  Banana , orange "
cleaned_data = clean_data(data)

emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)

texts = "Hello! , Yes? , No. , "
processed_texts = process_text(texts)

numbers = "10, 20, 30, 40, 50"
normalized_numbers = normalize_data(numbers)

data_to_concatenate = "Hello, World!, How, are, you?"
separator = ","
concatenated_data = concatenate_strings(data_to_concatenate, separator)

numeric_strings = "10, 20, abc, 30, def, 40"
sum_of_numeric_strings = sum_numeric_strings(numeric_strings)

numbers_to_filter = "10, 20, abc, 30, def, 40"
threshold = 25
filtered_numbers = filter_numbers(numbers_to_filter, threshold)

numbers_to_square = "1, 2, 3, 4, 5"
squared_numbers = map_to_squares(numbers_to_square)

strings_to_reverse = "apple, banana, orange, PEAR, kiwi"
reversed_strings = reverse_strings(strings_to_reverse)
