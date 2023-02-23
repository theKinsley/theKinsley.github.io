---
title: "Trecvid2023 All"
date: 2023-02-22T09:29:21+08:00
draft: false
---


(1) 有几年历史？（2）近3年的参赛队伍有多少支，有哪些队伍；（3）仅3年的排名前3的队伍；（4）与我们的相关度。我看你列了2个任务都跟医学相关？

## Ad-hoc Video Search (AVS)
- 本届任务 https://www-nlpir.nist.gov/projects/tv2023/avs.html
	1. Main：使用20个固定ad-hoc qeury（文本）和2023年新加的20个ad-hoc query（文本）检索视频片段
	2. Progress：使用本次周期内的20个ad-hoc qeury检索视频（今年评估2022年、2023年个10个固定query）
- History：首届TRECVID竞赛为2016年，从2022年开始额外使用新的V3C2子集作为测试集（三年更新，本次周期：2022-2024）
	- 2022：7队参加
	![Image1](https://images2.imgbox.com/37/1b/Jncvr4Xz_o.png)![Image2](https://images2.imgbox.com/ae/10/8zqFdVSi_o.png)
		- 排名：早稻田大学&明星大学&软银；人民大学（李锡荣）；希腊科技研究中心（CERTH）
	- 2021：8队参加
	![Image1](https://images2.imgbox.com/54/89/I3YNynjw_o.png)![Image2](https://images2.imgbox.com/c7/46/eS9sLTiG_o.png)
		- 排名：香港城市大学；快手；人民大学（李锡荣）
	- 2020：9队参加
	![Image1](https://images2.imgbox.com/41/c5/HqG6O6hh_o.png)![Image2](https://images2.imgbox.com/b8/50/8dMCbFYK_o.png)
		- 排名：人民大学（金琴）；人民大学（李锡荣）；香港城市大学
	- 基本固定参与：人民大学
- 与实验室关联：跨媒体检索

## Activities in Extended Video (ActEv)
- 本届任务 https://www-nlpir.nist.gov/projects/tv2023/actev.html https://actev.nist.gov/SRL
	- 给定描述物体活动的qeury（文本，主体多为人、车），检测并定位视频中相符的（时&空）目标
- History：首届TRECVID竞赛为2019年
	- 2022：6队参加
	![Image](https://images2.imgbox.com/9a/b7/OBlL5ufD_o.png)
		- 排名：北京邮电大学；马里兰大学；杭州电子科技大学
	- 2021：6队参加
	![Image](https://images2.imgbox.com/3f/c5/onbHFjdd_o.png)
		- 排名：北京邮电大学；中央佛罗里达大学；卡内基梅隆大学
	- 2020：7队参加
	![Image](https://images2.imgbox.com/fa/14/B4NemEDO_o.png)
		- 排名：卡内基梅隆大学；北京邮电大学；中央佛罗里达大学
	- 基本固定参与：北京邮电大学
- 与实验室关联：跨媒体检索

## Deep Video Understanding (DVU)
- 本届任务（同时建议参与ACM MM Grand Challenge）https://www-nlpir.nist.gov/projects/tv2023/dvu.html
	- 给定（a）1.5至2小时的电影原片、（b）主要实体（人物、位置和概念）的图像、（c）全片级以及（d）场景级的实体之间的ontology（关系、交互、位置和情感），生成主要角色以及他们的（1）全片级关系知识库、（2）场景级互动知识库，以支持以下查询：
	1. Movie-level track（全片级）
		- Query 1, Question Answering (QA)：给定不局限于ontology的open domain选择题（多选题），基于结果知识库回答
		- Query 2, Fill in the Graph Space：给定特定节点的关系、事件或动作以及未完成（节点被未知变量替换的）的知识图谱，完成该知识图谱
	2. Scene-level track（场景级）
		- Query 1 & 2, Find Next or Previous Interaction：给定一个特定场景、两个主体之间的一个特定交互，选出他们的前一个或后一个交互（多选题）
		- Query 3, Find the Unique Scene：给定原片中一个特定场景的交互列表，定位出该场景
		- Query 4, Match Scene to Text Description：给定数个文本描述和数个场景，匹配相符的描述与场景
		- Query 5, Scene Sentiment Classification：给定一个特定的场景和一组可能的情绪，找出场景的正确情绪标签（分类）
- History：首届TRECVID竞赛为2022年，2020年起为ACM MM Grand Challenge
	- 2022（TRECVID)：3队参加
	![Image](https://images2.imgbox.com/75/8a/JeteT31S_o.png)
		1. Movie-level track：哥伦比亚大学；武汉大学
		2. Scene-level track：都柏林城市大学；哥伦比亚大学；武汉大学
	- 2022（ACM MM）：6队参加
	![Image](https://images2.imgbox.com/8c/97/oYoNghWq_o.png)
		1. Movie-level track：南京大学；HERO TVQA（HERO是微软发表于EMNLP 2020的VLP模型）；苏黎世大学
		2. Scene-level track：图策科技；南京大学
	- 2021（ACM MM）：2队参加
		- 排名：哥伦比亚大学；南京大学
	- 2020（ACM MM)：3队参加
		- 排名：南京大学 https://dl.acm.org/doi/10.1145/3394171.3416303；苏黎世大学 https://dl.acm.org/doi/10.1145/3394171.3416292；哥伦比亚大学 https://dl.acm.org/doi/pdf/10.1145/3394171.3416305
	- 基本固定参与：哥伦比亚大学、南京大学
- 与实验室关联：跨媒体知识图谱

## Video to Text (VTT)
- 本届任务 https://www-nlpir.nist.gov/projects/tv2023/vtt.html
	1. Description Generation (Main Task)：给定5至15秒的视频，生成一个文本描述、置信分数（0/1，仅用于分析系统，不用于评分）
	2. VTT Robustness SubTask (optional subtask)：同Main Task，但在测试数据中将引入对音频或音频的扰动，以验证系统的鲁棒性
- History：首届为2016年TRECVID竞赛
	- 2022：6队参加
	![Image](https://images2.imgbox.com/de/d0/yTHtm7W3_o.png)
		- 排名：人民大学（金琴）&腾讯；杭州电子科技大学；ELYADATA
	- 2021：5队参加
	![Image](https://images2.imgbox.com/59/53/r4PsNgcc_o.png)
		- 排名：人民大学（金琴）；人民大学（李锡荣）；奥格斯堡大学
	- 2020：6队参加
	![Image](https://images2.imgbox.com/67/79/htopOVTJ_o.png)
		- 排名：人民大学（金琴）；阿尔托大学理工学院；奥格斯堡大学
	- 基本固定参与：人民大学
- 与实验室关联：视觉到文本生成

## Medical Video Question Answering (MedVidQA)
- 本届任务 https://medvidqa.github.io/index.html
	1. Video Corpus Visual Answer Localization (VCVAL)：给定Query，从语料库检索包含答案的视频并定位答案所在时间段，类似首届的两个任务合并
	2. Medical Instructional Question Generation (MIQG)：给定视频切片、字幕，生成该片段所能解答的指导性问题
- History：首届为2022年ACL Workshop、今年首次引入TRECVID竞赛
	- 2022 (ACL BioNLP Workshop Shared task)：13队参加
	![Image](https://images2.imgbox.com/49/f5/RkaZTLKo_o.png)
		- 该届任务及排名（1；2；3）
			1. Medical Video Classification (MVC)：湖南大学&中科院；无锡启益医疗；百度
			2. Medical Visual Answer Localization (MVAL)：平安健康医疗；上海交大&依图科技；华盛顿大学
- 与实验室关联：视觉问答

