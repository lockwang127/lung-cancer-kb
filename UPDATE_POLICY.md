# 更新规范 (Update Policy)

## 核心原则

本知识库遵循**前瞻性增量更新**原则，确保知识积累可追溯、质量可控。

---

## 更新规则

| 规则 | 说明 |
|------|------|
| ✅ 只加不改 | 新建批次文件，不修改已入库的历史文件 |
| ✅ 按时间命名 | `literature_batch_YYYYMMDD.json` |
| ✅ 仅收录新文献 | 每次只整理最近一段时间的新文献/指南更新 |
| ✅ 自动同步 | build 后立即 push 到 GitHub |
| ❌ 禁止回补旧内容 | 不针对过去的文献期间补录 |

---

## 一次完整更新流程

### 1. 新建批次文件

```bash
# 在 data/knowledge-graph/ 下创建新的批次文件
vim data/knowledge-graph/literature_batch_$(date +%Y%m%d).json
```

批次文件格式示例：

```json
[
  {
    "head": "晚期非小细胞肺癌",
    "relation": "一线免疫治疗推荐",
    "tail": "帕博利珠单抗（Pembrolizumab）+ 含铂双药化疗",
    "source": "KEYNOTE-189 (NCT02578680) / CSCO NSCLC 2024",
    "evidence": "I级",
    "domain": "系统治疗",
    "confidence": 0.95,
    "pmid": "33439993"
  }
]
```

### 2. 构建知识库

```bash
cd scripts
python build_kb.py
```

### 3. 校验格式

```bash
python tests/test_kb_format.py
```

### 4. 同步 GitHub

```bash
python sync_to_github.py
```

### 5. 更新 CHANGELOG.md

记录本次更新的内容、来源和条目数量。

---

## 版本号递增规则

| 触发条件 | 版本递增 |
|----------|----------|
| 新增 ≥50 条三元组 | patch: x.x.Z+1 |
| 新增新 Domain 分类 | minor: x.Y.0 |
| Schema/架构重构 | major: X.0.0 |

---

## 知识三元组字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| head | ✅ | 实体/概念名称（主语） |
| relation | ✅ | 关系谓词（动词短语） |
| tail | ✅ | 实体/值/描述（宾语） |
| source | ✅ | 原始出处（指南版本/PMID/试验编号） |
| evidence | ✅ | 证据等级（I级/II级/I级专家共识/专家共识） |
| domain | ✅ | 所属知识域 |
| confidence | ✅ | 置信度（0.0-1.0） |
| pmid | ❌ | PubMed ID（可选） |
| conditions | ❌ | 适用条件（可选） |
| update_date | 自动 | 更新日期（自动生成） |

---

## 禁止包含的内容

⚠️ **公开仓库禁止包含以下内容**：
- 个人姓名、单位机构、联系方式
- 患者隐私数据
- 内部项目代号或流水号
- 未经授权的版权内容
