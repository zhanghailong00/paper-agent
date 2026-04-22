# PaperAgent

> **一个基于工作流编排的 LLM Agent 系统，用于将中文学术草稿自动转化为高质量英文论文文本。**

PaperAgent 不是简单的 Prompt 集合，而是一个可扩展的多阶段学术写作工作流系统。  
它将翻译、学术重写、自然化润色与审稿视角评估串联为统一 pipeline，便于复用、调优与工程化迭代。

## 项目介绍

中文科研草稿到英文论文成稿通常要经历多个割裂步骤：翻译、重写、润色、找反馈。  
PaperAgent 把这些步骤产品化为一个可追踪、可复现的 LLM workflow agent，帮助你：

- 降低手工切换 Prompt 的成本
- 稳定输出学术表达质量
- 在投稿前获得 reviewer 视角反馈
- 以工程方式持续优化写作流程

## 系统架构

```text
[中文学术草稿]
      |
      v
+--------------------------+
| 1) Translate             |
| 中文 -> 英文             |
+--------------------------+
      |
      v
+--------------------------+
| 2) Academic Rewrite      |
| 学术化重写与术语规范化   |
+--------------------------+
      |
      v
+--------------------------+
| 3) De-AI Polish          |
| 去AI味与自然化润色       |
+--------------------------+
      |
      v
+--------------------------+
| 4) Reviewer Evaluation   |
| 模拟审稿人反馈           |
+--------------------------+
      |
      v
[outputs/result.txt]
```

## 核心功能

- 🧠 **多阶段 LLM 编排**：翻译、重写、润色、评估四阶段串行执行
- 🧩 **Prompt 模块化**：每个阶段独立 Prompt 文件，便于单点调优
- 🔍 **过程可观察**：每一步输出可落盘，方便排查与回归对比
- ⚙️ **工程可扩展**：可插拔阶段设计，便于新增质量检查或后处理节点
- 📦 **轻量运行方式**：Python + OpenAI API，依赖简单，便于集成

## 项目结构

```text
PaperAgent/
├── main.py
├── core/
│   └── pipeline.py
├── llm/
│   └── client.py
├── prompts/
│   ├── translate.txt
│   ├── rewrite.txt
│   ├── deai.txt
│   └── review.txt
├── outputs/
│   └── result.txt
├── .env
└── README.md
```

## 使用示例（输入 -> 输出）

```text
输入（中文草稿）：
“我们提出了一种用于低资源场景的文本分类方法，并在三个公开数据集上验证了有效性。”

输出（写入 outputs/result.txt）：
===== TRANSLATE =====
We propose a text classification method for low-resource scenarios and validate its effectiveness on three public datasets.

===== REWRITE =====
This study presents a text classification approach tailored to low-resource settings, with empirical validation on three benchmark datasets.

===== DEAI =====
We introduce a text classification method designed for low-resource settings and show its effectiveness across three public benchmark datasets.

===== REVIEW =====
Strengths: clear motivation and evaluation setup.
Weaknesses: limited ablation and error analysis.
Suggestions: add stronger baselines and significance testing.
```

## 设计思想

为什么不是单一 Prompt，而是 workflow？

- 单一 Prompt 难以同时兼顾“忠实翻译 + 学术表达 + 自然风格 + 审稿反馈”
- 多阶段拆分后，每个节点职责单一、可独立优化
- 出现问题时可快速定位到具体阶段，而不是整体重写 Prompt
- 便于后续加入规则校验、引用检查、术语一致性检查等节点

换句话说，PaperAgent 的核心价值在于 **pipeline/agent system 设计**，而不是某一条“万能提示词”。

## 技术栈

- **Python**：流程编排与执行入口
- **OpenAI API**：大语言模型调用
- **Prompt Engineering**：分阶段模板化提示词设计
- **File-based Artifacts**：结果落盘与流程可追踪

## Future Work

- [ ] 支持 YAML/JSON 工作流配置（可视化定义阶段）
- [ ] 支持多模型路由与失败回退策略
- [ ] 增加术语一致性检查与引用格式检查节点
- [ ] 增加批量处理与命令行参数（CLI）
- [ ] 增加实验对比模式（不同 Prompt/模型的 A/B 输出）
- [ ] 增加最小化 Web UI 用于交互式编辑
- [ ] 增加单元测试与回归测试，保障迭代稳定性

## License

MIT（建议）
