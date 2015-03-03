def addPayment(a,b):
    return a-b
def addinput (a,b):
    return a+b
def updata_balance(num):
    str_balance=num
def showpay(num):
    print 'now the cont is %i' % num
if __name__=='__main__':
    str_balance=raw_input('Enter opening balance:')
    int_balance=int(str_balance)
    while True:
        print 'menue: \n' ' 1:add_pay | 2:add_input | 3 showpayment'
        str_meanme=raw_input('Please select meanume:')
        if str_meanme=='1':
            pay_count=raw_input('please enter pay count:')
            int_pay_count=int(pay_count)
            ss=addPayment(int_balance,int_pay_count)
            updata_balance(ss)
        elif str_meanme=='2':
            pay_count=raw_input('please enter pay count:')
            int_pay_count=int(pay_count)
            ss=addinput(int_balance,int_pay_count)
            updata_balance(ss)
        elif str_meanme=='3':
            showpay(int_balance)
        else:
                print 'you enter e eorr meanume,Please enter again!'
                continue
