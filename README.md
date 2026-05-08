# 肺癌知识库 (Lung Cancer Knowledge Base)

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-orange.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Knowledge Triplets](https://img.shields.io/badge/Knowledge%20Triplets-100%2B-blue)](data/kb.json)

🏥 **结构化、开源的肺癌医学知识库**，支持临床决策、科研查询与AI应用。

---

## 简介

本仓库收录肺癌（肺癌，Lung Cancer）的结构化医学知识，以知识三元组（Knowledge Triplet）形式存储，便于：
- 临床决策支持系统（CDSS）
- 医学知识检索增强生成（RAG）
- 医学知识图谱构建
- 患者教育与科普

## 仓库结构

```
lung-cancer-kb/
├── data/
│   ├── kb.json                    # 合并后的完整知识库（构建产物）
│   ├── kb_meta.json               # 元数据统计
│   └── knowledge-graph/           # 源批次文件（*.json）
│       ├── epidemiology.json       # 流行病学数据
│       ├── csco_2024.json         # CSCO指南推荐
│       ├── nccn_2024.json         # NCCN指南推荐
│       └── biomarkers.json        # 生物标志物
├── scripts/
│   ├── build_kb.py                # 构建脚本
│   ├── sync_to_github.py         # GitHub同步脚本
│   └── tests/
│       └── test_kb_format.py     # 格式校验
├── schemas/
│   └── triplet_schema.json       # JSON Schema定义
├── docs/
│   └── domain_guide.md          # 知识域说明
├── UPDATE_POLICY.md              # 更新规范
├── CHANGELOG.md
└── README.md
```

## 快速开始

### 查看知识库

```bash
# 查看知识库统计
cat data/kb_meta.json

# 搜索特定知识
grep "靶向治疗" data/kb.json
```

### 构建知识库

```bash
cd scripts
python build_kb.py
```

### 同步到GitHub

```bash
cd scripts
python sync_to_github.py
```

## 数据质量

### 知识域分布

| 知识域 | 条目数 | 占比 |
|--------|--------|------|
| 流行病学与筛查 | ~15 | ~15% |
| 临床诊断与分期 | ~15 | ~15% |
| 基因突变与分子机制 | ~20 | ~20% |
| 系统治疗（化疗/靶向/免疫） | ~30 | ~30% |
| 外科治疗 | ~10 | ~10% |
| 放射治疗 | ~5 | ~5% |
| 随访与预后 | ~5 | ~5% |

### 证据等级分布

| 证据等级 | 说明 |
|----------|------|
| I级 | RCT/大规模前瞻性研究 |
| II级 | 队列研究/病例对照 |
| I级专家共识 | 权威指南强烈推荐 |
| 专家共识 | 专家意见/指南一般推荐 |

## 核心统计数据（2022年）

| 指标 | 数值 |
|------|------|
| 新发病例 | 106.06万（全球第1） |
| 死亡人数 | 73.33万（全球第1） |
| 病死比 | 69% |
| 主要病理类型 | 非小细胞肺癌（85%）、小细胞肺癌（15%） |

## 更新规范

详见 [UPDATE_POLICY.md](UPDATE_POLICY.md)

**核心原则：前瞻性增量更新，只加不改**

## 核心数据来源

- CSCO肺癌诊疗指南 2024
- NCCN Guidelines: NSCLC/SCLC 2024
- IARC GLOBOCAN 2022
- KEYNOTE系列研究
- IMpower系列研究
- CheckMate系列研究

## 许可证

- **内容**：CC BY-NC-SA 4.0（知识共享署名-非商业性-相同方式共享）
- **代码**：MIT License

---

*本知识库为开源医学知识共享项目，仅供学术研究和临床参考，不构成医疗建议。*
