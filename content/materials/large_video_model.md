+++
title = 'Large_video_model'
date = 2023-12-03T20:44:54+08:00
draft = false
+++

![PG-Video-LLaVA](https://mbzuai-oryx.github.io/Video-LLaVA/images/figures/1-architecture.png)
- PG-Video-LLaVA (Australian National University) https://mbzuai-oryx.github.io/Video-LLaVA/
	- Highlight: First **video-based LMM** with **pixel-level** grounding capabilities
	- Contribution: novel grounding module, incorporation of audio context, benchmark for prompt-based object grounding & video-based conversational models
	- Architecture
		- Visual encoder, scene detector, voice activity detector
		- CLIP as visual encoder, Vicuna LLM
		- 7B, 13B
		
