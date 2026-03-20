import logic
import csv

with open("data.txt", "r") as file:
    content = file.read()


data_dict = logic.word_counter(content)

sorted_list = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

print(f"{'word':<15} | {'quantity':<10}")
print("-" * 30)
for word, count in sorted_list:
    print(f"{word.capitalize():<15} | {count:<10}")

with open("report.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["word", "quantity"])
    
    for word, count in sorted_list:
        writer.writerow([word, count])

print("\n✅ File 'report.csv' created and updated!")