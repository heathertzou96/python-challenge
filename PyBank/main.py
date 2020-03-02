import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)

    csvheader = next(csvreader)
    print(f" CSV Header: {csvheader}")

    total_month = 0
    net_total = 0
    profit_loss_list = []

    for row in csvreader:      
        
        total_month += 1
       
        net_total = int(row[1]) + int(net_total)
    
        profit_loss_list.append((row[0], int(row[1])))
            
    diff_sum = 0
    average_change = 0
    max_inc_val = 0
    max_inc_date = None
    max_dec_val = 0
    max_dec_date = None

    for i in range(1, len(profit_loss_list)):
        diff = profit_loss_list[i][1] - profit_loss_list[i - 1][1]
        if diff > max_inc_val:
            max_inc_val = diff
            max_inc_date = profit_loss_list[i][0]
        if diff < max_dec_val:
            max_dec_val = diff
            max_dec_date = profit_loss_list[i][0]
        diff_sum += diff
        average_change = round((diff_sum / (len(profit_loss_list) - 1)), 2)
    
    

    print("Financial Analysis \n---------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_inc_date} (${max_inc_val})")
    print(f"Greatest Decrease in Profits: {max_dec_date} (${max_dec_val})")
    
    textfile = open("results.txt", "w")
    textfile.write("Financial Analysis \n---------------------------\n")
    textfile.write(f"Total Months: {total_month} \n")
    textfile.write(f"Total: ${net_total} \n")
    textfile.write(f"Average Change: ${average_change} \n")
    textfile.write(f"Greatest Increase in Profits: {max_inc_date} (${max_inc_val}) \n")
    textfile.write(f"Greatest Decrease in Profits: {max_dec_date} (${max_dec_val}) \n")
    textfile.close()
    
    


    

        

