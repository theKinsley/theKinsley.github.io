---
title: "TRECVID2023"
date: 2023-02-20T15:48:13+08:00
draft: false
---

### Introduction

#### 医学视频问答 - 定位视频中出现答案的时间/医学指导性问题生成 (Medical Video Question Answering - Localize the visual answer / Medical instructional question generation) (https://medvidqa.github.io/index.html)
- 主要开发数据集：MedVidQA (https://arxiv.org/pdf/2201.12888.pdf) (https://github.com/deepaknlp/MedVidQACL)

##### Task1: Video Corpus Visual Answer Localization (VCVAL)
- IOP
	- I: 视频语料库、医学query
	- O: 解答目标query的视频+答案出现的时间段
	- P: 视频检索+时域分割预测
- 数据集
	- 训练
		- MedVidQA
			- \*人工标注
			- 构成：899条视频、3,010条问题（与健康相关的问题、视觉答案所在的时间戳），共95.71小时
			- 比例：800条训练、49条验证、50条测试
		- HealthVidQA
			- \*自动标注
			- 构成：约15,000条视频、50,000条问题
	- 验证：25条视频、50条问题
	- 测试：25条视频、50条问题
- 指标
	- 检索：\[1\]\[2\]
	- 时域预测：IoU

##### Task2: Medical Instructional Question Generation (MIQG)
- IOP
	- I: 视频分割片段、字幕
	- O: 视频片段所解答的问题
	- P: 文本生成
- 数据集
	- 训练：由MedVidQA中800条视频构造的2710个I-O对
	- 验证：由49条视频构造的145个I-O对
	- 测试：由45条视频构造的100个I-O对
- 指标
	- BLEU
	- Rouge
	- BertScore


### Prior works
- 湖南大学（主要做分类） (https://aclanthology.org/2022.bionlp-1.21.pdf) (https://github.com/Lireanstar/MedVidCL)
- 美国NIH https://aclanthology.org/2022.bionlp-1.25.pdf
- 维也纳工业大学 https://aclanthology.org/2022.bionlp-1.43.pdf

### Ref
[1] Sparck Jones. Report on the need for and provision of an" ideal" information retrieval test collection. 1975.
[2] Chris Buckley, Darrin Dimmick, Ian Soboroff, and Ellen Voorhees. Bias and the limits of pooling for large collections. Information retrieval, 10(6):491–508, 2007\\