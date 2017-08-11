# coding=utf-8
import random
import time
'''
I make the program to help children study

Author: hatcher fang
'''


class arithmeticOperations(object):
    def add(self):
        print '欢迎来到加法练习，请先设定加法范围，例如10以内加法请输入：10'
        scope = raw_input()
        while not scope.isdigit():
            print "请输入数字作为运算范围"
            scope = raw_input()
        scope = int(scope)
        beginTime = time.time()
        rightCount = 0
        wrongCount = 0
        total = 0
        while 1:
            a = random.randint(0, scope)
            b = random.randint(0, scope)
            print str(a) + '+' + str(b) + '=' + '?'
            c = raw_input()
            if c == 'tc':
                accuracy = rightCount*100/float(total) if total else 0
                print '目前为止您的得分是：',
                print '您共答对 %d 道题, 答错 %d 道题，正确率：%r%% \n总共用时：%r秒 \n%s, 下次再见哦！'\
                % (rightCount, wrongCount, accuracy, time.time()-beginTime, \
                   '太棒了！' if accuracy >= 80 else '不错哦！' if accuracy >= 60 else '多多练习，你一定可以的！')

                return
            if c == 'ck':
                accuracy = rightCount*100/float(total) if total else 0
                print '目前为止，您共答对 %d 道题, 答错 %d 道题，正确率：%r%% \n总共用时：%r秒 \n%s, 继续加油哦！'\
                % (rightCount, wrongCount, accuracy, time.time()-beginTime, '太棒了！' if accuracy >= 80 else '不错哦！' if accuracy >= 60 else '多多练习，你一定可以的！')
                continue
            if c == 'gh':
                print '请输入新的运算范围：'
                scope = raw_input()
                while not scope.isdigit():
                    print "请输入数字更换运算范围"
                    scope = raw_input()
                scope = int(scope)
                continue
            if not c.isdigit():
                print '继续答题请输入数字, 退出请输入：tc, 查看成绩请输入：ck, 更换运算范围请输入：gh'
                continue
            c = int(c)
            while a + b != c:
                print '很可惜，您答错了，请重新输入:'
                print str(a) + '+' + str(b) + '=' + '?'
                c = raw_input()
                while not c.isdigit():
                    print '请输入数字类型或输入tc跳过本题'
                    c = raw_input()
                    if c == 'tc':
                        break
                if c == 'tc':
                    break
                c = int(c)
                wrongCount = wrongCount + 1
                total = total + 1
            if c == 'tc':
                continue
            rightCount = rightCount + 1
            total = total + 1
            print '答对了，您真聪明!'
            if total % 10 == 0:
                accuracy = rightCount*100/float(total) if total else 0
                print '目前为止，您共答对 %d 道题, 答错 %d 道题，正确率：%r%% \n总共用时：%r秒 \n%s, 继续加油！'\
                    % (rightCount, wrongCount, accuracy, time.time()-beginTime,
                       '太棒了！' if accuracy >= 80 else '不错哦！' if accuracy >= 60 else '多多练习，你一定可以的！')

    def switch_func(self, num):
        switch_dict = {
            '1': self.add,
            '2': '正在开发,请耐心等待。。。',
            '3': '正在开发,请耐心等待。。。',
            '4': '正在开发,请耐心等待。。。'
        }
        func = switch_dict.get(num)
        while not func:
            print "请输入正确参数：1，2，3，4"
            num = raw_input()
            func = switch_dict.get(num)
        if callable(func):
            func()
        else:
            print func

if __name__ == '__main__':
    print '请输入您想做的算数练习:'
    print '加法请按：1'
    print '减法请按：2'
    print '乘法请按：3'
    print '除法请按：4'
    num = raw_input()
    ca = arithmeticOperations()
    ca.switch_func(num)
