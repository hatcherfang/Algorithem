# coding=utf-8
import random
import time
'''
I make the program to help children study arithmetic operations

Author: hatcher fang
'''


class arithmeticOperations(object):

    def __init__(self):
        self.rightCount = 0
        self.wrongCount = 0
        self.total = 0
        self.beginTime = time.time()

    def arithmetic_result(self):
        accuracy = self.rightCount*100/float(self.total) if self.total else 0
        print '总共 {} 道题, 您共答对 {} 道题, 答错 {} 道题 \n正确率：{}% \n总共用时：{}秒 \n{} '\
        .format(self.total, self.rightCount, self.wrongCount, accuracy,
                time.time()-self.beginTime, '太棒了！' if accuracy >= 80
                else '不错哦！' if accuracy >= 60 else
                '多多练习，你一定可以的！\n')

    def addition(self):
        print '请先设定加法运算范围哦！ \n例如10以内加法请输入：10'
        scope = raw_input()
        while not scope.isdigit():
            print "请输入数字作为运算范围哦！"
            scope = raw_input()
        scope = int(scope)
        print '\n欢迎进入 %d 以内加法！' % scope
        print '退出该运算请输入: tc'
        print '查看当前成绩请输入：ck'
        while 1:
            a = random.randint(0, scope)
            b = random.randint(0, scope)
            print str(a) + '+' + str(b) + '=' + '?'
            c = raw_input()
            if c == 'tc':
                print '\n目前为止您的得分是：',
                self.arithmetic_result()
                print '下次再见哦！\n'
                return
            if c == 'ck':
                print '\n目前为止,',
                self.arithmetic_result()
                print '继续加油哦！\n'
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
                self.wrongCount = self.wrongCount + 1
                self.total = self.total + 1
                if self.wrongCount > self.rightCount and self.total % 10 == 0:
                    print '\n目前为止，',
                    self.arithmetic_result()
            if c == 'tc':
                continue
            self.rightCount = self.rightCount + 1
            self.total = self.total + 1
            print '答对了，您真聪明！\n'
            if self.total % 100 == 0:
                print '您已经答了上百道题,劳逸结合对学习事半功倍哦！\n'
                continue
            if self.total % 10 == 0:
                print '\n目前为止，',
                self.arithmetic_result()
                print '继续加油！\n'

    def substration(self):
        print '请先设定减法运算范围哦！ \n例如10以内减法请输入：10'
        scope = raw_input()
        while not scope.isdigit():
            print "请输入数字作为运算范围哦！"
            scope = raw_input()
        scope = int(scope)
        print '\n欢迎进入 %d 以内减法！' % scope
        print '退出该运算请输入: tc'
        print '查看当前成绩请输入：ck'
        while 1:
            a = random.randint(0, scope)
            b = random.randint(0, scope)
            while a < b:
                a = random.randint(0, scope)
                b = random.randint(0, scope)
            print str(a) + '-' + str(b) + '=' + '?'
            c = raw_input()
            if c == 'tc':
                print '\n目前为止您的得分是：',
                self.arithmetic_result()
                print '下次再见哦！\n'
                return
            if c == 'ck':
                print '\n目前为止,',
                self.arithmetic_result()
                print '继续加油哦！\n'
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
            while a - b != c:
                print '很可惜，您答错了，请重新输入:'
                print str(a) + '-' + str(b) + '=' + '?'
                c = raw_input()
                while not c.isdigit():
                    print '请输入数字类型或输入tc跳过本题'
                    c = raw_input()
                    if c == 'tc':
                        break
                if c == 'tc':
                    break
                c = int(c)
                self.wrongCount = self.wrongCount + 1
                self.total = self.total + 1
                if self.wrongCount > self.rightCount and self.total % 10 == 0:
                    print '\n目前为止，',
                    self.arithmetic_result()
            if c == 'tc':
                continue
            self.rightCount = self.rightCount + 1
            self.total = self.total + 1
            print '答对了，您真聪明！\n'
            if self.total % 100 == 0:
                print '您已经答了上百道题,劳逸结合对学习事半功倍哦！\n'
                continue
            if self.total % 10 == 0:
                print '\n目前为止，',
                self.arithmetic_result()
                print '继续加油！\n'

    def multiplication(self):
        print '请先设定乘法运算范围哦！ \n例如10以内乘法请输入：10'
        scope = raw_input()
        while not scope.isdigit():
            print "请输入数字作为运算范围哦！"
            scope = raw_input()
        scope = int(scope)
        print '\n欢迎进入 %d 以内乘法！' % scope
        print '退出该运算请输入: tc'
        print '查看当前成绩请输入：ck'
        while 1:
            a = random.randint(0, scope)
            b = random.randint(0, scope)
            print str(a) + 'x' + str(b) + '=' + '?'
            c = raw_input()
            if c == 'tc':
                print '\n目前为止您的得分是：',
                self.arithmetic_result()
                print '下次再见哦！\n'
                return
            if c == 'ck':
                print '\n目前为止,',
                self.arithmetic_result()
                print '继续加油哦！\n'
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
            while a * b != c:
                print '很可惜，您答错了，请重新输入:'
                print str(a) + 'x' + str(b) + '=' + '?'
                c = raw_input()
                while not c.isdigit():
                    print '请输入数字类型或输入tc跳过本题'
                    c = raw_input()
                    if c == 'tc':
                        break
                if c == 'tc':
                    break
                c = int(c)
                self.wrongCount = self.wrongCount + 1
                self.total = self.total + 1
                if self.wrongCount > self.rightCount and self.total % 10 == 0:
                    print '\n目前为止，',
                    self.arithmetic_result()
            if c == 'tc':
                continue
            self.rightCount = self.rightCount + 1
            self.total = self.total + 1
            print '答对了，您真聪明！\n'
            if self.total % 100 == 0:
                print '您已经答了上百道题,劳逸结合对学习事半功倍哦！\n'
                continue
            if self.total % 10 == 0:
                print '\n目前为止，',
                self.arithmetic_result()
                print '继续加油！\n'

    def division(self):
        print '欢迎来到除法运算！ \n请先设定除法运算范围哦！ \n例如10以内除法请输入：10'
        scope = raw_input()
        while not scope.isdigit():
            print "请输入数字作为运算范围哦！"
            scope = raw_input()
        scope = int(scope)
        print '\n欢迎进入 %d 以内除法！' % scope
        print '退出该运算请输入: tc'
        print '查看当前成绩请输入：ck'
        while 1:
            zc = random.randint(0, scope)
            b = random.randint(0, scope)
            while not b:
                b = random.randint(0, scope)
            a = zc*b
            print str(a) + '÷' + str(b) + '=' + '?'
            c = raw_input()
            if c == 'tc':
                print '\n目前为止您的得分是：',
                self.arithmetic_result()
                print '下次再见哦！\n'
                return
            if c == 'ck':
                print '\n目前为止,',
                self.arithmetic_result()
                print '继续加油哦！\n'
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
            while a / b != c:
                print '很可惜，您答错了，请重新输入:'
                print str(a) + '÷' + str(b) + '=' + '?'
                c = raw_input()
                while not c.isdigit():
                    print '请输入数字类型或输入tc跳过本题'
                    c = raw_input()
                    if c == 'tc':
                        break
                if c == 'tc':
                    break
                c = int(c)
                self.wrongCount = self.wrongCount + 1
                self.total = self.total + 1
                if self.wrongCount > self.rightCount and self.total % 10 == 0:
                    print '\n目前为止，',
                    self.arithmetic_result()
            if c == 'tc':
                continue
            self.rightCount = self.rightCount + 1
            self.total = self.total + 1
            print '答对了，您真聪明！\n'
            if self.total % 100 == 0:
                print '您已经答了上百道题,劳逸结合对学习事半功倍哦！\n'
                continue
            if self.total % 10 == 0:
                print '\n目前为止，',
                self.arithmetic_result()
                print '继续加油！\n'

    def switch_func(self):
        while 1:
            print '***********************'
            print '请输入您想做的算数练习:'
            print '加法请按：1'
            print '减法请按：2'
            print '乘法请按：3'
            print '除法请按：4'
            print '退出算术运算请输入: tc'
            print '查看成绩请输入：ck'
            print '***********************'
            print '请选择：',
            num = raw_input()
            if num == 'tc':
                print '欢迎再来哦！拜拜！'
                return
            if num == 'ck':
                print '\n目前为止,',
                self.arithmetic_result()
                print '继续加油哦！\n'
            switch_dict = {
                '1': self.addition,
                '2': self.substration,
                '3': self.multiplication,
                '4': self.division
            }
            func = switch_dict.get(num)
            if not func:
                continue
            if callable(func):
                func()
            else:
                print func

if __name__ == '__main__':
    ca = arithmeticOperations()
    ca.switch_func()
