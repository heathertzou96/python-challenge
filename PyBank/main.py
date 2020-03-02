import os
import csv

#storing file path associated with budget_data csv file
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')


with open(csvpath) as csvfile:

    #csv reader specifies delimiter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)

    #reading the header row first and printing the header
    csvheader = next(csvreader)
    print(f" CSV Header: {csvheader}")

    
    #The total # of months included in the dataset
    #The net total of "Profit/Losses" over the entire period
    total_month = 0
    net_total = 0
    
    # profit_loss_list = []

    # for row in csvreader:      
    #     total_month += 1
    #     net_total = int(row[1]) + int(net_total)
    
    #     profit_loss_list.append(int(row[1]))
    #         # for i, k in enumerate(profit_loss_list):
    #         #     i+1

    # diff_sum = 0
    # for i in range(1, len(profit_loss_list)):
    #     print(profit_loss_list[i], profit_loss_list[i - 1])
    #     diff_sum += profit_loss_list[i] - profit_loss_list[i - 1]
    
    # print(diff_sum / len(profit_loss_list) - 1)
    
    # greatest_increase = 0 


    profit_loss_list = []

    for row in csvreader:      
        total_month += 1
        net_total = int(row[1]) + int(net_total)
    
        profit_loss_list.append((row[0], int(row[1])))
            

    diff_sum = 0
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
    
    
    print(diff_sum / (len(profit_loss_list) - 1))
    print(max_inc_date, max_inc_val)
    print(max_dec_date, max_dec_val)
    
    print("--------")

    print(total_month)
    print(net_total)
    print(profit_loss_list)

    

        

