import random
import pyfpgrowth
def generate_random_transactions(num_transactions=10, num_items=5):
    items = ["Milk", "Bread", "Saffron", "Butter", "Wafer", "Cheese", "Eggs", "Juice", "Sugar", "Tea",]
    transactions = []
    for _ in range(num_transactions):
        transaction_length = random.randint(2, num_items) 
        transaction = random.sample(items, transaction_length)
        transactions.append(transaction)
    return transactions
transactions = generate_random_transactions(num_transactions=10, num_items=5)
print("Generated Transactions:")
for idx, transaction in enumerate(transactions, start=1):
    print(f"Transaction {idx}: {transaction}")
print("\n" + "-" * 50)
FrequentPatterns = pyfpgrowth.find_frequent_patterns(transactions, support_threshold=0.5)
print("Frequent Patterns (Support >= 0.5):")
for pattern, support in FrequentPatterns.items():
    print(f"Pattern: {pattern}, Support: {support}")
print("\n" + "-" * 50)
print("Generating rules with min confidence threshold=0.5")
Rules = pyfpgrowth.generate_association_rules(FrequentPatterns, confidence_threshold=0.5)
for rule, confidence in Rules.items():
    print(f"Rule: {rule}, Confidence: {confidence}")