# Sample code to do FP-Growth in Python
import pyfpgrowth
# Creating Sample Transactions
transactions = [
     ['Milk', 'Bread', 'Saffron'],
     ['Milk', 'Saffron'],
     ['Bread', 'Saffron','Wafer'],
     ['Bread','Wafer'],
 ]
 
#Finding the frequent patterns with min support threshold=0.5
FrequentPatterns=pyfpgrowth.find_frequent_patterns(transactions=transactions,support_threshold=0.5)
print(FrequentPatterns)

# Generating rules with min confidence threshold=0.5
print("Generating rules with min confidence threshold=0.5")
Rules=pyfpgrowth.generate_association_rules(patterns=FrequentPatterns,confidence_threshold=0.5)
print(Rules)
