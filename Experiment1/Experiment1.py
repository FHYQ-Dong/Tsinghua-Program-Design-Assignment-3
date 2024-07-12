"""
* coding=utf-8
* python=3.11
* File: Experiment1.py
* Author: donghy23@mails.tsinghua.edu.cn
* Created: 2024-7-12
* Repo: https://github.com/FHYQ-Dong/Tsinghua-Program-Design-Assignment-3/blob/main/Experiment1/Experiment1.py
"""


import argparse
import json

def calMonthPayment(totalPrice: float, downPayment: float, interestRate_perYear: float, loanDuration: int) -> float:
    """计算每月还款额
    每年

    ### Args:
        totalPrice (float): 总价（单位：元）
        downPayment (float): 首付（单位：元）
        interestRate_perYear (float): 年利率（单位：%）
        loanDuration (int): 贷款期限（单位：月）
    
    ### Returns:
        float: 每月还款额（单位：元），保留两位小数（四舍五入）
    """
    loanAmount = totalPrice - downPayment
    interestRate_perMonth = interestRate_perYear / 12 / 100
    monthPayment = loanAmount * interestRate_perMonth * (1 + 1 / ((1 + interestRate_perMonth)**loanDuration - 1))
    return "%.2f" % monthPayment


def main():
    parser = argparse.ArgumentParser(description='Calculate monthly payment')
    parser.add_argument('-t', '--totalPrice', type=float, help='Total price (unit: RMB)')
    parser.add_argument('-p', '--downPayment', type=float, help='Down payment (unit: RMB)')
    parser.add_argument('-i', '--interestRate', type=float, help='Interest rate per year (unit: %%)')
    parser.add_argument('-d', '--loanDuration', type=int, help='Loan duration (unit: month)')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='Input file (JSON)')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), help='Output file (JSON)')
    parser.add_argument('-j', '--showTemplateJsonFormat', action='store_true', help='Show template JSON format of input file')
    
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(e)
        parser.print_help()
        exit(1)
        
    if args.showTemplateJsonFormat:
        templateInput = [
            {
                "name": "Name1",
                "totalPrice": 1000000,
                "downPayment": 200000,
                "interestRate": 5,
                "loanDuration": 240
            },
            {
                "name": "Name2",
                "totalPrice": 2000000,
                "downPayment": 400000,
                "interestRate": 4,
                "loanDuration": 120
            }
        ]
        print(json.dumps(templateInput, indent=4))
        return
    
    if args.file:
        data = json.load(args.file)
        output = []
        for item in data:
            item['monthlyPayment'] = calMonthPayment(
                item['totalPrice'],
                item['downPayment'],
                item['interestRate'],
                item['loanDuration']
            )
            output.append(item)
        if args.output:
            args.output.write(json.dumps(output, indent=4))
        else:
            for i, item in enumerate(output):
                print(('\n' + '-'*48 + '\n') * bool(i))
                print(f'Name: {item["name"]}')
                print(f'Total price: {item["totalPrice"]}')
                print(f'Down payment: {item["downPayment"]}')
                print(f'Interest rate: {item["interestRate"]}')
                print(f'Loan duration: {item["loanDuration"]}')
                print(f'Monthly payment: {item["monthlyPayment"]}')
    else:
        if args.totalPrice and args.downPayment and args.interestRate and args.loanDuration:
            monthPayment = calMonthPayment(args.totalPrice, args.downPayment, args.interestRate, args.loanDuration)
            print(f'Monthly payment: {monthPayment}')
        else:
            parser.print_help()
            

if __name__ == '__main__':
    main()