---
title: "TRECVID2023"
date: 2023-02-20T15:48:13+08:00
draft: false
---

### Introduction

#### 医学视频问答 - 定位视频中出现答案的时间/医学指导性问题生成 (Medical Video Question Answering - Localize the visual answer / Medical instructional question generation) (https://medvidqa.github.io/index.html)

##### Task1: Video Corpus Visual Answer Localization (VCVAL)
- IOP
	- I: 视频语料库、医学query
	- O: 解答目标query的视频+答案出现的时间段
	- P: 视频检索+时域分割预测
- 数据集
	- 训练
		- MedVidQA (https://arxiv.org/pdf/2201.12888.pdf) (https://github.com/deepaknlp/MedVidQACL)
			- \*人工标注
			- 构成：899条视频、3,010条问题（与健康相关的问题、视觉答案所在的时间戳），共95.71小时
			- 比例：800条训练、49条验证、50条测试
		- HealthVidQA
			- \*自动标注
			- 构成：约15,000条视频、50,000条问题
	- 测试

##### Task2: Medical Instructional Question Generation (MIQG)
- IOP
	- I: 视频分割片段、字幕
	- O: 视频片段所解答的问题
	- P: 文本生成

- 指标
	- BLEU
	- Rouge
	- BertScore


### Prior works
- 湖南大学

- Topic novelty
- 

### 