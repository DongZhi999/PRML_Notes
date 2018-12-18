#!/usr/bin/env python 
# encoding: utf-8  
__author__ = "lizhiyi"

import pandas as pd
import numpy as np
from math import log
'''决策树类'''
class Decision(object):


    '''通过pandas读取数据文件'''
    def getData(self,path):
        dataSet = pd.read_csv(path)
        label = list(dataSet.columns)[:]
        dataSet = np.array(dataSet).tolist()
        return dataSet,label

    '''数据集处理了所有属性，但类标签仍不唯一，采用多数表决的方式来定义该节点的分类'''
    def majority(self,classlist):
        classcount=dict()
        for value in classlist:
            classcount[value] = len([item for item in classcount if item==value])
        result = sorted(classcount.values(), reverse=True).pop(0)
        return result

    '''计算数据集的信息熵'''
    def calcuEntropy(self, dataSet):
        lenDataSet = len(dataSet)
        #定义一个类别标签字典
        tag = dict()
        entropy = 0.0
        for data in dataSet:
            currentTag = data[-1]
            if currentTag not in tag.keys():
                tag[currentTag] = 1
            else:
                tag[currentTag] += 1
        #计算熵
        for key in tag:
            entropy +=-(float(tag[key])/float(lenDataSet)* \
                        log(float(tag[key])/float(lenDataSet), 2))
        return entropy

    '''进行数据集切分'''
    def splitData(self, dataSet, i, fea_value):
        subDataSet = []
        for data in dataSet:
            subData = []
            if data[i] == fea_value:
                #下面两行只是为了把第i个数据值从数据集中剔除
                subData = data[:i]
                subData.extend(data[i+1:])
                subDataSet.append(subData)
        return subDataSet

    '''选择分类最好的特征，也即熵最小，信息增益最高'''
    def chooseBestFeature(self,dataSet):
        #计算总共的属性列,去掉标签列即可
        lenFeature = len(dataSet[0])-1
        #计算原始数据信息熵
        EntropyInit = self.calcuEntropy(dataSet)
        bestGain = 0.0
        bestFeature = 0
        for i in range(lenFeature):
            EntropyFeature = 0.0
            #获取第i个特征的所有数据
            feature = [value[i] for value in dataSet]
            #获取第i个特征的所有类别值，相当于去重
            feature = set(feature)
            for fea in feature:
                #的数据集按照分类值分类
                subData = self.splitData(dataSet, i, fea)
                EntropyFeature += float(len(subData))/float(len(dataSet))* \
                                  self.calcuEntropy(subData)
            #计算信息增益
            Gain = EntropyInit - EntropyFeature
            if Gain > bestGain:
                bestGain = Gain
                bestFeature = i
        return  bestFeature

    '''创建分类决策树树'''
    def createTree(self,dataSet,label):
        #获取数据集类别标签
        classList = [value[-1] for value in dataSet]
        #若这两值相等，则classList中只有一类标签，直接返回即可
        if classList.count(classList[0]) == len(classList):
            return classList[0]
        #处理完所有特征标签类别仍不唯一
        if len(dataSet[0]) == 1:
            return self.majority(classList)
        #获取最佳分类特征,值为0,1,2，，，
        bestFrature = self.chooseBestFeature(dataSet)
        #使用该特征进行分类
        feature_value=[value[bestFrature] for value in dataSet]
        feature_value_only =set(feature_value)
        newlabel = label[bestFrature]
        #从标签字典中删除已经使用完的特征
        del self.labelDict[bestFrature]
        updateLabel = list()
        #将更新后的标签加入updateLabel
        for value in self.labelDict.values():
            updateLabel.append(value)

        #创建一个多重字典，存储决策树，格式类似与json
        Tree = {newlabel:{}}
        for value in feature_value_only:
            subLabel = updateLabel[:]
            Tree[newlabel][value] = self.createTree(self.splitData(dataSet, bestFrature, value), subLabel)
        return Tree

    '''对测试集进行预测'''
    def predict(self, tree_model, label, test):
        #获取树的第一个健
        firstFeature = list(tree_model.keys())[0]
        #获得第一个健的值，有可能是个标签，也有可能还是个字典
        secondDict = tree_model[firstFeature]
        #获得第一个特征在label中的索引
        labelIndex = label.index(firstFeature)
        #遍历第二个字典的键，存在俩中情况
        for key in secondDict.keys():
            #如果测试集的第labelIndex个特征与第二个字典的键相等时
            if test[labelIndex] == key:
                #判断一下是否为字典，若是，递归继续
                if type(secondDict[key]).__name__ == "dict":
                    testlabel = self.predict(secondDict[key], label, test)
                #若不是，将标签赋给testlabel，返回
                else:
                    testlabel = secondDict[key]
        return testlabel

    '''构造函数'''
    def __init__(self,path,test):
        self.dataSet, self.label = self.getData(path)
        self.labelDict = dict()
        for i,key in enumerate(self.label):
            self.labelDict[i] = key
        self.tree_model = self.createTree(self.dataSet, self.label)
        print("建立的树模型为：", end="")
        print(self.tree_model)
        tag = self.predict(self.tree_model, self.label, test)
        print("预测结果为: "+tag)

if __name__ == '__main__':
    path = "weather1.csv"
    test = ["晴天","温柔","高","强"]
    Decision(path,test)
