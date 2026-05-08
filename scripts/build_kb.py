#!/usr/bin/env python3
"""
build_kb.py — 肺癌知识库构建脚本

用法：python build_kb.py
环境变量：
  KB_SRC  - 源数据目录（默认 ../data/knowledge-graph）
  KB_OUT  - 输出文件（默认 ../data/kb.json）
  KB_VER  - 版本号（默认 1.0.0）
"""
import json, os, sys
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.environ.get("KB_SRC", os.path.join(SCRIPT_DIR, "../data/knowledge-graph"))
OUT_FILE = os.environ.get("KB_OUT", os.path.join(SCRIPT_DIR, "../data/kb.json"))
VERSION  = os.environ.get("KB_VER", "1.0.0")

# ── Domain 推断规则（按肺癌关键词定制）────────────────────────
DOMAIN_RULES: list[tuple[list[str], str]] = [
    (["筛查", "流行病学", "发病率", "死亡率", "病死"], "流行病学与筛查"),
    (["分期", "TNM", "AJCC", "分级", "病理"],          "临床诊断与分期"),
    (["基因", "突变", "EGFR", "ALK", "ROS1", "KRAS", "PD-L1", "MSI"], "基因突变与分子机制"),
    (["手术", "切除", "肺叶", "淋巴结", "微创"],          "外科治疗"),
    (["化疗", "靶向", "免疫", "TKI", "PD-1", "PD-L1"],   "系统治疗"),
    (["放疗", "放射", "SBRT", "SABR", "立体定向"],       "放射治疗"),
    (["随访", "监测", "生存率", "预后"],                   "随访与预后"),
    (["支持", "营养", "疼痛", "CINV"],                    "支持治疗"),
]

def infer_domain(head: str, existing: str) -> str:
    if existing and existing.strip():
        return existing.strip()
    for keywords, domain in DOMAIN_RULES:
        if any(kw.upper() in head.upper() for kw in keywords):
            return domain
    return "系统治疗"  # 默认

def normalize(entry: dict) -> dict:
    h = entry.get("head", entry.get("subject", ""))
    base = {
        "head": h,
        "relation": entry.get("relation", entry.get("predicate", "")),
        "tail": entry.get("tail", entry.get("object", "")),
        "source": entry.get("source", ""),
        "evidence": entry.get("evidence", entry.get("evidence_level", "")),
        "domain": infer_domain(h, entry.get("domain", "")),
        "confidence": entry.get("confidence", 0.5),
        "conditions": entry.get("conditions", None),
        "update_date": datetime.now().strftime("%Y-%m-%d"),
    }
    if entry.get("pmid"):
        base["pmid"] = entry["pmid"]
    return base

def build():
    all_entries, seen = [], set()
    stats = {"total": 0, "duplicates": 0, "by_file": {}}

    for fname in sorted(os.listdir(SRC_DIR)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(SRC_DIR, fname), encoding="utf-8") as f:
            data = json.load(f)
        added = 0
        for entry in data:
            norm = normalize(entry)
            key = (norm["head"], norm["relation"], norm["tail"])
            if key not in seen:
                seen.add(key); all_entries.append(norm); added += 1
            else:
                stats["duplicates"] += 1
        stats["by_file"][fname] = added
        print(f"  + [{fname}]: {added} 条")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_entries, f, ensure_ascii=False, indent=2)

    domains = {}
    for e in all_entries:
        d = e.get("domain", "未分类")
        domains[d] = domains.get(d, 0) + 1

    meta = {
        "version": VERSION,
        "update_date": datetime.now().strftime("%Y-%m-%d"),
        "total_entries": len(all_entries),
        "duplicates_removed": stats["duplicates"],
        "source_files": stats["by_file"],
        "domains": domains,
    }
    meta_out = os.path.join(os.path.dirname(OUT_FILE), "kb_meta.json")
    with open(meta_out, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 构建完成: {len(all_entries)} 条 | 去重 {stats['duplicates']} 条")
    print(f"📊 知识域分布:")
    for domain, count in sorted(domains.items(), key=lambda x: -x[1]):
        print(f"   {domain}: {count}")

if __name__ == "__main__":
    build()
