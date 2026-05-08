# 部署指南

## 本地已完成

✅ 肺癌知识库本地仓库已创建并初始化

```
~/WorkBuddy/lung-cancer-kb/
├── data/kb.json              # 48条知识三元组
├── data/kb_meta.json         # 元数据统计
├── README.md                 # 完整文档
└── scripts/                 # 构建和同步脚本
```

## GitHub 仓库创建步骤

### 方法一：手动创建（推荐）

1. **登录 GitHub**
   - 访问 https://github.com/new
   - Repository name: `lung-cancer-kb`
   - Description: `肺癌结构化医学知识库 | Lung Cancer Knowledge Base`
   - 选择 **Public**（公开仓库）
   - **不要勾选** "Add a README file"（本地已有）
   - 点击 "Create repository"

2. **推送代码**
   ```bash
   cd ~/WorkBuddy/lung-cancer-kb
   git remote set-url origin git@github.com:lockwang127/lung-cancer-kb.git
   git push -u origin main
   ```

### 方法二：使用 Token API

如果你有 GitHub Personal Access Token，可以运行：

```bash
# 设置 token（仅本次会话）
export GITHUB_TOKEN="your_token_here"

# 创建仓库并推送
curl -s -X POST "https://api.github.com/user/repos" \
  -H "Authorization: token $GITHUB_TOKEN" \
  -d '{"name":"lung-cancer-kb","description":"Lung Cancer Knowledge Base","private":false}' \
  && cd ~/WorkBuddy/lung-cancer-kb && git push -u origin main
```

## 验证部署

推送成功后，访问：
- 仓库地址: https://github.com/lockwang127/lung-cancer-kb
- 知识库: https://github.com/lockwang127/lung-cancer-kb/blob/main/data/kb.json
